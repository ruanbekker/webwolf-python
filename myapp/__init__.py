import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    payload = {"status": 200, "message": "test message", "language": "python", "tags": ["programming", "web", "python"]}
    return jsonify(payload)

@app.route("/envs")
def envs():
    return jsonify(os.environ)

if __name__ == "__main__":
    app.run()
