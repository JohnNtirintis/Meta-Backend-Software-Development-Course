class MyClass:
    index = "Author-Book"
    def __init__(self, author, book):
        self.author = author
        self.book = book

    def hand_list(self):
        return self.author + " wrote the book: " + self.book

platoBook = MyClass("Plato", "Republic")
sunTzuBook = MyClass("Sun Tzu", "Art of War")

print(platoBook.hand_list())
print(sunTzuBook.hand_list())
