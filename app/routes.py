from flask import render_template
from flask import send_from_directory
from geopy.geocoders import Nominatim
from app import app
import pandas as pd

@app.route('/')
@app.route('/index')
def index():
    df=pd.read_excel('/Users/Me/Documents/identity-quest/app/static/Identity-Quest-Demo-Resources.xlsx')
    address=[]
    name=[]
    tags=[]
    link=[]
    service_type=[]
    for index,row in df.iterrows():
        address.append(row['Address'])
        name.append(row['Organization Name'])
        service_type.append(row['Service Type'])
        link.append(row['Website'])
        tags.append([i.lower() for i in row['Filter Tags'].split(", ")])
    resources={'address':address,'name':name,'tags':tags,'type':service_type,'link':link}
    return render_template('index.html', resources=resources,title='Home')

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