from datetime import datetime
from collections import Counter
from collections import OrderedDict

class Ratings:
    """
    Analyzing data from ratings.csv
    """
    def __init__(self, path_to_the_file):
        self.file = path_to_the_file

    class Movies:    
        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts. 
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            
            years=[]
            for i, line in enumerate(open(self.file)):
                if (i == 0): continue
                
                timestamp = int(line.split(',')[-1])
                dt_object = datetime.fromtimestamp(timestamp)
                years.append(int(dt_object.year))

            cnt = Counter(years)
            ratings_by_year = dict(cnt)
            ratings_by_year = dict(sorted(ratings_by_year.items(), key=lambda item: item[0]))
            return ratings_by_year
        
        def dist_by_rating(self):
            """
            The method returns a dict where the keys are ratings and the values are counts.
         Sort it by ratings ascendingly.
            """
            rating=[]
            for i, line in enumerate(open(self.file)):
                if (i == 0): continue
                
                rating.append(line.split(',')[-2])

            cnt = Counter(rating)
            ratings_distribution = dict(cnt)
            ratings_distribution = dict(sorted(ratings_distribution.items(), key=lambda item: item[0]))

            return ratings_distribution
        
        def top_by_num_of_ratings(self, n):
            """
            The method returns top-n movies by the number of ratings. 
            It is a dict where the keys are movie titles and the values are numbers.
            Sort it by numbers descendingly.
            """

            movieId=[]
            id_title_film = self.create_dict_id_title_film()
            for i, line in enumerate(open(self.file)):
                if (i == 0): continue
                
                film_name = id_title_film[int(line.split(',')[1])]
                movieId.append(film_name)

            cnt = Counter(movieId)
            top_movies = dict(cnt)
            sorted_pairs = sorted(top_movies.items(), key=lambda item: -item[1])
            top_movies = OrderedDict()
            for k, v in sorted_pairs:
                if k not in top_movies:
                    top_movies[k] = v
                    if len(top_movies) == n:
                        break

            return dict(top_movies)
        
        def top_by_ratings(self, n, metric='average'):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            movies={}
            id_title_film = self.create_dict_id_title_film()
            for i, line in enumerate(open(self.file)):
                if (i == 0): continue
                
                film_name = id_title_film[int(line.split(',')[1])]
                if (film_name not in movies.keys()):
                    arr_for_metric = []
                    movies[film_name] = arr_for_metric
                movies[film_name].append(float(line.split(',')[2]))
            if (metric == 'average'):
                for key in movies:
                    movies[key] = round(self.average(movies[key]),2)
            if (metric == 'median'):
                for key in movies:
                    movies[key] = round(self.median(movies[key]),2)

            sorted_pairs = sorted(movies.items(), key=lambda item: -item[1])
            top_movies = OrderedDict()
            for k, v in sorted_pairs:
                if k not in top_movies:
                    top_movies[k] = v
                    if len(top_movies) == n:
                        break

            return dict(top_movies)
        
        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
          Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            movies={}
            id_title_film = self.create_dict_id_title_film()
            for i, line in enumerate(open(self.file)):
                if (i == 0): continue
                
                film_name = id_title_film[int(line.split(',')[1])]
                if (film_name not in movies.keys()):
                    arr_for_metric = []
                    movies[film_name] = arr_for_metric
                movies[film_name].append(float(line.split(',')[2]))

            for key in movies:
                movies[key] = self.variance(movies[key])

            sorted_pairs = sorted(movies.items(), key=lambda item: -item[1])
            top_movies = OrderedDict()
            for k, v in sorted_pairs:
                if k not in top_movies:
                    top_movies[k] = v
                    if len(top_movies) == n:
                        break

            return dict(top_movies)
    
    def create_dict_id_title_film(self):
        dictionary = {}
        file = open('ml-latest-small/movies.csv')
        for i, line in enumerate(file):
            if (i == 0): continue
            id_film = int(line.split(',')[0])
            
            chunks = line.split(',')
            if (len(chunks) > 3):
                for i in range(len(chunks)):
                    if (i > 1 and i < len(chunks) - 1):
                        chunks[1] += (',' + chunks[i])
                del chunks[2:len(chunks) - 1]

            title = chunks[1]
            index_end = int(title.rfind('(')) + 1
            if (index_end != -1):
                title = title[0:index_end-1].strip()

            if (title[0] == '"'):
                title = title[1::]
            dictionary[id_film] = title
        return dictionary
    
    def average(self, list_el):
        return (float(sum(list_el)) / len(list_el))

    def median(self, list_el):
        list_el = sorted(list_el)
        if (len(list_el) % 2 == 1):
            return list_el[len(list_el)//2]
        else:
            return list_el[len(list_el)//2] + list_el[len(list_el)//2 - 1]

    def variance(self, list_el):
        avarage = self.average(list_el)
        return sum([(el - avarage)**2 for el in list_el])/len(list_el)

    class Users(Movies):
        """
        In this class, three methods should work. 
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
     Inherit from the class Movies. Several methods are similar to the methods from it.
        """
        def user_count_ratings(self):
            userId=[]
            for i, line in enumerate(open(self.file)):
                if (i == 0): continue
                
                userId.append(line.split(',')[0])

            cnt = Counter(userId)
            ratings_user = dict(cnt)
            ratings_user = dict(sorted(ratings_user.items(), key=lambda item: -item[1]))

            return ratings_user

        def user_metric_ratings(self, metric='average'):
            users={}
            for i, line in enumerate(open(self.file)):
                if (i == 0): continue
                
                user_id = int(line.split(',')[0])
                if (user_id not in users.keys()):
                    arr_for_metric = []
                    users[user_id] = arr_for_metric
                users[user_id].append(float(line.split(',')[-2]))

            if (metric == 'average'):
                for key in users:
                    users[key] = round(self.average(users[key]),2)
            if (metric == 'median'):
                for key in users:
                    users[key] = round(self.median(users[key]),2)

            users = dict(sorted(users.items(), key=lambda item: -item[1]))

            return dict(users)

        def user_variance_ratings(self, n):
            top_users={}
            for i, line in enumerate(open(self.file)):
                if (i == 0): continue
                
                user_id = int(line.split(',')[0])
                if (user_id not in top_users.keys()):
                    arr_for_metric = []
                    top_users[user_id] = arr_for_metric
                top_users[user_id].append(float(line.split(',')[-2]))

            for key in top_users:
                top_users[key] = round(self.variance(top_users[key]),2)

            sorted_pairs = sorted(top_users.items(), key=lambda item: -item[1])
            top_users = OrderedDict()
            for k, v in sorted_pairs:
                if k not in top_users:
                    top_users[k] = v
                    if len(top_users) == n:
                        break
            return dict(top_users)
