from flask import Flask,redirect,url_for,request
from markupsafe import escape


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
    return "This is fail" + escape(str(score))


@app.route("/result/<int:score>")
def result(score):
    if score < 50: 
        result = "fail"
        # return redirect(url_for)
    else:
        result = "success"
        # return "This is pass " +str(score)
    
    return redirect(url_for(result,score=score))



#* Routes for Digital Ocean Course:

@app.route('/query-example')
def query_example():
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)


@app.route('/query-example-multiple-variables')
def query_example_multiple_variables():
    language = request.args.get('language')

    framework = request.args['framework']

    # if key doesn't exist, returns None
    website = request.args.get('website')

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)
    

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == "__main__":
    app.run(debug=True)