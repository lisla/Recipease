from flask import Flask, request, render_template
from flask_cors import CORS
import json
import sys

app = Flask(__name__, static_folder="./static", template_folder="./build")
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
    print(i, file=sys.stderr)
    json_data = json.dumps(i)
    return json_data
    
if __name__ == "__main__":
    app.run(debug=True)