from collections import Counter
from collections import OrderedDict

class Movies:
    """
    Analyzing data from movies.csv
    """
    def __init__(self, path_to_the_file):
        self.file = path_to_the_file
    
    def get_film_by_idx(self, idx):
        for i, line in enumerate(open(self.file)):
            if (i == 0): continue
            if (int(line.split[','][0] == idx)):
                return line

    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts. 
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        years = []
        #preprocessing
        for i, line in enumerate(open(self.file)):
            if (i == 0): continue
            chunks = line.split(',')
            if (len(chunks) > 3):
                for i in range(len(chunks)):
                    if (i > 1 and i < len(chunks) - 1):
                        chunks[1] += (',' + chunks[i])
                del chunks[2:len(chunks) - 1]

            title = chunks[1]
            index_begin = int(title.rfind('(')) + 1
            index_end = int(title.rfind(')'))
            if (index_begin != -1 and index_end != -1):
                years.append(title[index_begin:index_end])
        cnt = Counter(years)
        release_years = dict(cnt)
        release_years = dict(sorted(release_years.items(), key=lambda item: -item[1]))
        return release_years
    
    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
     Sort it by counts descendingly.
        """
        genres = []
        for i, line in enumerate(open(self.file)):
            if (i == 0): continue
            for g in line.split(',')[-1].split('|'):
                genres.append(g.strip())
        cnt = Counter(genres)
        genres = dict(cnt)
        genres = dict(sorted(genres.items(), key=lambda item: -item[1]))
        return genres
        
    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and 
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        movies = {}
        for i, line in enumerate(open(self.file)):
            if (i == 0): continue
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

            count = 0
            if (chunks[-1] != '(no genres listed)'):
                count = len(chunks[-1].split('|'))
            if (title[0] == '"'):
                title = title[1::]
            movies[title] = count

        sorted_pairs = sorted(movies.items(), key=lambda item: -item[1])
        movies = OrderedDict()
        for k, v in sorted_pairs:
            if k not in movies:
                movies[k] = v
                if len(movies) == n:
                    break
        return movies            