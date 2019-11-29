import requests
from datetime import datetime

if __name__ == '__main__':
    # Get acccess token
    HOST = 'http://localhost:5000/{endpoint}'
    CLIENT_ID = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
    CLIENT_SECRET = 'TWljaGHFgiBCYXJ0b3N6a2lld2ljeiEh'

    auth_headers = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    auth_resp = requests.post(HOST.format(endpoint='auth'), headers=auth_headers).json()

    # Get data
    data_params = {
        'start_date': datetime(2019, 10, 6).strftime("%d-%b-%Y"),
        'end_date': datetime(2019, 10, 7).strftime("%d-%b-%Y")
    }
    data_headers = {
        'Authorization': auth_resp['access_token']
    }
    data_resp = requests.get(HOST.format(endpoint='data'), params=data_params, headers=data_headers).json()

    print(data_resp['value'])