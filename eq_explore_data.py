import json


def main():
    filename = './datasets/eq_data_1_day_m1.json'
    with open(filename, newline='') as f:
        # eq_data是一个庞大的字典
        eq_data = json.load(f)

    # 将eq_data转存到另一个文件中
    readable_file = './datasets/readable_eq_data_1_day_m1.json'
    with open(readable_file, 'w') as f:
        # json.dump接收Python字典对象和文件对象f，即将转存到f中
        json.dump(eq_data, f, indent=4)


if __name__ == '__main__':
    main()
