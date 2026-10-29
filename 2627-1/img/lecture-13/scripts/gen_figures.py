#!/usr/bin/env python3
"""Sinh hình cho Bài 13: seaborn, cách mã hoá, bộ hình lỗi để phản biện, bản đồ.
Chạy: python gen_figures.py <vis-listings.csv> <vis-reviews.csv> <neighbourhoods.geojson>
(ba file visualisations/ của mốc chụp Santiago 2026-06-29)

Hình xuất SVG (chữ -> path, nền trong) theo công thức chung của môn, xem
img/lecture-12/scripts/gen_figures.py và EDIT-PASS-NOTES.md mục 11.
"""
from pathlib import Path
import sys

import matplotlib
import matplotlib.dates
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.colors import LogNorm
from matplotlib.ticker import FuncFormatter, MultipleLocator
import numpy as np
import pandas as pd
import seaborn as sns

OUT = Path(__file__).resolve().parent.parent
FONT_DIR = OUT.parent.parent / "revealjs" / "dist" / "theme" / "fonts" / "source-sans-pro"
for font_file in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(font_file))
INK, MUTED = "#333333", "#666666"
BLUE, ORANGE, GRAY, RED = "#1E93AB", "#E8890C", "#9a9a9a", "#c0392b"
VN = FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", "."))

# Công thức SVG: chữ -> outline, nền trong, font Source Sans Pro, trục xám.
# seaborn set_theme() ghi đè rcParams -> áp LẠI block này ngay sau mỗi lần gọi.
SVG_RC = {
    "font.family": "Source Sans Pro",
    "svg.fonttype": "path",
    "figure.facecolor": "none", "savefig.facecolor": "none",
    "text.color": INK, "axes.labelcolor": MUTED, "axes.edgecolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED,
}


def save(fig, ten):
    fig.savefig(OUT / ten, dpi=150)
    plt.close(fig)
    print(ten)


df = pd.read_csv(sys.argv[1])                       # mọi chỗ ở (18.534)
co_gia = df.dropna(subset=["price"])                # chỗ ở có giá (17.688)
rv = pd.read_csv(sys.argv[2], parse_dates=["date"])
GEOJSON = sys.argv[3]

sns.set_theme(style="whitegrid", rc={"grid.alpha": 0.3, "font.size": 12})
plt.rcParams.update(SVG_RC)

# ================================================================ 1. seaborn
# ---------------------------------------------------------------- cách đọc một hộp
pr = co_gia.loc[co_gia["room_type"] == "Private room", "price"]
lg = np.log10(pr)
q1, tv, q3 = np.percentile(lg, [25, 50, 75])
iqr = q3 - q1
rau_duoi = lg[lg >= q1 - 1.5 * iqr].min()
rau_tren = lg[lg <= q3 + 1.5 * iqr].max()
fig, ax = plt.subplots(figsize=(8.6, 3.0))
sns.boxplot(x=pr, log_scale=True, color=BLUE, width=0.3, ax=ax,
            flierprops={"marker": "o", "markersize": 3, "alpha": 0.4})
ax.set_xlim(2e3, 3e6)
ax.set_xlabel("giá phòng riêng (CLP/đêm, thang log)")
ax.xaxis.set_major_formatter(VN)
ax.set_ylim(0.62, -0.62)
mui = dict(arrowstyle="->", color=RED, lw=0.8)
ax.annotate("Q1 (25%)", xy=(10 ** q1, -0.16), xytext=(10 ** (q1 - 0.45), -0.5), color=RED,
            ha="center", fontsize=11, arrowprops=mui)
ax.annotate("trung vị", xy=(10 ** tv, -0.16), xytext=(10 ** tv, -0.5), color=RED,
            ha="center", fontsize=11, arrowprops=mui)
ax.annotate("Q3 (75%)", xy=(10 ** q3, -0.16), xytext=(10 ** (q3 + 0.45), -0.5), color=RED,
            ha="center", fontsize=11, arrowprops=mui)
ax.annotate("râu dưới", xy=(10 ** rau_duoi, 0.02), xytext=(10 ** rau_duoi, 0.45), color=RED,
            ha="center", fontsize=11, arrowprops=mui)
