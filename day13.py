#!/bin/python3

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def display(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Price: ", self.price)


class myBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author, price)


title = input()
author = input()
price = int(input())

newNovel = myBook(title, author, price)
newNovel.display()
