# mapquest_ui.py

# This module is responsible for tying together
# the user input, the API module and the output
# module through various functions.

import mapquest_api
import mapquest_op


def _num_of_inputs() -> int:
    
    # Gets the number of address the user wants to navigate to
    # and returns and integer value.
    # It also makes sure that the value entered by the user is
    # an integer, and handles all appropriate errors as well.
    
    while True:
        try:
           print('Enter the number of addresses (minimum 2):')
           address_num = int(input())
           if address_num < 2:
                print('Error; enter a value of 2 or larger')
           else:
               return address_num
               break
        except ValueError:
            print('Error; the number of address you want to navigate to has to be an integer')
        except TypeError:
           print('Error; the number of address you want to navigate to has to be an integer')
        

def get_addresses() -> str:
    
    # Gets the addresses of the different locations the user wants
    # to navigate to and returns a list of those addresses.
    
    address_num = _num_of_inputs()
    locations = []
    for location in range(address_num):
        if (location == 0):
            print("FROM: ")
        elif (location == address_num-1):
            print("TO: ")
        else:
            print("STOP: ")
        location = input()
        locations.append(location)
    return locations


def get_actions() -> list:

    # Receives the actions given by a user and returns
    # a list of actions
    actions = []
    print("List of Actions:")
    print("STEPS: Detailed steps of journey")
    print("TOTALDISTANCE: Total distance traveled")
    print("TOTALTIME: Total time traveled")
    print("LATLONG: Latitude and Longitude")
    print("ELEVATION: Elevation\n")
    while True:
        print("Enter action or STOP to process request:")
        action = input()
        if (action == "STOP"):
            if (len(actions) != 0):
                break;
            else:
                print("ERROR: need at least 1 action")
        else:
            actions.append(action)
    return actions

def process_info(addresses:list, actions:list) -> str:

    # This function takes in the acquired list of actions
    # and addresses, and passes them on to the output module
    # with respect to the user-entered command.
    
    for action in actions:
        if action == 'STEPS':
            directions = mapquest_api.get_result(mapquest_api.creating_dir(addresses))
            mapquest_op.STEPS.run(directions)
        if action == 'TOTALDISTANCE':
            directions = mapquest_api.get_result(mapquest_api.creating_dir(addresses))
            mapquest_op.TOTALDISTANCE.run(directions)
        if action == 'TOTALTIME':
            directions = mapquest_api.get_result(mapquest_api.creating_dir(addresses))
            mapquest_op.TOTALTIME.run(directions)
        if action == 'LATLONG':
            directions = mapquest_api.get_result(mapquest_api.creating_dir(addresses))
            mapquest_op.LATLONG.run(directions)
        if action == 'ELEVATION':
            directions = mapquest_api.get_result(mapquest_api.creating_dir(addresses))
            mapquest_op.ELEVATION.run(directions)
    print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
                
                
if __name__ == '__main__':
    addresses = get_addresses()
    actions = get_actions()
    process_info(addresses, actions)
 
    
    
              
    

        
