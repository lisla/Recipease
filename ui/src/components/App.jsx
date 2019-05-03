import React, { Component } from 'react';
import { connect } from 'react-redux';
import './App.css';
import SearchRecipes from './SearchRecipes';

class App extends Component {
    render() {
        return (
            <div className="App">
                <SearchRecipes />
            </div>
        );
    }
}

const ConnectedApp = connect(
    state => state
)(App);

export default ConnectedApp;