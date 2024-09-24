import requests
import json


def main():
    # 执行api调用
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")

    # 响应体返回一个json格式的字符串，r.json方法将这个字符串转换为python字典
    response_dict = r.json()
    print(response_dict.keys())
    print(f"Total repositories: {response_dict['total_count']}")

    # 将响应体保存到文件中
    with open('./datasets/python_repos.json', 'w') as f:
        json.dump(r.json(), f, indent=4)

    # 搜索仓库的信息
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")

    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        print(f"\nName: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")


if __name__ == '__main__':
    main()
