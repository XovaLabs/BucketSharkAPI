from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.post("/v1/category/handler")
def update():
    payload = request.json
    print(payload['key'])
    return jsonify({'piza': 1})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
