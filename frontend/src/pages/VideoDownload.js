/* istanbul ignore file */
import React, { Component } from 'react';
import axios from 'axios';
import AnimatedBar from '../components/ProgressBar/ProgressBar.js'
import { motion } from "framer-motion";
import Styles from "../styles/VideoPage/VideoPage.module.css";
var fileDownload = require('js-file-download');

// Page for video page
class App extends Component {
  constructor(){
    super();
    this.state = {
      title: '',
      image: null,
      progressBarNr: '',
      finished: false,
      visibleBar: false,
      submittable: true,
      errorState: false,
      errorStatus: 'uplod',
      error: 'error',
    };
  }

  handleError = () => {
    this.setState({errorState:true}); 
    this.setState({visibleBar:false});
    this.setState({finished:false});
  };

  delay = ms => new Promise(
    resolve => setTimeout(resolve, ms)
  );

  // Sends GET request using axios to get progress of current task
  handleProgress = () => {
    axios.get('http://localhost:8000/api/progress/').then(res=>this.setState({progressBarNr:res.data.percent, error:res.data.description, errorStatus: res.data.state}));
  }

  // Handles download of text files with blob type
  handlePDFDownload = () => {
    axios.get('http://localhost:8000/api/download/', { 
        responseType: 'blob',
    }).then(res => {
        fileDownload(res.data, 'video_result.txt');
        console.log(res);
    }).catch(err => {
        console.log(err);
    })};

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value
    })
  };

  handleImageChange = (e) => {
    this.setState({
      image: e.target.files[0]
    })
  };

  // Handles sending videos to server
  handleSubmit = (e) => {
    this.setState({finished:false});
    e.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append('image', this.state.image, this.state.image.name);
    form_data.append('title', this.state.title);
    let url = 'http://localhost:8000/api/videos/';
    axios.post(url, form_data, { //POST request using axios, sent to server's URL
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
        .then(res => {
          this.setState({error:res.data.description, errorStatus: res.data.state});
        })
        .catch(err => console.log(err))
    this.handleStart();
  };

  handleStart = async event => {
    await this.delay(500);
    if(this.state.errorStatus!='ERROR'){
      this.setState({visibleBar:true});}
      await this.delay(8000);
      if(this.state.errorStatus!='ERROR'){
      this.setState({finished:true});}
      else {this.handleError()}
  };

  render() {
    let temp=parseInt(this.state.progressBarNr);
    let finito=this.state.finished;
    return (
      <div class={Styles.border}>
        <motion.div
          class="Styles.container"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 1 }}>
        <p class={Styles.title}>Facial Emotion Recognition for videos</p><hr/>
        <div class={Styles.app}>
          <form onSubmit={this.handleSubmit}>
            <p>
              <input type="text" placeholder='Title' id='title' value={this.state.title} onChange={this.handleChange} required/>
            </p>
            <p>
              <input type="file"
                      id="image"
                      accept="video/mp4, video/avi, video/mkv" onChange={this.handleImageChange} required/>
            </p>
            {this.state.errorState&&<div><div class={Styles.errorDesc}><p>{this.state.errorStatus} : {this.state.error}</p></div>
                <button class={Styles.button} onClick={() => window.location.reload(true)}>Reupload</button></div>
                }
            <div class={Styles.submitButton}>
              {!(this.state.errorState)&&<input type="submit" onClick={this.handleProgress()} value="Submit" className="btn btn-primary"/>}</div>
          </form>
        <div>&nbsp;
      </div>
      {this.state.visibleBar&&<div class={Styles.progressbar}><AnimatedBar percent={parseInt(temp)}></AnimatedBar></div>}&nbsp;
        {(parseInt(temp)===100)&&(finito===true)&&(<div>
          <button class={Styles.button}
            onClick={() => this.handlePDFDownload()}>Download
          </button>
          <button class={Styles.button} onClick={() => window.location.reload(true)}>Reupload</button>
        </div>
      )}
      </div>
    </motion.div>
  </div>
  );
}
}

export default App;