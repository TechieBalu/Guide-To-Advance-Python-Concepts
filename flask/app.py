from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "This is welcome page"

@app.route("/hello")
def hello():
    return "This is hello"


# Building Dynami URL 1st type 
@app.route("/success/<int:score>")
def success(score):
    return "This is pass" + str(score)


@app.route("/fail/<int:score>")
def fail(score):
    return "This is pass" + str(score)

if __name__ == "__main__":
    app.run(debug=True)