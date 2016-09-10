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
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from requests import put, get
import os
import psycopg2
import urlparse

# urlparse.uses_netloc.append("postgres")
# url = urlparse.urlparse(os.environ["DATABASE_URL"])
# url = urlparse.urlparse('postgres://gxspomxmufoybd:dskomEuwa9JYaxf8Jd7h8JYVKo@ec2-54-221-253-117.compute-1.amazonaws.com:5432/d62ndf8grb25cb')
# print url.hostname
# print url.username
# print url.password
# print url.port
# conn = psycopg2.connect(
#     database=url.path[1:],
#     user=url.username,
#     password=url.password,
#     host='/tmp/',
#     port=url.port
# )
# cursor = conn.cursor()



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gxspomxmufoybd:dskomEuwa9JYaxf8Jd7h8JYVKo@ec2-54-221-253-117.compute-1.amazonaws.com:5432/d62ndf8grb25cb'
db = SQLAlchemy(app)
db.create_all()

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name


# api = Api(app)

# class Buy(Resource):
#     """
#     Buy Api to place an order
#     """
#     def get(self, todo_id):
#         """
#         Get all placed orders
#         :param todo_id:
#         :return:
#         """
#         return {}
#
#     def put(self, id, num, type):
#         """
#         Place a new Buying order
#         :param order:
#         :return:
#         """
#         order = {}
#
#
#         return {}
#
# class Sell(Resource):
#     """
#     Sell Api
#     """
#     def put(self, user, vol, price, ticker, isBuy, isMarket):
#         """
#         Creates a new order and enqueues it in the priority queue
#         :param order:
#         :return:
#         """
#         cursor.execute(
#             'INSERT INTO order(vol, price, ticker, isBuy, isMarket) '
#             'VALUES (%s, %s, %s, %s, %s)'
#             % (vol, price, ticker, isBuy, isMarket))
#         cursor.execute(
#             'INSERT INTO user_to_order(userId, orderId) '
#             'VALUES (%s, %s)'
#         )
#         conn.commit()
#         return {}
#
# class Entity(Resource):
#     def get(self):
#         """
#         :return: All Users
#         """
#         cursor.execute(
#             'SELECT * FROM "entity"'
#         )
#         return cursor.fetchall()
#
# class UserToOrder(Resource):
#     def get(self):
#         """
#         :return: All Users
#         """
#         cursor.execute(
#             'SELECT * FROM "user_to_order"'
#         )
#         return cursor.fetchall()
#
# class Inventory(Resource):
#     def get(self, userid):
#         cursor.execute(
#             'SELECT * FROM "inventory" WHERE userid = \'%s\' ' % userid
#         )
#         return cursor.fetchall()
#
# class Order(Resource):
#     def get(self):
#         cursor.execute(
#             'SELECT * FROM "ledger"'
#         )
#         return cursor.fetchall()
#
# class Ledger(Resource):
#     def get(self):
#         cursor.execute(
#             'SELECT * FROM "ledger"'
#         )
#         return cursor.fetchall()
#
#
#
# api.add_resource(Buy, '/buy')
# api.add_resource(Inventory, '<string:userid>')

if __name__ == '__main__':
    app.run(debug=True)