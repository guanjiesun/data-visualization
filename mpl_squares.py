import matplotlib.pyplot as plt


def main():
    """数据可视化初探"""

    # 准备数据
    numbers = [1, 2, 3, 4, 5]
    squares = [pow(number, 2) for number in numbers]

    # 生成图表
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(numbers, squares, linewidth=3, color='red')

    # 设置坐标轴刻度的样式
    ax.tick_params(axis='both', labelsize=10)

    # 设置坐标轴标签
    ax.set_xlabel('Numbers', fontsize=14)
    ax.set_ylabel('Squares', fontsize=14)

    # 设置图表标题
    ax.set_title("Square Numbers", fontsize=18)

    # 保存图片
    plt.savefig('./saved_figures/mpl_squares.pdf',
                format='pdf', bbox_inches='tight', pad_inches=0.1)

    # 显示图表
    plt.show()


if __name__ == '__main__':
    main()
