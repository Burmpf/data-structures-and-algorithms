# Sorting: Comparison

## Context:
In the first half of this code challenge, you will write functions which sort domain objects. Your functions will receive an array of Movie objects. Each Movie object has a title (string), a year (number), and a list of genres (array of strings). One function will sort the movies by most recent year first. One function will sort the movies, alphabetical by title, but will ignore any leading “A”s, “An”s, or “The”s. Test outputs for these functions, and an array of sample data, have been provided in test and movies.

In the second half of the code challenge, you will write tests for your comparator functions. This may necessitate refactoring the code you wrote in part one. Your tests will need to call the comparator functions directly, and make assertions about the response values given test inputs.

## Functions:
###### functions can be found in comparison.py file

- create_movies()- takes in a list of movies and sends them out into the Movie class.
- Movie class- creates a movie object with a title, year, and genre.
- sort_year()- takes in a list of movies and sorts them by year.
- sort_title()- takes in a list of movies and sorts them by title.

## Tests:
- use pytest to run the tests in the tests.py file.
- use a pytest fixture to create a list of movies to test with.
- tests are `test_sort_year()` and `test_sort_title()`

## Whiteboard:

