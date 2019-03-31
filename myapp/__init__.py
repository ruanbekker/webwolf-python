import os
from flask import Flask

name = os.environ['NAME']

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, {}".format(name)

if __name__ == "__main__":
    app.run()
