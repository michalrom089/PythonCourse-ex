"""test api: https://jsonplaceholder.typicode.com/
"""

import requests
import traceback


def get_example(id):
    url = f'https://jsonplaceholder.typicode.com/todos/{id}'

    resp = requests.get(url)
    if resp.status_code == 200:
        json = resp.json()
    else:
        raise Exception(f"Exception raised, Status code: {resp.status_code}")

    return json


if __name__ == '__main__':
    id = 2

    try:
        j = get_example(id)
        print(j)
    except Exception:
        print(traceback.print_exc())
