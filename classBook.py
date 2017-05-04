# Rowan Sharman

import isbnlib
import textMiner


class Book:
    '''
    A class to keep track of all information known about a book.
    Also contains functions which call textMiner to get more information.
    ATTRIBUTES:
        isbn
        title
        author
        publisher
        year
        language
        authorLoc
        publisherLoc
        plotLoc
    '''

    def __init__(self, info):
        '''
        Instantiate Book objects with either ISBN or title
        INPUT: String that is either a book title or an ISBN
        OUTPUT: None
        '''

        if isbnlib.notisbn(info):  # Instantiate using ISBN
            self.title = info
            self.isbn = ''

        else:  # Instantiate using title
            self.isbn = info
            self.title = ''

        # Create all attributes that will be used
        self.author = 'x'
        self.publisher = 'x'
        self.year = 'x'
        self.language = 'x'
        self.authorLoc = 'x'
        self.publisherLoc = 'x'
        self.plotLoc = 'x'

    def getInfo(self):
        '''
        Get basic info stored in remote ISBN database
        INPUT: None
        OUTPUT: None (updates attributes of self)
        '''

        self.info = isbnlib.meta(self.isbn)

        # If ISBN found in database, write info to attributes
        if self.info is not None:
            self.title = self.info['Title']
            self.author = self.info['Authors']
            self.publisher = self.info['Publisher']
            self.year = self.info['Year']
            self.language = self.info['Language']

    def getLocations(self):
        '''
        Use textMiner to get whatever locations possible
        INPUT: None
        OUTPUT: None (updates attributes of self)
        '''

        if self.title != '':
            self.authorLoc = textMiner.getAuthorLocation(self)
            self.plotLoc = textMiner.getPlotLocation(self)
        else:
            self.authorLoc = 'Book is missing title'
        if self.publisher != '':
            self.publisherLoc = textMiner.getPublisherLocation(self)
        else:
            self.publisherLoc = 'Book is missing publisher info'

    def __str__(self):  # Print all known information about the book
        '''
        Provide pretty printable string containing all known attributes
        INPUT: None
        OUTPUT: Printable string
        '''

        infoString = ''
        infoString += ('Title:\t\t\t' + self.title + '\n')

        # Deal with printing single/multiple authors coherently
        plural = 'Author:\t\t\t'
        authors = ''
        if self.author != '':
            for element in self.author:
                if len(authors) > 1:
                    plural = 'Authors:\t\t'
                    authors += ', ' + element
                else:
                    authors += element
        infoString += (plural + authors + '\n')

        infoString += ('Publisher:\t\t' + self.publisher + '\n')
        infoString += ('Year:\t\t\t' + self.year + '\n')
        infoString += ('Language:\t\t' + self.language + '\n')
        infoString += ('Author Location:\t' + self.authorLoc + '\n')
        infoString += ('Publisher Location:\t' + self.publisherLoc + '\n')
        infoString += ('Plot Location:\t\t' + self.plotLoc + '\n')

        return infoString
