import json
import requests
import os
# def get_dictionary():
#     recipe_to_ingredients = {}
#     with open("recipes_with_ingredients.txt", "r") as myfile:
#         args = []
#         for line in myfile:
#             line = line.rstrip()
#             space_position = line.find(' ')
#             args = line.split()
#             recipe_link, ingredients_string = line[:space_position], line[space_position:]
#             ingredients_list = ingredients_string.split(':')
#             recipe_to_ingredients[recipe_link] = ingredients_list[0:len(ingredients_list) - 1]
#     return recipe_to_ingredients

# gets dictionary using data from API
def get_dictionary():
    with open("recipe_ids_to_info.json", "r") as myfile:
        recipe_ids_to_info_string = json.load(myfile)
        recipe_ids_to_info = json.loads(recipe_ids_to_info_string)
    # print(recipe_ids_to_info)
    return recipe_ids_to_info

def get_info(recipe_id):
    URL = 'http://api.yummly.com/v1/api/recipe/'+recipe_id+'?_app_id=5c90e1d3&_app_key=53cb9fb0d408116e7199f1a38099a0e8'
    r = requests.get(url = URL)
    return r.json()

def execute_query(terms, recipe_ids_to_info):
    scores = {}
    for key in recipe_ids_to_info:
        ingredients = recipe_ids_to_info[key][1]
        terms_matched = 0.0
        for t in terms:
            if any(t in i for i in ingredients):
                terms_matched += 1.0
        scores[key] = terms_matched / len(ingredients)
    sorted_scores = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)[:5]
    output = []
    for recipe in sorted_scores:
        output.append(get_info(recipe))
    return output
