# README
This is a very basic personal weather website using Flask. 
Pulls weather from NOAA API while using MapBox to locate Latitude and Longitude coordinates.
I plan to keep working on this site as I learn other skills.

## Configuration
There are two environment variables to set to configure the app:

    SECRET_KEY=<FLASK_SECRET_KEY>
    MAPBOX_KEY_API=<API_KEY_FOR_MAPBOX_API>

The easiest way is to create a file `web.env` with the above contents and source it in whichever way you choose to run the app.

## Running the app
### With Docker
1. Bring up the container
        `docker container run -p 5000:5000 --env-file web.env  davebrown/flask-weather-app:latest`
2. Access the site at http://127.0.0.1:5000.
### With Docker-compose
1. Bring up the container
        `docker-compose up`
2. Access the site at http://127.0.0.1:5000.
### Locally
1. Clone the repo
2. Create a `web.env` file. You will need a free API key from mapbox.com
3. Install dependencies.  
	`pipenv install`
4. Activate the environment. 
	`pipenv shell`
5. Set environmental variables. 
	`source web.env`
6. Start the server. 
	`flask run`
7. Access the site at http://127.0.0.1:5000.
