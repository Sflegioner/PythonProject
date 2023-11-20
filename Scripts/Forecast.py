import unittest
import RequestsData

forecast = RequestsData.GetWheather()
forecast.GetFromJson1()
forecast.GetFromJson2()
forecast.GetFromJson3()
print('\n', forecast.PrintYourQuery(),forecast.TakeForecast2(),forecast.TakeForecast3())