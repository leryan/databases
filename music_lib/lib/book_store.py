"""

Set up a new project called book_store from the starter.
Use the book_store SQL seed instead of the music_library seed. You can find this in the seeds directory in the starter.
Start recording yourself.
Test-drive a Book class that has attributes for each column in the books table.
Test-drive a BookRepository class that has a method all that returns a list of Book objects.
Write a small program in app.py using the class BookRepository to print out the list of books to the terminal.
You should get an output that looks roughly like this:

# In the project directory book_store

; pipenv shell
; python app.py

1 - Nineteen Eighty-Four - George Orwell
2 - Mrs Dalloway - Virginia Woolf
3 - Emma - Jane Austen
4 - Dracula - Bram Stoker
5 - The Age of Innocence - Edith Wharton

"""

class Book:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author_name})"


# Example format below        
# class Album:
#     def __init__(self, id, title, release_year, artist_id):
#         self.id = id 
#         self.title = title 
#         self.release_year = release_year
#         self.artist_id = artist_id

#     def __eq__(self, other):
#         return self.__dict__ == other.__dict__

#     def __repr__(self):
#         return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"