import pandas as pd
import numpy as np
import pickle


class Forecast:
    """
    Predicting the rating or the class
    """
    def __init__(self, list_of_ingredients):
        self.ingredients = list_of_ingredients
        self.matrix_ingredients = pd.read_csv("epi_r.csv", ',').drop(['title', 'sodium','fat','protein','calories', 'rating','#cakeweek','#wasteless',\
                        '22-minute meals','3-ingredient recipes','30 days of groceries','advance prep required'], axis=1)
        self.matrix_ingredients = pd.DataFrame(0, index = range(0, 1), columns=self.matrix_ingredients.keys())

    def preprocess(self):
        """
This method transforms the list of ingredients to the data structure that is used in machine learning algorithms for predictions.
        """
        for ingredient in self.ingredients:
            self.matrix_ingredients.loc[0, ingredient] = 1
                
    def predict_rating(self):
        """
This method returns the rating for the list of ingredients using the regression model that you trained upfront. Besides the rating itself, the method returns a text that interprets the rating and gives a recommendation as in the example above.
        """
        self.preprocess()
        loaded_model = pickle.load(open("finalized_model_regressor.sav", 'rb'))
        rating = loaded_model.predict(self.matrix_ingredients)[0]
        if (rating < 2):
            text = """You might find it tasty, but in our opinion, it is a bad idea to have a dish with that list of ingredients"""
        if (rating in (2,3)):
            text = """SO-SO"""
        if (rating > 3):
            text = """GREEEAT!"""
        return rating, text
        
    def predict_rating_category(self):
        """
This method returns the rating category for the list of ingredients using the classification model that you trained upfront. Besides the rating itself, the method returns a text that interprets the rating category and gives a recommendation as in the example above.
        """
        self.preprocess()
        loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
        rating_cat = loaded_model.predict(self.matrix_ingredients)
        if (rating_cat < 2):
            text = """You might find it tasty, but in our opinion, it is a bad idea to have a dish with that list of ingredients"""
        if (rating_cat in (2,3)):
            text = """SO-SO"""
        if (rating_cat > 3):
            text = """GREEEAT!"""
        return rating_cat, text