import requests
import camelot
import pandas as pd


class NutritionFacts:
    """
    Offering nutritional facts on given ingredients.
    """
    def __init__(self, list_of_ingredients):
        """
        Put any fields here that you think you will need.
        """
        self.ingredients = list_of_ingredients
        self.api_key = 'GigHKcaieaN2FBDmrFAwGpLjnjt0a652Si1J1YZh'
        self.facts = self.retrieve()


    def retrieve(self):
        """
This method gets all the nutrient facts about the given ingredients from the file with pre-collected
information. It returns any structure that you find useful.
        """
        facts = dict()
        for element in self.ingredients:
            try:
                response = requests.get(f'https://api.nal.usda.gov/fdc/v1/foods/list?query={element}&pageSize=1&api_key={self.api_key}')
            except Exception as err:
                print(f'Other error occurred: {err}')
            else:
                for index, dict_ in enumerate(response.json()):
                    if 'foodNutrients' in dict_:
                        facts[element] = list(dict_['foodNutrients'])

        return facts

    def get_must_nutrients(self):
        """
This method gets reference values for must nutrients
        """
        data = camelot.read_pdf('./data/Daily-Reference-Values-_DRVs_-under-the-New-NFL.pdf', pages='all')
        data_1 = camelot.read_pdf('./data/Reference-Daily-Intakes-_RDIs_-in-the-New-Nutrition-Facts-Label.pdf', pages='all')

        df = data[0].df.drop(labels=[0,1], axis=0)
        df_1 = data_1[0].df.drop(labels=[0,1], axis=0)
        must_nutrients = pd.concat([df, df_1], ignore_index=True).drop(labels=[1,3,4,5], axis=1)
        must_nutrients = must_nutrients.set_index(must_nutrients[0]).T.to_dict('list')
        return must_nutrients

    def daily_value(self, must_nutrients, ingridient, n):
        facts = self.retrieve()
        nutrients = facts[ingridient]
        daily_val = dict()
        for i in nutrients:
            for index in range(len(i.get('name').split(','))):
                if i.get('name').split(',')[index] in must_nutrients:
                    key = i.get('name').split(',')[index]
                    x = (i.get('amount') * 100) / float(must_nutrients[key][1].replace(',', ''))
                    daily_val[i.get('name')] = round(x)

        return dict(sorted(daily_val.items(), key=lambda x: x[1], reverse=True)[:n])

    def filter(self, must_nutrients, n):
        """
This method selects from the nutrient facts only nutrients from the list
of must_nutrients (for example, from PDF-files below) and the top-n nutrients with the highest
values of daily value norms for the given ingredient. It returns a text formatted as in the example above.
        """
        text_with_facts = 'II. NUTRITION FACTS\n'

        for i in range(len(self.ingredients)):
            text_with_facts += self.ingredients[i] + '\n'
            daily_value = self.daily_value(must_nutrients, self.ingredients[i], n)
            for k, v in daily_value.items():
                text_with_facts += f'{k} - {v}% of Daily Value\n'

        return text_with_facts



