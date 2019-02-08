import React, { Component } from 'react';
import './formCheckbox.css';

class FormCheckbox extends Component {
  render() {
    return (
      <form className="formCheckbox">
        <input type="radio" name={this.props.label}/>
        <label htmlFor="">{this.props.label}</label>
      </form>
    );
  }
}

export default FormCheckbox;
