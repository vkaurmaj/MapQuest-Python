# mapquest_api.py

# This module handles all the connections between the whole program
# and the MapQuest API online


# Consumer Key: NQCHIGr6QVLGVhWoHo14iPYpyFGW9lYE
# Consumer Secret: kGlZ5D0GtHRkrVBF

import json
import urllib.parse
import urllib.request

##########################################################

MAPQUEST_KEY = 'NQCHIGr6QVLGVhWoHo14iPYpyFGW9lYE'

##########################################################

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/route?key='+ MAPQUEST_KEY + '&'

ELEVATION = 'http://open.mapquestapi.com/elevation/v1/'


def creating_dir(locations: list) -> str:
    info_list = []
    info_list.append(('from',locations[0]))
    for place in locations[1:]:
        info_list.append(('to', place))
    return BASE_MAPQUEST_URL + urllib.parse.urlencode(info_list)

def elevation(locations:str) -> str:
    parameters = [('key', MAPQUEST_KEY), ('unit','f'), ('latLngCollection', locations)]
    return ELEVATION + 'profile?' + urllib.parse.urlencode(parameters)

def get_result(url: str) -> dict:
    RESPONSE = None
    try:
        RESPONSE = urllib.request.urlopen(url)
        response = RESPONSE.read().decode(encoding = 'utf-8')
        return json.loads(response)
    except urllib.error.URLError:
        print()
        print('MAPQUEST ERROR')
        if RESPONSE != None:
            RESPONSE.close()
