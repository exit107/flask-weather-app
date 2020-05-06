#!/bin/sh

gunicorn -b 0.0.0.0:5000 weather_app:app 
