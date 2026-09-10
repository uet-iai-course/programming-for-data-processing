#!/usr/bin/env python3
"""Sơ đồ tự vẽ cho Bài 3, cùng ma trận A với slide và notebook.

Chạy từ root repo: .venv/bin/python 2627-1/img/lecture-03/scripts/gen_memory_figures.py
Nguồn kiến thức: McKinney, Python for Data Analysis, chương 4 (mở đầu, §4.1);
NumPy internals / ndarray / copies and views; CPython Design FAQ;
SciPy Lecture Notes (CPU cache effects). Không sao chép hình hay văn bản nguồn.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
from matplotlib import font_manager
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
from example_data import A, ROW_COLORS

OUT=Path(__file__).resolve().parent.parent
for font in (OUT.parent.parent/'revealjs/dist/theme/fonts/source-sans-pro').glob('*.ttf'):
    font_manager.fontManager.addfont(str(font))
INK,MUTED='#333333','#666666'
BLUE,ORANGE,GREEN=ROW_COLORS[:3]
VALUE_COLORS={int(v):ROW_COLORS[r] for r,row in enumerate(A) for v in row}
plt.rcParams.update({'font.family':'Source Sans Pro','font.size':18,'font.weight':400,
    'svg.fonttype':'path','svg.hashsalt':'pfdp-numpy-foundations',
    'figure.facecolor':'none','savefig.facecolor':'none','text.color':INK})

def canvas(h=4.7):
    fig,ax=plt.subplots(figsize=(10,h))
    ax.set(xlim=(0,10),ylim=(0,h)); ax.axis('off')
    fig.subplots_adjust(left=.01,right=.99,top=.99,bottom=.01)
    return fig,ax

def label(ax,x,y,s,size=18,color=INK,ha='left',weight=400):
    ax.text(x,y,s,fontsize=size,color=color,ha=ha,va='center',weight=weight)

def box(ax,x,y,w,h,s='',color=BLUE,size=17):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.025,rounding_size=.04',
                              facecolor='white',edgecolor=color,lw=1.6))
    label(ax,x+w/2,y+h/2,s,size,color=INK,ha='center')

def arrow(ax,p,q,color=BLUE):
    ax.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','color':color,'lw':2,'shrinkA':3,'shrinkB':3})

def cell(ax,x,y,w,h,v,color=BLUE,selected=True,size=18):
    ax.add_patch(Rectangle((x,y),w,h,facecolor=color,alpha=.14 if selected else .035))
    ax.add_patch(Rectangle((x,y),w,h,fill=False,edgecolor=color if selected else '#b9b9b9',lw=1.4))
    label(ax,x+w/2,y+h/2,str(v),size,color=INK if selected else '#9a9a9a',ha='center')

def matrix(ax,x,y,values,w=.68,selection=None):
    rows,cols=values.shape
    for r in range(rows):
        for c in range(cols):
            active=True if selection is None else (r,c) in selection
            cell(ax,x+c*w,y+(rows-r-1)*w,w,w,values[r,c],VALUE_COLORS[int(values[r,c])],active)
    for c in range(cols): label(ax,x+(c+.5)*w,y+rows*w+.22,str(c),14,MUTED,'center')
    for r in range(rows): label(ax,x-.2,y+(rows-r-.5)*w,str(r),14,MUTED,'center')

def buffer(ax,y,selection=None):
    for i,v in enumerate(A.ravel()):
        cell(ax,.35+i*.77,y,.77,.6,v,ROW_COLORS[i//3],selection is None or i in selection,17)
        label(ax,.35+(i+.5)*.77,y-.25,str(i*A.itemsize),13,MUTED,'center')
    label(ax,5,y-.58,'độ lệch từ đầu vùng dữ liệu (byte)',14,MUTED,'center')

def save(fig,name,description):
    fig.savefig(OUT/name,metadata={'Date':None,'Description':description})
    path=OUT/name
    path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines())+'\n')
    plt.close(fig)
    print(name)

fig,ax=canvas(4.65)
label(ax,.15,4.32,'xs = [10, 12, 11]',20,ORANGE,weight=600)
label(ax,.25,3.63,'list lưu\ntham chiếu',16,MUTED)
for i,(xobj,yobj,v) in enumerate([(2,2.4,10),(4.3,1.9,12),(7.2,2.4,11)]):
    cell(ax,2.2+i*2.0,3.35,1.7,.56,'địa chỉ',ORANGE,size=16)
    box(ax,xobj,yobj,1.8,.78,f'đối tượng int\ngiá trị {v}',ORANGE,16)
    arrow(ax,(3.05+i*2,3.35),(xobj+.9,yobj+.78),ORANGE)
label(ax,.15,1.24,'np.array(xs, dtype=np.int64)',20,BLUE,weight=600)
for i,v in enumerate(A[0]): cell(ax,2.2+i*2,.35,2,.6,v,BLUE)
label(ax,5.2,.10,'mỗi ô 8 byte, chứa trực tiếp giá trị số',15,MUTED,'center')
save(fig,'memory-layout.svg','CPython list chứa tham chiếu; ndarray int64 chứa trực tiếp 10,12,11. Sơ đồ vị trí đối tượng giản lược.')

fig,ax=canvas(4.75)
label(ax,.25,4.45,'A: 4 hàng × 3 cột',21,weight=600)
matrix(ax,.8,1.75,A,w=.53)
box(ax,4.05,2.09,5.5,1.69,'shape = (4, 3): 4 hàng, 3 cột\ndtype = int64: mỗi số 8 byte\nCác số cùng hàng nằm liền nhau',BLUE,19)
label(ax,5,1.4,'Vùng dữ liệu: 12 giá trị xếp theo thứ tự từng hàng',19,MUTED,'center')
for i,v in enumerate(A.ravel()):
    cell(ax,.35+i*.77,.61,.77,.6,v,ROW_COLORS[i//3],size=19)
label(ax,5,.2,'Mỗi hàng gồm 3 số × 8 byte = 24 byte',18,MUTED,'center')
save(fig,'array-strides.svg','Shape và dtype mô tả vùng dữ liệu của A. Các phần tử trong mỗi hàng liên tiếp nhau; mỗi hàng giữ một màu.')

fig,ax=canvas(4.5)
label(ax,.2,4.13,'[x * 2 for x in xs]',22,ORANGE,weight=600)
for i,v in enumerate(A[0]):
    y=2.95-i*.95
    box(ax,.2,y,2.15,.65,f'int: {v}',ORANGE)
    box(ax,3.2,y,3.2,.65,'phép nhân Python',ORANGE)
    box(ax,7.25,y,2.35,.65,f'int: {v*2}',ORANGE)
    arrow(ax,(2.38,y+.325),(3.18,y+.325),ORANGE)
    arrow(ax,(6.42,y+.325),(7.23,y+.325),ORANGE)
label(ax,5,.40,'Mỗi lượt: lấy đối tượng số → nhân → lưu tham chiếu kết quả',17,MUTED,'center')
save(fig,'python-loop.svg','Phép nhân Python trên từng đối tượng của xs=[10,12,11]; kết quả là các đối tượng số 20,24,22.')

# Minh hoạ chọn đoạn mã đã có sẵn theo kiểu đầu vào.
# Với số nguyên Python 2 và ba dtype dưới đây, dtype đầu ra giữ nguyên.
for dtype in (np.int32, np.int64, np.float64):
    x_type=np.array(A[0],dtype=dtype)
    assert np.multiply(x_type,2).dtype==np.dtype(dtype)
fig,ax=canvas(4.55)
label(ax,.2,4.2,'y = np.multiply(x, 2)',23,BLUE,weight=600)
box(ax,.2,1.77,2.38,1.2,'x.dtype: int64\nx: [10, 12, 11]',BLUE,19)
label(ax,6.4,3.58,'Các đoạn mã nhân có sẵn trong NumPy',19,weight=600,ha='center')
rows=[(2.75,'int32: số nguyên, 4 byte',False),(1.87,'int64: số nguyên, 8 byte',True),(.99,'float64: số thực, 8 byte',False)]
for y,txt,selected in rows:
    color=BLUE if selected else '#b9b9b9'
    ax.add_patch(FancyBboxPatch((3.35,y),6.18,.66,boxstyle='round,pad=.015,rounding_size=.04',
        facecolor='#e7f4f7' if selected else 'white',edgecolor=color,lw=2.4 if selected else 1.1))
    label(ax,3.55,y+.33,txt,20,INK if selected else MUTED,weight=600 if selected else 400)
    if selected:
        label(ax,9.3,y+.33,'được dùng',17,BLUE,'right',600)
arrow(ax,(2.63,2.2),(3.33,2.2),BLUE)
label(ax,5,.35,'int64 và float64 cùng 8 byte, nhưng dùng phép tính khác nhau',18,MUTED,'center')
save(fig,'ufunc-dispatch.svg','Ba đoạn mã minh hoạ cho phép nhân. x int64 nhân số nguyên 2 dùng đoạn mã int64. Dtype quyết định cả cách đọc bit lẫn phép tính.')

fig,ax=canvas(4.65)
label(ax,.2,4.32,'y = np.multiply(x, 2)',23,BLUE,weight=600)
label(ax,2.57,3.84,'x: ba ô int64, mỗi ô 8 byte',18,BLUE,'center')
for i,v in enumerate(A[0]):
    px=.55+i*1.33
    cell(ax,px,2.9,1.33,.62,v,BLUE,size=23)
    label(ax,px+.665,2.64,f'x[{i}]',16,MUTED,'center')
    cell(ax,px,.65,1.33,.62,v*2,GREEN,size=23)
    label(ax,px+.665,.4,f'y[{i}]',16,MUTED,'center')
    arrow(ax,(px+.665,2.45),(px+.665,1.29),BLUE)
    label(ax,px+.88,1.94,'× 2',17,BLUE)
label(ax,2.55,.06,'y: ghi trực tiếp giá trị vào từng ô',17,GREEN,'center')
label(ax,5.12,3.71,'Xử lý phần tử đầu tiên',20,weight=600)
steps=[('1. Đọc 8 byte tại x[0] → số 10',3.16),
       ('2. Nhân hai số nguyên: 10 × 2 = 20',2.48),
       ('3. Ghi 20 vào 8 byte tại y[0]',1.80)]
for txt,y in steps:
    label(ax,5.12,y,txt,18)
box(ax,5.09,.52,4.59,.77,'Dịch 8 byte để tới x[1], y[1]\nrồi lặp lại các bước trên',BLUE,18)
save(fig,'numpy-loop.svg','Với x int64 liên tục: đọc 8 byte tại x[0], nhân 2, ghi 8 byte tại y[0], dịch 8 byte rồi lặp. Các kết quả là 20,24,22. Sơ đồ logic không mô tả số lệnh máy/SIMD thực tế.')

fig,ax=canvas(4.7)
label(ax,.15,4.4,'1. Đọc 10: khối dữ liệu chưa có trong cache',21,weight=600)
for x,title in [(1.5,'RAM'),(5.4,'Cache'),(8.9,'CPU')]:
    label(ax,x,3.88,title,20,BLUE if title=='Cache' else INK,'center',600)
for i,v in enumerate(A.ravel()[:4]):
    cell(ax,.3+i*.6,2.95,.6,.6,v,BLUE,size=20)
    cell(ax,4.2+i*.6,2.95,.6,.6,v,BLUE,size=20)
arrow(ax,(2.8,3.25),(4.1,3.25),ORANGE)
label(ax,3.45,2.62,'nạp cả khối',16,ORANGE,'center')
arrow(ax,(6.7,3.25),(8.0,3.25),BLUE)
label(ax,7.35,2.62,'lấy 10',17,BLUE,'center')
box(ax,8.1,2.95,1.6,.6,'10 × 2',BLUE,20)
label(ax,.15,2.02,'2. Đọc tiếp 12: đã có sẵn trong cache',21,weight=600)
label(ax,1.55,1.05,'Không cần nạp lại\nkhối này từ RAM',18,MUTED,'center')
for i,v in enumerate(A.ravel()[:4]):
    cell(ax,4.2+i*.6,.76,.6,.6,v,GREEN if i==1 else BLUE,selected=i==1,size=20)
arrow(ax,(6.7,1.06),(8.0,1.06),GREEN)
label(ax,7.35,.46,'lấy 12',17,GREEN,'center')
box(ax,8.1,.76,1.6,.6,'12 × 2',GREEN,20)
label(ax,5,.08,'Khối 4 ô chỉ để minh hoạ cách nạp dữ liệu',16,MUTED,'center')
save(fig,'memory-cache.svg','Hai bước của cùng phép nhân: khối chứa 10,12,11,20 được nạp từ RAM vào cache khi chưa có; đọc tiếp 12 dùng dữ liệu đã nạp. Khối 4 ô là mô hình minh hoạ, không phải kích thước cache line thực tế.')


# Địa chỉ A[2,1]: hai bước hàng rồi một bước cột.
assert A[2,1]==33 and A.strides==(24,8)
fig,ax=canvas(5.05)
label(ax,.25,4.74,'A[2, 1] = 33',23,BLUE,weight=600)
matrix(ax,.8,2.24,A,.50,selection={(2,1)})
box(ax,4.1,2.6,5.4,1.12,'Strides: bước dịch theo mỗi chiều (byte)\nA.strides = (24, 8)\n+1 hàng: +24 byte     +1 cột: +8 byte',BLUE,18)
label(ax,6.8,2.15,'2 × 24 + 1 × 8 = 56 byte',21,BLUE,'center',600)
buffer(ax,.70,selection={7})
arrow(ax,(.735,1.73),(5.355,1.73),BLUE)
label(ax,3.045,2.02,'2 bước hàng: +48 byte',18,BLUE,'center')
arrow(ax,(5.355,1.44),(6.125,1.44),ORANGE)
label(ax,7.75,1.6,'1 bước cột: +8 byte',17,ORANGE,'center')
for x,y in [(.735,1.7),(5.355,1.7),(6.125,1.4)]:
    ax.plot([x,x],[1.32,y],color=MUTED,lw=1,ls=':')
save(fig,'strides-addressing.svg','A[2,1] là 33, độ lệch 56 byte. Đi hai bước hàng 24 byte và một bước cột 8 byte từ đầu A. Strides đo bằng byte.')

fig,ax=canvas(1.45)
for i,v in enumerate(A.ravel()):
    cell(ax,.35+i*.77,.50,.77,.65,v,ROW_COLORS[i//3],size=22)
label(ax,5,.25,'Vùng dữ liệu của A, bắt đầu từ ô 10',17,MUTED,'center')
save(fig,'strides-exercise.svg','Dãy 12 giá trị của A để sinh viên tự xác định độ lệch byte. Không ghi sẵn đáp án địa chỉ.')

fig,ax=canvas(4.75)
label(ax,.25,4.43,'B = A[:2, 1:]',22,weight=600)
selected={(r,c) for r in range(2) for c in [1,2]}
matrix(ax,.9,1.03,A,.7,selected)
matrix(ax,6.0,1.78,A[:2,1:],.85)
arrow(ax,(3.65,2.48),(5.55,2.48))
label(ax,2, .56,'A.shape = (4, 3)',18,MUTED,'center')
label(ax,6.85,1.15,'B.shape = (2, 2)',18,BLUE,'center')
save(fig,'slicing-selection.svg','A[:2,1:] lấy [[12,11],[21,24]], tạo view offset 8 byte và strides (24,8).')

B=A[:,::2]
assert B.shape==(4,2) and B.strides==(24,16) and np.shares_memory(A,B)
fig,ax=canvas(4.75)
label(ax,.25,4.43,'B = A[:, ::2]',22,weight=600)
matrix(ax,.8,1.65,B,.54)
box(ax,4.1,2.25,5.5,1.36,'shape = (4, 2)\nstrides = (24, 16)\nDùng chung dữ liệu với A',BLUE,17)
buffer(ax,.8,selection={r*3+c for r in range(4) for c in [0,2]})
save(fig,'strided-view.svg','A[:,::2] là view shape(4,2), strides(24,16); ô có màu là phần tử được chọn.')

fig,ax=canvas(4.65)
label(ax,.5,4.3,'A',22,BLUE,weight=600)
label(ax,6,4.3,'A.T',22,ORANGE,weight=600)
matrix(ax,.9,1.2,A,.62)
matrix(ax,6,1.6,A.T,.62)
arrow(ax,(3.6,2.5),(5.55,2.5))
label(ax,2,.7,'shape (4, 3)\nstrides (24, 8)',17,MUTED,'center')
label(ax,7.1,.7,'shape (3, 4)\nstrides (8, 24)',17,MUTED,'center')
label(ax,5,.16,'Hàng thành cột, cột thành hàng; dữ liệu vẫn ở nguyên chỗ',17,MUTED,'center')
save(fig,'transpose-layout.svg','A.T dùng chung dữ liệu, đổi shape từ(4,3) sang(3,4) và hoán đổi strides.')

# Hai đường thực thi: bytecode được thông dịch và vòng lặp mã máy có sẵn.
fig,ax=canvas(5.5)
label(ax,2.45,5.18,'Python (CPython)',23,ORANGE,'center',600)
label(ax,7.5,5.18,'NumPy',23,BLUE,'center',600)
ax.plot([5,5],[.12,5.35],color='#dddddd',lw=1)
box(ax,.55,4.35,3.8,.5,'[v * 2 for v in xs]',ORANGE,19)
box(ax,5.6,4.35,3.8,.5,'Vòng lặp viết bằng C',BLUE,19)
arrow(ax,(2.45,4.32),(2.45,3.66),ORANGE)
arrow(ax,(7.5,4.32),(7.5,3.66),BLUE)
label(ax,2.68,4.0,'biên dịch',16,MUTED)
label(ax,7.73,4.0,'biên dịch sẵn',16,MUTED)
box(ax,1.4,3.12,2.1,.5,'Bytecode',ORANGE,20)
box(ax,6.45,3.12,2.1,.5,'Mã máy',BLUE,20)
arrow(ax,(2.45,3.08),(2.45,2.62),ORANGE)
arrow(ax,(7.5,3.08),(7.5,2.62),BLUE)
# Khung runtime và mũi tên quay lại chỉ rõ vị trí lặp.
box(ax,.35,1.05,4.2,1.55,'',ORANGE)
box(ax,5.4,1.05,4.2,1.55,'',BLUE)
label(ax,2.45,2.34,'Trình thông dịch',20,ORANGE,'center',600)
label(ax,7.5,2.34,'Vòng lặp mã máy',20,BLUE,'center',600)
label(ax,.62,1.83,'Đọc lệnh',18)
label(ax,2.72,1.83,'Xử lý int',18)
arrow(ax,(1.8,1.83),(2.57,1.83),ORANGE)
label(ax,7.5,1.83,'Đọc số → × 2 → ghi số',18,INK,'center')
for left,color in [(0,ORANGE),(5.05,BLUE)]:
    ax.annotate('',xy=(left+1.15,1.57),xytext=(left+3.7,1.57),
        arrowprops={'arrowstyle':'->','color':color,'lw':2,
                    'connectionstyle':'arc3,rad=-0.25'})
# Cùng ba giá trị; Python xử lý đối tượng, NumPy xử lý ô số.
for i,v in enumerate([10,12,11]):
    box(ax,.65+i*1.2,.18,.85,.45,str(v),ORANGE,18)
    cell(ax,6.15+i*.9,.18,.9,.45,v,BLUE,size=18)
label(ax,2.45,.83,'các đối tượng int của list',15,MUTED,'center')
label(ax,7.5,.83,'các ô int64 trong mảng',15,MUTED,'center')
save(fig,'interpreted-compiled.svg','CPython biên dịch mã Python thành bytecode rồi thông dịch; vòng lặp số học C của NumPy được biên dịch sẵn thành mã máy. Mũi tên quay lại thể hiện phần công việc lặp. Cả hai chạy trên CPU; sơ đồ dữ liệu giản lược, không mô tả địa chỉ vật lý.')

# Lọc số chẵn: màu của ô được giữ từ A qua mask tới kết quả.
fig,ax=canvas(4.8)
mask = A % 2 == 0
label(ax,2.2,4.5,'A',22,INK,'center',600)
label(ax,7.2,4.5,'mask = (A % 2 == 0)',21,INK,'center',600)
for r in range(4):
    for c in range(3):
        color=ROW_COLORS[r]
        cell(ax,1.0+c*.8,1.95+(3-r)*.52,.8,.52,A[r,c],color,bool(mask[r,c]),19)
        cell(ax,5.85+c*.9,1.95+(3-r)*.52,.9,.52,str(bool(mask[r,c])),color,bool(mask[r,c]),17)
arrow(ax,(3.7,3.0),(5.5,3.0))
label(ax,4.6,3.4,'Số chẵn?',18,INK,'center')
label(ax,5,1.55,'A[mask] lấy các giá trị ở ô True',20,INK,'center',600)
for i,v in enumerate(A[mask]):
    cell(ax,1.4+i*.9,.65,.9,.60,v,VALUE_COLORS[int(v)],True,21)
label(ax,5,.25,'shape = (8,)',17,MUTED,'center')
save(fig,'boolean-selection.svg','A % 2 == 0 đánh dấu các số chẵn. Màu mỗi hàng được giữ trong mask và kết quả [10,12,20,24,30,40,44,42], đọc theo thứ tự hàng; shape (8,).')

fig,ax=canvas(4.4)
label(ax,5,4.1,'A[[0, 2], [1, 2]]',24,INK,'center',600)
label(ax,1.05,3.35,'Hàng',18,MUTED,'center')
label(ax,2.15,3.35,'Cột',18,MUTED,'center')
for y,r,c,v,color in [(2.55,0,1,12,BLUE),(1.6,2,2,31,GREEN)]:
    cell(ax,.7,y,.7,.6,r,color,size=22)
    cell(ax,1.8,y,.7,.6,c,color,size=22)
    arrow(ax,(2.65,y+.3),(3.2,y+.3),color)
    label(ax,3.4,y+.3,f'A[{r}, {c}] = {v}',21,color)
matrix(ax,7.0,1.0,A,w=.6,selection={(0,1),(2,2)})
label(ax,3.0,.8,'Ghép các chỉ mục cùng vị trí.',20,INK,'center')
label(ax,5,.25,'Kết quả: [12, 31]     shape = (2,)',21,INK,'center')
save(fig,'index-pairs.svg','Chỉ mục hàng thứ nhất 0 ghép với chỉ mục cột thứ nhất 1: A[0,1]=12. Cặp thứ hai 2 và 2: A[2,2]=31. Kết quả [12,31].')

fig,ax=canvas(4.4)
label(ax,5,4.1,'A[np.ix_([0, 2], [1, 2])]',24,INK,'center',600)
label(ax,5,3.6,'Lấy cột 1 và 2 ở mỗi hàng 0 và 2.',21,INK,'center')
matrix(ax,1.1,.65,A,w=.6,selection={(0,1),(0,2),(2,1),(2,2)})
arrow(ax,(3.45,1.9),(5.15,1.9))
for r,source_r in enumerate([0,2]):
    for c,source_c in enumerate([1,2]):
        cell(ax,5.8+c*1.15,1.2+(1-r)*.8,1.15,.8,A[source_r,source_c],ROW_COLORS[source_r],size=24)
    label(ax,8.3,1.6+(1-r)*.8,f'hàng {source_r}',18,MUTED)
label(ax,6.95,.65,'shape = (2, 2)',20,MUTED,'center')
save(fig,'index-grid.svg','np.ix_ chọn cả cột 1 và 2 ở từng hàng 0 và 2. Hàng 0 cho [12,11], hàng 2 cho [33,31], tạo mảng kết quả shape (2,2).')

fig,ax=canvas(3.9)
label(ax,1.8,3.6,'A',22,BLUE,'center',600)
matrix(ax,.85,.4,A,.63,selection={(2,1)})
arrow(ax,(3.15,1.8),(4.25,1.8))
label(ax,6.8,2.8,'A[2, 1] = 33',25,BLUE,'center',600)
label(ax,6.8,2.0,'hàng 2, cột 1',23,INK,'center')
label(ax,6.8,1.2,'Chỉ mục bắt đầu từ 0.',20,MUTED,'center')
save(fig,'index-basics.svg','A[2,1] chọn phần tử 33 tại giao của hàng 2 và cột 1, chỉ mục bắt đầu từ 0.')
fig,ax=canvas(4.4)
label(ax,1.8,4.08,'A',22,BLUE,'center',600)
matrix(ax,.85,.8,A,.63,selection={(r,c) for r in [0,1] for c in [1,2]})
arrow(ax,(3.15,2.05),(5.3,2.05))
label(ax,4.3,2.65,'A[:2, 1:]',21,BLUE,'center',600)
matrix(ax,6.05,1.38,A[:2,1:],.68)
label(ax,7.0,.85,'shape (2, 2)',19,MUTED,'center')
label(ax,5,.25,':2 → hàng 0, 1       1: → cột 1, 2',20,INK,'center')
save(fig,'slice-basics.svg','A[:2,1:] chọn hai hàng đầu và các cột từ 1 đến cuối. Kết quả [[12,11],[21,24]], chưa bàn về cơ chế bộ nhớ.')

# Hai hướng dùng lại số trong broadcasting.
for mode in ['columns','rows']:
    fig,ax=canvas(3.9)
    column_mode=mode=='columns'
    delta=np.array([1,2,3]) if column_mode else np.array([10,20,30,40])[:,None]
    result=A+delta
    label(ax,2.2,3.65,'A + b' if column_mode else 'A + d[:, None]',23,INK,'center',600)
    for r in range(4):
        for c in range(3):
            color=ROW_COLORS[c] if column_mode else ROW_COLORS[r]
            cell(ax,1.3+c*.65,.8+(3-r)*.55,.65,.55,A[r,c],color,size=19)
            cell(ax,6.5+c*.65,.8+(3-r)*.55,.65,.55,result[r,c],color,size=19)
    if column_mode:
        for c,v in enumerate(delta):label(ax,1.3+(c+.5)*.65,3.25,f'+{v}',20,ROW_COLORS[c],'center',600)
    else:
        for r,v in enumerate(delta[:,0]):label(ax,.85,.8+(3-r+.5)*.55,f'+{v}',20,ROW_COLORS[r],'center',600)
    arrow(ax,(3.7,1.9),(5.9,1.9))
    label(ax,4.8,2.4,'cộng theo cột' if column_mode else 'cộng theo hàng',18,INK,'center')
    label(ax,7.5,3.65,'Kết quả',22,INK,'center',600)
    label(ax,5,.3,'b.shape = (3,)' if column_mode else 'd[:, None].shape = (4, 1)',20,INK,'center')
    save(fig,'broadcast-'+mode+'.svg','Cộng [1,2,3] theo cột.' if column_mode else 'Cộng [10,20,30,40] theo hàng. Màu nối số được cộng và phần tử kết quả.')
