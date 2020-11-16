# mapquest_op.py

# This module is responsible for the behind-the-scenes
# processes that receive actions and addresses from the
# user, and print the appropriate information.

import mapquest_api

class STEPS:

    # This class takes in a dictionary created
    # by the mapquest API module, which collects
    # information from the online MapQuest Public
    # API, and uses it to print step by step
    # directions between a set of addresses entered
    # by the user.
    
    def run(response) -> None:
        try:
            steps = []
            for x in response['route']['legs']:
                for y in x['maneuvers']:
                    steps.append(y['narrative'])
            print()
            print('DIRECTIONS:')
            for items in steps:
                print(items)
        except TypeError:
            pass
        except KeyError:
            print()
            print('NO ROUTE FOUND')
    
class TOTALDISTANCE:

    # This class takes in a dictionary created by the
    # mapquest API module and uses it to print the total
    # distance the user has to travel to get from their
    # initial destination to their final destination.
    
    def run(response) -> None:
        try:
            print()
            print('TOTAL DISTANCE: ' + str(round((response['route']['distance']))) + ' miles')
        except TypeError:
            pass
        except KeyError:
            print()
            print('MAPQUEST ERROR')


class TOTALTIME:

    # This class takes in a dictionary created by the mapquest
    # API module and uses it to print the total time it would take
    # the user to get from their initial location to their final
    # destination.
    
    def run(response) -> None:
        try:
            print()
            print('TOTAL TIME: ' + str(round((response['route']['time'])/60)) + ' minutes')
        except TypeError:
            pass
        except KeyError:
            print()
            print('MAPQUEST ERROR')
    
            
class LATLONG:

    # This class takes in a dictionary created by the mapquest
    # API module and uses it to print the lattitude and longitude
    # of all the user inputted addresses in a specific format.

    def process_latlong(number: float) -> str:
        try:
            space = ''
            if number >= 0:
                return space + str(round(abs(number))) + ' °N'
            if number <= 0:
                return space + str(round(abs(number))) + ' °S'
            if number >= 0:
                return space + str(round(abs(number))) + ' °W'
            if number <= 0:
                return space + str(round(abs(number))) + ' °E'
        except KeyError:
            print()
            print('MAPQUEST ERROR')

    def assemble_list(response: dict):
        try:
            latlng = []
            for x in response['route']['locations']:
                latlong = (x['latLng']['lat'], x['latLng']['lng'])
                latlng.append(latlong)
            return latlng
        
        except TypeError:
            pass
        except KeyError:
            print()
            print('MAPQUEST ERROR')
            
    def run(response) -> None:
        try:
            latlng = LATLONG.assemble_list(response)
            print()
            print('LATLONG:')
            for items in latlng:
                print(LATLONG.process_latlong(items[0]), LATLONG.process_latlong(items[1]))
        except TypeError:
            pass
        except KeyError:
            print()
            print('MAPQUEST ERROR')
        
    
class ELEVATION:

    # This class uses the dictionary created by the mapquest
    # API module and a list from the assemble_list function
    # from the LATLONG class to calculate the elevation of the
    # different user inputted addresses.
    
    def run(response: dict) -> None:
        try:
            latlng = LATLONG.assemble_list(response)
            print()
            print('ELEVATION:')
            for items in latlng:
                y = str(abs(items[0])) + ',' + str(abs(items[1]))
                elev = mapquest_api.get_result(mapquest_api.elevation(y))
                for x in elev['elevationProfile']:
                    print(round(x['height']))
        except TypeError:
            pass
        except KeyError:
            print()
            print('MAPQUEST ERROR')
        
