import pytest
from comparison import sort_title, sort_year
from movies import movies

# Expected test output of test #1
expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# Expected test output of test #2
expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"];

def test_sort_year(movies_fixture):
    movies = sort_year(movies_fixture)
    actual = [movie.__str__() for movie in movies]
    expected = expected_year
    assert actual == expected

def test_sort_title(movies_fixture):
    movies = sort_title(movies_fixture)
    actual = [movie.__str__() for movie in movies]
    expected = expected_title
    assert actual == expected

@pytest.fixture
def movies_fixture():
    movie_data = movies
    return movie_data