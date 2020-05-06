# Weather App powered by Flask
import json
import os
import sys 

from flask import Flask, render_template, request, redirect, url_for
from icecream import ic
import requests
from requests.exceptions import HTTPError, Timeout
import yaml

from forms import ZipcodeForm
from location import Location

# Handle configuration of the application
SECRET_KEY = os.environ.get("SECRET_KEY")
MAPBOX_API_KEY = os.environ.get("MAPBOX_API_KEY")

if not MAPBOX_API_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")
if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")

# Setup the app and add variables to config params
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MAPBOX_API_KEY'] = MAPBOX_API_KEY


@app.route("/", methods=['GET', 'POST'])
def home():
    form = ZipcodeForm()

    if request.method == 'POST':
        if form.validate():
            zipcode = form.zipcode.data
            print(f'Zipcode entered: {zipcode}\n')

            location = Location()
            location.location_as_zip(zipcode, app.config['MAPBOX_API_KEY'])
            tomorrow_summary = location.weather_forecast['properties']['periods'][2]['shortForecast']
            print(f"Forecase presented: Tomorrow's forecast in {location.city}, {location.state} is: {tomorrow_summary}")

            return render_template("weather.html", result=tomorrow_summary, city=location.city, state=location.state)
        else:
            return render_template('home.html', form=form)

    return render_template('home.html', form=form)
