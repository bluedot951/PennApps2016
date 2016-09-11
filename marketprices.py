import requests
import numpy
import threading


def calculatePrice(data):
    # [ [id, datetime, price] [] [] ... ]
    # threading.Timer(10.0, getstd).start()

    unzippped = zip(*data)

    m, c = numpy.polyfit(unzipped[1], unzipped[2])
    return m * (time() - 30) + c
