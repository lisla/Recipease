from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import os

recipes = set()

# Get list of recipes
def generate_urls():
    for i in range(2):
        r  = requests.get("https://www.allrecipes.com/recipes/?page=" + str(i))

        data = r.text

        soup = BeautifulSoup(data, "html.parser")

        for link in soup.find_all('a'):
            if link.has_attr('href'):
                if '/recipe/' in link['href']:
                    recipes.add(link['href'])

# Get list of ingredients for each of these recipes
def get_ingredients(link):
    r = requests.get(link)

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    item_ingredients = []

    with open("recipes_with_ingredients2.txt", "w") as myfile:
        myfile.write(link.rstrip('\n') + " ")
        for ingredient in soup.find_all("span", {"itemprop": "recipeIngredient"}):
            myfile.write(ingredient.text.rstrip('\n') + ":")
        myfile.write("\n")

generate_urls()

p = Pool(10)
l = list(recipes)
for recipe in l:
    try:
        get_ingredients(recipe)
    except:
        print("There was an error")
p.terminate()
p.join()
