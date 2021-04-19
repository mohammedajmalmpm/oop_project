"""Library Management System
    Class - Library --> display_book, borrow_book, add_book
    class - Student --> take_book, return_book.
"""

class Library:
    def __init__(self,availableBooks):
        """Init function

        Args:
            availableBooks ([str]): [all available books in the library]
        """
        self.books = availableBooks

    def display_book(self):
        """Display all books
        """
        for book in self.books:
            print(book)

    def lend_book(self,lndbook):
        """Lend Book

        Args:
            lndbook ([str]): [book name from user]
        """
        print("Enter the Book")
        self.book = lndbook
        if self.book in self.books:
            print(f'you borrowed {self.book} now')
            self.books.remove(self.book)
        else:
            print("Book is not available")

    def return_books(self,rbook):
        """Returned Books

        Args:
            rbook ([str]): [return book from user input]
        """
        print(rbook)
        self.books.append(rbook)
        print("book is returned")

    def add_book(self):
        """Add Book to the library

        Returns:
            [str]: [Add book to the library ]
        """
        print("add your book")
        self.add_book = str(input())
        if self.add_book in self.books:
            return f'{self.add_book} is already in library'
        else:
            self.books.append(self.add_book)
            return f'{self.add_book} is added in library'

class Student():
    def request_Book(self):
        """To Request for book

        Returns:
            [str]: [return user input book name]
        """
        print("Enter the book you needed")
        self.request_Book = input()
        return self.request_Book

    def return_book(self):
        """To return book

        Returns:
            [str]: [To return book as per user input]
        """
        print("Enter the book you return")
        self.return_bk = input()
        #print(self.return_bk)
        return self.return_bk

def main():
    """In main function call student class and Library class with list of books

    Returns:
        [type]: [description]
    """
    lib = Library(["abcd","asdf","xvgf"])
    student = Student()
    done = False
    while done == False:
        print("Enter your choice")
        print("1- List of available book\n2-borrow book\n3-return book\n4-add_book")
        choice = int(input("enter choice"))
        if choice == 1:
            lib.display_book()
        elif choice == 2:
            lib.lend_book(student.request_Book())
        elif choice == 3:
            lib.return_books(student.return_book())
        elif choice == 4:
            print(lib.add_book())
        else:
            print("Invalid Choice")
            break

if __name__ == '__main__':
    main()
"""issues
1 - thrown erro when same option enter twise at a time.
"""
