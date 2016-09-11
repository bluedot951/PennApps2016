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
import algos
import urllib2
import json


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

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/balance', methods=['GET'])
def get_balance():
    url = "http://api.reimaginebanking.com/accounts/57d40d4ee63c5995587e8651?key=3a0f0fa4ae6f43cc9f70854d69e0f78f"
    # urllib2.urlopen(url).read()

    response = urllib2.urlopen(url)
    data = json.load(response)

    return jsonify(data["balance"])



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
def get_priority_queue():
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
    # if not request.json or 'vol' not in request.json \
    #     or 'price' not in request.json or 'ticker' not in request.json \
    #     or 'isMarket' not in request.json or 'userId' not in request.json:
    #     abort(400)
    vol = request.json['vol']
    price = request.json['price']
    ticker = request.json['ticker']
    isMarket = request.json['isMarket']
    userId = request.json['userId']

    return orderCallback(vol, price, ticker, 'TRUE', isMarket, userId)

@app.route('/sell/', methods=['POST'])
def sell():
    # if not request.json or 'vol' not in request.json \
    #     or 'price' not in request.json or 'ticker' not in request.json \
    #     or 'isMarket' not in request.json or 'userId' not in request.json:
    #     abort(400)
    vol = request.json['vol']
    price = request.json['price']
    ticker = request.json['ticker']
    isMarket = request.json['isMarket']
    userId = request.json['userId']

    return orderCallback(vol, price, ticker, 'FALSE', isMarket, userId)

def orderCallback(vol, price, ticker, isBuy, isMarket, userId):
    # collect past orders
    cursor.execute(
        'SELECT * FROM "order"'
    )
    old_orders = cursor.fetchall()
    print 'old orders'
    print old_orders

    # create new order
    id = random.randint(0, 100000000)
    cursor.execute(
        'INSERT INTO "order"(id, vol, price, ticker, isbuy, ismarket, userid) VALUES '
        '(%s, %s, %s, \'%s\', %s, %s, %s);' % (id, vol, price, ticker, isBuy, isMarket, userId)
    )
    conn.commit()
    cursor.execute(
        'SELECT * FROM "order" WHERE id = %s;' % id
    )
    new_order = cursor.fetchall()
    print 'new order'
    print new_order

    # collect past general ledger history
    cursor.execute(
        'SELECT * FROM "ledger";'
    )
    gl = cursor.fetchall()
    print 'gl'
    print gl

    # collect priority queue
    cursor.execute(
        'SELECT * FROM "priority_queue"'
    )
    pq = cursor.fetchall()
    print 'pq'
    print pq

    # call an algos.py function right here
    # update ledger
    # and update pq
    new_pq, new_ledger = algos.getData(pq, old_orders, gl, new_order[0])
    print 'new pq'
    print new_pq

    print 'new ledger'
    print new_ledger

    # update priority queue
    cursor.execute(
        'DELETE TABLE "priority_queue" *'
    )
    conn.commit()
    for order in new_pq:
        cursor.execute(
            'INSERT INTO "priority_queue"(id, stamp, orderid) VALUES '
            '( %s, %s, %s) ' % ('DEFAULT', 'now()', order['id'])
        )

    # update ledger
    cursor.execute(
        'DELETE TABLE "ledger" *'
    )
    conn.commit()
    for l in new_ledger:
        cursor.execute(
            'INSERT INTO "ledger"(id, stamp, orderid) VALUES '
            '( %s, %s, %s) ' % ('DEFAULT', 'now()', l['id'])
        )

    #
    # # update price history
    # cursor.execute(
    #     'INSERT INTO "%s_price_history"(id, stamp, price) VALUES '
    #     '( %s, %s, %s) ' % ('DEFAULT', 'now()', new_market_price)
    # )

    # update user inventory
    operation = '+' if isBuy else '-'

    # increase user inventory, decrease from the central market
    cursor.execute(
        'UPDATE "inventory" SET count = count %s %s WHERE userid = 2 AND ticker = \'%s\''
        % (operation, vol, ticker)
    )
    cursor.execute(
        'UPDATE "inventory" SET count = count %s %s WHERE userid = 2 AND ticker = \'%s\''
        % (operation, vol, ticker)
    )
    conn.commit()

    return jsonify({'status': 200, 'message': 'success :)'})
    # return jsonify({'new_market_price' : new_market_price, 'date_of_update': datetime_of_update})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)