import React, { Component } from 'react';
import {PageMainHeading, PageSubHeading, PageSubSubHeading, PagePara} from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/page-main-heading/pageMainHeading';
import ControlButton from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/control-button/controlButton';
import './confirmation.css';
import propertyImg from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/rental_block/sampleImg.png';
import ProgressBar from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/progressBar/progressBar';
import {Link } from 'react-router-dom'; 

class Confirmation extends Component {
  render() {
    return (
      <div className="confirmationBlock">
        <ProgressBar percent="80"/>
        <PageMainHeading title="You're nearly there John!"/>
        <div className="confirmationBlock--propertyDetails">
          <div className="confirmationBlock--propertyDetails__detail">
            <PageSubHeading title="You are applying to be considered for this property"/>
            <PageSubSubHeading title="13 Tawa Street, Tawa"/>
            <div className="confirmationBlock--propertyDetails__detail___img">
              <img src={propertyImg} alt=""/>
            </div>
          </div>
          <div className="confirmationBlock--propertyDetails__adultsInvited">
            <PageSubHeading title="Other adults you have invited"/>
          </div>
        </div>
        <div className="confirmationBlock--controlButtons">
          <div className="left">
            <Link to="/adultprofile">
              <ControlButton name="Edit"/>
            </Link>
          </div>
          <div className="right">
            <Link to="/applicationsuccess">
             <ControlButton name="Confirm"/>
            </Link>
          
          </div>
        </div>
      </div>
    );
  }
}

export default Confirmation;
