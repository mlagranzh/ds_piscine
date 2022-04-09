from movies import Movies
from ratings import Ratings
from tags import Tags
from links import Links
from collections import Counter

class Tests:
    def setup_class(self):
        self.movies = Movies('ml-latest-small/movies.csv')
        self.rating = Ratings('ml-latest-small/ratings.csv')
        self.tags = Tags('ml-latest-small/tags.csv')
        self.links = Links('ml-latest-small/links.csv')

    def test_movies_dist_by_release(self):
        result = self.movies.dist_by_release()
        assert (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result.values(), reverse=True) == list(result.values()))

    def test_movies_dist_by_genres(self):
        result = self.movies.dist_by_genres()
        assert (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result.values(), reverse=True) == list(result.values()))

    def test_movies_most_genres(self):
        result = self.movies.most_genres(10)
        assert (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result.values(), reverse=True) == list(result.values()))

    def test_rating_dist_by_year(self):
        result = self.rating.Movies.dist_by_year(self.rating)
        assert (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {int}) and
                sorted(list(result.keys()), reverse=False) == list(result.keys()))

    def test_rating_dist_by_rating(self):
        result = self.rating.Movies.dist_by_rating(self.rating)
        assert (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(list(result.keys()), reverse=False) == list(result.keys()))

    def test_rating_top_by_num_of_ratings(self):
        result = self.rating.Movies.top_by_num_of_ratings(self.rating, 5)
        assert (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result.values(), reverse=True) == list(result.values()))

    def test_rating_top_by_ratings(self):
        for metric in ['average', 'median']:
            result = self.rating.Movies.top_by_ratings(self.rating, 100, metric)
            assert (isinstance(result, dict) and
                    (set(map(type, result.values())) == {float} and
                     set(map(type, result.keys())) == {str}) and
                    sorted(result.values(), reverse=True) == list(result.values()))

    def test_rating_top_controversial(self):
        result = self.rating.Movies.top_controversial(self.rating, 5)
        assert (isinstance(result, dict) and
                (set(map(type, result.values())) == {float} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result.values(), reverse=True) == list(result.values()))

    def test_tags_most_words(self):
        result = self.tags.most_words(10)
        assert (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result.values(), reverse=True) == list(result.values()))

    def test_tags_longest(self):
        result = self.tags.longest(10)
        assert (isinstance(result, list) and
                (set(map(type, result)) == {str}))

    def test_tags_most_words_and_longest(self):
        result = self.tags.most_words_and_longest(232)
        assert (isinstance(result, list) and
                set(map(type, result)) == {str})

    def test_tags_most_popular(self):
        result = self.tags.most_popular(10)
        assert (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result.values(), reverse=True) == list(result.values()))

    def test_tags_with(self):
        result = self.tags.tags_with('Netflix')
        assert (isinstance(result, list) and
                set(map(type, result)) == {str} and
                sorted(result, reverse=False) == list(result))

    def test_get_imdb(self):
        result = self.links.get_imdb(['1', '2', '3', '4', '5'], ['director', 'name', 'genre', 'actor'])
        assert (isinstance(result, list) and
                set(map(type, result)) == {list} and
                sorted(result, reverse=True, key=lambda x: x[0]) == list(result))

    def test_top_directors(self):
        self.links.get_imdb(['1', '2', '3', '4', '5'], ['director', 'name', 'genre', 'actor'])
        result = self.links.top_directors(3)
        assert (isinstance(result, dict) and
                (set(map(type, result.values())) == {int} and
                 set(map(type, result.keys())) == {str}) and
                sorted(result, reverse=True, key=lambda x: x[1]) == list(result))