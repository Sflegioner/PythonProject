import requests
import unittest
import urllib.parse
import json


key = "2b5942aa67f1438dbcd103443230211"
key1 = "c7d546a951b04912b2e7c84f69991743"

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
       self.lat = None
       self.lon = None
       self.data1 = {}
       self.data2 = {}
       self.data3 = {}

    def BuildURL(self,base_url, *req, **param) -> str:
        url = base_url
        for r in req:
            url = '{}/{}'.format(url,r)
        if param:
            url = '{}?{}'.format(url,urllib.parse.urlencode(param))
        return url
    
    def GetResponce(self,url):
        responce = requests.get(url)
        data = responce.json()
        return data
    
    def GetFromJson1(self) -> dict:
        url1 = self.BuildURL('http://api.weatherapi.com','v1','forecast.json',key ="2b5942aa67f1438dbcd103443230211",q = self.parametr,days = self.days,aqi = "no")
        self.data1 = self.GetResponce(url1)
        self.lat = self.data1['location']['lat']
        self.lon = self.data1['location']['lon']
        print(self.lat,self.lon)
        return self.data1
    
    def GetFromJson2(self):
        url2 = self.BuildURL('https://api.brightsky.dev','weather',lat= self.lat , lon = self.lon, date='2023-11-20')
        self.data2 = self.GetResponce(url2)
        return self.data2
        
    def GetFromJson3(self):
        url3 = self.BuildURL('https://api.weatherbit.io','v2.0','current',lat=self.lat,lon=self.lon,key=key1,include='minutely')
        self.data3 = self.GetResponce(url3)
        return self.data3
    
    def TakeForecast1(self)->str:
        return [(day['date'], 
                 day['day']['condition']['text']) 
                 for day in self.data1['forecast']['forecastday']]    
    def TakeForecast2(self)->str:
        return '\nweather from another API1: ' + self.data2['weather'][0]['condition']
    def TakeForecast3(self)->str:
        return '\nweather from another API2: ' + self.data3['data'][0]['weather']['description']
    def __str__(self) -> str:
        return "json data: {}".format(self.data1)
    
    






