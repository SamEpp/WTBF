# Sarah Barden
'''Takes an ISBN code and returns a map highlighting the locations of
the Author, Plot and Publisher.'''

import folium   # library for data visualization on maps
from opencage.geocoder import OpenCageGeocode  # geocoding service
from key import geokey
from time import sleep


def geocode(place):
    """
    Uses the OpenCage geocoder to get latitude and longitude of a place.

    INPUT: a place name as an attribute of a book object
    OUTPUT: a list containing the latitude and longitude for that place
    """
    geocoder = OpenCageGeocode(geokey)
    location = geocoder.geocode(place, key=geokey)
    # We search wikipedia for 3 locations, but don't always get 3.
    # If a location isn't found, it's an empty list, so we do not plot it.
    if location == []:
        pass
    else:
        longitude = location[0]['geometry']['lng']  # lat/long are within a nested
        latitude = location[0]["geometry"]["lat"]   # results dictionary under geometry
        print(latitude, longitude)
        return [latitude, longitude]


def plotGraph(book):
    """
    Takes a book object and uses geocode() to find locations of three attributes:
    author location, publisher location, and plot location.

    INPUT: a book object
    OUTPUT: a map with pins on locations
    """
    # Creates the map
    map1 = folium.Map(zoom_start=2, tiles='Mapbox bright')

    # Adds marker for the each location
    locations = [book.authorLoc, book.publisherLoc, book.plotLoc]
    colors = ['red', 'green', 'blue']
    popups = ['{} is from {}'.format(book.author, book.authorLoc),
              'This edition was published in {}'.format(book.publisherLoc),
              '{} takes place in {}'.format(book.title, book.plotLoc)]

    # Loops through lists above to create markers
    for i in range(0, 3):
        if locations[i] == []:
            pass
        else:
            folium.Marker(geocode(locations[i]),
                          icon=folium.Icon(color=colors[i]),
                          popup=popups[i]
                          ).add_to(map1)
        sleep(1)  # Delays calls to open cage geocoder
    map1.save('map.html')


if __name__ == '__main__':
    pass
