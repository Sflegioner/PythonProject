import unittest
import RequestsData 
class TestsURL(unittest.TestCase):
    def SetUp(self) -> None:
        self.req =RequestsData.GetWheather()
        self.req.parametr = "London"
        self.req.days = 2

    def TestURL(self):
        url = self.req.BuildURL('http://api.weatherapi.com', 'v1', 'forecast.json', key="2b5942aa67f1438dbcd103443230211", q=self.get_weather_instance.parametr, days=self.get_weather_instance.days, aqi="no")
        self.assertEqual(url,'http://api.weatherapi.com/v1/forecast.json?key=2b5942aa67f1438dbcd103443230211&q=London&days=2&aqi=no')
    
    def TestJson(self):
        self.data = self.req.GetFromJson()
        locname = self.data['location']['name']
        self.assertEqual(self.req.parametr,locname)

if __name__ == '__main__':
    unittest.main()