from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import os

recipes = set()

if os.path.exists("recipes_with_ingredients.txt"):
  os.remove("recipes_with_ingredients.txt")

# Get list of recipes on the first 100 pages of AllRecipes.com
def generate_urls():
    for i in range(1):
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

    with open("recipes_with_ingredients.txt", "a") as myfile:
        myfile.write(link.rstrip('\n') + " ")
        for ingredient in soup.find_all("span", {"itemprop": "recipeIngredient"}):
            myfile.write(ingredient.text.rstrip('\n') + "@")
        myfile.write("\n")

generate_urls()

p = Pool(10)
p.map(get_ingredients, list(recipes))
p.terminate()
p.join()
