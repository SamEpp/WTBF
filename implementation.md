---
title: Implementation
layout: template
filename: implementation
---
# Code Structure
<img src="/pictures/Code_structure.PNG">

### Scan a book and use isbnlib
Get book’s title, author, publisher, etc. 
Make them attributes of a Book object

### That info + text mining from wikipedia = locations:
Publisher headquarters 
Author's birthplace
Where the book takes place
Make this information attributes of the Book object

### Plot the locations in a plotly choropleth map

# Results
Our software quickly finds the book associated with the ISBN entered, looks up the book on Wikipedia, searches for relevant information, and plots the locations it finds on a map.
