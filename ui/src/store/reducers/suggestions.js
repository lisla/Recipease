const initialState = [];

const SuggestionsReducer = (state = initialState, action) => {
    switch (action.type) {
        case 'Suggestions:LOADED':
            return [
                ...action.suggestions
            ];

        default:
            return state;
    }
};

export default SuggestionsReducer;
