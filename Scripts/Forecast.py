import unittest
import RequestsData
    
forecast = RequestsData.GetWheather()
forecast.GetFromJson()

print('\n', forecast.PrintYourQuery(),forecast.TakeForecast())



