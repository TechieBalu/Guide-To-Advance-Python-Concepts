from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "This is welcome page"

@app.route("/hello")
def hello():
    return "This is hello"


if __name__ == "__main__":
    app.run(debug=True)