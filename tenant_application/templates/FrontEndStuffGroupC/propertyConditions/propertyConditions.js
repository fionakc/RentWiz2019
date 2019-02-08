import React, { Component } from 'react';
import './propertyConditions.css';
import FormCheckbox from '../formCheckbox/formCheckbox';
import ControlButton from '../control-button/controlButton';
import ProgressBar from '../progressBar/progressBar';
import {Link } from 'react-router-dom'; 

class PropertyConditions extends Component {
  render() {
    return (
      <div class="propertyConditions">
          <ProgressBar percent="60"/>
          <h1>
            Are you aware of the below Duties & Conditions of this property?
          </h1>
          <h3>
           Please confirm below that you are happy to accept <br></br>the Conditions and Duties set out by the lanlord <br></br> of this property.
          </h3>
          <div className="propertyConditions--block">
              <div className="propertryCondition--block_list">       
                <div className="propertyCondition--block_list__item">
                    <h2>
                      Conditions: 
                    </h2>
                    <ol>
                        <li>No Pets</li>
                        <li>No motorbikes</li>
                        <li>No smoking</li>
                        <li>Max 3 tenents</li>
                        <li>This is a list item</li>
                        <li>Yup, another list item</li>
                        <li>Yup, another list item</li>
                    </ol>
                    <FormCheckbox label="I accept"/>
                </div>
                </div>
                <div className="propertyCondition--block_list__item">
                    <h2>
                      Duties of tenant: 
                    </h2>
                    <ol>
                      <li>Tenant must clean roof  annually</li>
                      <li>Lawns mowed fortnightly</li>
                      <li>Must sweep chimney weekly</li>
                      <li>Must keep garden tidy</li>
                      <li>This is a list item</li>
                      <li>Yup, another list item</li>
                      <li>This is a list item</li>
                    </ol>
                    <div>
                    <FormCheckbox label="I accept"/>
                    </div>
                </div>    
          </div>
          <div className="propertyCondition--controlButtons">
            <Link to="/adultprofile">
              <ControlButton name="Back"/>
            </Link>

            <Link to="/propertyconfirmation">
              <ControlButton name="Agree & Next"/>
            </Link>
            
          </div>
          
     </div>
    );
  }
}

export default PropertyConditions;
