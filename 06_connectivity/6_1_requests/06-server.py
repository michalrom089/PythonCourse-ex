from flask import Flask, request
import json

app = Flask(__name__)
ids = []


@app.route("/append_id", methods=['POST'])
def append_id():
    content = request.data
    j = json.loads(content)
    ids.append(j['id'])
    print(ids)

    return 'Ok'


if __name__ == "__main__":
    app.run()
