#!/usr/bin/env python3
"""Sinh hình minh hoạ cho Bài 3 (NumPy). Chạy từ root repo bằng .venv/bin/python; dùng --only để chọn hình.

Xuất SVG, chữ vẽ bằng outline của Source Sans Pro (bản vendored trong revealjs/) —
trùng font slide, nét ở mọi độ phóng. Không dùng svg.fonttype=none vì SVG nhúng qua
<img> là tài liệu cô lập, không thấy font của trang.
"""
import argparse
import json
import platform
import statistics
import sys
from datetime import datetime, timezone
from timeit import repeat
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
import matplotlib.pyplot as plt
import numpy as np
from example_data import A, B, ROW_COLORS

OUT = Path(__file__).resolve().parent.parent
FONT_DIR = OUT.parent.parent / "revealjs" / "dist" / "theme" / "fonts" / "source-sans-pro"
for f in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(f))

INK, MUTED = "#333333", "#666666"
plt.rcParams.update({
    "font.family": "Source Sans Pro",
    "font.size": 14,
    "svg.hashsalt": "pfdp-lecture03",
    "svg.fonttype": "path",            # chữ → outline: <img> không load được font ngoài
    "figure.facecolor": "none",
    "savefig.facecolor": "none",
    "text.color": INK,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
})

BLUE, ORANGE, GREEN, GRAY = "#1E93AB", "#E8890C", "#2E8B57", "#9aa3a8"



def clean_svg(path):
    """Bỏ khoảng trắng cuối dòng do matplotlib sinh, không thay đổi hình."""
    path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")


def generate_speed():
    n = 1_000_000
    xs_list = list(range(n))
    xs_np = np.arange(n, dtype=np.int64)
    functions = {
        "for_list": lambda: [x * 2 for x in xs_list],
        "for_ndarray": lambda: [x * 2 for x in xs_np],
        "numpy": lambda: xs_np * 2,
    }
    expected = xs_np * 2
    samples = {}
    for name, function in functions.items():
        np.testing.assert_array_equal(function(), expected)
        samples[name] = [t * 1000 for t in repeat(function, repeat=5, number=1)]
    medians = {name: statistics.median(times) for name,times in samples.items()}
    # Các giá trị phân biệt, nằm ngoài vùng số nguyên nhỏ dùng chung của CPython.
    items = list(range(1000, 11_000))
    arr = np.array(items, dtype=np.int64)
    list_refs = sys.getsizeof(items)
    list_objects = sum(sys.getsizeof(item) for item in items)
    array_total = sys.getsizeof(arr)
    record = {
        "measured_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(), "numpy": np.__version__,
        "architecture": platform.machine(), "n": n, "dtype": "int64",
        "expressions": {"for_list": "[x * 2 for x in xs_list]",
                        "for_ndarray": "[x * 2 for x in xs_np]", "numpy": "xs_np * 2"},
        "setup_timed": False, "warmup": True, "repeat": 5, "number": 1,
        "statistic": "median", "samples_ms": samples, "medians_ms": medians,
        "memory": {"n": len(items), "list_references_bytes": list_refs,
                   "list_objects_bytes": list_objects, "array_total_bytes": array_total,
                   "array_data_bytes": arr.nbytes},
    }
    (OUT/"speed-comparison-measurements.json").write_text(json.dumps(record,indent=2)+"\n")
    fig,ax = plt.subplots(figsize=(9,3.8))
    keys=["numpy","for_ndarray","for_list"]
    values=[medians[k] for k in keys]
    bars=ax.barh(["Phép toán NumPy", "Vòng for trên ndarray", "Vòng for trên list"],
                 values,color=[BLUE,ORANGE,GRAY],height=.55)
    ax.bar_label(bars,[f" {v:.1f} ms" for v in values],fontsize=15,color=INK)
    ax.set(xlabel="thời gian nhân đôi 1 triệu số (ms)",xlim=(0,max(values)*1.25))
    ax.spines[["top","right"]].set_visible(False)
    ax.set_title("Trung vị của 5 lần chạy",weight=600,color=INK)
    fig.tight_layout(); fig.savefig(OUT/"speed-comparison.svg",metadata={"Date":None}); clean_svg(OUT/"speed-comparison.svg"); plt.close(fig)
    generate_memory()
    print(json.dumps({"medians_ms":medians,"memory":record["memory"]}))


def generate_memory():
    """Vẽ lại nhãn từ số đo đã lưu, không chạy lại benchmark khi chỉ sửa hình."""
    memory=json.loads((OUT/"speed-comparison-measurements.json").read_text())["memory"]
    list_refs=memory["list_references_bytes"]
    list_objects=memory["list_objects_bytes"]
    array_total=memory["array_total_bytes"]
    fig,ax=plt.subplots(figsize=(9,3.3))
    ax.barh(["list Python","ndarray int64"],[list_refs/1024,array_total/1024],color=[ORANGE,BLUE],height=.55)
    ax.barh(["list Python"],[list_objects/1024],left=[list_refs/1024],color=GRAY,height=.55)
    for i,v in enumerate([list_refs+list_objects,array_total]):
        ax.text(v/1024+4,i,f"{v/1024:.1f} KiB",va="center",fontsize=16)
    ax.text(list_refs/2048,0,"tham chiếu",ha="center",va="center",fontsize=12)
    ax.text((list_refs+list_objects/2)/1024,0,"các đối tượng int",ha="center",va="center",fontsize=14)
    ax.set(xlabel="kích thước đo được (KiB; 1 KiB = 1024 byte)",xlim=(0,(list_refs+list_objects)/1024*1.25))
    ax.spines[["top","right"]].set_visible(False)
    ax.set_title("Cùng lưu dãy 1000, 1001, …, 10999",weight=600,color=INK)
    fig.tight_layout()
    fig.savefig(OUT/"memory-size.svg",metadata={"Date":None})
    clean_svg(OUT/"memory-size.svg")
    plt.close(fig)
    print("memory-size.svg (dùng số đo đã lưu)")


