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

from flask import Flask, abort, jsonify, request, send_from_directory, render_template
from flask_restful import Resource, Api

import os
import random
import psycopg2
import urlparse
from custom_json_encoder import CustomJsonEncoder
import Algos

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

app = Flask(__name__, static_url_path='')
app.json_encoder = CustomJsonEncoder
api = Api(app)


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

@app.route('/priority_queue/', methods=['GET'])
def get_ledgers():
    cursor.execute(
        'SELECT * FROM "priority_queue"'
    )
    return jsonify(cursor.fetchall())



@app.route('/price_history/<string:ticker>', methods=['GET'])
def get_price_history(ticker):
    cursor.execute(
        'SELECT * FROM "%s_price_history"' % ticker
    )
    # print cursor.fetchall()
    return jsonify(cursor.fetchall())



@app.route('/buy/', methods=['POST'])
def buy():
    print request
    if not request.json or 'vol' not in request.json \
        or 'price' not in request.json or 'ticker' not in request.json \
        or 'userId' not in request.json or 'isMarket' not in request.json:
        abort(400)
    val = request.json['val']
    price = request.json['price']
    ticker = request.json['ticker']
    isMarket = request.json['isMarket']
    userId = request.json['userId']
    id = random.randint(100000)
    cursor.execute(
        'INSERT INTO "order"(id, val, price, ticker, isBuy, isMarket, userId) VALUES '
        '(%s, %s, %s, %s, %s, %s, %s)' % ('DEFAULT', val, price, ticker, 'TRUE', isMarket, userId)
    )
    cursor.execute(
        'INSERT INTO "priority_queue"(id, stamp, orderid) VALUES '
        '( %s, %s, %s) ' % ('DEFAULT', 'now()', id)
    )
    conn.commit()
    return jsonify({'status': 200, 'message': 'success :)'})

@app.route('/sell/', methods=['POST'])
def sell():
    if not request.json or 'vol' not in request.json \
        or 'price' not in request.json or 'ticker' not in request.json \
        or 'isMarket' not in request.json:
        abort(400)
    val = request.json['val']
    price = request.json['price']
    ticker = request.json['ticker']
    isMarket = request.json['isMarket']
    id = random.randint(100000)
    cursor.execute(
        'INSERT INTO "order"(id, val, price, ticker, isBuy, isMarket) VALUES '
        '(%s, %s, %s, %s, %s, %s, %s)' % ('DEFAULT', val, price, ticker, 'FALSE', isMarket)
    )
    cursor.execute(
        'INSERT INTO "priority_queue"(id, stamp, orderid) VALUES '
        '( %s, %s, %s) ' % ('DEFAULT', 'now()', id)
    )
    conn.commit()

    # call an algos.py function right here

    return jsonify({'status': 200, 'message': 'success :)'})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)