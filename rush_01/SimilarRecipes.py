import requests
from bs4 import BeautifulSoup
import pandas as pd


class SimilarRecipes:
    """
    Recommending similar recipes with additional information
    """
    url = 'https://www.epicurious.com'

    

    def __init__(self, list_of_ingredients):
        """
        Put any here fields that you think you will need.
        """    
        self.ingridients = list_of_ingredients

    def find_all(self):
        """
This method returns a list of indexes of the recipes that contain the given list of ingredients.
If there is no recipe that contains all the ingredients, handle it.
        """
        search_ingid = ''
        for i in range(len(self.ingridients)):
            search_ingid += self.ingridients[i].lower() + '%20'
        try:
            page = requests.get(self.url + '/search/' + search_ingid + '?content=recipe')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            soup = BeautifulSoup(page.text, 'lxml')
            rating = soup.find_all('dl', class_="recipes-ratings-summary")
            recipe_title = soup.find_all('h4', class_="hed")
        row = dict()
        for line in recipe_title:
            row[line.text] = self.url + line.find('a').get('href')
        ratings = []
        for i in rating:
            ratings.append(i.get('data-reviews-rating'))

        df = pd.DataFrame(list(row.items()), columns=['title', 'links'])
        df['ratings'] = ratings
        df.to_csv('./data/similar_recipes.csv')

        indexes = df
        return indexes

    def top_similar(self, n):
        """
This method returns a text formatted as in the example above with title, rating, and URL. Before that,
it finds top-n most similar recipes by the number of additional ingredients that are required in the recipes
using indexes from the find_all method. The most similar is the one that does not require any other ingredients.
Next is the one that requires only one, etc. If it requires 5 more ingredients, do not return those recipes.
        """
        text_with_recipes = f'III.TOP - {n} SIMILAR RECIPES:\n'
        recipes = self.find_all().sort_values(by='ratings', ascending=False).reset_index(drop=True)

        for i in range(n):
            text_with_recipes += f'- {recipes["title"][i]}, rating: {recipes["ratings"][i]}, URL: {recipes["links"][i]}\n'

        return text_with_recipes

