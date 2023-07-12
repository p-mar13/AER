import React from 'react';
import { motion } from "framer-motion";
import Styles from "../styles/AboutPage/AboutPage.module.css";
import Background from "../assets/images/about_bg.jpg"; 
import Image from "../assets/images/FAQ_header.png"; 
import Tutorial from "../components/Tutorial";

// Page where info about application and tutorial are displayed
const About = () =>{
  return (
    <div class="page">
      <motion.div
        className="container text-center"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        transition={{ duration: 1 }}
      >
      <div class={Styles.bg} style={{ backgroundImage:`url(${Background})`,backgroundRepeat:"repeat",width:1535 }}>
        <div class={Styles.border}>
        <div><br/><br/><br/><br/>
          <div><img class={Styles.faqHeader} src={Image} alt="logo"/></div>
          <hr class={Styles.hl} style={{background: "#9b9ca1", height: "5px", border: "none",}}/>
          <table class={Styles.table}>    
            <tr>
              <td class="question">What is AER app?</td>
            </tr>
            <tr>
              <td >AER is an Automated Facial Recognizer application. It allows to analyze uploaded media - either image or video - and classify emotions of all detected faces.</td>
            </tr>
            <tr>
              <td class="question">What model is used for FER*?</td>
            </tr>
            <tr>
              <td >Implemented model is called DAN and it has been created by Zhengyao Wen, Wenzhong Lin, Tao Wang and Ge Xu from Minjiang University in China. <br></br>Link to source code: <a href="https://github.com/yaoing/DAN/">DAN model</a></td>
            </tr>
            <tr>
              <td class="question">What are image mode and video mode?</td>
            </tr>
            <tr>
              <td >Image mode is for FER based on image file, while video mode is for video file.</td>
            </tr>
            <tr>
              <td class="question">In what form results are presented after successful FER process?</td>
            </tr>
            <tr>
              <td >In both modes, results are available in downloadable text file.</td>
            </tr>
            <tr>
              <td  class="question">What kind of changes were introduced to the model?</td>
            </tr>
            <tr>
              <td >Multiple face detection using cv2 library** and adjusting the model to work on video files by dividing them into frames.</td>
            </tr>
            <tr>
              <td  class="question">What API was used?</td>
            </tr>
            <tr>
              <td >REST API was implemented using Django Rest Framework. It allows communication between client and server through json files. Defined requests: GET, DELETE and POST</td>
            </tr>
            <tr>
              <td class="question">What future features are planned to be developed as of now?</td>
            </tr>
            <tr>
              <td >Development of own FER model, adding login option and bot chat.</td>
            </tr>
            <tr>
              <td class="question">What is the structure of file with results?</td>
            </tr>
            <tr>
              <td >1. image mode result file - recognized emotion : face coordinates<br/>2. video mode result file - recognized emotion : face coordinates : time : frame</td>
            </tr>
            <tr>
              <td class="question">What was used to create web application?</td>
            </tr>
            <tr>
              <td >Mainly for web application creation Django framework was used for backend, DFR as API and React together with HTML, CSS, bootstrap for frontend.</td>
            </tr>
            <tr>
              <td class="question">Why was the app created?</td>
            </tr>
            <tr>
              <td >The developed app is a part of my thesis, to prove my engineering skills.</td>
            </tr>
          </table><br/><br/>
          <hr style={{background: "#9b9ca1", height: "5px", border: "none"}}/>
          <div>
            <Tutorial/>
          </div>
        </div>
      </div>
    </div>
  </motion.div>
</div>
  );
}
export default About;
