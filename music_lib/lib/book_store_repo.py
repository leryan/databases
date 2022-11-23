from lib.book_store import Book

class BookRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM books")
        return [
            Book(row["id"], row["title"], row["author_name"])
            for row in rows
        ]