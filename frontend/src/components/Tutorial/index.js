import React from "react";
import HeaderImage from "../../assets/images/tutorial/tutorial_header.png"; 
import Styles from "../../styles/AboutPage/AboutPage.module.css";
import Step1 from "../../assets/images/tutorial/image_mode/step1.png";
import Step2 from "../../assets/images/tutorial/image_mode/step2.png";
import Step3 from "../../assets/images/tutorial/image_mode/step3.png";
import Step4 from "../../assets/images/tutorial/image_mode/step4.png";
import Step5 from "../../assets/images/tutorial/image_mode/step5.png";
import Step6 from "../../assets/images/tutorial/image_mode/step6.png";
import VStep1 from "../../assets/images/tutorial/video_mode/step1.png";
import VStep2 from "../../assets/images/tutorial/video_mode/step2.png";
import VStep3 from "../../assets/images/tutorial/video_mode/step3.png";
import VStep4 from "../../assets/images/tutorial/video_mode/step4.png";
import VStep5 from "../../assets/images/tutorial/video_mode/step5.png";
import VStep6 from "../../assets/images/tutorial/video_mode/step6.png";

//Tutorial with steps and images of how to use image and video mode
const Tutorial = () => {
return(
    <div>
          <img class={Styles.headerTut} src={HeaderImage} alt="logo"/>        
        <hr class={Styles.hl} style={{background: "#9b9ca1", height: "5px", border: "none",}}/>
      <h2 class={Styles.titleTutorial}>I. Image mode</h2>
        <p>Step 1. Go to Home page</p>
          <img class={Styles.tutorialImage} src={Step1} alt="Step 1."/>
        <p>Step 2. Click button "Upload image"</p>
          <img class={Styles.tutorialImage} src={Step2} alt="Step 2."/>
        <p>Step 3. Fill "title" field</p>
          <img class={Styles.tutorialImage} src={Step3} alt="Step 3."/>
        <p>Step 4. Choose file to upload (image)</p>
          <img class={Styles.tutorialImage} src={Step4} alt="Step 4."/>
        <p>Step 5. Click button "Submit" and wait</p>
          <img class={Styles.tutorialImage} src={Step5} alt="Step 5."/>
        <p>Optional: Step 6. Click "Download" button to download result/"Reupload" button to upload another image</p>
          <img class={Styles.tutorialImage} src={Step6} alt="Step 6."/>
        <br/><br/><br/><br/>
        <hr class={Styles.hl} style={{background: "#9b9ca1", height: "5px", border: "none",}}/>
      <h2 class={Styles.titleTutorial}>II. Video mode</h2>
        <p>Step 1. Go to Home page</p>
          <img class={Styles.tutorialImage} src={VStep1} alt="Step 1."/>
        <p>Step 2. Click button "Upload video"</p>
          <img class={Styles.tutorialImage} src={VStep2} alt="Step 2."/>
        <p>Step 3. Fill "title" field</p>
          <img class={Styles.tutorialImage} src={VStep3} alt="Step 3."/>
        <p>Step 4. Choose file to upload (video)</p>
          <img class={Styles.tutorialImage} src={VStep4} alt="Step 4."/>
        <p>Step 5. Click button "Submit" and wait until progress bar shows 100%</p>
          <img class={Styles.tutorialImage} src={VStep5} alt="Step 5."/>
        <p>Optional: Step 6. Click "Download" button to download result/"Reupload" button to upload another image</p>
          <img class={Styles.tutorialImageLast} src={VStep6} alt="Step 6."/>
    </div>
      )}
    export default Tutorial;