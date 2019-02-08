import React, { Component } from 'react';
import './progressBar.css';
import {PageSubSubHeading} from '../page-main-heading/pageMainHeading';



class ProgressBar extends Component {

  render() {
    let percentage = this.props.percent+'%';
   
    return (
        <div className="progressBar">
             <div className="progressBar--indicator">
                <span style={{width: percentage}}></span>
             </div>
             <div className="progressBar--percent">
              <PageSubSubHeading title="Application Status"/>
              <PageSubSubHeading title={this.props.percent+'%'}/>
             </div>
        </div>
    );
  }
}

export default ProgressBar;
