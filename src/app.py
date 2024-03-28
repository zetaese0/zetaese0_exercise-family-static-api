"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET', "POST"])
def handle_members():
    response_body = {}
    if request.method == "GET":
        print("Incoming GET request for all members")
        members = jackson_family.get_all_members()
        response_body["message"] = "OK"
        response_body["family"] = members
        return jsonify(response_body), 200
    
    if request.method == "POST":
        data = request.json
        print("Incoming POST request for ", data)
        jackson_family.add_member(data)
        response_body["message"] = "Successfully updated"
        response_body["person"] = data
        return response_body, 201

@app.route('/members/<int:id>', methods=["GET", "DELETE", "PUT"])
def handle_member(id):
    response_body = {}
    if request.method == "GET":
        member = jackson_family.get_member(id)
        if member:
            response_body["message"] = "OK"
            response_body["member"] = member
            return response_body, 200
        response_body["message"] = "Person doesn't exists"
        return response_body, 404
    
    if request.method == "DELETE":
        deleted = jackson_family.delete_member(id)
        if deleted == False:
            response_body["message"] = "Person doesn't exists"
            return response_body, 404
        response_body["message"] = "Person deleted"
        return response_body, 200
    
    if request.method == "PUT":
        data = request.json
        updated_member = jackson_family.update_member(id, data)
        if updated_member != "Error1" and updated_member != "Error2":
            response_body["message"] = "Person updated successfully"
            response_body["result"] = updated_member
            return response_body, 200
        if updated_member == "Error1":
            response_body["message"] = "Invalid body"
            return response_body, 406
        if updated_member == "Error2":
            response_body["message"] = "Person doesn't exist"
            return response_body, 404

    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
