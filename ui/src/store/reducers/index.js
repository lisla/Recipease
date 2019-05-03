import { routerReducer } from 'react-router-redux';
import { combineReducers } from 'redux';
import recipesReducer from './recipes';
import appReducer from './app';

const reducer = combineReducers(
    {
        router: routerReducer,
        app: appReducer,
        recipes: recipesReducer
    }
);

export default reducer;