#!/usr/bin/env python3
"""Sinh hình SVG cho Bài 10 từ dữ liệu giá chỗ ở tại Santiago.

Mặc định tải mốc chụp 2026-06-29 từ Inside Airbnb. Có thể truyền đường dẫn tới
``listings.csv.gz`` làm đối số thứ nhất để chạy hoàn toàn cục bộ.
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent.parent
FONT_DIR = OUT.parent.parent / "revealjs" / "dist" / "theme" / "fonts" / "source-sans-pro"
for font_file in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(font_file))

INK, MUTED = "#333333", "#666666"
plt.rcParams.update({
    "font.family": "Source Sans Pro",
    "font.size": 15,
    "svg.fonttype": "path",
    "svg.hashsalt": "lecture-10-price-distribution",
    "figure.facecolor": "none",
    "savefig.facecolor": "none",
    "text.color": INK,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
})
BLUE, ORANGE = "#1E93AB", "#E8890C"

URL = ("https://data.insideairbnb.com/chile/rm/santiago/"
       "2026-06-29/data/listings.csv.gz")
PATH = sys.argv[1] if len(sys.argv) > 1 else URL
df = pd.read_csv(PATH, usecols=["price"])
gia_chu = (df["price"].str.replace("$", "", regex=False)
           .str.replace(",", "", regex=False))
gia = pd.to_numeric(gia_chu, errors="coerce")
assert not (df["price"].notna() & gia.isna()).any(), "Có giá không chuyển được thành số."
gia = gia.dropna()
gia = gia[gia > 0]

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))

axes[0].hist(gia / 1_000_000, bins=60, color=BLUE)
axes[0].set_title("Thang giá gốc", fontsize=14)
axes[0].set_xlabel("giá (triệu CLP/đêm)")
axes[0].set_ylabel("số chỗ ở")

axes[1].hist(np.log10(gia), bins=60, color=ORANGE)
axes[1].set_title("Thang log₁₀ của giá", fontsize=14)
axes[1].set_xlabel("log10(giá)")
axes[1].set_ylabel("số chỗ ở")

for ax in axes:
    ax.spines[["top", "right"]].set_visible(False)
fig.suptitle("Phân phối giá chỗ ở tại Santiago", fontweight=600)
fig.tight_layout()
target = OUT / "phan-phoi-gia.svg"
fig.savefig(target, metadata={"Date": None})
target.write_text("\n".join(line.rstrip() for line in target.read_text().splitlines()) + "\n")
print("phan-phoi-gia.svg done")
