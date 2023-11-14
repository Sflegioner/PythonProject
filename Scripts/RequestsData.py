import requests
import unittest
import urllib.parse
import json

key = "2b5942aa67f1438dbcd103443230211"

class GetUserInput():
    def __init__(self) -> str:
        self.parametr = input("Hi there, write city: ")
        self.days = input("Days: ")
        return self.parametr,self.days
    def PrintYourQuery(self) -> str:
        return "Your query is weather in {} for {} days: ".format(self.parametr,self.days)
    
class GetWheather(GetUserInput):
    def __init__(self):
       super().__init__()
       self.data = {}
    def BuildURL(self,base_url, *req, **param) -> str:
        url = base_url
        for r in req:
            url = '{}/{}'.format(url,r)
        if param:
            url = '{}?{}'.format(url,urllib.parse.urlencode(param))
        return url
    def GetFromJson(self) -> dict:
        url1 = self.BuildURL('http://api.weatherapi.com','v1','forecast.json',key ="2b5942aa67f1438dbcd103443230211",q = self.parametr,days = self.days,aqi = "no")
        responce = requests.get(url1)
        self.data = responce.json()
        return self.data
    def TakeForecast(self)->str:
        return [(day['date'], 
                 day['day']['condition']['text']) 
                 for day in self.data['forecast']['forecastday']]     
    def __str__(self) -> str:
        return "json data: {}".format(self.data)
    






