"""Sơ đồ float32 tự vẽ; ví dụ kiểm chứng bằng struct và Fraction.
Nguồn: Oracle Numerical Computation Guide, IEEE Arithmetic;
https://docs.oracle.com/cd/E19957-01/806-3568/ncg_math.html
Chạy: .venv/bin/python -B 2627-1/img/lecture-03/scripts/gen_float_figures.py
"""
from pathlib import Path
import struct
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt, font_manager
from matplotlib.patches import Rectangle
OUT=Path(__file__).resolve().parent.parent
for f in (OUT.parent.parent/'revealjs/dist/theme/fonts/source-sans-pro').glob('*.ttf'):
    font_manager.fontManager.addfont(str(f))
plt.rcParams.update({'font.family':'Source Sans Pro','svg.fonttype':'path',
    'svg.hashsalt':'numpy-float-bits','figure.facecolor':'none','savefig.facecolor':'none','text.color':'#333333'})
bits=''.join(f'{b:08b}' for b in struct.pack('>f',6.5))
assert bits=='0'+'10000001'+'101'+'0'*20
fig,ax=plt.subplots(figsize=(10,4.5))
fig.subplots_adjust(left=.02,right=.98,top=.98,bottom=.02)
ax.set(xlim=(0,10),ylim=(0,4.5));ax.axis('off')
def text(x,y,s,size=19,color='#333333',weight=400):
    ax.text(x,y,s,ha='center',va='center',fontsize=size,color=color,weight=weight)
text(5,4.17,'6.5 = 1.101₂ × 2²',25,weight=600)
fields=[(.15,1.1,'Dấu: 1 bit',bits[0],'#E8890C'),(1.25,2.85,'Số mũ: 8 bit',bits[1:9],'#1E93AB'),(4.1,5.75,'Phần sau dấu chấm: 23 bit',bits[9:],'#2E8B57')]
for x,w,label,value,color in fields:
    text(x+w/2,3.5,label,17,color,600)
    ax.add_patch(Rectangle((x,2.55),w,.66,facecolor=color,alpha=.15))
    ax.add_patch(Rectangle((x,2.55),w,.66,fill=False,edgecolor=color,lw=1.6))
    text(x+w/2,2.88,value,18,color)
text(.7,2.05,'0: dương',17,'#E8890C')
text(2.68,2.02,'129 − 127 = 2',19,'#1E93AB')
text(6.99,2.02,'1 ngầm + .101… → 1.101₂',20,'#2E8B57')
text(5,1.25,'Số mũ được lưu = số mũ thực + 127',21)
text(5,.80,'127 là độ lệch cố định để mã hoá cả số mũ âm',18,'#666666')
text(5,.2,'Đọc lại: (+1) × (1 + 1/2 + 1/8) × 2² = 6.5',21,weight=600)
p=OUT/'float32-bits.svg'
fig.savefig(p,metadata={'Date':None,'Description':'IEEE 754 binary32 của 6.5: 0 | 10000001 | 10100000000000000000000. Số chuẩn hoá có bit 1 ngầm; exponent bias 127.'})
p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n')
plt.close(fig)
print(p)
