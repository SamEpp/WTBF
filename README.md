# Welcome to "Where's That Book From?"
### **Team InterWEBS**: Gracey Wilson, Sam Eppinger, Sarah Barden, Rowan Sharman
Have you ever wondered where your favorite book takes place? What about where the author of the book is from? How do those two things relate to where the publisher of the book is located? Then, this software is for you. All that is needed is a book's barcode (the isbn) which we will scan into our program and output a map with all the locations you've been missing for so long.

## How to use it

### Libraries to Download
You will need to install these Python libraries:
- isbnlib
- wikipedia
- bs4
- folium
- indicoio (create an account and paste your key into a file "key.py")
- opencage (create an account and paste your key into a file "key.py")

key.py should look like this:

indicoio_key = 'your key'

geo_key = 'your key'

### How to Run It
1. Run "integration.py" with Python 3
2. Follow instructions to choose input method and enter book title or scan ISBN.
3. Navigate to the directory where the python files are stored, and open map.html in a browser

### Here's an example
Jane Eyre (isbn: 9780679886181)
![Jane Eyre gif](/pictures/janeeyre.gif)

[Visit our website!](https://samepp.github.io/WTBF)

