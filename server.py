from flask import Flask, request, render_template
from flask_cors import CORS
import json
import sys
import searcher as s
import associated as a

app = Flask(__name__, static_folder="./ui/static", template_folder="./ui/build")
CORS(app)

recipe_ids_to_info = {}
ranked_related_ingredients_map = {}

recipe_ids_to_info = s.get_dictionary()
ranked_related_ingredients_map = a.get_associated_ingredients_map(recipe_ids_to_info)

def json_output(output):
    return json.dumps(output, default=str, indent=4)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'GET':
        place = request.args.get('place', None)
        if place:
            return place
        return "No place information is given"

@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/recipes", methods = ['GET'])
def recipes():
    ingredients = request.args.get('ingredients')
    i = ingredients.split(',')

    # TODO: Rank all recipes based on their ingredients
    # Get top 5 and fetch links for these recipes using the API
    # Return recipe:link
    result = s.execute_query(i, recipe_ids_to_info)

    # print(i, file=sys.stderr)
    json_data = json.dumps(result)
    return json_data

# Get the associated ingredients for a particular ingredient
@app.route("/associated", methods = ['GET'])
def associated():
    ingredient = request.args.get('ingredient')
    associated_ingredients = ranked_related_ingredients_map[ingredient]
    json_data = json.dumps(associated_ingredients)
    return json_data

if __name__ == "__main__":
    app.run(debug=False)
