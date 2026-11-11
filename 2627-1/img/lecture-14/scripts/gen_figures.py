#!/usr/bin/env python3
"""Sinh hình cho Bài 14 (kể chuyện bằng dữ liệu).
Chạy: python gen_figures.py <vis-reviews.csv>   (visualisations/reviews.csv, mốc chụp Santiago 2026-06-29)

SVG theo công thức chung (EDIT-PASS §11): chữ -> path, nền trong, Source Sans Pro;
mỗi hình vẽ đúng cỡ hiển thị trên slide (rộng = px / 96 inch).
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter
import pandas as pd

OUT = Path(__file__).resolve().parent.parent
FONT_DIR = OUT.parent.parent / "revealjs" / "dist" / "theme" / "fonts" / "source-sans-pro"
for font_file in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(font_file))
INK, MUTED = "#333333", "#666666"
BLUE, ORANGE, GRAY = "#1E93AB", "#E8890C", "#b5b5b5"
VN = FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", "."))
SVG_RC = {"font.family": "Source Sans Pro", "font.size": 12, "svg.fonttype": "path",
          "figure.facecolor": "none", "savefig.facecolor": "none", "text.color": INK}

rv = pd.read_csv(sys.argv[1], parse_dates=["date"])
rv = rv[rv["date"] <= "2026-06-29"]                       # cắt theo mốc chụp
thang = rv.set_index("date").resample("ME").size().loc["2024":"2026-05"]   # bỏ tháng 6 chưa trọn
t5_25, t5_26 = thang["2025-05"].iloc[0], thang["2026-05"].iloc[0]

# ---------------------------------------------------------------- tiêu đề mô tả và tiêu đề nêu kết luận
# Khung trái: kiểu mặc định, tiêu đề chỉ gọi tên; khung phải: tiêu đề nêu kết luận, tô nổi hai điểm so sánh.
plt.rcParams.update(SVG_RC)
for ten, kieu in [("tieu-de-mo-ta.svg", "mo_ta"), ("tieu-de-ket-luan.svg", "ket_luan")]:
    with plt.rc_context({"axes.spines.top": kieu == "mo_ta", "axes.spines.right": kieu == "mo_ta",
                         "axes.edgecolor": INK if kieu == "mo_ta" else MUTED,
                         "xtick.color": INK if kieu == "mo_ta" else MUTED,
                         "ytick.color": INK if kieu == "mo_ta" else MUTED}):
        fig, ax = plt.subplots(figsize=(4.6, 2.9))
        if kieu == "mo_ta":
            ax.plot(thang.index, thang.values)
            ax.set_title("Số đánh giá theo tháng")
        else:
            ax.plot(thang.index, thang.values, color=GRAY, lw=2)
            for d, v in [(thang.index[thang.index.strftime("%Y-%m") == "2025-05"][0], t5_25),
                         (thang.index[-1], t5_26)]:
                ax.plot(d, v, "o", color=ORANGE, ms=7)
            ax.annotate(f"05/2025: {t5_25:,}".replace(",", "."), (thang.index[16], t5_25),
                        xytext=(0, -26), textcoords="offset points", color=ORANGE, ha="center",
                        bbox=dict(fc="white", ec="none", pad=1))
            ax.annotate(f"05/2026\n{t5_26:,}".replace(",", "."), (thang.index[-1], t5_26),
                        xytext=(7, 0), textcoords="offset points", color=ORANGE, ha="left",
                        va="center", linespacing=1.1)
            # chừa chỗ bên phải điểm cuối cho nhãn, để nhãn không đè lên đường
            ax.set_xlim(right=thang.index[-1] + pd.DateOffset(months=7))
            # tiêu đề căn từ mép trái của cả hình (rộng hơn vùng trục) để không bị cắt
            fig.suptitle(f"Số đánh giá tháng 5/2026 tăng {t5_26 / t5_25 - 1:.0%}\nso với tháng 5/2025",
                         x=0.02, ha="left", fontweight="bold", fontsize=plt.rcParams["axes.titlesize"])
            ax.grid(axis="y", alpha=0.3)
        ax.set_xlabel("Tháng", color=INK if kieu == "mo_ta" else MUTED)
        ax.set_ylabel("Số đánh giá", color=INK if kieu == "mo_ta" else MUTED)
        ax.yaxis.set_major_formatter(VN)
        ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1]))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        fig.tight_layout()
        fig.savefig(OUT / ten, dpi=150)
        plt.close(fig)
        print(ten)
