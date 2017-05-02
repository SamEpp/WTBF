---
title: Implementation
layout: template
filename: implementation
---
# Code Structure
![Code_structure](/pictures/Code_structure.PNG)

### Scan a book and get basic info
The library isbnlib takes an ISBN entered manually or with a barcode scanner and looks up some basic information such as title, author, publisher, language, and publication year.

### Look up information on Wikipedia
Next, the program uses the Wikipedia library to find the book page and publisher page and download the HTML.

Author location is found by searching the HTML of the book's page, and publisher location is pulled from the publisher's page

Another library called inidicoio searches through the book page for information that looks like locations. It returns its confidence in all of the places it finds, and the highest-confidence location becomes the plot location.

All of these attributes are then written to the Book object.

### Plot the locations in a plotly choropleth map

# Results
Our software quickly finds the book associated with the ISBN entered, looks up the book on Wikipedia, searches for relevant information, and plots the locations it finds on a map.
