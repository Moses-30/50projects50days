import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体或者宋体等
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# 创建一个新的图和轴
fig, ax = plt.subplots(figsize=(12, 8))

# 设定一些常量
x_positions = [1, 3, 5, 7]
stages = ["感觉异常期", '局部缺血期', '营养障碍期', '坏疽溃疡期']
pathways = ['炎症反应 (TGF-β/Smad)', '缺氧反应 (HIF-1α)', '代谢紊乱', '过度EMT激活 (TGF-β/Smad)']
effects = ['EMT激活', '新生血管形成', 'EMT部分抑制', '组织纤维化']

# 绘制每个阶段的矩形框和标题
for i, (x, stage) in enumerate(zip(x_positions, stages)):
    ax.add_patch(mpatches.Rectangle((x-0.5, 6), 1, 1, edgecolor='black', facecolor='lightblue'))
    ax.text(x, 6.5, stage, horizontalalignment='center', verticalalignment='center', fontsize=12, fontweight='bold')

# 绘制每个阶段的具体机制和效果
for i, (x, pathway, effect) in enumerate(zip(x_positions, pathways, effects)):
    ax.add_patch(mpatches.Rectangle((x-0.5, 3), 1, 2, edgecolor='black', facecolor='lightgreen'))
    ax.text(x, 4, pathway, horizontalalignment='center', verticalalignment='center', fontsize=10)
    ax.add_patch(mpatches.Rectangle((x-0.5, 0), 1, 2, edgecolor='black', facecolor='lightcoral'))
    ax.text(x, 1, effect, horizontalalignment='center', verticalalignment='center', fontsize=10)

# 连接矩形框的箭头
for x in x_positions:
    ax.annotate('', xy=(x, 5.5), xytext=(x, 4.5), arrowprops=dict(arrowstyle='->', lw=1.5))
    ax.annotate('', xy=(x, 2.5), xytext=(x, 1.5), arrowprops=dict(arrowstyle='->', lw=1.5))

# 设置轴的范围和标题
ax.set_xlim(0, 8)
ax.set_ylim(-1, 7)
ax.axis('off')

plt.title('EMT贯穿糖尿病足溃疡分期分证的病理机制', fontsize=16, fontweight='bold')
plt.show()
