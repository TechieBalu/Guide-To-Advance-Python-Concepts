''' Copyright (C) 2022 by SeQuenX  - All Rights Reserved

* This file is part of the ComplyVantage product development,

* and is released under the "Commercial License Agreement".

*

* You should have received a copy of the Commercial License Agreement license with

* this file. If not, please write to: legal@sequenx.com, or visit www.sequenx.com

'''

from flask import Flask,redirect,url_for,request,jsonify, make_response
from markupsafe import escape
import requests
import publisher_local
import publisher_prod
from decouple import config
import json
from flask_cors import CORS
from flask_cors import cross_origin
import sys

app = Flask(__name__)
# CORS(app,origins='http://localhost:3000')
cors = CORS(app, resources={r"/signup": {"origins": "http://localhost:3000"}, r'/login':{"origins": "http://localhost:3000"},
                            r'/profile':{"origins": "http://localhost:3000"}, r'/repo-match/':{"origins": "http://localhost:3000"}, 
                            r'/repos/':{"origins": "http://localhost:3000"}})

# CORS(app)


@app.route('/matchrequest',methods=['POST'])
def CodeSignatureData():
    returnData = {"status":200}
    # data = jsonify(request.json)
    # print(data)
    print(request.json)
    print(type(request.json))
    publisher_local.publish(request.json)
    return  returnData



@app.route('/login',methods=["POST"])
@cross_origin()
def login():
    try: 
        if request.method == "POST":
            # json = jsonify(request.json)
            print(request.json)
            response = requests.post(
            url = config("LOGIN"),
            json = request.json,
            headers={"Accept": "application/json"}
            )
            print("\nSTATUS CODE: ",response.status_code)  # Print the status code
            # print("\nHEADERS: ",response.headers)  # Print the response headers
            print("\nTEXT: ",response.text)  # Print the response content as text
            # return make_response({"status" :response.status_code, "text":response.text},response.status_code)
            return make_response(response.text,response.status_code)
    except: 
        errors = json.dumps({"errors":"Requested server is not responding."})
        return make_response(errors, 503)

@app.route('/profile',methods=["GET", "PUT"])
@cross_origin()
def profile():
    if request.method == "GET":
        # json = jsonify(request.json)
        # print(request.json)
        # url = '127.0.0.1:8000/api/user/profile/'
        print("CONFIG: ", config("PROFILE"))
        headers = request.headers
        Authorization = headers.get("Authorization")
        Accept = headers.get("Accept")
        headers = {
            "Accept": Accept,
            "Authorization": Authorization
        }
        print(headers)
        # print("Headers in PROFILE: ",headers)
        # print(type(headers))
    
        response = requests.get(
            url = config("PROFILE"), 
            headers= headers
        )
        print(response.status_code)
        # print(type(response.text))
        # print("\nSTATUS CODE: ",response.status_code)  # Print the status code
        # print("\nHEADERS: ",response.headers)  # Print the response headers
        # print("\nTEXT: ",response.text)  # Print the response content as text
        # # return make_response({"status" :response.status_code, "text":response.text},response.status_code)
        return make_response(response.text,response.status_code)  
        # return "OK"  

    
    if request.method == "PUT":

        print("CONFIG: ", config("PROFILE"))
        headers = request.headers
        Authorization = headers.get("Authorization")
        Accept = headers.get("Accept")
        headers = {
            "Accept": Accept,
            "Authorization": Authorization
        }
        # data = json.loads(request.data)
        data = request.get_json()
        
        # Check if the request contains JSON data
        if not data:
            return jsonify({"error": "No JSON data provided."}), 400
        # try:
        check = data.get("firstName", None)
        if check != None:
            name = data["firstName"] + " " + data["lastName"]
            data["name"] = name
            response = requests.put(
                url = config("PROFILE"), 
                headers= headers,
                json = data
            )
            print(response.status_code)
            return make_response(response.text,response.status_code)  
        password = password2 = data.get("password", None)
        if password == None: 
            return jsonify({"error": "No JSON data provided."}), 400

        data = {
            "password": password,
            "password2": password2
        }
        response = requests.put(
            url = config("CHANGEPASS"), 
            headers= headers,
            json = data
        )
        print(response.status_code)
        return make_response(response.text,response.status_code)  
    

@app.route('/signup',methods=["POST", "OPTIONS"])
# @cross_origin(origin='http://localhost:3000')
@cross_origin()
def signup():
    try:
        data = request.data
        data = json.loads(data)

        print("DATA IS: \n", data)

        data["tc"] = True
        data["password2"] = data["password"]
        name = data["firstName"] + " " + data["lastName"]
        data["name"] = name
        # print(data)
        data.pop("firstName", "NO KEY FOUND")
        data.pop("lastName", "NO KEY FOUND")
        
        if request.method == "POST": 
            response = requests.post(
            url = config("SIGNUP"),
            json = data,
            headers={"Accept": "application/json"}
            )
        # print(response.status_code)  # Print the status code
        # print(response.headers)  # Print the response headers
        # print(response.text)  # Print the response content as text
        # print(response.json())  # Deserialize the JSON response content
        # print(response.url)
        return make_response(response.text,response.status_code)
    except: 
        errors = json.dumps({"errors":"Requested server is not responding."})
        return make_response(errors, 503)


@app.route('/repos/',methods=["GET"])
@cross_origin()
def repos():
    if request.method == "GET":
        # Creating Header
        headers = request.headers
        Authorization = headers.get("Authorization")
        Accept = headers.get("Accept")
        headers = {
            "Accept": Accept,
            "Authorization": Authorization
        }
    
        # Requesting to authenticate the User
        response = requests.get(
            url = config("PROFILE"), 
            headers= headers
        )

        # Request to get BOMDB results
        if response.status_code == 200:
            response = requests.get(
            url = config("REPO"), 
            headers= headers)
        print(response.status_code)
        print(response.text)

    return make_response(response.text)

# @app.route('/repo-match/',methods=["GET"])
# @cross_origin()
# def repo_match():
#     if request.method == "GET":
#         # Creating Header
#         # data = json.loads(request.data)
#         data = request.json
#         id = data["ID"]
#         headers = request.headers
#         Authorization = headers.get("Authorization")
#         Accept = headers.get("Accept")
#         headers = {
#             "Accept": Accept,
#             "Authorization": Authorization
#         }
    
#         # Requesting to authenticate the User
#         response = requests.get(
#             url = config("PROFILE"), 
#             headers= headers
#         )

#         # Request to get BOMDB results
#         if response.status_code == 200:
#             response = requests.get(
#                 data = json.dumps({"ID":id}),
#                 url = config("REPOMATCH"))
#         print(response.status_code)
#         print(response.text)

#     return make_response(response.text)




@app.route('/repo-match/<int:id>',methods=["GET"])
@cross_origin()
def repo_match(id):
    print("THIS IS ID: ", id)

    # return "ok"
    if request.method == "GET":
        # Creating Header
        # data = json.loads(request.data)
        
        headers = request.headers
        Authorization = headers.get("Authorization")
        Accept = headers.get("Accept")
        headers = {
            "Accept": Accept,
            "Authorization": Authorization
        }
    
        # Requesting to authenticate the User
        response = requests.get(
            url = config("PROFILE"), 
            headers= headers
        )

        # Request to get BOMDB results
        if response.status_code == 200:
            response = requests.get(
                data = json.dumps({"ID":id}),
                url = config("REPOMATCH"))
        print(response.status_code)
        print(response.text)

    return make_response(response.text)




if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True, port=5001)
    # config_path = '/path/to/your/.env'

    # # Load environment variables from the specified .env file
    # config.read(config_path)