ax.annotate("râu trên", xy=(10 ** rau_tren, 0.02), xytext=(10 ** rau_tren, 0.45), color=RED,
            ha="center", fontsize=11, arrowprops=mui)
ax.annotate("điểm ngoại lai", xy=(10 ** 5.95, 0.02), xytext=(10 ** 6.1, 0.45), color=RED,
            ha="center", fontsize=11, arrowprops=mui)
fig.tight_layout()
save(fig, "box-giai-thich.svg")

# ---------------------------------------------------------------- boxplot theo loại phòng
thu_tu = ["Shared room", "Private room", "Entire home/apt", "Hotel room"]
n = co_gia["room_type"].value_counts()
fig, ax = plt.subplots(figsize=(6.6, 2.6))
sns.boxplot(data=co_gia, x="price", y="room_type", order=thu_tu, log_scale=True,
            showfliers=False, color=BLUE, width=0.55, ax=ax)
ax.set_yticks(range(len(thu_tu)), [f"{t} (n = {n[t]:,})".replace(",", ".") for t in thu_tu])
ax.set_xlabel("giá (CLP/đêm, thang log)")
ax.set_ylabel("")
ax.xaxis.set_major_formatter(VN)
ax.set_title("Phân phối giá của các loại phòng chồng lấn đáng kể",
             loc="left", fontweight="bold", fontsize=12.5)
fig.tight_layout()
save(fig, "box-gia-loai.svg")

# ---------------------------------------------------------------- hue: hai quận
hai_quan = co_gia[co_gia["neighbourhood"].isin(["Santiago", "Las Condes"])]
fig, ax = plt.subplots(figsize=(6.4, 2.7))
sns.histplot(data=hai_quan, x="price", hue="neighbourhood", log_scale=True,
             element="step", stat="density", common_norm=False,
             palette={"Santiago": BLUE, "Las Condes": ORANGE}, ax=ax)
ax.get_legend().set_title("quận")
ax.set_xlim(5e3, 3e6)
ax.set_xlabel("giá (CLP/đêm, thang log)")
ax.set_ylabel("mật độ")
ax.xaxis.set_major_formatter(VN)
ax.set_title("Giá trung vị ở Las Condes gấp khoảng hai lần quận Santiago",
             loc="left", fontweight="bold", fontsize=12.5)
fig.tight_layout()
save(fig, "hist-hue-quan.svg")

# ---------------------------------------------------------------- col: đặt cạnh nhau
bon_quan = ["Santiago", "Providencia", "Las Condes", "Ñuñoa"]
g = sns.displot(co_gia[co_gia["neighbourhood"].isin(bon_quan)], x="price", col="neighbourhood",
                col_order=bon_quan, log_scale=True, stat="density", common_norm=False, bins=40,
                color=BLUE, height=2.2, aspect=0.98, facet_kws={"despine": False})
g.set(xlim=(5e3, 2e6))
g.set_titles("{col_name}")
g.set_axis_labels("giá (nghìn CLP/đêm, log)", "mật độ")
for ax in g.axes.flat:
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v / 1000:,.0f}".replace(",", ".")))
    ax.tick_params(axis="x", labelsize=11)
g.figure.tight_layout()
g.figure.savefig(OUT / "facet-quan.svg", dpi=150)
plt.close(g.figure)
print("facet-quan.svg")

# ---------------------------------------------------------------- heatmap
quan_dong = df["neighbourhood"].value_counts().head(8).index
pv = (co_gia[co_gia["neighbourhood"].isin(quan_dong)]
      .pivot_table(values="price", index="neighbourhood", columns="room_type", aggfunc="median")
      [["Entire home/apt", "Private room"]] / 1000)
fig, ax = plt.subplots(figsize=(4.9, 2.35))
sns.heatmap(pv.sort_values("Entire home/apt", ascending=False), annot=True, fmt=".0f",
            cmap="Blues", cbar_kws={"label": "giá trung vị (nghìn CLP/đêm)"}, ax=ax)
ax.set_title("Nguyên căn đắt gấp gần ba lần ở quận giá cao",
             loc="left", fontweight="bold", fontsize=12.5)
ax.set_xlabel(""); ax.set_ylabel("")
fig.tight_layout()
save(fig, "heatmap-quan-loai.svg")

