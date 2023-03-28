from flask import Flask, jsonify

class User:
    def signup(self):
        user={
            "_first name":"",
            "last name":"",
            "email":"",
            "password":"",
            "address":"",
            "address2":"",
            "city":"",
            "state":"",
            "zip":""
        }
        return jsonify(user),200
    