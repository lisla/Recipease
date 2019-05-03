const initialState = [];

const RecipesReducer = (state = initialState, action) => {
    switch (action.type) {
        case 'RECIPES:LOADED':
            return [
                ...action.recipes
            ];

        default:
            return state;
    }
};

export default RecipesReducer;