# ================================================================ 2. cách mã hoá
plt.rcdefaults()
plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
plt.rcParams.update(SVG_RC)

nam_quan = df["neighbourhood"].value_counts().head(5)        # 5 quận đông nhất
ten = ["A", "B", "C", "D", "E"]
gt = nam_quan.values
fig, axes = plt.subplots(1, 4, figsize=(9.4, 2.8))
# vị trí / độ dài
axes[0].bar(ten, gt, color=BLUE, width=0.6)
axes[0].set_title("độ dài (cột)")
axes[0].yaxis.set_major_formatter(VN)
# góc
axes[1].pie(gt, labels=ten, colors=[BLUE] * 5, startangle=90, counterclock=False,
            wedgeprops={"edgecolor": "white", "linewidth": 1.5}, textprops={"fontsize": 11})
axes[1].set_title("góc (biểu đồ tròn)")
# diện tích
# diện tích tỷ lệ với số chỗ ở; hình lớn nhất vừa một ô để không chồng, không bị cắt
axes[2].scatter(range(5), [0] * 5, s=gt / gt.max() * 1000, color=BLUE, alpha=0.85, clip_on=False)
axes[2].set_xticks(range(5), ten)
axes[2].set_yticks([])
axes[2].set_xlim(-0.7, 4.7); axes[2].set_ylim(-1, 1)
axes[2].spines[["left"]].set_visible(False)
axes[2].set_title("diện tích (hình tròn)")
# màu
axes[3].imshow(gt.reshape(1, -1), cmap="Blues", aspect="auto", vmin=0)
axes[3].set_xticks(range(5), ten)
axes[3].set_yticks([])
axes[3].set_title("độ đậm màu")
fig.suptitle("Số chỗ ở của năm quận đông nhất theo bốn cách biểu diễn",
             x=0.01, ha="left", fontweight="bold")
fig.tight_layout()
save(fig, "ma-hoa.svg")

# ---------------------------------------------------------------- bảng màu
x = np.linspace(0, 1, 256).reshape(1, -1)
bang = [("Blues", "tuần tự: độ lớn (giá, số chỗ ở)"),
        ("RdBu", "phân kỳ: lệch hai phía quanh một giá trị giữa"),
        ("tab10", "định tính: nhóm không có thứ tự (loại phòng)"),
        ("jet", "tránh: độ sáng lên xuống, mắt thấy ranh giới giả")]
fig, axes = plt.subplots(len(bang), 1, figsize=(8.6, 2.9))
for ax, (cm, mo_ta) in zip(axes, bang):
    if cm == "tab10":
        ax.imshow(np.arange(10).reshape(1, -1), cmap=cm, aspect="auto")
    else:
        ax.imshow(x, cmap=cm, aspect="auto")
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.text(-0.02, 0.5, cm, transform=ax.transAxes, ha="right", va="center", fontsize=12,
            family="monospace")
    ax.text(1.02, 0.5, mo_ta, transform=ax.transAxes, ha="left", va="center", fontsize=12,
            color=RED if cm == "jet" else INK)
fig.subplots_adjust(left=0.1, right=0.45, hspace=0.7, top=0.97, bottom=0.03)
save(fig, "bang-mau.svg")

# ================================================================ 3. bộ hình lỗi
# Hình A: chuỗi GIÁ là số MINH HOẠ tự sinh (không phải giá Airbnb thật); số đánh giá là dữ liệu thật.
thang = rv[rv["date"] < "2026-06-01"].set_index("date").resample("ME").size().loc["2024":]
gia_minh_hoa = pd.Series(
    np.linspace(55, 62, len(thang)) + np.random.default_rng(3).normal(0, 1.2, len(thang)),
    index=thang.index)
