"""test api: https://jsonplaceholder.typicode.com/
"""

import requests
import traceback


def get_example(userId):
    url = f'https://jsonplaceholder.typicode.com/posts'
    params = {
        'userId': userId
    }

    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        json = resp.json()
    else:
        raise Exception(f"Exception raised, Status code: {resp.status_code}")

    return json


if __name__ == '__main__':
    userId = 1

    try:
        j = get_example(userId)
        print(j)
    except Exception:
        print(traceback.print_exc())
