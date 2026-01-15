# classmethods & staticmethods

class Book:

    format = 'Paperback'

    def __init__(self, book_title, author_name, no_of_pages):
        self.book_title = book_title
        self.author_name = author_name
        self.no_of_pages = no_of_pages

    def description(self):
        print(f"Title: {self.book_title}")
        print(f"Author: {self.author_name}")
        print(f"Pages: {self.no_of_pages}")

    @classmethod
    def formatSpecifier(cls, format):
        cls.format = format

    @classmethod
    def fromString(cls, str_unreleased):
        # alternate constructor
        book_name, author_name = str_unreleased.split(' - ')
        return cls(book_name, author_name, 0)
    
    @staticmethod
    def publishingHouse():
        return 'Harper Voyager'

# A class method takes cls as the first parameter while a static method needs no specific parameters. 
# A class method can access or modify the class state while a static method can’t access or modify it.

agot = Book('A Game of Thrones', 'George R.R. Martin', 694)
acok = Book('A Clash of Kings', 'George R.R. Martin', 768)
asos = Book('A Storm of Swords', 'George R.R. Martin', 973)
afoc = Book('A Feast of Crows', 'George R.R. Martin', 753)
adwd = Book('A Dance with Dragons', 'George R.R. Martin', 1056)

print(f"Book.format = {Book.format}")
Book.format = 'Hardcover'
print(f"Book.format = {Book.format}")
Book.formatSpecifier('Graphic Novel')
print(f"Book.format = {Book.format}")

agot.formatSpecifier('E-book')
acok.formatSpecifier('E-book')
asos.formatSpecifier('E-book')
afoc.formatSpecifier('E-book')
adwd.formatSpecifier('E-book')

awow_unreleased = 'The Winds of Winter - George R. R. Martin'
ados_unreleased = 'A Dream of Spring - George R. R. Martin'
awow = Book.fromString(awow_unreleased)
ados = Book.fromString(ados_unreleased)
awow.description()
ados.description()

print(f"Book.publishingHouse(): {Book.publishingHouse()}")
