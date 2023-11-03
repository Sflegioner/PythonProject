import requests
import unittest
import json

parametr = input("Hi there, write city: ")
data = {} 

key = "2b5942aa67f1438dbcd103443230211"
url = "http://api.weatherapi.com/v1/current.json?key=2b5942aa67f1438dbcd103443230211&q={}&aqi=no".format(parametr)
responce = requests.get(url)
data = responce.json()

cityname = data['location']['name']
localtime = data['location']['localtime']
weather = data['current']['condition']['text']



