import React from 'react';
import {connect} from 'react-redux';
import { searchRecipes } from '../actions/recipes';
import { getSuggestions } from '../actions/suggestions';
import {Button, Input, Container, Checkbox} from 'semantic-ui-react';
import styles from "./Home.module.scss";
import IngredientList from "./IngredientList";

class SearchRecipes extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loading: false,
            showResults: false,
            showSuggestions: false,
            value: '',
            recipes: [],
            ingredients: [],
            suggestions: [],
            suggestionsToAdd: []
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

        if(this.props.suggestions !== prevProps.suggestions) {
            this.setState({suggestions: this.props.suggestions})
        }

    }

    updateValue(event) {
        this.setState({value: event.target.value});
    }

    addItem() {
        this.setState({ingredients: this.state.ingredients.concat(this.state.value)});
        this.setState({value: ''});
    }

    onChange = async (e) => {
      let value = String(e.target.innerHTML);
      const {suggestionsToAdd} = this.state;
      if (suggestionsToAdd.includes(value)) {
        await this.setState({suggestionsToAdd: suggestionsToAdd.filter(word => word === value)});
      }
      else {
        await this.setState({suggestionsToAdd: suggestionsToAdd.concat(value)});
      }
    }

    handleSubmit = async () => {
      const { ingredients } = this.state;
      this.props.getSuggestions({ingredients});
      this.setState({showSuggestions: true});
      console.log(this.state);
    }

    getResults = async () => {
      console.log(this.state);
      await this.setState({ingredients: this.state.ingredients.concat(this.state.suggestionsToAdd), suggestionsToAdd: [], suggestions: []});
      const { ingredients } = this.state;
      console.log(ingredients);
      this.props.searchRecipes({ingredients});
      this.setState({showResults: true, showSuggestions: false});
    }

    displaySuggestions = () => {
      let self = this;
      return (
        <div>
          <Container>
            <h2>We have some suggested ingredients for you!</h2>
            <p>Based on your current list of ingredients, we have some other ingredients that are commonly found with the ones you already listed.
            Check off those that you have and click <strong>Continue</strong></p>
            {self.state.suggestions.map(function(item, index){
              return (
                <Checkbox className={styles.suggestion} label={item} onChange={self.onChange}/>
              );
            })}
          </Container>
          <Button onClick={this.getResults}>Continue</Button>
        </div>
      );
    };

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
                {this.state.showSuggestions ?
                  this.displaySuggestions() :
                  <Button onClick={this.handleSubmit}>Submit</Button>
                }
                {this.state.showResults ?
                    this.populateResults()  :
                    null
                }
            </div>
        );
    }
}

export default connect(state => ({
    recipes: state.recipes,
    suggestions: state.suggestions
}), {
    searchRecipes,
    getSuggestions
})(SearchRecipes);
