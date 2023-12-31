import requests
# from bs4 import BeautifulSoup
# import json
# import re
import pandas as pd
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

global tracker_urls
global json_urls

def create_instance():
    tracker_urls = []
    for node in list(Rovers):
        tracker_urls.append(tracker_url(node.value))
    return tracker_urls
        

def tracker_url(node_id):
    return (MARC_SERVER+TRACKER_IN_DOMAIN+str(node_id))

#TODO - remove duplicate code and apply recent changes with lists to update_table()

tracker_in_19_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_19)
tracker_in_20_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_20)
tracker_in_21_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_21)
tracker_in_22_url = (MARC_SERVER+TRACKER_IN_DOMAIN+ROVER_22)
tracker_in_100_url = (MARC_SERVER+TRACKER_IN_DOMAIN+BASE_100)
tracker_in_101_url = (MARC_SERVER+TRACKER_IN_DOMAIN+BASE_101)


def create_json_instance():
    json_urls = []
    for url_link in create_instance():
        json_urls.append(request_page(url_link))
    return json_urls

# can create a for a loop to instantiate multiple nodes 
def request_page(tracker_page):
    return requests.get(tracker_page, params={'load_amount':10, 'offset': 0})

page_19_json = requests.get(tracker_in_19_url, params={'load_amount':10, 'offset': 0})
page_20_json = requests.get(tracker_in_20_url, params={'load_amount':10, 'offset': 0})
page_21_json = requests.get(tracker_in_21_url, params={'load_amount':10, 'offset': 0})
page_22_json = requests.get(tracker_in_22_url, params={'load_amount':10, 'offset': 0})
page_100_json = requests.get(tracker_in_100_url, params={'load_amount':10, 'offset': 0})
page_101_json = requests.get(tracker_in_101_url, params={'load_amount':10, 'offset': 0})
# print(page_19_json.headers['Content-Type']) - returns application/json

def jsonify(data_entry):
    json_data_list = []
    for element in data_entry:
        json_data = element.json()
        json_data_list.append(json_data[-1])
    return json_data_list
    # for element in create_json_instance:
    #     return .json() 

data_rover_19 = page_19_json.json()
data_rover_20 = page_20_json.json()
data_rover_21 = page_21_json.json()
data_rover_22 = page_22_json.json()
data_base_100 = page_100_json.json()
data_base_101 = page_101_json.json()

def length_of_data_entries(data_entry):
    len_list = []
    for element in data_entry:
        len_list.append(len(element))
    return len(data_entry)

size_of_19 = (len(data_rover_19))
size_of_20 = (len(data_rover_20))
size_of_21 = (len(data_rover_21))
size_of_22 = (len(data_rover_22))
size_of_100 = (len(data_base_100))
size_of_101 = (len(data_base_101))

''' Get Latest JSON Entry '''
def latest_entry(data_entry):
    return data_entry[-1]

# latest_entry_19 = data_rover_19[-1]
# latest_entry_20 = data_rover_20[-1]
# latest_entry_21 = data_rover_21[-1]
# latest_entry_22 = data_rover_22[-1]
# latest_entry_100 = data_base_100[-1]
# latest_entry_101 = data_base_101[-1]

# TODO: Last update flag and create a timestamp with it
last_updated = False

# TODO: while True system to run forever whilst the script is running 

def update_table():
    for node in list(Rovers):
        # print(node.value)
        match node.value:
            case 19:
                # print("Node 19")
                # print(data_rover_19[-1])
                if (len(data_rover_19)) > size_of_19:
                    print(size_of_19)

                    print("New Data Entry Obtained on Node: %s" % ROVER_19)
                    latest_entry_19 = data_rover_19[-1]
                    # print(latest_entry_19)
                else:
                    print("%s - Up-to-date" % ROVER_19)
                    latest_entry_19 = data_rover_19[-1]
                    # print(latest_entry_19)
            case 20:
                # print("Node 20")
                # print(data_rover_20[-1])
                
                if (len(data_rover_20)) > size_of_20:
                    print(size_of_20)
                    print("New Data Entry Obtained on Node: %s" % ROVER_20)
                    latest_entry_20 = data_rover_20[-1]
                    # print(latest_entry_20)
                else:
                    print("%s - Up-to-date" % ROVER_20)
                    latest_entry_20 = data_rover_20[-1]
                    # print(latest_entry_20)
            case 21:
                # print("Node 21")
                # print(data_rover_21[-1])
                if (len(data_rover_21)) > size_of_21:
                    print(size_of_21)
                    print("New Data Entry Obtained on Node: %s" % ROVER_21)
                    latest_entry_21 = data_rover_21[-1]
                    # print(latest_entry_21)
                else:
                    print("%s - Up-to-date" % ROVER_21)
                    latest_entry_21 = data_rover_21[-1]
                    # print(latest_entry_21)
            case 22:
                # print("Node 21")
                # print(data_rover_21[-1])
                if (len(data_rover_22)) > size_of_22:
                    print(size_of_22)
                    print("New Data Entry Obtained on Node: %s" % ROVER_21)
                    latest_entry_22 = data_rover_22[-1]
                    # print(latest_entry_21)
                else:
                    print("%s - Up-to-date" % ROVER_22)
                    latest_entry_22 = data_rover_22[-1]
                    # print(latest_entry_21)
            case 100:
                # print("Node 100")
                # print(data_base_100[-1])
                if (len(data_base_100)) > size_of_100:
                    print(size_of_100)
                    print("New Data Entry Obtained on Node: %s" % BASE_100)
                    latest_entry_100 = data_base_100[-1]
                    # print(latest_entry_100)
                else:
                    print("%s - Up-to-date" % BASE_100)
                    latest_entry_100 = data_base_100[-1]
                    # print(latest_entry_100)
            case 101:
                # print("Node 101")
                # print(data_base_101[-1])
                if (len(data_base_101)) > size_of_101:
                    print(size_of_101)
                    print("New Data Entry Obtained on Node: %s" % BASE_101)
                    latest_entry_101 = data_base_101[-1]
                    # print(latest_entry_101)
                else:
                    print("%s - Up-to-date" % BASE_101)
                    latest_entry_101 = data_base_101[-1]
                    # print(latest_entry_101)
            case _:
                print("Invalid Node")

    list_of_data = list((latest_entry_19,latest_entry_20,latest_entry_21,latest_entry_22,latest_entry_100,latest_entry_101))

    with open("latest_data.html", "w") as file:
        file.write(json2html.convert(json=list_of_data, table_attributes="id=\"info-table\" class=\"table table-bordered table-hover\""))
    print("Done")
# while True:
#     if (len(data_rover_19)) > size_of_19:
#         print("New Data Entry Obtained on Node: %s", ROVER_19)
#         latest_entry_19 = data_rover_19[-1]
#         print(latest_entry_19)
#         break

def main():
    # print(create_instance())
    # print(create_json_instance())
    # print(data_rover_19[-1])
    # print()
    # for i in jsonify(create_json_instance()):
    #     print(i)
    # print(jsonify(create_json_instance()))
    # print(length_of_data_entries(create_json_instance()))
    latest_entry_19 = create_json_instance()[0]
    latest_entry_20 = create_json_instance()[1]
    latest_entry_21 = create_json_instance()[2]
    latest_entry_22 = create_json_instance()[3]
    latest_entry_100 = create_json_instance()[4]
    latest_entry_101 = create_json_instance()[5]
    update_table()

if __name__ == '__main__':
    main()
    