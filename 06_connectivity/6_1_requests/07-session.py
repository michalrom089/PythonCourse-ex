"""test api: https://jsonplaceholder.typicode.com/
"""

import requests
import traceback


def get_example(session, userId):
    url = 'http://localhost:5000/append_id'
    params = {
        'id': userId
    }

    resp = session.post(url, params=params)
    if resp.status_code == 200:
        print('Adding suceeded')
    else:
        raise Exception(f"Exception raised, Status code: {resp.status_code}")


if __name__ == '__main__':

    try:
        with requests.Session() as s:
            s.headers.update({
                'Accept': 'application/json',
                'Authorization': 'token=123'
            })
            j = get_example(s, 7)
            j = get_example(s, 5)
    except Exception:
        print(traceback.print_exc())
