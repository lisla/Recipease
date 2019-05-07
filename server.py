from flask import Flask, request, render_template
from flask_cors import CORS
import json
import sys
import searcher as s
import associated as a

app = Flask(__name__, static_folder="./ui/static", template_folder="./ui/build")
CORS(app)

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
    recipe_ids_to_info = s.get_dictionary()
    sorted_scores = s.execute_query(i, recipe_ids_to_info)

    # print(i, file=sys.stderr)
    print(sorted_scores[:5])
    json_data = json.dumps(sorted_scores[:5])
    return json_data

if __name__ == "__main__":
    app.run(debug=False)
