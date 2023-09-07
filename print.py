import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False

year = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
tudi = [1.09, 1.5, 1.87, 2.28, 2.78, 3.41, 4.03, 4.47, 4.79, 5.12, 5.3, 5.55]  # 土地流转面积
laodong = [2.25, 2.3, 2.42, 2.53, 2.63, 2.69, 2.74, 2.77, 2.81, 2.89, 2.95, 3.13]  # 农村劳动力转移数（亿人）
mianji = [8.07, 12.1, 14.7, 17.8, 21.5, 25.7, 30.4, 33.3, 35.3, 38.2, 41.78, 44.88]  # 流转面积占家庭承包面积比例（%）




fig = plt.figure()
# 通过 add_subplot 方式创建两个坐标轴，相当于在同一个子图上叠加了两对坐标系
ax = fig.add_subplot(111, label="1")
ax2 = fig.add_subplot(111, label="2", frame_on=False)
# ax3 = fig.add_subplot(111, label="3", frame_on=False)
# 绘制图1并将绘图句柄返回，以便添加合并图例
lns1 = ax.plot(year, tudi, color='#ff6633', label='土地流转面积（亿亩）', marker='o')
for a, b in zip(year, tudi):
    ax.text(a, b, b, ha='right', va='bottom', fontsize=12, color='#ff6633')
lns = lns1
lns2 = ax.plot(year, laodong, color='#009900', label='农村劳动力转移数（亿人）', marker='s')
for a, b in zip(year, laodong):
    ax.text(a, b, b, ha='left', va='top', fontsize=12, color='#009900')
lns += lns2
lns3 = ax2.plot(year, mianji, color='#1608e3', label='流转面积占家庭承包面积比例（%）', marker='^')
for a, b in zip(year, mianji):
    ax2.text(a, b, b, ha='left', va='top', fontsize=12, color='#1608e3')
lns += lns3
# 调整第二对坐标轴的label和tick位置，以实现双X轴双Y轴效果
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right')
# ax3.yaxis.tick_right()

ax.set_xticks(year)
ax2.set_xticks(year)

# 设置坐标轴标注
ax.set_xlabel("年份", fontsize=14)
# ax.set_ylabel("农村劳动力转移数(亿人)", fontsize=14)
# ax3.set_ylabel('流转面积占家庭承包面积比例(%)', fontsize=14)
# 设置图表标题
fig.suptitle("", fontsize=16)

# 设置坐标轴刻度颜色
# ax.tick_params(axis='y', colors=c1)
ax2.tick_params(axis='y', colors='#1608e3')

# 设置坐标轴线颜色
# ax.spines["left"].set_color("#7ae677")   # 修改左侧颜色
ax.spines["right"].set_color("#1608e3")   # 修改右侧颜色


# 添加图例
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=2, fontsize=12)

plt.tight_layout()
plt.show()

