class Book:
    def __init (self, book_id: str, title: str, author: str, is_borrowed: bool = False)
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    
    def borrow(self):
        if self.is_borrowed is False:
            self.is_borrowed = True
    
    def return_book(self):
        if self.is_borrowed is True:
            self.is_borrowed = False

class Member:
    def __init__ (self, member_id: str, name: str, borrowed_books: list[str]):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books
    
    def borrow_book(self, book: Book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
        return self.borrowed_books
    
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        return self.borrowed_books
    
class Library:
    def __init__(self, books: dict[str, Book], members: dict[str, Member]):
        self.books = books
        self.members = members
    
    def add_book(self, book_id: str, title: str, author: str):
        if book_id not in self.books.keys():
            new_books = Book(title, author)
            return self.books.update(book_id, new_books)
    
    def register_member (self, member_id: str, name: str):
        if member_id not in self.members.keys():
            new_member = Member(name)
            return self.members.update(member_id, new_member)
    
    def borrow_book(self, member_id: str, book_id: str):
        if 