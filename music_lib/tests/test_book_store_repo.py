from lib.book_store_repo import BookRepository
from lib.book_store import Book

"""
When #all is called
We get back all the books as instances
"""

def test_all(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repo = BookRepository(db_connection)
    result = repo.all()
    assert result == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
    ]