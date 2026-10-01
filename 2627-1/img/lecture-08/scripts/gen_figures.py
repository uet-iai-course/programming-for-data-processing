#!/usr/bin/env python3
"""Sinh hai hình SVG cho Bài 8 từ dữ liệu đánh giá Santiago.

Mặc định đọc dữ liệu tại mốc chụp 2026-06-29 từ Inside Airbnb. Có thể truyền đường dẫn tới
``reviews.csv`` làm đối số thứ nhất để chạy hoàn toàn cục bộ.
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
import matplotlib.pyplot as plt
import pandas as pd

OUT = Path(__file__).resolve().parent.parent
FONT_DIR = OUT.parent.parent / "revealjs" / "dist" / "theme" / "fonts" / "source-sans-pro"
for font_file in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(font_file))

INK, MUTED = "#333333", "#666666"
plt.rcParams.update({
    "font.family": "Source Sans Pro",
    "font.size": 16,
    "svg.fonttype": "path",
    "figure.facecolor": "none",
    "savefig.facecolor": "none",
    "text.color": INK,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
})
BLUE, ORANGE, GRAY = "#1E93AB", "#E8890C", "#9aa3a8"


def save_svg(fig, name):
    path = OUT / name
    fig.savefig(path)
    path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")

URL = ("https://data.insideairbnb.com/chile/rm/santiago/"
       "2026-06-29/visualisations/reviews.csv")
PATH = sys.argv[1] if len(sys.argv) > 1 else URL
SNAPSHOT = pd.Timestamp("2026-06-29")
rv = pd.read_csv(PATH, parse_dates=["date"])
rv = rv.loc[rv["date"] <= SNAPSHOT].copy()  # bỏ 204 ngày sau mốc chụp
theo_thang = rv.set_index("date").sort_index().resample("ME").size()
thang_day_du = theo_thang.loc[theo_thang.index < SNAPSHOT.replace(day=1)]
muot = thang_day_du.rolling(6, min_periods=6).mean()
pham_vi = thang_day_du.loc["2016":]

# ------------------------------------------------ theo tháng + cửa sổ trượt
fig, ax = plt.subplots(figsize=(11, 3.8))
ax.plot(pham_vi.index, pham_vi.values, color=GRAY, lw=1.4, label="Mỗi tháng")
ax.plot(pham_vi.index, muot.loc["2016":],
        color=BLUE, lw=2.6, label="Trung bình 6 tháng gần nhất")
ax.set_ylabel("Số đánh giá")
ax.legend(frameon=False, loc="upper left")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
save_svg(fig, "reviews-theo-thang.svg")
plt.close(fig)
print("reviews-theo-thang.svg done")

# ------------------------------------------------ seasonality profile
# Chỉ dùng các năm đầy đủ 2022–2025 để mỗi tháng góp mặt cùng số lần.
tron_nam = rv.loc[(rv["date"] >= "2022-01-01") & (rv["date"] <= "2025-12-31")]
thang_tb = tron_nam.groupby(tron_nam["date"].dt.month).size()
thang_tb = thang_tb / thang_tb.mean() * 100

fig, ax = plt.subplots(figsize=(10, 4.2))
colors = [ORANGE if m == 11 else BLUE for m in thang_tb.index]
ax.bar(thang_tb.index, thang_tb.values, color=colors)
ax.axhline(100, color="#555", lw=1, ls="--")
ax.set_xticks(range(1, 13), [f"T{m}" for m in range(1, 13)])
ax.set_ylabel("Chỉ số (100 = trung bình)")
ax.set_ylim(0, 155)
ax.set_title("Cùng tập năm 2022–2025", fontweight="bold")
ax.bar_label(ax.containers[0], labels=thang_tb.round().astype(int), padding=3)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
save_svg(fig, "mua-vu.svg")
plt.close(fig)
print("mua-vu.svg done")
