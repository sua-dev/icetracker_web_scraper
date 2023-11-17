import matplotlib.pyplot as plt
# import pandas
# # import matplotlib.cbook as cbook
# from urllib.request import urlopen
import json
from pprint import pprint
import json2html


from jinja2 import Environment, FileSystemLoader
import os



import requests
from enum import Enum
from json2html import *

class Rovers(Enum):
    ROVER_19 = 19
    ROVER_20 = 20
    ROVER_21 = 21
    ROVER_22 = 22
    BASE_100 = 100
    BASE_101 = 101

global latest_entry_19
global latest_entry_20
global latest_entry_21
global latest_entry_22
global latest_entry_100 
global latest_entry_101

''' main url links to access data from marc server '''
MARC_SERVER = "http://marc.ecs.soton.ac.uk/"
TRACKER_IN_DOMAIN = "tracker-in/"
ROVER_19 = "19"
ROVER_20 = "20"
ROVER_21 = "21"
ROVER_22 = "22"
BASE_100 = "100"
BASE_101 = "101"

def tracker_url(node_id):
    return (MARC_SERVER+TRACKER_IN_DOMAIN+node_id)

# tracker_url(ROVER_19)
# request_page(tracker_url(ROVER_19))
# jsonify(request_page(tracker_url(ROVER_19)))


# length_of_data_entries(jsonify(request_page(tracker_url(ROVER_19))))
# latest_entry(jsonify(request_page(tracker_url(ROVER_19))))


tracker_in_19_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_19)
tracker_in_20_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_20)
tracker_in_21_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_21)
tracker_in_22_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_22)
tracker_in_100_url = (MARC_SERVER+TRACKER_IN_DOMAIN+BASE_100)
tracker_in_101_url = (MARC_SERVER+TRACKER_IN_DOMAIN+BASE_101)

def request_page(tracker_page):
    return requests.get(tracker_page, params={'load_amount':10, 'offset': 0})

page_19_json = requests.get(tracker_in_19_url, params={'load_amount':10, 'offset': 0})
page_20_json = requests.get(tracker_in_20_url, params={'load_amount':10, 'offset': 0})
page_21_json = requests.get(tracker_in_21_url, params={'load_amount':10, 'offset': 0})
page_22_json = requests.get(tracker_in_22_url, params={'load_amount':10, 'offset': 0})
page_100_json = requests.get(tracker_in_100_url, params={'load_amount':10, 'offset': 0})
page_101_json = requests.get(tracker_in_101_url, params={'load_amount':10, 'offset': 0})
# print(page_19_json.headers['Content-Type']) - returns application/json

def jsonify(data_page):
    return data_page.json() 

data_rover_19 = page_19_json.json()
data_rover_20 = page_20_json.json()
data_rover_21 = page_21_json.json()
data_rover_22 = page_22_json.json()
data_base_100 = page_100_json.json()
data_base_101 = page_101_json.json()


# using matplotlib
def plot_lat_long(n):
    ''' Specify a node number and it will plot the corresponding lat long values for that node'''
    data = None
    match n:
        case 19:
            data = data_rover_19
        case 20:
            data = data_rover_20
        case 21:
            data = data_rover_21
        case 22:
            data = data_rover_22
        case 100:
            data = data_base_100
        case 101:
            data = data_base_100
            
    node_long = []
    node_lat = []
    for i in data:
        if i == None:
            continue
        else:
            if i['long'] is None:
                continue
            if i['lat'] is None:
                continue
            else:
                node_long.append(i['long'])
                node_lat.append(i['lat'])


    plt.plot(node_long,node_lat, linewidth=1.0)
    plt.show()

# plot_lat_long(22)

list_of_data_19 = list((data_rover_19))
list_of_data_20 = list((data_rover_20))
list_of_data_21 = list((data_rover_21))
list_of_data_22 = list((data_rover_22))
list_of_data_100 = list((data_base_100))
list_of_data_101 = list((data_base_101))

# pprint(list_of_data_22)
temperature = []
alt = []
lat = []
long = []
voltage = []
timestamp = []

def split_data(n):

    data = None
    match n:
        case 19:
            data = data_rover_19
        case 20:
            data = data_rover_20
        case 21:
            data = data_rover_21
        case 22:
            data = data_rover_22
        case 100:
            data = data_base_100
        case 101:
            data = data_base_100

    for i in data:

            if i['temperature'] > 15:
                continue
            else:
                # temperature.clear()
                temperature.append(i['temperature'])

            if i['alt'] is None:
                continue
            else:
                # alt.clear()
                alt.append(i['alt'])

            if i['lat'] is None:
                continue
            else:
                # lat.clear()
                lat.append(i['lat'])
            
            if i['long'] is None:
                continue
            else:
                # long.clear()
                long.append(i['long'])
            
            # voltage.clear()
            voltage.append(i['voltage'])

            # timestamp.clear()
            timestamp.append(i['timestamp'])

# split_data(22)

# print(temperature)
# pprint(alt)
# pprint(lat)
# pprint(long)
# print(voltage)
# print(timestamp)