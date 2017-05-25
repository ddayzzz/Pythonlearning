#!/bin/python3
# coding=utf-8
# Weather report
# yahoo api https://developer.yahoo.com/weather/#python
import requests


class WeatherReport(object):

    def __init__(self, json_data):
        self.city = json_data['query']['results']['channel']['location']['city']
        self.country = json_data['query']['results']['channel']['location']['country']
        self.region = json_data['query']['results']['channel']['location']['region']
        # 
        # self.unit_distance = json_data['query']['results']['channel']['units']['distance']
        # self.unit_pressure = json_data['query']['results']['channel']['units']['pressure']
        # self.unit_speed = json_data['query']['results']['channel']['units']['speed']
        self.unit_temperature = json_data['query']['results']['channel']['units']['temperature']
        # 
        self.curr_temp = json_data['query']['results']['channel']['item']['condition']['temp']
        self.curr_wea = json_data['query']['results']['channel']['item']['condition']['text']
        # 
        self.forcast = {}
        for vs in json_data['query']['results']['channel']['item']['forecast']:
            self.forcast[vs['date']] = list((vs['low'], vs['high'], vs['text']))

    def report(self):
        print('Here is weather of %s, %s, %s' % (self.city, self.region, self.country))
        print('Currect weather is %s, %s %s' % (self.curr_wea, self.curr_temp, self.unit_temperature))
        print('Weather forcast :')
        for da, dat in self.forcast.items():
            print('On %s Low:%s %s  High:%s %s  Weather:%s' % (da, dat[0], self.unit_temperature, dat[1], self.unit_temperature, dat[2]))


city = 'tianjin'
# city = input('Please inuput the city name (eg \'xiangtan\') : ')
link = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22' + city +'%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
s = requests.session()
wp = WeatherReport(s.get(link).json())
wp.report()
