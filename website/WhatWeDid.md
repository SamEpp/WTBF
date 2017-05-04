---
title: Implementation
layout: template
filename: WhatWeDid
---
# Code Structure
![codestructure](/pictures/codestructure.png)

### 1) Scan a book and get basic info.
The library isbnlib takes an ISBN entered manually or with a barcode scanner and looks up some basic information such as title, author, publisher, language, and publication year.

### 2) Look up location information.
Next, the program uses the Wikipedia library to find the book and publisher's pages and download the HTML. The author's location is found by searching the HTML of the book's Wikipedia page. The publisher's location is pulled from the HTML of the publisher's Wikipedia page.

Another library called inidicoio searches through the book page for information that looks like locations. It returns its confidence in all of the places it finds, and the highest-confidence location becomes the plot location.

All of these locations are then written to the Book object as attributes.

### 3) Plot the locations on a map.
Finally, the locations associated with the ISBN code originally entered, are plotted on a map using a library called Folium.
