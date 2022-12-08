from classes.WeatherProvider import WeatherProvider
from classes.Converter import Converter
from classes.Weather import Weather
from classes.Parser import Parser
from classes.Cache import Cache


class Facade(object):
    def get_forecast(self, city, country, api_key):
        cache = Cache('myfile')
        cache_result = cache.load()
        if cache_result:
            return cache_result
        else:
            weather_provider = WeatherProvider()
            weather_data = weather_provider.get_weather_data(city, country, api_key)
            parser = Parser()
            parsed_data = parser.parse_weather_data(weather_data)
            weather = Weather(parsed_data)
            converter = Converter()
            temperature_celcius = converter.from_kelvin_to_celcius(weather.temperature)
            cache.save(temperature_celcius)
            return temperature_celcius
