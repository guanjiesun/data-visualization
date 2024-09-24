import requests
import json


def main():
    """获取响应体然后将内容保存到一个json文件中"""

    url = 'http://api.github.com'
    response = requests.get(url)
    print(response.status_code)
    print(response.encoding)
    print(response.headers.get('Content-Type'))

    # 将json格式的字符串写入文件
    with open('./datasets/github.json', 'w') as f:
        f.write(response.text)

    # json.load 从文件中读取 JSON 数据并将其转换为 Python 对象
    with open('./datasets/github.json', 'r') as f:
        data = json.load(f)

    # json.dump 将 Python 对象转换为 JSON 格式并写入文件
    with open('./datasets/readable_github.json', 'w') as f:
        # 这里增加里缩进，提高了json文件的可读性
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    main()
