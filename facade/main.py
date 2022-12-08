from classes.Facade import Facade

WEATHER_API_KEY = 'YOUR OWN OPEN WEATHER API KEY'

if __name__ == '__main__':
    facade = Facade()
    print facade.get_forecast('London', 'UK', WEATHER_API_KEY)
