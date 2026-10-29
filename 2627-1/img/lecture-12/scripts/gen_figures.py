#!/usr/bin/env python3
"""Sinh hình cho Bài 12 (trực quan hoá cơ bản).
Chạy: python gen_figures.py <vis-listings.csv> <vis-reviews.csv>
(hai file visualisations/ của mốc chụp Santiago 2026-06-29)
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent.parent
FONT_DIR = OUT.parent.parent / "revealjs" / "dist" / "theme" / "fonts" / "source-sans-pro"
for font_file in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(font_file))
INK, MUTED = "#333333", "#666666"
plt.rcParams.update({
    "font.family": "Source Sans Pro", "font.size": 13,
    "svg.fonttype": "path",                       # chữ thành path -> hiện đúng font khi nhúng <img>
    "figure.facecolor": "none", "savefig.facecolor": "none",
    "text.color": INK,
    "axes.edgecolor": MUTED, "axes.labelcolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25, "grid.linewidth": 0.7,
})
BLUE, ORANGE, GRAY, GREEN = "#1E93AB", "#E8890C", "#8a8a8a", "#2E8B57"
from matplotlib.ticker import FuncFormatter, MaxNLocator
import matplotlib.dates as mdates
VN = FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", "."))   # 25.000 thay cho 25,000

LISTINGS = sys.argv[1] if len(sys.argv) > 1 else "listings.csv"
REVIEWS = sys.argv[2] if len(sys.argv) > 2 else "reviews.csv"
df = pd.read_csv(LISTINGS)
rv = pd.read_csv(REVIEWS, parse_dates=["date"])

# ---------------------------------------------------------------- anscombe
ans = {
    "I":   ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
            [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
    "II":  ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
            [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
    "III": ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
            [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
    "IV":  ([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
            [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]),
}
fig, axes = plt.subplots(1, 4, figsize=(9.4, 3.4), sharey=True)
for ax, (ten, (x, y)) in zip(axes, ans.items()):
    ax.scatter(x, y, s=42, color=BLUE, alpha=0.85)
    b, a = np.polyfit(x, y, 1)
    xs = np.array([3, 20])
    ax.plot(xs, a + b * xs, color=ORANGE, lw=1.8)
    ax.set_title(f"Bộ {ten}", fontsize=12)
    ax.set_xlim(2, 20)
fig.suptitle("Bốn bộ dữ liệu cùng thống kê nhưng khác hình dạng", fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "anscombe.svg", dpi=150)
plt.close(fig)
print("anscombe.svg")

# ---------------------------------------------------------------- anatomy
# bỏ tháng 06/2026 chưa trọn (mốc chụp 29/06), như bài 8
thang_du = (rv[rv["date"] < "2026-06-01"]
            .set_index("date").resample("ME").size().loc["2023":])
fig, ax = plt.subplots(figsize=(8.2, 4.3))
fig.subplots_adjust(top=0.80, bottom=0.20)
ax.plot(thang_du.index, thang_du.values, color=BLUE, lw=2.2)
ax.set_title("Số đánh giá hằng tháng tại Santiago tăng hơn bốn lần trong ba năm", fontweight="bold", loc="left")
ax.set_xlabel("tháng")
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%Y"))
ax.set_ylabel("số đánh giá / tháng")
peak = thang_du.idxmax()
ax.yaxis.set_major_formatter(VN)
ax.annotate(f"đỉnh {peak:%m/%Y}: {thang_du.max():,.0f}".replace(",", "."),
            xy=(peak, thang_du.max()), xytext=(-150, -6), textcoords="offset points",
            fontsize=12, color=ORANGE, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=ORANGE))
RED = "#c0392b"
# các chú thích "giải phẫu" đặt ngoài vùng vẽ
ax.text(0.0, 1.22, "1) tiêu đề — nêu thông điệp, không chỉ gọi tên biểu đồ",
        transform=ax.transAxes, fontsize=12, color=RED, style="italic")
ax.annotate("", xy=(0.02, 1.075), xytext=(0.035, 1.20), xycoords="axes fraction",
            arrowprops=dict(arrowstyle="->", color=RED))
ax.annotate("2) chú thích — chỉ vào điểm cần lưu ý",
            xy=(0.60, 0.93), xytext=(0.22, 0.80), xycoords="axes fraction",
            fontsize=12, color=RED, style="italic", ha="left", va="center",
            arrowprops=dict(arrowstyle="->", color=RED))
ax.annotate("3) nhãn trục + đơn vị",
            xy=(-0.085, 0.61), xytext=(0.03, 0.61), xycoords="axes fraction",
            fontsize=12, color=RED, style="italic", ha="left", va="center",
            annotation_clip=False, arrowprops=dict(arrowstyle="->", color=RED))
ax.text(0.53, -0.24, "4) nguồn dữ liệu →", transform=ax.transAxes, fontsize=12,
        color=RED, style="italic", ha="right")
ax.text(1.0, -0.24, "Nguồn: Inside Airbnb, mốc chụp 29/06/2026", transform=ax.transAxes,
        fontsize=11, color="#777", ha="right")
fig.savefig(OUT / "anatomy.svg", dpi=150)
plt.close(fig)
print("anatomy.svg")

# ---------------------------------------------------------------- barh ranking
tk = df.groupby("neighbourhood")["price"].agg(median="median", n="size")
top = tk[tk["n"] >= 500].nlargest(5, "median").sort_values("median")
fig, ax = plt.subplots(figsize=(6.8, 3.0))
bars = ax.barh(top.index, top["median"], color=[ORANGE if i == len(top) - 1 else BLUE
                                                for i in range(len(top))], height=0.62)
ax.bar_label(bars, [f" {v:,.0f}".replace(",", ".") for v in top["median"]], fontsize=12)
ax.set_title("Giá trung vị ở Lo Barnechea gấp 4,4 lần quận thứ hai", fontweight="bold", loc="left")
ax.set_xlabel("giá trung vị (CLP/đêm), 5 quận có ≥ 500 chỗ ở")
ax.xaxis.set_major_locator(MaxNLocator(5))
ax.xaxis.set_major_formatter(VN)
ax.grid(axis="y", alpha=0)
fig.tight_layout()
fig.savefig(OUT / "barh-quan.svg", dpi=150)
plt.close(fig)
print("barh-quan.svg")

# ---------------------------------------------------------------- hist: thang thường rồi thang log
gia = df["price"].dropna()
fig, ax = plt.subplots(figsize=(6.4, 2.6))
ax.hist(gia, bins=50, color=BLUE)
ax.set_title("99,9% chỗ ở nằm trong khoảng giá đầu tiên", fontweight="bold", loc="left")
ax.set_xlabel("giá (CLP/đêm)")
ax.set_ylabel("số chỗ ở")
ax.xaxis.set_major_locator(MaxNLocator(4))
ax.xaxis.set_major_formatter(VN)
ax.yaxis.set_major_formatter(VN)
fig.tight_layout()
fig.savefig(OUT / "hist-tho.svg", dpi=150)
plt.close(fig)
print("hist-tho.svg")

fig, ax = plt.subplots(figsize=(6.2, 2.5))
ax.hist(np.log10(gia), bins=50, color=BLUE)
ax.set_title("Giá tập trung quanh 60.000 CLP/đêm",
             fontweight="bold", loc="left")
ax.set_xlabel("log10(giá CLP/đêm)")
ax.set_ylabel("số chỗ ở")
ax.yaxis.set_major_formatter(VN)
fig.tight_layout()
fig.savefig(OUT / "hist-gia.svg", dpi=150)
plt.close(fig)
print("hist-gia.svg")

# ---------------------------------------------------------------- scatter map
s = df.dropna(subset=["price"])          # đủ 17.688 chỗ ở có giá
mau = np.where(s["price"] > s["price"].median(), ORANGE, BLUE)
fig, ax = plt.subplots(figsize=(4.6, 4.0))
# rasterized=True: riêng lớp điểm thành ảnh pixel, chữ và trục vẫn là vector -> SVG nhẹ
ax.scatter(s["longitude"], s["latitude"], s=6, c=mau, alpha=0.45, linewidths=0,
           rasterized=True)
ax.set_title("Chỗ ở đắt hơn trung vị (cam)\ntập trung ở phía đông bắc", fontweight="bold",
             loc="left", fontsize=12.5)
ax.set_xlabel("kinh độ")
ax.set_ylabel("vĩ độ")
ax.set_aspect("equal")
ax.grid(alpha=0.15)
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([], [], marker="o", ls="", color=BLUE, label="giá ≤ trung vị"),
                   Line2D([], [], marker="o", ls="", color=ORANGE, label="giá > trung vị")],
          frameon=False, loc="lower right", fontsize=12)
fig.tight_layout()
fig.savefig(OUT / "scatter-map.svg", dpi=150)
plt.close(fig)
print("scatter-map.svg")

# ---------------------------------------------------------------- y-axis truncation pair
mien = df.groupby("room_type")["price"].median() / 1000          # nghìn CLP/đêm
mien = mien[["Private room", "Entire home/apt", "Hotel room"]]
mien.index = ["Phòng riêng", "Nguyên căn", "Khách sạn"]
fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.3))
for ax, (bat_dau, title, color) in zip(
        axes, [(30, "Trục y bắt đầu từ 30", "#c0392b"),
               (0, "Trục y bắt đầu từ 0", GREEN)]):
    bars = ax.bar(mien.index, mien.values, color=BLUE, width=0.55)
    ax.set_ylim(bat_dau, 130)
    ax.set_title(title, fontsize=12.5, color=color, fontweight="bold")
    ax.bar_label(bars, [f"{v:.0f}" for v in mien.values], fontsize=12)   # trục đã là nghìn CLP
    ax.set_ylabel("giá trung vị (nghìn CLP/đêm)")
    ax.grid(axis="x", alpha=0)
fig.tight_layout()
fig.savefig(OUT / "truc-y.svg", dpi=150)
plt.close(fig)
print("truc-y.svg")

# ---------------------------------------------------------------- subplots: hai loại phòng, chung thang
nguyen_can = df.dropna(subset=["price"]).loc[lambda d: d["room_type"] == "Entire home/apt", "price"]
phong_rieng = df.dropna(subset=["price"]).loc[lambda d: d["room_type"] == "Private room", "price"]
fig, axes = plt.subplots(1, 2, figsize=(7.4, 2.3), sharex=True, sharey=True)
axes[0].hist(np.log10(nguyen_can), bins=50, color=BLUE)
axes[0].set_title(f"Nguyên căn (n = {len(nguyen_can):,})".replace(",", "."), fontsize=12.5)
axes[1].hist(np.log10(phong_rieng), bins=50, color=BLUE)
axes[1].set_title(f"Phòng riêng (n = {len(phong_rieng):,})".replace(",", "."), fontsize=12.5)
for ax in axes:
    ax.set_xlabel("log10(giá CLP/đêm)")
axes[0].set_ylabel("số chỗ ở")
axes[0].yaxis.set_major_formatter(VN)
fig.tight_layout()
fig.savefig(OUT / "subplots-loai.svg", dpi=150)
plt.close(fig)
print("subplots-loai.svg")

# ---------------------------------------------------------------- bản nháp pandas .plot (giữ kiểu mặc định)
with plt.rc_context({"axes.spines.top": True, "axes.spines.right": True, "axes.grid": False,
                     "axes.edgecolor": INK, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK}):
    fig, ax = plt.subplots(figsize=(4.6, 2.7))
    df["room_type"].value_counts().plot.barh(ax=ax)
    fig.tight_layout()
    fig.savefig(OUT / "plot-nhap.svg", dpi=150)
    plt.close(fig)
print("plot-nhap.svg")
