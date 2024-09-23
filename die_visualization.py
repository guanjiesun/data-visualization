from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


def make_one_die(num_sides=6, roll_number=1000):
    # 实例化一个六面的骰子
    die = Die(num_sides=num_sides)

    # 投一千次骰子，记录每次的点数
    results = []
    for _ in range(roll_number):
        result = die.roll()
        results.append(result)

    # 统计每一个点数出现的次数
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # 可视化结果
    x_values = list(range(1, die.num_sides+1))
    data = [Bar(x=x_values, y=frequencies)]

    # 配置坐标轴的属性
    x_axis_config = {'title': 'result'}
    y_axis_config = {'title': 'frequency of corresponding result'}

    # 指定图表布局和配置
    layout = Layout(title=f"One die: d{die.num_sides}",
                    xaxis=x_axis_config, yaxis=y_axis_config)

    # 生成文件名
    target = f"d{die.num_sides}.html"
    # 生成条形图并保存文件
    offline.plot({'data': data, 'layout': layout}, filename='./saved_files/'+target)


def make_two_dice():
    # 创建两个骰子
    die1 = Die(num_sides=6)
    die2 = Die(num_sides=6)

    # 同时投掷这两个骰子若干次，保存它们点数之和
    results = [die1.roll() + die2.roll() for _ in range(1000)]
    # results = []
    # for _ in range(1000):
    #     result = die1.roll() + die2.roll()
    #     results.append(result)

    # 统计每一个点数出现的次数
    min_result = 2
    max_result = die1.num_sides + die2.num_sides
    frequencies = [results.count(value) for value in range(min_result, max_result+1)]
    # frequencies = []
    # for value in range(min_result, max_result+1):
    #     frequency = results.count(value)
    #     frequencies.append(frequency)

    # 可视化结果
    x_values = list(range(min_result, max_result+1))
    data = [Bar(x=x_values, y=frequencies)]

    # 配置坐标轴的属性
    x_axis_config = {'title': 'result', 'dtick': 1}
    y_axis_config = {'title': 'frequency of corresponding result'}

    # 指定图表布局和配置
    layout = Layout(title=f"Two dice: d{die1.num_sides} and d{die2.num_sides}",
                    xaxis=x_axis_config, yaxis=y_axis_config)

    # 生成条形图并保存文件
    offline.plot({'data': data, 'layout': layout}, filename='./saved_files/d6_d6.html')


def main():
    # 指定骰子的面数和投掷骰子的次数
    # make_one_die(num_sides=6, roll_number=2_000)

    # 一次投掷两个六面骰子
    make_two_dice()


if __name__ == '__main__':
    main()
