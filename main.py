import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd
from enum import Enum
from json2html import *

class Rovers(Enum):
    ROVER_19 = 19
    ROVER_20 = 20
    ROVER_21 = 21
    BASE_100 = 100
    BASE_101 = 101

global latest_entry_19
global latest_entry_20
global latest_entry_21
global latest_entry_100 
global latest_entry_101

''' main url links to access data from marc server '''
MARC_SERVER = "http://marc.ecs.soton.ac.uk/"
TRACKER_IN_DOMAIN = "tracker-in/"
ROVER_19 = "19"
ROVER_20 = "20"
ROVER_21 = "21"
BASE_100 = "100"
BASE_101 = "101"

tracker_in_19_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_19)
tracker_in_20_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_20)
tracker_in_21_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_21)
tracker_in_100_url = (MARC_SERVER+TRACKER_IN_DOMAIN+BASE_100)
tracker_in_101_url = (MARC_SERVER+TRACKER_IN_DOMAIN+BASE_101)

page_19_json = requests.get(tracker_in_19_url, params={'load_amount':10, 'offset': 0})
page_20_json = requests.get(tracker_in_20_url, params={'load_amount':10, 'offset': 0})
page_21_json = requests.get(tracker_in_21_url, params={'load_amount':10, 'offset': 0})
page_100_json = requests.get(tracker_in_100_url, params={'load_amount':10, 'offset': 0})
page_101_json = requests.get(tracker_in_101_url, params={'load_amount':10, 'offset': 0})
# print(page_19_json.headers['Content-Type']) - returns application/json

data_rover_19 = page_19_json.json()
data_rover_20 = page_20_json.json()
data_rover_21 = page_21_json.json()
data_base_100 = page_100_json.json()
data_base_101 = page_101_json.json()

size_of_19 = (len(data_rover_19))
size_of_20 = (len(data_rover_20))
size_of_21 = (len(data_rover_21))
size_of_100 = (len(data_base_100))
size_of_101 = (len(data_base_101))


for node in list(Rovers):
    # print(node.value)
    match node.value:
        case 19:
            print("Node 19")
            # print(data_rover_19[-1])
            print(size_of_19)
            if (len(data_rover_19)) > size_of_19:
                print("New Data Entry Obtained on Node: %s", ROVER_19)
                latest_entry_19 = data_rover_19[-1]
                # print(latest_entry_19)
            else:
                print("Up-to-date")
                latest_entry_19 = data_rover_19[-1]
                # print(latest_entry_19)
        case 20:
            print("Node 20")
            # print(data_rover_20[-1])
            print(size_of_20)
            if (len(data_rover_20)) > size_of_20:
                print("New Data Entry Obtained on Node: %s", ROVER_20)
                latest_entry_20 = data_rover_20[-1]
                # print(latest_entry_20)
            else:
                print("Up-to-date")
                latest_entry_20 = data_rover_20[-1]
                # print(latest_entry_20)
        case 21:
            print("Node 21")
            # print(data_rover_21[-1])
            print(size_of_21)
            if (len(data_rover_21)) > size_of_21:
                print("New Data Entry Obtained on Node: %s", ROVER_21)
                latest_entry_21 = data_rover_21[-1]
                # print(latest_entry_21)
            else:
                print("Up-to-date")
                latest_entry_21 = data_rover_21[-1]
                # print(latest_entry_21)
        case 100:
            print("Node 100")
            # print(data_base_100[-1])
            print(size_of_100)
            if (len(data_base_100)) > size_of_100:
                print("New Data Entry Obtained on Node: %s", BASE_100)
                latest_entry_100 = data_base_100[-1]
                # print(latest_entry_100)
            else:
                print("Up-to-date")
                latest_entry_100 = data_base_100[-1]
                # print(latest_entry_100)
        case 101:
            print("Node 101")
            # print(data_base_101[-1])
            print(size_of_101)
            if (len(data_base_101)) > size_of_101:
                print("New Data Entry Obtained on Node: %s", BASE_101)
                latest_entry_101 = data_base_101[-1]
                # print(latest_entry_101)
            else:
                print("Up-to-date")
                latest_entry_101 = data_base_101[-1]
                # print(latest_entry_101)
        case _:
            print("Invalid Node")

list_of_data = list((latest_entry_19,latest_entry_20,latest_entry_21,latest_entry_100,latest_entry_101))

with open("latest_data.html", "w") as file:
    file.write(json2html.convert(json=list_of_data, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\""))
print("Done")
# while True:
#     if (len(data_rover_19)) > size_of_19:
#         print("New Data Entry Obtained on Node: %s", ROVER_19)
#         latest_entry_19 = data_rover_19[-1]
#         print(latest_entry_19)
#         break



#TODO: Store length of current entry -
# if length of new entry is greater than the one stored - 
# save the latest data entry from each node into an updated variable
# write that variable to a static html file
