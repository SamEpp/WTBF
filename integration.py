# Rowan Sharman, Gracey Wilson

'''
This script runs all of the necessary commands to look up a book and display
the output map. It also takes care of user input.
'''
import isbnlib
from LocationsToMap import plotGraph
from classBook import Book


def pickInput():
    '''
    Request user choice for lookup by ISBN or title
    INPUT: None
    OUTPUT: string (usually 's' or 't') or False
    '''
    choice = ''
    while choice != 's' and choice != 't':
        choice = input("Press 's' to scan or enter ISBN or 't' to enter title: ")
        if choice == 'x':  # Exit program when 'x' entered
            return False
    return choice


def getIsbn():
    '''
    Request user input of ISBN number
    INPUT: None
    OUTPUT: Valid ISBN string or False
    '''
    code = input('Scan book barcode or enter ISBN code: ')
    if code == 'x':  # Exit program when 'x' entered
        return False
    while isbnlib.notisbn(code):
        code = input('\nPlease scan or enter a valid ISBN code: ')
        if code == 'x':  # Exit program when 'x' entered
            return False
    return code


def getTitle():
    '''
    Request user input of a book title
    INPUT: None
    OUTPUT: String (ostensibly a book title) or False
    '''
    title = input("Enter a book title: ")
    if title == 'x':  # Exit program when 'x' entered
        return False
    return title


if __name__ == '__main__':
    while True:
        choice = pickInput()

        if choice == 's':
            isbn = getIsbn()
            if not isbn:  # Exit program when 'x' entered
                break
            thisBook = Book(isbn)
            thisBook.getInfo()

        elif choice == 't':
            title = getTitle()
            if not title:  # Exit program when 'x' entered
                break
            thisBook = Book(title)
        else:
            break
        thisBook.getLocations()
        print(thisBook)
        plotGraph(thisBook)
