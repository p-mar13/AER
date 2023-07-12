import React from 'react';
import {Link} from "react-router-dom";
import Background from "../assets/images/bg2.jpg"; 
import Styles from "../styles/HomePage/HomePage.module.css";
import { motion } from "framer-motion";
import Image from "../assets/logo/logo_nobg.png"; 
import MainImage from "../assets/images/home_main.png"; 

// Home page where main page of application is
const Home = () =>{
  return (
    <motion.div
      class="Styles.container"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 1 }}
    >
      <div style={{ backgroundImage:`url(${Background})`,backgroundRepeat:"no-repeat",height:700,width:1535 }}>
        <img class={Styles.homeImage} src={MainImage} alt="logo"/>
        <div class ={Styles.page} >
          <div class ={Styles.title}><img class={Styles.logoHeader} src={Image} alt="logo"/>
      </div>
      <div class={Styles.text}>
        <p>Automated tool for recognizing facial emotions in both image and video file.</p> 
        <p>Application uses innovative DAN model to identify expressions.</p>
      </div>
      <div class={Styles.header}>
        <div class={Styles.round}>
          <Link to="/image_upload" style={{ textDecoration: 'none', color: 'white' }}>Upload image</Link>
        </div>
        <div class={Styles.round}>
          <Link to="/video_upload" style={{ textDecoration: 'none', color: 'white' }}> Upload video </Link>
        </div>
      </div>
    </div>
    </div>
    </motion.div>
     );
}
export default Home;