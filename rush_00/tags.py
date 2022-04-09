from collections import Counter
from collections import OrderedDict

class Tags:
    """
    Analyzing data from tags.csv
    """
    def __init__(self, path_to_the_file):
        self.file = path_to_the_file

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict 
 where the keys are tags and the values are the number of words inside the tag.
 Drop the duplicates. Sort it by numbers descendingly.
        """
        tags = {}
        for i, line in enumerate(open(self.file)):
            if (i == 0): continue
            tag = line.split(',')[2]
            tags[tag] = len(tag.split(' '))

        tags = dict(sorted(tags.items(), key=lambda item: -item[1]))
        sorted_pairs = sorted(tags.items(), key=lambda item: -item[1])
        big_tags = OrderedDict()
        for k, v in sorted_pairs:
            if k not in big_tags:
                big_tags[k] = v
                if len(big_tags) == n:
                    break

        return dict(big_tags)

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        tags = {}
        for i, line in enumerate(open(self.file)):
            if (i == 0): continue
            tag = line.split(',')[2]
            tags[tag] = len(tag)

        tags = dict(sorted(tags.items(), key=lambda item: -item[1]))
        sorted_pairs = sorted(tags.items(), key=lambda item: -item[1])
        big_tags = OrderedDict()
        for k, v in sorted_pairs:
            if k not in big_tags:
                big_tags[k] = v
                if len(big_tags) == n:
                    break
                
        return list(big_tags.keys())

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and 
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        a = self.longest(n)
        b = self.most_words(n).keys()
        big_tags = list(set(a) & set(b))
        return big_tags
        
    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        tags = {}
        for i, line in enumerate(open(self.file)):
            if (i == 0): continue
            tag = line.split(',')[2]
            if (tag not in tags.keys()):
                tags[tag] = 0
            tags[tag] += 1

        sorted_pairs = sorted(tags.items(), key=lambda item: -item[1])
        popular_tags = OrderedDict()
        for k, v in sorted_pairs:
            if k not in popular_tags:
                popular_tags[k] = v
                if len(popular_tags) == n:
                    break

        return popular_tags
        
    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        tags = {}
        for i, line in enumerate(open(self.file)):
            if (i == 0): continue
            tag = line.split(',')[2]
            if (tag not in tags.keys()):
                tags[tag] = 0
            tags[tag] += 1

        tags_with_word = sorted([k for k,v in tags.items() if (k.find(word) != -1 and v==1)])
        return tags_with_word
