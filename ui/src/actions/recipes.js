const recipesLoaded = recipes => ({
    type: 'RECIPES:LOADED',
    recipes: recipes
});

const searchRecipes = (query) => (dispatch, getState) => {
    let url = new URL('http://127.0.0.1:5000/recipes');
    JSON.stringify(query);
    Object.keys(query).forEach(key => url.searchParams.append(key, query[key]));
    console.log(url);
    fetch(url.href, {
        method: 'GET'
    })
        .then(response => response.json())
        .then((recipes) => dispatch(recipesLoaded(recipes)))
        .catch(err => {
            console.error(err);
        });
};

export {
    searchRecipes
}