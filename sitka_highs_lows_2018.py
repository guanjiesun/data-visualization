import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_highs_lows_dates(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)

        # 获取f的表头
        header = next(reader)
        print(header)
        # 打印表头字段信息
        for i, column in enumerate(header):
            print(i, column)

        # 获取最高温度和日期
        highs, dates, lows = list(), list(), list()
        for row in reader:
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
            highs.append(int(row[5]))
            lows.append(int(row[6]))

        return highs, lows, dates


def plot_highs_lows(highs, lows, dates):
    """绘制每日最高温度"""
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.set_title("Max and Min temp in 2018")
    ax.plot(dates, highs, c='red', alpha=0.6, label='Max Temp')
    ax.plot(dates, lows, c='blue', alpha=0.6, label='Min Temp')

    # 填充highs和lows之间的空间
    ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)

    # 显示图例
    plt.legend()

    # 保存图片
    plt.savefig('./saved_figures/sitka_highs_lows_2018.pdf',
                format='pdf', bbox_inches='tight', pad_inches=0.1)

    # 显示图片
    plt.show()


def main():
    # 数据集: 七月份sitka地区的每天的天气信息
    filename = './datasets/sitka_weather_07-2018_simple.csv'
    # 数据集: 2018年sitka地区的每天的天气信息
    filename = './datasets/sitka_weather_2018_simple.csv'

    # 获取最高温度、最低温度和日期
    highs, lows, dates = get_highs_lows_dates(filename)

    # 绘制每日最高温度
    plot_highs_lows(highs, lows, dates)


if __name__ == '__main__':
    main()