# Mỗi hình lỗi vẽ hai khổ: khổ lớn cho slide câu hỏi, khổ nhỏ (đuôi -nho) cho slide trước/sau.
def ve_truc_kep(figsize, ten, nho=False):
    fig, ax1 = plt.subplots(figsize=figsize)
    ax1.plot(thang.index, thang.values, color=BLUE, lw=2)
    ax1.set_ylabel("số đánh giá" if nho else "số đánh giá / tháng", color=BLUE)
    ax1.yaxis.set_major_formatter(VN)
    ax2 = ax1.twinx()
    ax2.plot(gia_minh_hoa.index, gia_minh_hoa.values, color=RED, lw=2, ls="--")
    ax2.set_ylabel("giá (minh hoạ)" if nho else "giá trung vị (nghìn CLP, minh hoạ)", color=RED)
    ax2.set_ylim(52, 64)
    ax2.spines[["right"]].set_visible(True)
    ax1.set_title("Nhu cầu tăng làm giá tăng", fontweight="bold")
    if nho:
        ax1.xaxis.set_major_locator(matplotlib.dates.MonthLocator(bymonth=[1]))
        ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
        ax2.yaxis.set_major_locator(MultipleLocator(4))
    else:
        ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%m/%Y"))
    fig.tight_layout()
    save(fig, ten)


ve_truc_kep((8.1, 3.4), "ai-loi-truc-kep.svg")
ve_truc_kep((4.6, 2.6), "ai-loi-truc-kep-nho.svg", nho=True)

fig, (axA, axB) = plt.subplots(2, 1, sharex=True, figsize=(4.6, 2.6))
axA.plot(thang.index, thang.values, color=BLUE, lw=2)
axA.set_ylabel("số đánh giá")
axA.set_ylim(0, None)
axA.yaxis.set_major_formatter(VN)
axB.plot(gia_minh_hoa.index, gia_minh_hoa.values, color=ORANGE, lw=2)
axB.set_ylabel("giá, nghìn CLP\n(minh hoạ)")
axB.set_ylim(0, 70)
axA.set_title("Số đánh giá và giá cùng tăng theo thời gian", loc="left", fontweight="bold")
axB.xaxis.set_major_locator(matplotlib.dates.MonthLocator(bymonth=[1]))
axB.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
fig.tight_layout()
save(fig, "sua-truc-kep.svg")

# Hình B: biểu đồ tròn 12 lát (dữ liệu thật, sai DẠNG hình và bỏ phần còn lại)
quan12 = df["neighbourhood"].value_counts().head(12)


def ve_pie(figsize, ten):
    fig, ax = plt.subplots(figsize=figsize)
    ax.pie(quan12.values, labels=quan12.index, colors=plt.cm.tab20.colors, startangle=90,
           textprops={"fontsize": 10})
    ax.set_title("Phân bố chỗ ở theo quận", fontweight="bold")
    fig.tight_layout()
    save(fig, ten)


ve_pie((5.8, 3.7), "ai-loi-pie.svg")
ve_pie((4.6, 2.7), "ai-loi-pie-nho.svg")

pct = df["neighbourhood"].value_counts(normalize=True) * 100
K = 7                                                # khổ nhỏ trên slide: 7 quận + phần còn lại
con_lai = pct.iloc[K:].sum()
bang_b = pd.concat([pct.iloc[:K], pd.Series({f"{len(pct) - K} quận còn lại": con_lai})])
bang_b = bang_b.iloc[::-1]
fig, ax = plt.subplots(figsize=(4.6, 2.8))
mau = [GRAY if "còn lại" in q else (ORANGE if q == "Santiago" else BLUE) for q in bang_b.index]
bars = ax.barh(bang_b.index, bang_b.values, color=mau, height=0.7)
ax.bar_label(bars, [f" {v:.1f}%".replace(".", ",") for v in bang_b.values], fontsize=11)
ax.set_xlabel(f"% tổng số chỗ ở (n = {len(df):,})".replace(",", "."))
ax.set_xlim(0, 46)
ax.set_title("Quận Santiago chiếm 38,8% số chỗ ở", loc="left", fontweight="bold")
ax.grid(axis="y", alpha=0)
ax.tick_params(axis="y", labelsize=11)
fig.tight_layout()
save(fig, "sua-pie.svg")

# Hình C: hai quy mô trên một trục (dữ liệu thật: số đánh giá mỗi năm của hai quận)
dg = rv.merge(df[["id", "neighbourhood"]], left_on="listing_id", right_on="id")
dg = dg[(dg["date"] >= "2022-01-01") & (dg["date"] < "2026-01-01")]
nam = dg.groupby([dg["date"].dt.year, "neighbourhood"]).size().unstack()
hai = nam[["Santiago", "Estación Central"]]


