import json
from pathlib import Path

import plotly.express as px
import pandas as pd


def main():
    """绘制过去一天或者三十天的全球地震散点图"""

    # filename = Path('./datasets/eq_data_1_day_m1.json')
    filename = Path('./datasets/eq_data_30_day_m1.json')
    with open(filename, newline='') as f:
        # eq_data是一个庞大的字典
        eq_data = json.load(f)

    # 将eq_data转存到另一个文件中
    readable_file = Path('./datasets/readable_' + filename.stem + '.json')
    with open(readable_file, 'w') as f:
        # json.dump接收Python字典对象和文件对象f，即将转存到f中
        json.dump(eq_data, f, indent=4)

    # 提取所有地震的震级,标题和位置数据（经度和纬度）
    all_eq_dicts = eq_data['features']
    mags, titles, longitudes, latitudes = list(), list(), list(), list()
    for eq_dict in all_eq_dicts:
        mags.append(eq_dict['properties']['mag'])
        titles.append(eq_dict['properties']['title'])
        longitudes.append(eq_dict['geometry']['coordinates'][0])
        latitudes.append(eq_dict['geometry']['coordinates'][1])

    # 基于提取的地震相关信息，绘制散点图
    df = pd.DataFrame(
        data=zip(longitudes, latitudes, titles, mags),
        columns=['longitude', 'latitude', 'title', 'magnitude']
    )

    fig = px.scatter(
        df,
        x='longitude',  # x_values = df['longitude']
        y='latitude',   # y_values = df['latitude']
        title='Scatter Graph of Global Earthquakes',  # 图表标题
        size='magnitude',  # 震级越大，散点的尺寸越大
        size_max=10,  # 散点尺寸的最大值
        color='magnitude',  # 震级越大，散点的颜色越深
        hover_name='title',  # 鼠标悬停在散点之上的时候，显示data中title字段对应的内容
    )

    # 保存html文件
    fig.write_html('./saved_files/global_earthquakes.html')

    # 显示图片
    fig.show()


if __name__ == '__main__':
    main()
