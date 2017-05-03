---
title: How to Use It
layout: template
filename: instructions
---

# How to use it

### Libraries to Download
You will need to install these Python libraries:
- isbnlib
- wikipedia
- bs4
- folium
- indicoio (create an account and paste your key into a file "key.py")
- opencage (create an account and paste your key into a file "key.py")

### How to Run It
1. Run "integration.py" with Python 3
2. Follow instructions to choose input method and enter book title or scan ISBN.
3. Navigate to the directory where the python files are stored, and open map.html in a browser

### Results
After entering the book information, the program searches an ISBN database (if applicable) and Wikipedia for more information. The information found is displayed in the terminal, and whatever locations found are saved to an HTML file which displays the locations on a map when opened with a browser. An example is shown below.

### Example: Jane Eyre
![Jane Eyre](/pictures/janeeyre.png)
![Jane Eyre gif](/pictures/janeeyre.gif)
