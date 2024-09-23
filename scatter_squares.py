import matplotlib.pyplot as plt


def main():
    # 生成数据
    x_values = list(range(1, 101))
    y_values = [pow(x, 2) for x in x_values]

    plt.style.use('seaborn-v0_8')

    # 绘制散点图
    fig, ax = plt.subplots()
    # 根据y值设置cmap
    ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.get_cmap('Blues'))

    # 设置坐标轴刻度属性, which指定要更改的是主刻度线(major ticks)
    ax.tick_params(axis='both', labelsize=14, which='major')

    # 设置每一个坐标轴的取值范围
    ax.axis([0, 110, 0, 11000])

    plt.show()


if __name__ == '__main__':
    main()
