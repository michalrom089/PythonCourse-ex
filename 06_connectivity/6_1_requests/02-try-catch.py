"""test api: https://jsonplaceholder.typicode.com/
"""

import requests
import traceback


def get_example():
    base_url = 'https://jsonplaceholder.typicode.com/{endpoint}'

    url = base_url.format(endpoint='todos1/1')

    resp = requests.get(url)
    if resp.status_code == 200:
        json = resp.json()
    else:
        raise Exception(f"Exception raised, Status code: {resp.status_code}")

    return json


if __name__ == '__main__':
    try:
        get_example()
    except Exception:
        print(traceback.print_exc())
