import matplotlib.pyplot as plt

from random_walk import RandomWalk


def main():
    # 实例化一个RandomWalk
    rw = RandomWalk(num_points=10_000, max_step=10)
    rw.fill_walk()

    # 可视化rw
    fig, ax = plt.subplots()
    point_numbers = list(range(rw.num_points))

    # 通过cmap反应随机漫步的路径
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.get_cmap('Blues'), edgecolors='none', s=10)

    # 突出显示随机漫步的起点和终点
    ax.scatter(rw.x_values[0], rw.y_values[0], s=50, c='red', edgecolors='none')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], s=50, c='orange', edgecolors='none')

    # 设置图表标题
    # ax.set_title("RandomWalk Visualization")

    # 隐藏坐标轴，沉浸式查看随机漫步路径
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 隐藏图表四个边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # 保存图片
    plt.savefig('./saved_figures/rw_visualization.pdf',
                format='pdf', bbox_inches='tight', pad_inches=0.1)

    # 显示图片
    plt.show()


if __name__ == '__main__':
    main()
