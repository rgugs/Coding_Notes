class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        check_title = book.title.lower()
        check_author = book.author.lower()

        for b in self.books:
            lib_title = b.title.lower()
            lib_author = b.author.lower()
            
            if check_title == lib_title and check_author == lib_author:
                self.books.remove(b)
                

    def search_books(self, search_string):
        ss_lower = search_string.lower()
        matched_list = []
        for b in self.books:
            lib_title = b.title.lower()
            lib_author = b.author.lower()

            if ss_lower in lib_author or ss_lower in lib_title:
                matched_list.append(b)
        return matched_list


book1 = Book('Little Women', 'Louisa May Alcott')
book2 = Book('Frankenstein', 'Mary Shelley')
book3 = Book('Dragon Song', 'Anne McCaffrey')
book4 = Book('A Wrinkle in Time', "Madeleine L'Engle")
book5 = Book('little Women', 'louisa May Alcott')

home_lib = Library('Home')

home_lib.add_book(book1)
home_lib.add_book(book2)
home_lib.add_book(book3)

# home_lib.remove_book(book5)

for b in home_lib.books:
    print(b.title)

print('---------')

matches = home_lib.search_books('dra')

for m in matches:
    print(m.title)