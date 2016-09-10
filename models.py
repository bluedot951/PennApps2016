from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gxspomxmufoybd:dskomEuwa9JYaxf8Jd7h8JYVKo@ec2-54-221-253-117.compute-1.amazonaws.com:5432/d62ndf8grb25cb'
db = SQLAlchemy(app)
db.create_all()

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    balance = db.Column(db.Numeric)

    def __init__(self, username, balance):
        self.username = username
        self.email = balance

    def __repr__(self):
        return '<Entity Id %r>' % self.id

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vol = db.Column(db.Integer)
    price = db.Column(db.Numeric)
    ticker = db.Column(db.String(4))
    isBuy = db.Column(db.Boolean)
    isMarket = db.Column(db.Boolean)

    def __init__(self, vol, price, ticker, isBuy, isMarket):
        self.vol = vol
        self.price = price
        self.ticker = ticker
        self.isBuy = isBuy
        self.isMarket = isMarket

    def __repr__(self):
        return '<Order Id %r>' % self.id

class UserToOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    orderId = db.Column(db.Integer)

    def __init__(self, userId, orderId):
        self.userId = userId
        self.orderId = orderId

    def __repr__(self):
        return '<UserToOrder Id %r>' % self.id

class UserToLedger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    ledgerId = db.Column(db.Integer)

    def __init__(self, userId, ledgerId):
        self.userId = userId
        self.ledgerId = ledgerId

    def __repr__(self):
        return '<UserToLedger Id %r>' % self.id

class priorityQueue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timeStamp = db.Column(db.DateTime)
    orderId = db.Column(db.Integer)

    def __init__(self, userId, orderId):
        self.userId = userId
        self.orderId = orderId

    def __repr__(self):
        return '<UserToLedger Id %r>' % self.id
