import requests
import numpy
import threading

DB = requests.get('heroku db for stickers and their historic prices')


def lstsqest(data):
    # [ [id, datetime, price] [] [] ... ]
    # threading.Timer(10.0, getstd).start()

    unzippped = zip(*data)

    m, c = numpy.polyfit(unzipped[1], unzipped[2])
    return m * (time() - 30) + c
