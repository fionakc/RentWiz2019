import React, { Component } from 'react';
import './header.css';
import logo from './logo.png'
import userPic from './userPic.png';
import {BrowserRouter as Router, Route, Link } from 'react-router-dom'; 


class Header extends Component {
  render() {
    return (
      <header>
           <div className = "logo">
                <img src={logo} alt="" className="logo--img"/>
                <p className="logo--p">RentWiz</p>
           </div>
           <div class="menu">
               <ul class="menu--list">
                   <li><Link to="/">Home</Link></li>
                   <li><Link to="/rentals">Browse Rentals</Link></li>
                   <li><Link to="/advancesearch">Advanced Search</Link></li>
                   <li><Link to="/help">Help</Link></li>
               </ul>
           </div>
           <div className="user">
                <div className="user--status">
                        <p>Logged in as</p>
                        <p>John</p>
                </div>
                <div className="user--pic">
                    <img src={userPic} alt="" className="user--pic__img"/>
                </div>
           </div>
      </header>
    );
  }
}

export default Header;
