import requests
import json
from pymongo import MongoClient

db_client = MongoClient()
db = db_client['healthcare']
table = db['physicians']

def single_query(link):
    response = requests.get(link)
    if response.status_code != 200:
        print('WARNING', response.status_code)
    else:
        return response.json()

def parse_response(response):
    physician = response['results'][0]
    return physician

def query_builder(npi):
    base_link = 'https://npiregistry.cms.hhs.gov/api/?number='
    link = base_link + npi
    return link

def get_physician(npi):
    link = query_builder(npi)
    response = single_query(link)
    physician = parse_response(response)
    return physician


def get_npi():
    return ['1245319599', '1346336807']

def loop_through_queries():
    for npi in get_npi():
        physician = get_physician(npi)
        print(physician)
        table.insert(physician)

def scrape_meta():
    pass

def get_data():
    pass

if __name__ == '__main__':
    pass
    # scrape_meta()
    # get_physicians(table)
