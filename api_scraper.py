import requests
import os
import json

recipes = set()

baseURL = "http://api.yummly.com/v1/api/recipes?_app_id=5c90e1d3&_app_key=53cb9fb0d408116e7199f1a38099a0e8&maxResult=100&start="

recipe_ids_to_info = {}

data = []

for i in range(100):
    URL = baseURL + str(100*i + 1)
    # 100 recipes
    r = requests.get(url = URL)
    entry = r.json()
    data.append(entry)

dictionary_file = open("recipe_ids_to_info2.json", "w")

for entry in data:
    # map each recipe to ID to name and ingredients
    matches = entry['matches']

    for recipe in matches:
        recipe_id = recipe['id']
        recipe_name = recipe['recipeName']
        recipe_ingredients = recipe['ingredients']
        recipe_info = (recipe_name, recipe_ingredients)
        recipe_ids_to_info[recipe_id] = recipe_info

    recipe_ids_to_info_json = json.dumps(recipe_ids_to_info)
    json.dump(recipe_ids_to_info_json, dictionary_file)

print(len(recipe_ids_to_info))
