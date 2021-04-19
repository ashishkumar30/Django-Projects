
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd
import requests
import urllib.request
import json
import os

# using google api
def Google_api_(address):
    try:
        api = 'AIzaSyBoUGqjWoJmy4z4DRfKDnEJPq-t1lODbuo'
        base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
        parameters = {"address": address, "key": api}
        response = requests.get(f"{base_url}{urllib.parse.urlencode(parameters)}")

        # response & fetching locaion data
        data = json.loads(response.content)
        data_geo = data.get("results")[0].get("geometry")
        data_location = data_geo.get("location")
        return {address: data_location}
    except Exception as e:
        print("Error", str(e))
        return None


# using geopy python library
def Secondary_library(address):
    try:
        from geopy.geocoders import Nominatim
        from geopy.distance import geodesic
        geolocator = Nominatim(user_agent="ashish")
        # enter first location
        start=address.title()
        latitude_ = geolocator.geocode(start).latitude
        longitude_ = geolocator.geocode(start).longitude

        return {address: {'lat':latitude_, 'lng': longitude_}}
    except:
        return {address: {'lat':"None", 'lng': "None"}}

# function to read data from excel file
def read_file_data_(filename):
    try:
        if filename.endswith(".csv"):
            print("use csv function")
            df = pd.read_csv(filename)
        else:
            print("use Excel file function")
            df = pd.read_excel(filename)

        df = pd.DataFrame(df)
        all_address = df['location']
        return all_address  # list of all address in it
    except:
        return None


# function to get file from froentend
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        read_file=myfile.name
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        dir_=os.path.join(os.getcwd(), "media",read_file)
        data = read_file_data_(dir_)
        all_location_data = list(map(Google_api_, data))

        if all(all_location_data):
            pass
        else:
            print("Google api no working ")
            all_location_data = list(map(Secondary_library, data))

        print(all_location_data,"all_location_data")
        csv_data = pd.DataFrame({"Latitue And Longitude": all_location_data})
        dir_csv = os.path.join(os.getcwd(), "media", "location_data.xlsx")
        csv_data.to_excel(dir_csv)
        filestorage="/media/location_data.xlsx"

        return render(request, 'simple_upload.html', {
            'uploaded_file_url': filestorage
        })
    return render(request, 'simple_upload.html')
