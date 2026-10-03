#!/usr/bin/env python3
"""Sinh hình cho Bài 13: seaborn nâng cao + choropleth + bộ 'hình AI lỗi' để phản biện.
Chạy: python gen_figures.py <vis-listings.csv> <vis-reviews.csv>
(geojson tải trực tiếp từ Inside Airbnb)

Hình xuất SVG (chữ -> path, nền trong) theo công thức chung của môn — xem
img/lecture-12/scripts/gen_figures.py và EDIT-PASS-NOTES.md mục 11.
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import pandas as pd
import seaborn as sns

OUT = Path(__file__).resolve().parent.parent
FONT_DIR = OUT.parent.parent / "revealjs" / "dist" / "theme" / "fonts" / "source-sans-pro"
for font_file in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(font_file))
INK, MUTED = "#333333", "#666666"
BLUE, ORANGE, GRAY = "#1E93AB", "#E8890C", "#8a8a8a"

# Công thức SVG: chữ -> outline, nền trong, font Source Sans Pro, trục xám.
# seaborn set_theme() và plt.rcdefaults() ghi đè rcParams -> phải áp LẠI block này
# ngay SAU mỗi lần gọi chúng.
SVG_RC = {
    "font.family": "Source Sans Pro",
    "svg.fonttype": "path",
    "figure.facecolor": "none", "savefig.facecolor": "none",
    "text.color": INK, "axes.labelcolor": MUTED, "axes.edgecolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED,
}

LISTINGS = sys.argv[1]
REVIEWS = sys.argv[2]
df = pd.read_csv(LISTINGS)
df = df[df["price"].notna() & (df["price"] > 0)]
rv = pd.read_csv(REVIEWS, parse_dates=["date"])

# ---------------------------------------------------------------- seaborn box (log)
sns.set_theme(style="whitegrid", rc={"grid.alpha": 0.3, "font.size": 12})
plt.rcParams.update(SVG_RC)
thu_tu = ["Shared room", "Private room", "Entire home/apt", "Hotel room"]
fig, ax = plt.subplots(figsize=(8.8, 3.9))
sns.boxplot(data=df, x="price", y="room_type", order=thu_tu, color=BLUE,
            showfliers=False, ax=ax, width=0.55)
ax.set_xscale("log")
ax.set_xlabel("giá (CLP/đêm, thang log)")
ax.set_ylabel("")
ax.set_title("Các loại phòng có mức giá khác nhau nhưng phân phối chồng lấn đáng kể",
             loc="left", fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "box-gia-loai.svg", dpi=150)
plt.close(fig)
print("box-gia-loai.svg")

# ---------------------------------------------------------------- heatmap
quan_lon = df["neighbourhood"].value_counts().head(8).index
pv = (df[df["neighbourhood"].isin(quan_lon)]
      .pivot_table(values="price", index="neighbourhood", columns="room_type", aggfunc="median")
      [["Entire home/apt", "Private room"]] / 1000)
fig, ax = plt.subplots(figsize=(7.6, 4.2))
sns.heatmap(pv.sort_values("Entire home/apt", ascending=False), annot=True, fmt=".0f",
            cmap="Blues", cbar_kws={"label": "giá trung vị (nghìn CLP)"}, ax=ax)
ax.set_title("Chênh lệch giá giữa nguyên căn và phòng riêng lớn hơn ở các quận đắt",
             loc="left", fontweight="bold", fontsize=12.5)
ax.set_xlabel(""); ax.set_ylabel("")
fig.tight_layout()
fig.savefig(OUT / "heatmap-quan-loai.svg", dpi=150)
plt.close(fig)
print("heatmap-quan-loai.svg")

# ---------------------------------------------------------------- hue histplot (2 quận tương phản)
hai_quan = df[df["neighbourhood"].isin(["Santiago", "Las Condes"])]
fig, ax = plt.subplots(figsize=(8.6, 3.7))
sns.histplot(data=hai_quan, x="price", hue="neighbourhood", log_scale=True,
             element="step", stat="density", common_norm=False,
             palette={"Santiago": BLUE, "Las Condes": ORANGE}, ax=ax)
if ax.get_legend():
    ax.get_legend().set_title("quận")
ax.set_xlabel("giá (CLP/đêm, thang log)")
ax.set_ylabel("mật độ")
ax.set_title("Las Condes dịch phải rõ rệt — trung vị gấp ~2× Santiago",
             loc="left", fontweight="bold", fontsize=12.5)
fig.tight_layout()
fig.savefig(OUT / "hist-hue-quan.svg", dpi=150)
plt.close(fig)
print("hist-hue-quan.svg")

# ---------------------------------------------------------------- choropleth
import geopandas as gpd
geo = gpd.read_file("https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/"
                    "visualisations/neighbourhoods.geojson")
# Giản lược ranh giới (~22 m) để SVG nhẹ: 1,6 MB -> ~55 KB, mắt không phân biệt ở cỡ slide.
geo["geometry"] = geo["geometry"].simplify(0.0002)
kpi = df.groupby("neighbourhood").agg(gia=("price", "median"), n=("price", "size")).reset_index()
geo2 = geo.merge(kpi, on="neighbourhood", how="left")
fig, ax = plt.subplots(figsize=(8.4, 5.6))
geo2.plot(column="gia", cmap="Blues", legend=True, ax=ax, edgecolor="#999", linewidth=0.5,
          legend_kwds={"label": "giá trung vị (CLP/đêm)", "shrink": 0.7},
          missing_kwds={"color": "#eeeeee", "label": "không đủ dữ liệu"})
ax.set_axis_off()
ax.set_title("Giá trung vị cao hơn ở khu vực đông bắc Santiago",
             loc="left", fontweight="bold", fontsize=13)
fig.tight_layout()
fig.savefig(OUT / "choropleth-gia.svg", dpi=150)
plt.close(fig)
print("choropleth-gia.svg")

# ---------------------------------------------------------------- FacetGrid: lưới nhỏ theo mốc chụp
snap_cu = Path(LISTINGS).parent / "vis-2025-09-27-listings.csv"
if snap_cu.exists():
    cu = pd.read_csv(snap_cu); cu = cu[cu["price"] > 0]; cu["snapshot"] = "2025-09"
    moi = df.assign(snapshot="2026-06")
    hai_moc = pd.concat([cu[["price", "snapshot"]], moi[["price", "snapshot"]]], ignore_index=True)
    g = sns.displot(hai_moc, x="price", col="snapshot", log_scale=True, bins=45,
                    color=BLUE, height=3.2, aspect=1.15, facet_kws={"despine": False})
    g.set_titles("Mốc chụp {col_name}")
    g.set_axis_labels("giá (CLP/đêm, thang log)", "số chỗ ở")
    g.figure.subplots_adjust(top=0.82)
    g.figure.suptitle("Mỗi mốc chụp một khung nhỏ, chung thang đo — dễ so trực tiếp",
                      x=0.02, ha="left", fontweight="bold", fontsize=12.5)
    g.savefig(OUT / "facet-snapshot.svg", dpi=150)
    plt.close(g.figure)
    print("facet-snapshot.svg")
else:
    print("BỎ QUA facet-snapshot.svg — thiếu vis-2025-09-27-listings.csv")

# ================================================================ BỘ HÌNH "AI LỖI"
# Chuỗi GIÁ ở hình A và C là số MINH HOẠ tự sinh (np.linspace + nhiễu), không phải giá
# Airbnb thật — nhãn trên hình phải nói rõ. Chỉ số đánh giá ở hình A mới là dữ liệu thật.
plt.rcdefaults()
plt.rcParams.update({"font.size": 12})
plt.rcParams.update(SVG_RC)

# (a) dual axis — tương quan giả
# bỏ tháng 6/2026 chưa trọn (mốc chụp 29/06/2026), như bài 8
thang = rv[rv["date"] < "2026-06-01"].set_index("date").resample("ME").size().loc["2024":]
gia_thang = pd.Series(  # giá trung vị GIẢ LẬP trượt nhẹ để minh hoạ trục kép đánh lừa
    np.linspace(55, 62, len(thang)) + np.random.default_rng(3).normal(0, 1.2, len(thang)),
    index=thang.index)
fig, ax1 = plt.subplots(figsize=(8.8, 3.8))
ax1.plot(thang.index, thang.values, color=BLUE, lw=2, label="số đánh giá")
ax1.set_ylabel("số đánh giá", color=BLUE)
ax2 = ax1.twinx()
ax2.plot(gia_thang.index, gia_thang.values, color="red", lw=2, ls="--", label="giá trung vị")
ax2.set_ylabel("giá trung vị (nghìn CLP)", color="red")
ax2.set_ylim(54, 63)
ax1.set_title("Phân tích nhu cầu và giá — Santiago (giá: số liệu minh hoạ)", fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "ai-loi-truc-kep.svg", dpi=150)
plt.close(fig)
print("ai-loi-truc-kep.svg")

# (a-fixed) tách trục kép -> hai khung nhỏ, chung trục thời gian
fig, (axA, axB) = plt.subplots(2, 1, sharex=True, figsize=(8.6, 4.3))
axA.plot(thang.index, thang.values, color=BLUE, lw=2)
axA.set_ylabel("số đánh giá")
axB.plot(gia_thang.index, gia_thang.values, color=ORANGE, lw=2)
axB.set_ylabel("giá trung vị\n(nghìn CLP · minh hoạ)")
axA.set_title("Bản sửa: tách hai khung, chung trục thời gian", loc="left", fontweight="bold")
for a in (axA, axB):
    a.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT / "sua-truc-kep.svg", dpi=150)
plt.close(fig)
print("sua-truc-kep.svg")

# (b) biểu đồ tròn 12 lát và nhiều màu — dữ liệu THẬT (top-12 quận), chỉ sai DẠNG hình
quan12 = df["neighbourhood"].value_counts().head(12)
fig, ax = plt.subplots(figsize=(7.2, 4.6))
ax.pie(quan12.values, labels=quan12.index, autopct="%1.1f%%",
       colors=plt.cm.tab20.colors, startangle=90, textprops={"fontsize": 8.5})
ax.set_title("Phân bố chỗ ở theo quận", fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "ai-loi-pie.svg", dpi=150)
plt.close(fig)
print("ai-loi-pie.svg")

# (b-fixed) pie -> thanh ngang xếp hạng (dữ liệu thật, cùng top-12 quận)
pct = (quan12 / len(df) * 100).sort_values()
fig, ax = plt.subplots(figsize=(8.4, 4.6))
mau = [ORANGE if q == pct.index[-1] else BLUE for q in pct.index]
bars = ax.barh(pct.index, pct.values, color=mau, height=0.72)
ax.bar_label(bars, [f" {v:.1f}%" for v in pct.values], fontsize=10)
ax.set_xlabel("% tổng số chỗ ở")
ax.set_title("Bản sửa: thanh ngang xếp hạng thay cho biểu đồ tròn", loc="left", fontweight="bold")
ax.grid(axis="x", alpha=0.15)
fig.tight_layout()
fig.savefig(OUT / "sua-pie.svg", dpi=150)
plt.close(fig)
print("sua-pie.svg")

# (c) hai thành phố, hai tiền tệ trên cùng một trục — cả hai chuỗi đều GIẢ LẬP
scl = np.linspace(52, 65, 24) + np.random.default_rng(1).normal(0, 1.5, 24)
rio = np.linspace(280, 340, 24) + np.random.default_rng(2).normal(0, 8, 24)
idx = pd.date_range("2024-07-31", periods=24, freq="ME")
fig, ax = plt.subplots(figsize=(8.8, 3.8))
ax.plot(idx, scl * 1000, lw=2, color=BLUE, label="Santiago (CLP)")
ax.plot(idx, rio, lw=2, color=ORANGE, label="Rio de Janeiro (BRL)")
ax.set_title("So sánh giá: Santiago và Rio de Janeiro (số liệu minh hoạ)", fontweight="bold")
ax.set_ylabel("giá trung vị")
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "ai-loi-hai-tien-te.svg", dpi=150)
plt.close(fig)
print("ai-loi-hai-tien-te.svg")

# (c-fixed) quy về chỉ số 100 — thông điệp PHƯƠNG PHÁP, không khẳng định thành phố nào tăng nhanh hơn
fig, ax = plt.subplots(figsize=(8.8, 3.8))
ax.plot(idx, scl / scl[0] * 100, lw=2.2, color=BLUE, label="Santiago")
ax.plot(idx, rio / rio[0] * 100, lw=2.2, color=ORANGE, label="Rio de Janeiro")
ax.axhline(100, color="#777", lw=1, ls="--")
ax.set_ylabel("chỉ số giá (tháng đầu = 100)")
ax.set_title("Cùng quy về mốc 100 mới so được nhịp tăng (số liệu minh hoạ)", loc="left",
             fontweight="bold")
ax.legend(frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT / "sua-index-100.svg", dpi=150)
plt.close(fig)
print("sua-index-100.svg")

# ---------------------------------------------------------------- plotly (ảnh tĩnh minh hoạ tương tác)
# Ảnh tĩnh cho slide; bản thật là HTML rê chuột được. Chú thích 1 điểm để minh hoạ nội dung hover.
try:
    import plotly.express as px
    s = df.dropna(subset=["price", "longitude", "latitude", "room_type", "name"]).sample(1400, random_state=1)
    fpx = px.scatter(s, x="longitude", y="latitude", color="room_type",
                     hover_name="name", hover_data={"price": ":,.0f", "neighbourhood": True},
                     opacity=0.6, width=920, height=520,
                     labels={"longitude": "kinh độ", "latitude": "vĩ độ", "room_type": "loại phòng"},
                     title="plotly express: màu theo loại phòng — rê chuột để xem chi tiết")
    fpx.update_traces(marker={"size": 6})
    fpx.update_layout(font_family="Source Sans Pro",
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      legend={"orientation": "h", "y": -0.18, "title": ""})
    fpx.update_xaxes(showgrid=True, gridcolor="#eeeeee")
    fpx.update_yaxes(showgrid=True, gridcolor="#eeeeee")
    p = s.sort_values("price", ascending=False).iloc[0]
    fpx.add_annotation(x=p["longitude"], y=p["latitude"],
                       text=f"<b>{str(p['name'])[:26]}</b><br>{p['price']:,.0f} CLP · {p['neighbourhood']}",
                       showarrow=True, arrowhead=2, bgcolor="white", bordercolor="#999",
                       font={"size": 12}, ax=45, ay=-55, align="left")
    fpx.write_image(str(OUT / "plotly-hover.png"), scale=2)
    print("plotly-hover.png")
except Exception as e:
    print("BỎ QUA plotly-hover.png —", type(e).__name__, e)
