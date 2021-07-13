LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    },
    {
        "name": "East Nashville",
        "address": "111 Eastland Dr",
        "id": 3
    },
    {
        "name": "Franklin",
        "address": "111 Hillsboro",
        "id": 4
    }
]


def get_all_locations():
    """returning the location dictonaries
    """
    return LOCATIONS

# Function with a single parameter


def get_single_location(id):
    """loop over location dictonaries
    """
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the locations list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location):
    """creating new location
    """
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)

    return location

def delete_location(id):
    """delete location by id
    """
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the locationS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)
