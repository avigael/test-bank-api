from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

import accounts

app = Flask(__name__)
api = Api(app)

CORS(app)

class APP(Resource):
    def get(self):
        return jsonify({
            'author': 'Avigael <code@gaels.us>',
            'info': 'https://github.com/avigael/test-bank-api'
        })


class API(Resource):
    def get(self):
        amount = int(request.args.get("amount", 1))
        acc = accounts.get_accounts(amount)
        return acc

api.add_resource(APP, '/')
api.add_resource(API, '/api')

if __name__ == '__main__':
    app.run(debug=False)
