# Test-driving a Repository class

_**This is a Makers Vine.** Vines are designed to gradually build up
sophisticated skills. They contain a mixture of text and video, and may contain
some challenge exercises without proposed solutions. [Read more about how to use
Makers
Vines.](https://github.com/makersacademy/course/blob/main/labels/vines.md)_

Learn to test-drive **Model** and **Repository** classes to SELECT records from
the database.

## Introduction

[This is a bit easier to follow on the
video.](https://www.youtube.com/watch?v=POF2BNCBAgI&t=0s)

### Models and Repositories

In the realm of PostgreSQL, we manipulate tables, column names and records.
However, in Python programs, we represent data using classes, objects and
attributes. We therefore need a way to transform the data retrieved from the
database into data that can be used in our program. 

To achieve this, you will learn how to build two kind of classes — they're
regular Python classes, but designed to achieve a specific purpose in our
program:

* A **Model** class is used to hold a record's data.  
  For example, if we have a table `artists`, we'd have a class `Artist`, with
  attributes for each column. A single object holds the data for a specific
  artist record. This class usually doesn't contain any logic, but is only used
  to hold data.

* A **Repository** class implements methods to run SQL queries on the database
  to retrieve, create, update or delete data.  
  For example, if we have one table `artists`, we'd have a class
  `ArtistRepository` containing methods that communicates with the database
  using SQL.

### Designing a Repository class

We will build our repository class progressively over the next challenges. We
are going to start with the `all` method. This returns a list of all of the
records in the table.

Here is an example for the `ArtistRepository` class described above.

| Method | Job             | Arguments | SQL query it executes    | Returns             |
| ------ | --------------- | --------- | ------------------------ | ------------------- |
| `all`  | Get all artists | none      | `SELECT * FROM artists;` | A list of `Artist`s |

You can see an example of the code for these in the project starter.

## Exercise

Your assignment is to test-drive an `Album` class and an `AlbumRepository` class
with an `all` method.

1. Work in the `music_library` project you created earlier.
2. Test-drive an `Album` class that has attributes for each column in the
   `albums` table. You can find the table in `seeds/music_library.sql`.
3. Test-drive an `AlbumRepository` class that has a method `all` that returns a
   list of `Album` objects.
4. Write a small program in `app.py` using the class `AlbumRepository` to print
   out the list of albums to the terminal. 

[Example Solution](https://www.youtube.com/watch?v=POF2BNCBAgI&t=1721s)

## Challenge

This is a process feedback challenge. That means you should record yourself
doing it and submit that recording to your coach for feedback. [How do I do
this?](https://github.com/makersacademy/golden-square/blob/main/pills/process_feedback_challenges.md)

Your assignment is to test-drive a `Book` class and a `BookRepository` class
with an `all` method.

1. Set up a new project called `book_store` from the
   [starter](https://github.com/makersacademy/databases-in-python-project-starter).
2. Use the `book_store` SQL seed instead of the `music_library` seed. You can
   find this in the `seeds` directory in the starter.
3. Start recording yourself.
4. Test-drive a `Book` class that has attributes for each column in the `books`
   table.
5. Test-drive a `BookRepository` class that has a method `all` that returns a
   list of `Book` objects.
6. Write a small program in `app.py` using the class `BookRepository` to print
   out the list of books to the terminal.

You should get an output that looks roughly like this:

```shell
# In the project directory book_store

; pipenv shell
; python app.py

1 - Nineteen Eighty-Four - George Orwell
2 - Mrs Dalloway - Virginia Woolf
3 - Emma - Jane Austen
4 - Dracula - Bram Stoker
5 - The Age of Innocence - Edith Wharton
```

[After you're done, submit your recording
here](https://airtable.com/shrNFgNkPWr3d63Db?prefill_Item=dbpy_as01).


[Next Challenge](03_creating_sequence_diagrams.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F02_test_driving_model_repository_classes.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F02_test_driving_model_repository_classes.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F02_test_driving_model_repository_classes.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F02_test_driving_model_repository_classes.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=challenges%2F02_test_driving_model_repository_classes.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
