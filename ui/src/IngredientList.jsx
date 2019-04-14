import React, { Component } from 'react';
import { List } from 'semantic-ui-react'
import 'semantic-ui-css/semantic.min.css';
import styles from './Home.module.scss';

class IngredientList extends Component {
  constructor(props) {
      super(props);
  }

  render() {
    return(
       <List className={styles.list} bulleted>
        {this.props.ingredients.map((ingredient, index) => {
           return (
             <List.Item key={index}>{ingredient}</List.Item>
            );
           }
        )}
       </List>
    );
  }
}

export default IngredientList;