def diagram_canvas():
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.set(xlim=(0, 10), ylim=(0, 4.5))
    ax.axis("off")
    fig.subplots_adjust(left=.01, right=.99, top=.99, bottom=.01)
    return fig, ax


def diagram_grid(ax, values, x, y, size=.68):
    values = np.asarray(values)
    rows, cols = values.shape
    for r in range(rows):
        for c in range(cols):
            px, py = x+c*size, y+(rows-r-1)*size
            color = ROW_COLORS[r % len(ROW_COLORS)]
            ax.add_patch(plt.Rectangle((px,py),size,size,facecolor=color,alpha=.13))
            ax.add_patch(plt.Rectangle((px,py),size,size,fill=False,edgecolor=color,lw=1.3))
            ax.text(px+size/2,py+size/2,f"{values[r,c]:g}",ha="center",va="center",fontsize=19,color=INK)


def generate_broadcasting():
    fig,ax=diagram_canvas()
    diagram_grid(ax,A,.35,.9,.65)
    diagram_grid(ax,B.reshape(1,3),3.95,2.2,.65)
    diagram_grid(ax,A+B,7.6,.9,.65)
    ax.text(1.32,3.98,"A: (4, 3)",ha="center",fontsize=20,color=INK,weight=600)
    ax.text(4.93,3.98,"b: (3,)",ha="center",fontsize=20,color=INK,weight=600)
    ax.text(8.57,3.98,"kết quả: (4, 3)",ha="center",fontsize=20,color=INK,weight=600)
    ax.text(3.1,2.25,"+",ha="center",va="center",fontsize=32)
    ax.text(6.7,2.25,"=",ha="center",va="center",fontsize=32)
    ax.text(4.93,1.65,"dùng lại cho mỗi hàng",ha="center",fontsize=17,color=MUTED)
    ax.text(5,.25,"B[i, j] = A[i, j] + b[j]",ha="center",fontsize=21,color=INK)
    np.testing.assert_array_equal(A+B,[[11,14,14],[21,23,27],[31,35,34],[41,46,45]])
    fig.savefig(OUT/"broadcasting.svg",metadata={"Date":None}); clean_svg(OUT/"broadcasting.svg")
    plt.close(fig)
    print("broadcasting.svg")


def generate_axis():
    fig,ax=diagram_canvas()
    diagram_grid(ax,A,.55,1.35,.58)
    diagram_grid(ax,A,5.35,1.35,.58)
    ax.text(1.65,4.02,"A.mean(axis=0)",ha="center",fontsize=21,color=BLUE,weight=600)
    ax.text(7.15,4.02,"A.mean(axis=1)",ha="center",fontsize=21,color=ORANGE,weight=600)
    for c,v in enumerate(A.mean(axis=0)):
        x=.55+(c+.5)*.58
        ax.annotate("",xy=(x,.79),xytext=(x,1.26),arrowprops={"arrowstyle":"->","color":BLUE,"lw":2.3})
        ax.text(x,.54,f"{v:g}",ha="center",fontsize=18,color=BLUE,weight=600)
    for r,v in enumerate(A.mean(axis=1)):
        y=1.35+(3-r+.5)*.58
        ax.annotate("",xy=(8.08,y),xytext=(7.2,y),arrowprops={"arrowstyle":"->","color":ORANGE,"lw":2.3})
        ax.text(8.27,y,f"{v:.1f}".removesuffix('.0'),va="center",fontsize=20,color=ORANGE,weight=600)
    ax.text(3.05,2.45,"gộp\ncác hàng",ha="center",fontsize=18,color=BLUE)
    ax.text(1.5,.14,"(4, 3) → (3,)",ha="center",fontsize=18,color=INK)
    ax.text(7.3,.54,"gộp các cột",ha="center",fontsize=18,color=ORANGE)
    ax.text(7.3,.14,"(4, 3) → (4,)",ha="center",fontsize=18,color=INK)
    fig.savefig(OUT/"axis.svg",metadata={"Date":None}); clean_svg(OUT/"axis.svg")
    plt.close(fig)
    print("axis.svg (trung bình làm tròn 1 chữ số thập phân)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=["speed", "memory", "broadcasting", "axis", "all"], default="all")
    args = parser.parse_args()
    if args.only == "memory":
        generate_memory()
    for name, generate in [("speed", generate_speed), ("broadcasting", generate_broadcasting), ("axis", generate_axis)]:
        if args.only in (name, "all"):
            generate()
