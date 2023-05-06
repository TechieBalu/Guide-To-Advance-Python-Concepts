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


'''
You will need to program the part that handles the query arguments. This code will read in the language key by using either 
request.args.get('language') or request.args['language'].

By calling request.args.get('language'), the application will continue to run if the language key doesn’t exist in the URL. In that case, the result of the method will be None.

By calling request.args['language'], the app will return a 400 error if the language key doesn’t exist in the URL.

When dealing with query strings, it is recommended to use request.args.get() to prevent the app from failing.
'''


# http://127.0.0.1:5000/query-example-multiple-variables?language=Python&framework=Flask
# http://127.0.0.1:5000/query-example-multiple-variables?language=Python&framework=Flask&website=DigitalOcean
# http://127.0.0.1:5000/query-example-multiple-variables?framework=Flask&website=DigitalOcean


# Now let's create a URL in which framework field is missing
# ! It will generate error and give 404 Error
# ! http://127.0.0.1:5000/query-example-multiple-variables?language=Python&website=DigitalOcean
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
    

'''
Form data comes from a form that has been sent as a POST request to a route. So instead of seeing the data in the URL (except for cases when the form is submitted with a GET request), the form data will be passed to the app behind the scenes. Even though you cannot easily see the form data that gets passed, your app can still read it.

To demonstrate this, modify the form-example route in app.py to accept both GET and POST requests and returns a form:
'''

# allow both GET and POST requests
# http://127.0.0.1:5000/form-example
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    return '''
              <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
              </form>'''

'''

The browser should display a form with two input fields - one for language and one for framework - and a submit button.

The most important thing to know about this form is that it performs a POST request to the same route that generated the form. 
The keys that will be read in the app all come from the name attributes on our form inputs. In this case, language and 
framework are the names of the inputs, so you will have access to those in the app.

Inside the view function, you will need to check if the request method is GET or POST. If it is a GET request, 
you can display the form. Otherwise, if it is a POST request, then you will want to process the incoming data.
'''
# allow both GET and POST requests
# http://127.0.0.1:5000/form-example2?language=Python&framework=flask
@app.route('/form-example2', methods=['GET', 'POST'])
def form_example2():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == "__main__":
    app.run(debug=True)