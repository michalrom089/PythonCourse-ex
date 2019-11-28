from flask import Flask, request

app = Flask(__name__)
ids = []


@app.route("/append_id", methods=['POST'])
def append_id():
    if 'Accept' in request.headers:
        print(f"Accept: {request.headers.get('Accept')}")
    if 'Authorization' in request.headers:
        print(f"Authorization: {request.headers.get('Authorization')}")

    if 'id' in request.args:
        id = request.args.get('id')
        ids.append(id)

    print(ids)

    return 'Ok'


if __name__ == "__main__":
    app.run()
