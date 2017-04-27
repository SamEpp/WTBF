---
title: How to Use It
layout: template
filename: instructions
---

## How to use our project

### Libraries to Download
You will need to download these libraries in python:
- isbnlib
- plotly
- wikipedia
- bs4
- indicoio (create an account and paste your key into a file "key.py")

### How to Run It
1. Run "python3 integration.py" in the terminal
2. When prompted use a barcode scanner on the book or enter an isbn number.
3. A map with the book's locations will appear! At the top of the page there will be information

### Code Structure
![alt text](https://github.com/SamEpp/BookLocationPlotter/blob/master/Code_structure.PNG "")

#### Our Code is structured into 3 main parts

##### Scan a book and use isbnlib
Get book’s title, author, publisher, etc. 
Make them attributes of a book object

##### That info + text mining from wikipedia = locations:
Publisher headquarters 
Author's birthplace
Where the book takes place

##### Plot the locations in a plotly choropleth map
