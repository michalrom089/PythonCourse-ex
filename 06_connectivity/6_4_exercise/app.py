from flask import Flask, request, Response
import jwt
import json
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_pyfile('config.py')

# simulating database
sessions = []


@app.route("/auth", methods=['POST'])
def auth():
    """
    Generates the Auth Token
    :return: string
    """
    # Collecting request data
    client_id = request.headers.get('client_id')
    client_secret = request.headers.get('client_secret')

    # Request Validation
    if client_id is None:
        return Response('client_id not provided', 401)
    elif client_secret is None:
        return Response('client_secret not provided', 401)
    elif client_id != app.config.get('CLIENT_ID')\
            or client_secret != app.config.get('CLIENT_SECRET'):
        return Response('client not authorized', 401)

    # Calculating token
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, seconds=5),
            'iat': datetime.utcnow(),
            'sub': client_id
        }
        token = jwt.encode(payload, app.config.get('SECRET_KEY'), algorithm='HS256').decode('utf-8')
        sessions.append(token)
    except Exception as e:
        return e

    # Response
    return Response(json.dumps({
            'access_token': token
        }), 200)


@app.route("/data", methods=['GET'])
def get_data():
    # Collecting request data
    p_start_date = request.args.get('start_date', default=None, type=str)
    p_end_date = request.args.get('end_date', default=None, type=str)
    p_authorize = request.headers.get('Authorization')

    # Request Validation
    if p_start_date is None:
        return Response('start_date missing', 400)

    elif p_end_date is None:
        return Response('end_date missing', 400)

    elif p_authorize is None:
        return Response('Authorization header missing', 401)

    elif p_authorize not in sessions:
        return Response('client not authorized', 401)

    # Params parsing
    try:
        start_date = datetime.strptime(p_start_date, "%d-%b-%Y")
        end_date = datetime.strptime(p_end_date, "%d-%b-%Y")
    except Exception as e:
        return e

    # Data calculation
    sum = 0
    for d in app.config.get('DATA'):
        if d['date'] >= start_date and d['date'] <= end_date:
            sum = sum + d['value']

    # Response
    return Response(json.dumps({
        'value': sum
    }), 200)


if __name__ == "__main__":
    app.run()
