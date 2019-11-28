import secrets
from datetime import datetime

SECRET_KEY = secrets.token_urlsafe(nbytes=32)
CLIENT_ID = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
CLIENT_SECRET = 'TWljaGHFgiBCYXJ0b3N6a2lld2ljeiEh'
DATA = [
    {'date': datetime(2019, 10, 1), 'value': 1},
    {'date': datetime(2019, 10, 2), 'value': 2},
    {'date': datetime(2019, 10, 3), 'value': 3},
    {'date': datetime(2019, 10, 4), 'value': 4},
    {'date': datetime(2019, 10, 5), 'value': 5},
    {'date': datetime(2019, 10, 6), 'value': 6},
    {'date': datetime(2019, 10, 7), 'value': 7},
    {'date': datetime(2019, 10, 8), 'value': 8},
    {'date': datetime(2019, 10, 9), 'value': 9}
]