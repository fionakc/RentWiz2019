import React, { Component } from 'react';
import './rentalBlock.css';
import blockImg from './sampleImg.png';
import { Link } from 'react-router-dom'; 

class rentalBlock extends Component {
  render() {
    return (
      <div className="rentalBlock">
        <h1>Good Choice!</h1>
        <h4>You are applying to be considered for the following property:</h4>
        <div className="rentalBlock--img">
            <img src={blockImg} alt=""/>
        </div>
        <div className="rentalBlock--description">
            <ul className="rentalBlock--description__list">
                <li><span>Location:</span>13 Tawa Street</li>
                <li><span>Available:</span>Tue 5 Feb</li>
                <li><span>Property ID#:</span>GCG892</li>
                <li><span>Furnishings:</span></li>
                <li><span>In the area:</span></li>
                <li><span>Parking</span></li>
                <li><span>Idea Tenants</span></li>
                <li><span>Smoke Alarm:</span></li>

            </ul>
            <div className="rentalBlock--nextBtn">
              <Link to="/adultprofile">
                <button className="nextButton">Next</button>
              </Link>
            </div> 
            
        </div>
      </div>
    );
  }
}

export default rentalBlock;
