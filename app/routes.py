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
    resources={'name':name,'tags':tags,'type':service_type,'link':link}
    return render_template('index.html', resources=resources,title='Home')


@app.route('/map')
def map():
    df=pd.read_excel('/Users/Me/Documents/identity-quest/app/static/Identity-Quest-Demo-Resources.xlsx')
    lon=[]
    lat=[]
    name=[]
    for index,row in df.iterrows():
        if(row['Lon']==row['Lon']):
            lon.append(row['Lon'])
            lat.append(row['Lat'])
            name.append(str(row['Organization Name']))
    return render_template('map.html',data={'name':name,'lon':lon,'lat':lat}, title='Map')

@app.route('/q')
def questioning():
    return render_template('questioning.html', title='Questioning')

@app.route('/gi')
def gi():
    return render_template('genderidentity.html', title='Gender Identity')

@app.route('/s')
def s():
    return render_template('sexuality.html', title='Sexuality')

@app.route('/static/<path:path>')
def download_file(filename):
    return send_from_directory('static',filename)
