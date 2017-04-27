---
title: How to Use It
layout: template
filename: instructions
---

# How to use our project

### Libraries to Download
You will need to install these Python libraries:
- isbnlib
- plotly
- wikipedia
- bs4
- indicoio (create an account and paste your key into a file "key.py")

### How to Run It
1. Run "integration.py" with Python 3
2. Follow instructions to choose input method and enter book title or scan ISBN.

# Code Structure
hello4
![Code_structure](/pictures/Code_structure.PNG)

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
