recipe_to_ingredients = {}

def get_dictionary():
    with open("recipes_with_ingredients.txt", "r") as myfile:
        args = []
        for line in myfile:
            line = line.rstrip()
            space_position = line.find(' ')
            args = line.split()
            recipe_link, ingredients_string = line[:space_position], line[space_position:]
            ingredients_list = ingredients_string.split(':')
            recipe_to_ingredients[recipe_link] = ingredients_list[0:len(ingredients_list) - 1]

get_dictionary()
for key in recipe_to_ingredients:
    print (key + ': ' + str(recipe_to_ingredients[key]))
    print('')
    
def execute_query(terms):
    scores = {}
    for key in recipe_to_ingredients:
        ingredients = recipe_to_ingredients[key]
        terms_matched = 0.0
        for t in terms:
            if any(t in i for i in ingredients):
                terms_matched += 1.0
        scores[key] = terms_matched / len(ingredients) 
    sorted_scores = sorted(scores.keys(), key=lambda x: scores[x])
    return sorted_scores            