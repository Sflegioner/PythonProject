import unittest
import requests
import RequestsData


class CityForecast(unittest.TestCase):
    def __init__(self,cityName,weatherType,localDate,) -> None:
        self.city = cityName
        self.weather = weatherType
        self.date = localDate
    def __str__(self) -> str:
        return "So today weather is {} in {} ({})".format(self.city,self.weather,self.date)

City = CityForecast(cityName = RequestsData.cityname,weatherType=RequestsData.weather,localDate=RequestsData.localtime)
print(City)

