from lib.book_store import Book

"""
Constructs with
    id, title, author_name
"""

def test_contructs_all_fields():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book.id == 1
    assert book.title == 'Nineteen Eighty-Four'
    assert book.author_name == 'George Orwell'

"""
Can compare two identical books
And have them be equal
"""

def test_books_are_equal():
    book1 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    book2 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book1 == book2

"""
The books are formatted and presented nicely
"""

def test_formatted_correct():
    book = Book(1, "Nineteen Eighty-Four", "George Orwell")
    assert str(book) == "Book(1, Nineteen Eighty-Four, George Orwell)"
