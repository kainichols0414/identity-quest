from flask import render_template
from flask import send_from_directory
from geopy.geocoders import Nominatim
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/map')
def map():
    address='401 Branard Street'
    geolocator = Nominatim(user_agent="Identity Quest")
    location = geolocator.geocode(address)
    location = {'name':"Montrose Center",'lon':location.longitude,'lat':location.latitude}
    return render_template('map.html',location=location, title='Map')

@app.route('/static/<path:path>')
def download_file(filename):
    return send_from_directory('static',filename)

@app.route('/faq')
def faq():
    return render_template('index.html', title='Home')