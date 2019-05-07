# # working with dictionary that maps recipe ID --> name, ingredients
# recipe_ids_to_info = {'recipe1': {'ingredients': ['onion', 'garlic', 'potato', 'salt', 'milk', 'cheese'], 'name': 'one'},
#                     'recipe2': {'ingredients': ['garlic', 'onion', 'broth', 'cheese'], 'name':'two'},
#                     'recipe3': {'ingredients': ['milk', 'sugar', 'salt', 'cocoa'], 'name': 'three'},
#                     'recipe4': {'ingredients': ['sweet potato', 'cinnamon', 'salt', 'sugar'], 'name': 'four'},
#                     'recipe5': {'ingredients': ['potato', 'salt', 'cheese', 'sour cream'], 'name': 'five'}}

def get_associated_ingredients_map(recipe_ids_to_info):
    # Idea: build hash map where each entry is [ingredient] --> [hash map of entries related_ingredient --> count]
    related_ingredient_map = {}

    # Gather list of all ingredients across all retrieved recipes
    all_ingredients = []
    for key, value in recipe_ids_to_info.items():
        current_ingredients = value[1]
        all_ingredients = list(set(all_ingredients) | set(value[1]))

        for ingredient in current_ingredients:
            if not(ingredient in related_ingredient_map.keys()):
                related_ingredient_map[ingredient] = {}
                for related_ingredient in current_ingredients:
                    if related_ingredient != ingredient:
                        related_ingredient_map[ingredient][related_ingredient] = 0

            for related_ingredient in current_ingredients:
                if related_ingredient != ingredient:
                    if not(related_ingredient in related_ingredient_map[ingredient].keys()):
                        related_ingredient_map[ingredient][related_ingredient] = 0
                    related_ingredient_map[ingredient][related_ingredient] += 1

    # print("Related ingredients:")
    # print(related_ingredient_map)
    # print('\n')
    #
    # print("Related ingredients, RANKED:")

    # Sort entries inside inner dictionary in descending order of count (most related ingredients come first)
    ranked_related_ingredients_map = {}
    for ingredient, value in related_ingredient_map.items():
        sorted_related_list = sorted(related_ingredient_map[ingredient].keys(), key=lambda x: related_ingredient_map[ingredient][x], reverse=True)
        ranked_related_ingredients_map[ingredient] = sorted_related_list[:3]

    # print(ranked_related_ingredients_map)
    return ranked_related_ingredients_map
