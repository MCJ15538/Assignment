#Creation of book member and library classes with encapsulation
#Introducing the underscore in front of the variables encapsulates them meaning that they are protected
from enum import member
from operator import truediv


class Book:
    def __init__(self, book_code, title):
        self._book_code = book_code     #protexted attribute
        self._title = title         #protexted attribute
        self._borrowed_books = True #protexted attribute

class Member:
    def __init__(self, member_id, name):
        self._member_id = member_id      #protexted attribute
        self._name = name                #protexted attribute
        self._borrowed_books = []        #protexted attribute

class Library:
    def __init__(self):
        self._books =[]        #protexted attribute
        self._members =[]      #protexted attribute

#Below we see the implementation of Inheritance and polymorphism
# the member class is already created therefore we shall only implement the subclasses student and teacher

class Student(Member):         #students can borrow a maximum of 7 books
    def max_books(self):
        return 7

class Teachers(Member):        #teachers are allowed to borrow upto 10 books
    def max_books(self):
        return 10

#Below we see the controlled access

class Book:
    def __init__(self, book_code, title):
        self._book_code = book_code
        self._title = title
        self._is_borrowed = False

    def is_borrowed(self):
        return self._is_borrowed

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False

    def return_book(self):
        if self._is_borrowed:
            self._is_borrowed = False
            return True
        return False















