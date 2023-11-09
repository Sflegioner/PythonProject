import requests
import unittest
import json

key = "2b5942aa67f1438dbcd103443230211"

class Get_User_input(unittest.TestCase):
    def __init__(self) -> str:
        self.parametr = input("Hi there, write city: ")
        self.days = input("Days: ")
        return self.parametr,self.days
    def print_result(self):
        print(self.parametr,self.days)
    
class GetWheather(Get_User_input):
    def __init__(self):
       super().__init__()
       self.data = {}
    def get_from_json(self) -> dict:
        url = "http://api.weatherapi.com/v1/forecast.json?key=2b5942aa67f1438dbcd103443230211&q={}&days={}&aqi=no".format(self.parametr,self.days)
        responce = requests.get(url)
        self.data = responce.json()
        print(self.data)
        return self.data
    def take_days_forecast(self)->str:
        return [(day['date'], 
                 day['day']['maxtemp_c'],
                 day['day']['mintemp_c'], 
                 day['day']['avgtemp_c'], 
                 day['day']['condition']['text']) 
                 for day in self.data['forecast']['forecastday']]
            
            
    def __str__(self) -> str:
        return "json data: {}".format(self.data)
    
class Formator(GetWheather):
    def __init__(self):
        super().__init__()
        self.get_from_json()
        self.cityname = self.data['location']['name']
        self.localtime = self.data['location']['localtime']
        self.weather = self.data['current']['condition']['text']
    def Test(self):
        self.assertEqual(self.parametr, self.cityname)



if __name__ == '__main__':
    unittest.main()





