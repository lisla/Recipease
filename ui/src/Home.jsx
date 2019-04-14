import React, { Component } from 'react';
import { Input, Button } from 'semantic-ui-react'
import 'semantic-ui-css/semantic.min.css';
import styles from './Home.module.scss';
import IngredientList from './IngredientList';

class Home extends Component {
  constructor(props) {
      super(props);
      this.state = {
        value: '',
        ingredients: []
      };
  }

  updateValue = (event) => {
    this.setState({value: event.target.value});
  }

  addItem = () => {
    this.setState({ingredients: this.state.ingredients.concat(this.state.value)});
  }

  render() {
    return(
      <div className={styles.body}>
        <div className={styles.headerBar}>
          <h1>Recipease</h1>
        </div>
        <div className={styles.wrapper}>
          <div className={styles.input}>
            <Input onChange={this.updateValue} className={styles.tb} placeholder='Enter an ingredient!' />
            <Button onClick={this.addItem}>Add</Button>
          </div>
        </div>
        <div className={styles.listWrapper}>
          <IngredientList ingredients={this.state.ingredients} />
        </div>
      </div>
    );
  }
}

export default Home;
