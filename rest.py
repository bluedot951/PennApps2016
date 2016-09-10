"""
Primary restful api to handle requests to handle UI requests

User Interactions
- Buy/Sell Stickers
    - Number of stickers
    - Market or Limit(min, max) Order
    - Type of Sticker (id or name?)

Display Information
- Display User Information
    - Types and Count of stickers owned
    - Balance
    - Username
    - Avatar



"""
from flask import Flask
from flask_restful import Resource, Api
from requests import put, get

app = Flask(__name__)
api = Api(app)

class Buy(Resource):
    """
    Buy Api to place an order
    """
    def get(self, todo_id):
        """
        Get all placed orders
        :param todo_id:
        :return:
        """
        return {}

    def put(self, order):
        return {}

class Sell(Resource):
    """
    Sell Api
    """
    def put(self, order):
        return {}

api.add_resource(Buy, '/buy')

if __name__ == '__main__':
    app.run(debug=True)