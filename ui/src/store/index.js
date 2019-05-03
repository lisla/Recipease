import {
    applyMiddleware,
    createStore,
    compose
} from 'redux';

import createHistory from 'history/createBrowserHistory';
import { routerMiddleware } from 'react-router-redux';
import thunk from 'redux-thunk';
import reducer from './reducers';

const loggerMiddleware = store => next => action => {
    console.info("Action type:", action.type);
    console.info("Action payload:", action.payload);
    console.info("State before:", store.getState());
    next(action);
    console.info("State after:", store.getState());
};

let initialState = {};
const history = createHistory();

const createStoreWithMiddleware = compose(
    applyMiddleware(
        thunk,
        loggerMiddleware,
        routerMiddleware(history),
    )
)(createStore);

const store = createStoreWithMiddleware(reducer, initialState);

export default store;
export { history, store };