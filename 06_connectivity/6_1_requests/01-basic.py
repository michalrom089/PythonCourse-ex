"""test api: https://jsonplaceholder.typicode.com/
"""

import requests


def get_example():
    base_url = 'https://jsonplaceholder.typicode.com/{endpoint}'

    url = base_url.format(endpoint='todos/1')
    resp = requests.get(url)

    print(resp.json())


if __name__ == '__main__':
    get_example()
