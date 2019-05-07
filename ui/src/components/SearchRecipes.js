import React from 'react';
import {connect} from 'react-redux';
import { searchRecipes } from '../actions/recipes';
import {Button, Input, List, Card, Container} from 'semantic-ui-react';
import styles from "./Home.module.scss";
import IngredientList from "./IngredientList";

class SearchRecipes extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: false,
            showResults: false,
            value: '',
            recipes: [],
            ingredients: []
        }
        ;

        this.handleSubmit = this.handleSubmit.bind(this);
        this.updateValue = this.updateValue.bind(this);
        this.addItem = this.addItem.bind(this);
    }

    componentDidMount() {
        this.setState({ loading: true });
    }

    componentDidUpdate(prevProps) {
        if(this.props.recipes !== prevProps.recipes) {
            this.setState({recipes: this.props.recipes})
        }
    }

    updateValue(event) {
        this.setState({value: event.target.value});
    }

    addItem() {
        this.setState({ingredients: this.state.ingredients.concat(this.state.value)});
        this.setState({value: ''});
    }

    handleSubmit() {
        const { ingredients } = this.state;
        this.props.searchRecipes({ingredients});
        this.setState({showResults: true});
    }

    populateResults = () => {
        let self = this;
        return(
            <Container className={styles.section}>
              {self.state.recipes.map(function(item, index) {
                    return (
                      <a href = {item.attribution.url} target="_blank" className={styles.link}>
                        <div className={styles.card}>
                          <h2>{item.name}</h2>
                        </div>
                      </a>
                    );
                })}
             </Container>
        );
    };

    render() {
        return(
            <div className="Recipes">
                <div className={styles.body}>
                    <div className={styles.headerBar}>
                        <h1>Recipease</h1>
                    </div>
                    <div className={styles.wrapper}>
                        <div className={styles.input}>
                            <Input onChange={this.updateValue} value={this.state.value} className={styles.tb} placeholder='Enter an ingredient!' />
                            <Button onClick={this.addItem}>Add</Button>
                        </div>
                    </div>
                    <div className={styles.listWrapper}>
                        <IngredientList ingredients={this.state.ingredients} />
                    </div>
                </div>
                <Button onClick={this.handleSubmit}>Submit</Button>
                {this.state.showResults ?
                    this.populateResults()  :
                    null
                }
            </div>
        );
    }
}

export default connect(state => ({
    recipes: state.recipes
}), {
    searchRecipes
})(SearchRecipes);
