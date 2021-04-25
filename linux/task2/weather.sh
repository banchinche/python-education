#!/bin/bash
WEATHER_KEY='1534a3a4218184ba60906ab6139cba18'
CITY="Kharkiv"
curl -o $HOME/weather.json "api.openweathermap.org/data/2.5/weather?q=$CITY&appid=$WEATHER_KEY"
