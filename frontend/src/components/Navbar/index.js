import React from "react";
import {Nav, NavLink, Bars, NavMenu} from './NavbarElements';
import Image from "../../assets/logo/smallest_logo.png"; 

// Navigation bar with image and links defined
const Navbar = () => {
    return (
        <>
        <Nav>
          <Bars />
            <NavMenu>
              <NavLink to='/'>
                <img src={Image} alt="logo"></img>
              </NavLink>
              <NavLink to='/' activeStyle={{ color:'black' }}>
                Home
              </NavLink>
              <NavLink to='/about'  activeStyle={{ color:'black' }}>
                About
              </NavLink>
              <NavLink to='/history' activeStyle={{ color:'black' }}>
                History
              </NavLink>
              <NavLink to='/contact' activeStyle={{ color:'black' }}>
                Contact
              </NavLink>
            </NavMenu>
           </Nav> 
        </>
    );
};
export default Navbar;