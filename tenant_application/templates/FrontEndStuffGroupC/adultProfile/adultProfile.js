// import React, { Component } from 'react';
// import {Link } from 'react-router-dom';
// import './adultProfile.css';
// import profilePic from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/header/userPic.png';
// import tenantWho from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/header/tenantWho.png';
// import checkMark from './check-mark.png';
// import ControlButton from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/control-button/controlButton';
// import ProgressBar from '../../../../../../Documents/SWEN503/RENTWIZ/RentWiz3UI/src/components/progressBar/progressBar';
//
// class AdultProfile extends Component {
//   render() {
//     return (
//       <div className="adultProfile">
//
//       <ProgressBar percent="40"/>
//         <h1>What other adults* will live with you?</h1>
//
//          <div className="adultProfile--block">
//             <div className="adultProfile--details">
//                 <img src={profilePic} alt="" className="adultProfile--details__pic"/>
//                 <div className="adultProfile--details__nameBlock">
//                     <h3 className="adultProfile--details__nameBlock_name">JAck Smith</h3>
//                     <div className="adultProfile--details__nameBlock_verifiedStatus">
//                         <img src={checkMark} alt=""/>
//                         <p>Verified</p>
//                     </div>
//
//                 </div>
//                 <div className="adultProfile--details_info">
//                     <ul>
//                         <li>Email: JAck@gmail.com</li>
//                         <li>DOB: 12 Dec 92</li>
//                         <li>Pets: No</li>
//                         <li>Smoker: No</li>
//                         <li>Mobile: 021322323</li>
//                     </ul>
//                 </div>
//             </div>
//
//
//             <div className="adultProfile--details">
//                 <img src={tenantWho} alt="" className="adultProfile--details__pic"/>
//                 <div className="adultProfile--details__add">
//                     <input type="email" placeholder="someone@example.com"/>
//                     <button>Invite</button>
//                 </div>
//                 <div className="adultProfile--details_info">
//                     <p>
//                     Enter your potential flatmate's email address above to send them an invitation.
//                     </p>
//                 </div>
//             </div>
//
//
//             <div className="adultProfile--details">
//                 <img src={tenantWho} alt="" className="adultProfile--details__pic"/>
//                 <div className="adultProfile--details__add">
//                     <input type="email" placeholder="someone@example.com"/>
//                     <button>Invite</button>
//                 </div>
//                 <div className="adultProfile--details_info">
//                     <p>
//                     Enter your potential flatmate's email address above to send them an invitation.
//
//                     </p>
//                 </div>
//             </div>
//          </div>
//
//         <div className="controlButtons">
//             <Link to='/'>
//                 <div className="controlButtons--leftButton">
//                     <ControlButton name="Back"/>
//                 </div>
//             </Link>
//
//             <div className="controlButtons--centerButton">
//                 <ControlButton name="Add More People"/>
//             </div>
//             <Link to="/propertyconditions">
//                 <div className="controlButtons--rightButton">
//                     <ControlButton name="Next"/>
//                 </div>
//             </Link>
//
//
//         </div>
//
//       </div>
//
//
//
//     );
//   }
// }
//
// export default AdultProfile;
