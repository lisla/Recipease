const initialState = {
    api: {
        url: 'localhost:5000'
    }
};

const AppReducer = (state = initialState, action) => {
    switch (action.type) {
        default:
            return state;
    }
};

export default AppReducer;