def ve_quy_mo(figsize, ten, nho=False):
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(hai.index, hai["Santiago"], marker="o", lw=2, color=BLUE, label="Santiago")
    ax.plot(hai.index, hai["Estación Central"], marker="o", lw=2, color=ORANGE,
            label="Estación Central")
    ax.set_xticks(hai.index)
    ax.set_ylabel("số đánh giá / năm")
    ax.yaxis.set_major_formatter(VN)
    ax.set_title("Estación Central gần như không tăng" if nho
                 else "Số đánh giá ở Estación Central gần như không tăng", fontweight="bold")
    ax.legend(frameon=False)
    fig.tight_layout()
    save(fig, ten)


ve_quy_mo((8.1, 3.4), "ai-loi-quy-mo.svg")
ve_quy_mo((4.6, 2.3), "ai-loi-quy-mo-nho.svg", nho=True)

chi_so = hai / hai.loc[2022] * 100
fig, ax = plt.subplots(figsize=(4.6, 2.3))
ax.plot(chi_so.index, chi_so["Santiago"], marker="o", lw=2.2, color=BLUE, label="Santiago")
ax.plot(chi_so.index, chi_so["Estación Central"], marker="o", lw=2.2, color=ORANGE,
        label="Estación Central")
ax.axhline(100, color="#777", lw=1, ls="--")
ax.set_xticks(chi_so.index)
ax.set_ylabel("chỉ số (2022 = 100)")
ax.set_title("Estación Central tăng nhanh hơn Santiago", loc="left", fontweight="bold")
ax.legend(frameon=False)
fig.tight_layout()
save(fig, "sua-chi-so.svg")

# Bài tập: xếp hạng không ghi cỡ mẫu (dữ liệu thật)
tk = co_gia.groupby("neighbourhood")["price"].agg(median="median", n="size")
top8 = tk.nlargest(8, "median").sort_values("median")
fig, ax = plt.subplots(figsize=(7.0, 3.1))
bars = ax.barh(top8.index, top8["median"] / 1000, color=BLUE, height=0.6)
ax.bar_label(bars, [f" {v / 1000:.0f}" for v in top8["median"]], fontsize=12)   # trục đã là nghìn CLP
ax.set_xlabel("giá trung vị (nghìn CLP/đêm)")
ax.set_title("La Pintana là quận đắt thứ hai ở Santiago", loc="left", fontweight="bold")
ax.grid(axis="y", alpha=0)
fig.tight_layout()
save(fig, "ai-loi-n.svg")

# ================================================================ 4. bản đồ (tự học)
import geopandas as gpd
geo = gpd.read_file(GEOJSON)
# Giản lược ranh giới (~22 m) để SVG nhẹ; mắt không phân biệt ở cỡ slide.
geo["geometry"] = geo["geometry"].simplify(0.0002)
kpi = co_gia.groupby("neighbourhood").agg(gia=("price", "median"), n=("price", "size")).reset_index()
ban_do = geo.merge(kpi, on="neighbourhood", how="left")
it = ban_do["n"].fillna(0) < 30                       # quận quá ít chỗ ở: không tô màu
fig, ax = plt.subplots(figsize=(4.9, 3.7))
ban_do[~it].plot(column="gia", cmap="Blues", norm=LogNorm(), legend=True, ax=ax,
                 edgecolor="#999", linewidth=0.5,
                 legend_kwds={"label": "giá trung vị (CLP/đêm, thang log)", "shrink": 0.7})
ban_do[it].plot(color="#e6e6e6", edgecolor="#999", linewidth=0.5, hatch="///", ax=ax)
cb = fig.axes[-1]
cb.yaxis.set_major_formatter(VN)
cb.yaxis.set_minor_formatter(FuncFormatter(lambda v, _: ""))
cb.set_yticks([3e4, 5e4, 1e5, 2e5, 4e5])
ax.set_axis_off()
ax.set_title("Giá trung vị cao nhất ở các quận phía đông bắc\n(gạch chéo: quận có dưới 30 chỗ ở)",
             loc="left", fontweight="bold", fontsize=12.5)
fig.tight_layout()
save(fig, "choropleth-gia.svg")
