"""
Primary restful api to handle requests to handle UI requests

User Interactions
- Buy/Sell Stickers
    - Type of Sticker (id or name?)
    - Number of stickers
    - Market or Limit(min, max) Order

Display Information
- Display User Information
    - Types and Count of stickers owned
    - Balance
    - Username
    - Avatar



"""

from flask import Flask, abort, jsonify
from flask_restful import Resource, Api

import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse('postgres://gxspomxmufoybd:dskomEuwa9JYaxf8Jd7h8JYVKo@ec2-54-221-253-117.compute-1.amazonaws.com:5432/d62ndf8grb25cb')

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
cursor = conn.cursor()

app = Flask(__name__)
api = Api(app)



# def get(todo_id):
#     """
#     Get all placed orders
#     :param todo_id:
#     :return:
#     """
#     return {}
#
# def put(id, num, type):
#     """
#     Place a new Buying order
#     :param order:
#     :return:
#     """
#     order = {}
#
#
#     return {}

# class Sell(Resource):
#     """
#     Sell Api
#     """
#     def put(user, vol, price, ticker, isBuy, isMarket):
#         """
#         Creates a new order and enqueues it in the priority queue
#         :param order:
#         :return:
#         """
#         return

@app.route('/entity/', methods=['GET'])
def get_entities():
    """
    :return: All Users
    """
    cursor.execute(
        'SELECT * FROM "entity"'
    )
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/inventory/<int:user_id>', methods=['GET'])
def get_inventory(user_id):
    cursor.execute(
        'SELECT * FROM "inventory" WHERE "userid" = %s' % user_id
    )
    return jsonify(cursor.fetchall())

@app.route('/order/', methods=['GET'])
def get_orders():
    cursor.execute(
        'SELECT * FROM "order"'
    )
    return jsonify(cursor.fetchall())

@app.route('/ledger/', methods=['GET'])
def get_ledgers():
    cursor.execute(
        'SELECT * FROM "ledger"'
    )
    return jsonify(cursor.fetchall())


@app.route('/price_history/<string:ticker>', methods=['GET'])
def get_price_history(ticker):
    cursor.execute(
        'SELECT * FROM "%sPriceHistory"' % ticker
    )
    return jsonify(cursor.fetchall())

if __name__ == '__main__':
    app.run(debug=True)