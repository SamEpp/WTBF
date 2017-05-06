---
title: How It Works
layout: template
filename: HowItWorks
---
# Code Structure
![codestructure](/pictures/codestructure.png)

### 1) Scan a book and get basic info.
The library isbnlib takes an ISBN entered manually or with a barcode scanner and looks up some basic information such as title, author, publisher, language, and publication year.

### 2) Look up location information.
Next, the program uses the [Wikipedia](https://pypi.python.org/pypi/wikipedia/) library to find the book and publisher's pages and download the HTML. The author's location is found by searching the HTML of the book's Wikipedia page. The publisher's location is pulled from the HTML of the publisher's Wikipedia page.

An API called [indico](https://indico.io/) searches through the book page for information that looks like locations. It returns its confidence in all of the places it finds, and the highest-confidence location becomes the plot location.

All of these locations are then written to the Book object as attributes.

### 3) Plot the locations on a map.
Finally, the locations associated with the ISBN code originally are plotted on a map. First, we take the location name and lookup it's latitude and longitude using the [OpenCage Geocoder API](https://geocoder.opencagedata.com/).  Then, we plot a pin at that latitude and longitude using the [Folium](https://github.com/python-visualization/folium) library.
