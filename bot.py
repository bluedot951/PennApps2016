import threading
from urllib import urlencode
from urllib2 import Request, urlopen

threading.Thread()



url = 'https://pennapps2k16.herokuapp.com/buy/' # Set destination URL here

# high frequency trading ->
goog_post_fields = {
	"vol":200,
	"price":0.20,
	"ticker":"GOOG",
	"isMarket":"TRUE",
	"userId":4
}


gthb_post_fields = {
	"vol":200,
	"price":0.20,
	"ticker":"GTHB",
	"isMarket":"TRUE",
	"userId":3
}


penn_post_fields = {
	"vol":200,
	"price":0.20,
	"ticker":"PENN",
	"isMarket":"TRUE",
	"userId":0
}


request1 = Request(url, urlencode(goog_post_fields).encode())
request2 = Request(url, urlencode(penn_post_fields).encode())
request3 = Request(url, urlencode(gthb_post_fields).encode())

json = urlopen(request1).read().decode()
print(json)