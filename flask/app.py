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


# http://127.0.0.1:5000/query-example-multiple-variables?language=Python&framework=Flask
# http://127.0.0.1:5000/query-example-multiple-variables?language=Python&framework=Flask&website=DigitalOcean
# http://127.0.0.1:5000/query-example-multiple-variables?framework=Flask&website=DigitalOcean


# Now let's create a URL in which framework field is missing
# ! It will generate error and give 404 Error
# ! http://127.0.0.1:5000/query-example-multiple-variables?language=Python&website=DigitalOcean
'''
You will need to program the part that handles the query arguments. This code will read in the language key by using either 
request.args.get('language') or request.args['language'].

By calling request.args.get('language'), the application will continue to run if the language key doesn’t exist in the URL. In that case, the result of the method will be None.

By calling request.args['language'], the app will return a 400 error if the language key doesn’t exist in the URL.

When dealing with query strings, it is recommended to use request.args.get() to prevent the app from failing.
'''
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