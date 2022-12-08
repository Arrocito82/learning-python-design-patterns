from classes.Facade import Facade

WEATHER_API_KEY = 'YOUR OWN OPEN WEATHER API KEY'
CITY='San Salvador'
COUNTRY='SV'
if __name__ == '__main__':
    facade = Facade()
    print facade.get_forecast(CITY,COUNTRY, WEATHER_API_KEY)
