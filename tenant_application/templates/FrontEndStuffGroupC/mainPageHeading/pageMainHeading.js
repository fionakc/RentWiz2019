import React, { Component } from 'react';
import './pageMainHeading.css';

class PageMainHeading extends Component {
  render() {
    return (
      <h1 className="pageMainHeading">
        {this.props.title}
      </h1>
    );
  }
}

class PageSubHeading extends Component {
  render() {
    return (
      <h3 class="pageSubHeading">
        {this.props.title}
      </h3>
    );
  }
}
class PageSubSubHeading extends Component {
  render() {
    return (
      <h4 className="pageSubSubHeading">
        {this.props.title}
      </h4>
    )
  }
}

class PagePara extends Component {
  render() {
    return (
      <p class="pagePara">
        {this.props.title}
      </p>
    )
  }
}
export {PageMainHeading, PageSubHeading, PageSubSubHeading, PagePara};
