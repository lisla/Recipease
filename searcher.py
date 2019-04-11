recipe_to_ingredients = {}

def get_dictionary():
    with open("recipes_with_ingredients.txt", "r") as myfile:
        args = []
        for line in myfile:
            space_position = line.find(' ')
            args = line.split()
            recipe_link, ingredients_string = line[:space_position], line[space_position:]
            ingredients_list = ingredients_string.split(':')
            recipe_to_ingredients[recipe_link] = ingredients_list

# def execute_query():
#     query = input("What ingredients do you have?\n")
#     ingredients = query.split(", ")
#     print(query)


get_dictionary()
print(recipe_to_ingredients)
# execute_query()
