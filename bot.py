import threading
from urllib import urlencode
from urllib2 import Request, urlopen

import time

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

def reset_timer():
	time_since_trigger = time.time() * 1000
	while time.time() * 1000 - time_since_trigger < RESET_TIME:
		time.sleep(0.001)
		Request(url, urlencode(goog_post_fields).encode())
		json1 = urlopen(request1).read().decode()
		print json1

		Request(url, urlencode(penn_post_fields).encode())
		json2 = urlopen(request2).read().decode()
		print json2

		Request(url, urlencode(gthb_post_fields).encode())
		json3 = urlopen(request3).read().decode()
		print json3
		time_since_trigger = time.time() * 1000


# Reset Timer
RESET_TIME = 10000
time_since_trigger = 0
reset_thread = threading.Thread(target=reset_timer)
# reset_thread.daemon = True
reset_thread.start()
