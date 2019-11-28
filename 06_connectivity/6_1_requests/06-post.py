"""test api: https://jsonplaceholder.typicode.com/
"""

import requests
import traceback
import json


def get_example(userId):
    url = 'http://localhost:5000/append_id'
    data = json.dumps({
        'id': userId
    })

    resp = requests.post(url, data=data)
    if resp.status_code == 200:
        print('Adding suceeded')
    else:
        raise Exception(f"Exception raised, Status code: {resp.status_code}")


if __name__ == '__main__':
    userId = 1

    try:
        j = get_example(userId)
    except Exception:
        print(traceback.print_exc())
