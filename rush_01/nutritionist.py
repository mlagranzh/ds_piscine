from NutritionFacts import NutritionFacts
from SimilarRecipes import SimilarRecipes
from forecast import Forecast
import sys

if __name__ == '__main__':
    ingrid = []
    for i in range(1, len(sys.argv)):
        ingrid.append(sys.argv[i])
    # forecast = Forecast(ingrid)
    # print(forecast.predict_rating_category())
    nutrition = NutritionFacts(ingrid)
    print(nutrition.filter(nutrition.get_must_nutrients(), 5))
    recipes = SimilarRecipes(ingrid)
    print(recipes.top_similar(5))
