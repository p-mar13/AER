/* istanbul ignore file */
import React, { Component } from 'react';
import axios from 'axios';
import { motion } from "framer-motion";
import Styles from "../styles/ImagePage/ImagePage.module.css";
var fileDownload = require('js-file-download');

// Page for image mode
class App extends Component {
  constructor(){
    super();
    this.state = {
      title: '',
      image: null,
      visibleDownload: false,
      submitState: true,
      errorState: false,
      errorStatus: '',
      error: '',
    };
  }

  handleError = () => {
    this.setState({errorState:true}); 
    this.setState({visibleDownload:false});
    this.setState({submitState:false});
  };

  delay = ms => new Promise(
    resolve => setTimeout(resolve, ms)
  );

  // Handles download of text files with blob type
  handlePDFDownload = () => {
    axios.get('http://localhost:8000/api/download/', { 
        responseType: 'blob',
    }).then(res => {
        fileDownload(res.data, 'image_result.txt');
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

  handleAfterUpload = (e) => {
    this.setState({
      image: e.target.files[0]
    })
  };

  // Handles sending images to server
  handleSubmit = (e) => {
    this.setState({visibleDownload:false});
    this.setState({submitState:false});
    e.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append('image', this.state.image, this.state.image.name);
    form_data.append('title', this.state.title);
    let url = 'http://localhost:8000/api/images/';
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
    await this.delay(1000);
    if(this.state.errorStatus==='ERROR')
    {
      this.handleError();
    }
    else {
    this.setState({visibleDownload:true});}
};

 // Rendering of the page (HTML) 
  render() {
    return (
      <div class={Styles.border}>
        <motion.div
          class="Styles.container"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 1 }}>
            <p class={Styles.title}>Facial Emotion Recognition for images</p><hr/>
            <div class={Styles.app}>
              <form onSubmit={this.handleSubmit}>
                <p>
                  <input type="text" placeholder='Title' id='title' value={this.state.title} onChange={this.handleChange} required/>
                </p>
                <p>
                  <input type="file"
                          id="image"
                          accept="image/png, image/jpeg"  onChange={this.handleImageChange} required/>
                </p>
                {this.state.errorState&&<div class={Styles.errorDesc}><p>{this.state.error}</p>
                <button class={Styles.button} onClick={() => window.location.reload(true)}>Reupload</button>
                </div>}
                <div class={Styles.submitButton}>
                {this.state.submitState&&<input type="submit" value="Submit" className="btn btn-primary"/>}
                </div>
              </form>&nbsp;
              {this.state.visibleDownload && <div>
                <button class={Styles.button}onClick={() => this.handlePDFDownload()}>Download</button>
                <button class={Styles.button} onClick={() => window.location.reload(true)}>Reupload</button>
                </div>}
                
            </div>
          </motion.div>
      </div>
    );
  }
}
export default App;