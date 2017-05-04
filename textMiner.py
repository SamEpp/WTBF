
import wikipedia
from bs4 import BeautifulSoup
import indicoio
from key import indico_key
indicoio.config.api_key = indico_key


def getAuthorLocation(book):
    if book.title != '':
        loc = find_author_origin(book.title)
        if loc is 'DisambiguationError':
            loc = find_author_origin(book.title + ' (novel)')
        if loc is 'StopIteration':
            return 'Author location not found on Wikipedia'
        if loc is 'PageError':
            return 'Book not found on Wikipedia'
        return loc
    return 'Book object has no title'


def getPublisherLocation(book):
    if book.publisher != '':
        loc = find_publisher_location(book.publisher)
        if loc is 'PageError':
            return 'Publisher not found on Wikipedia'
        if loc is 'DisambiguationError':
            return 'Publisher name not specific enough'
        return loc
    return 'Book object has no publisher'


def getPlotLocation(book):
    if book.title != '':
        loc = find_plot_country(book.title)
        if loc is 'DisambiguationError':
            print("Disambuguation")
            loc = find_plot_country(book.title + ' (novel)')
        if loc is 'StopIteration':
            return 'Plot location not found on Wikipedia'
        if loc is 'PageError':
            return 'Book not found on Wikipedia'
        return loc
    return 'Book object has no title'


def find_author_origin(book_page_name):
    '''Input: the name of a book's wikipedia page in the form of a string.
    Returns: the author and the country where the book takes place.
    Common program holes: books that are part of a series, books whose pages don't list
    the Country in the info box.
    Common user errors will probably include: inputting just the title of a book
    when the title of its wikipedia page contains more than simply the title of
    the book (i.e. "Emma (novel)").'''

    try:
        page_results = wikipedia.page(book_page_name)
    except wikipedia.exceptions.DisambiguationError:
        return 'DisambiguationError'
    except wikipedia.exceptions.PageError:
        return 'PageError'
    page_html = page_results.html()    # generate the page's html.
    soup = BeautifulSoup(page_html, "lxml")    # make it readable
    table = soup.findAll("table", {"class": "infobox"})  # select all parts that are prefixed by <th> (includes the country of the book)

    all_th = soup.table.find_all('th')
    try:
        country_header = next(element for element in all_th if element.getText() == 'Country')
    except StopIteration:
        return 'StopIteration'
    country_name = country_header.findNext('td').getText().strip()
    return country_name


def find_publisher_location(book_publisher):
    try:
        page_results = wikipedia.page(book_publisher)
    except wikipedia.exceptions.PageError:
        return 'PageError'
    except wikipedia.exceptions.DisambiguationError:
        return 'DisambiguationError'

    page_html = page_results.html()    # generate the page's html.
    soup = BeautifulSoup(page_html, 'lxml')    # make it readable

    all_tr = soup.find_all('tr')  # finds all of the table rows
    trlist = [element.getText() for element in all_tr]  # makes a pretty list with just text

    found = False
    for i in trlist:
        if i.startswith("Headquarters"):
            location = i
            found = True
    if not found:
        return "Publisher Location not found on Wikipedia"
    return location[22:]  # starts after "Location headquarters" and just returns the location


def find_plot_country(book_page_name):
    try:
        page_results = wikipedia.page(book_page_name)
    except wikipedia.exceptions.DisambiguationError:
        return 'DisambiguationError'
    except wikipedia.exceptions.PageError:
        return 'PageError'
    places = []
    page_plot = page_results.section('Plot')
    if page_plot is not None and page_plot != '':
        places = indicoio.places(page_plot)

    if places == []:
        page_summary = page_results.summary
        places = indicoio.places(page_summary)
    potentials = []
    for item in places:
        potentials.append((item['confidence'], item['text']))
    potentials.sort(reverse=True)

    if potentials != []:
        return potentials[0][1]
    return 'Plot location not found on Wikipedia'
