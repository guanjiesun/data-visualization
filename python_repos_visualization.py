import requests

from plotly.graph_objs import Bar
from plotly import offline


def main():
    # 执行web api调用
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")

    # 将json格式的响应体转换为python字典
    response_dict = r.json()
    repo_dicts = response_dict['items']
    # 保存每一个仓库的信息
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    # 可视化仓库流行的python仓库信息
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'Popular Python Repos (Sorted by Stars)',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository Names',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },

    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='./saved_files/python_repos.html')


if __name__ == '__main__':
    main()
