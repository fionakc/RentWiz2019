import React, { Component } from 'react';
import './controlButton.css';

class ControlButton extends Component {
  render() {
    return (
      
     
        <button className="controlButton">
          {this.props.name}
        </button>
     
      
    );
  }
}

export default ControlButton;
