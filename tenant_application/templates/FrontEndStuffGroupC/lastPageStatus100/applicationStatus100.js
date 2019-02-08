import React, { Component } from 'react';
import {PageMainHeading, PageSubHeading, PageSubSubHeading, PagePara} from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/page-main-heading/pageMainHeading';
import ControlButton from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/control-button/controlButton';
import ProgressBar from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/progressBar/progressBar';
import './applicationStatus100.css';
import {Link } from 'react-router-dom'; 

class ApplicationStatus100 extends Component {
  render() {
    return (
      <div className="applicationStatus100Block">
        <ProgressBar percent="100"/>
        <PageMainHeading title="Your're all done!"/>
       
        <div className="applicationStatus100Block--controlButtons">
          <div className="left">
            <Link to="/">
              <ControlButton name="New Application"/>
            </Link>
           
          </div>
          <div className="right">
            <Link to="/">
              <ControlButton name="My Dashboard"/>
            </Link>
            
          </div>
        </div>
      </div>
    );
  }
}

export default ApplicationStatus100;
