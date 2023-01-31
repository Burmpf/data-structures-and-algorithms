from movies import movies
from operator import attrgetter

# Create a Movie class for use in sorting
class Movie:
    def __init__(self, movie_obj):
        self.title = movie_obj['title']
        self.year = movie_obj['year']
        self.genres = movie_obj['genres']

    def __str__(self):
        return self.title

# Convert Movies list to objects
def create_movies(movie_data):
    movie_list = []

    for movie in movie_data:
        movie_list.append(Movie(movie))

    return movie_list

# Sort Title
def sort_title(movies):
    ignore = ['The', 'A', 'An']

    movie_class_list = create_movies(movies)

    sorted_obj = sorted(movie_class_list, key=lambda x: ' '.join([word for word in x.title.split() if word not in ignore]))

    return sorted_obj



# Sort Year
def sort_year(movies):
    movie_class_list = create_movies(movies)

    sorted_obj = sorted(movie_class_list, key=attrgetter('year', 'title'), reverse=True)

    return sorted_obj


if __name__ == '__main__':
    movies_data = movies

    sorted_title = sort_title(movies_data)
    sorted_year = sort_year(movies_data)

    print(sorted_title)
    print(sorted_year)