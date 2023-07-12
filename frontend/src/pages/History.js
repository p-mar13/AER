/* istanbul ignore file */
import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import axios from "axios";
import FileList from '../components/TextFiles/FileList.js'
import Styles from "../styles/HistoryPage/HistoryPage.module.css";
import Background from "../assets/images/bg_hist.jpg"; 
import { motion } from "framer-motion";
export const API_URL="http://localhost:8000/api/textfile/";

// History page that displays all successful tasks
class History extends Component {
  state = {
    files: [],
    images: false,
    videos: false,
  };

  constructor() {
    super();
    this.state = {
      images: false,
      videos: false,
  };}

  componentDidMount() {
    this.resetState();
  }

  getFiles = () => { // Get all files using axios GET request
    return axios.get(API_URL).then(res => this.setState({ files: res.data }));
  };

  resetState = () => {
    this.getFiles();
  };

  getVideos = () => { // Get all videos using axios GET request
    return axios.get("http://localhost:8000/api/textfile/video").then(res => this.setState({ files: res.data }));
  }

  getImages = () => { // Get all images using axios GET request
    return axios.get("http://localhost:8000/api/textfile/image").then(res => this.setState({ files: res.data }));
  }

  setImages = () => {
    if(this.state.images===false)
      {this.getImages();
    if(this.state.videos===true) {
        this.setState({videos: !this.state.videos});
      }
    }
    else{
      this.getFiles();
    }
    this.setState({images: !this.state.images});
  }

  setVideos = () => {
    if(this.state.videos===false)
      {this.getVideos();
    if(this.state.images===true)
    {
      this.setState({images: !this.state.images});
    }
    }
    else{
      this.getFiles();
    }
    this.setState({videos: !this.state.videos});
  }

  render() {
    return (
      <div style={{ backgroundImage:`url(${Background})`,backgroundRepeat:"repeat",width:1519.5 }}>
        <motion.div
          className="container"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 1 }}>
        <div class={Styles.Page}>
          <div class={Styles.border}>
            <div class={Styles.buttons}>
              <button class={this.state.images ? (Styles.clicked) : (Styles.unclicked)} onClick={() =>this.setImages()}>Show images</button>
              <button class={this.state.videos ? (Styles.clicked) : (Styles.unclicked)} onClick={() =>this.setVideos()}>Show videos</button>
            </div>
            <div class={Styles.table}>
            <Container style={{ marginTop: "20px" }}>
              <Row>
                <Col>
                  <FileList
                    files={this.state.files}
                    resetState={this.resetState}
                  />
                </Col>
              </Row>
            </Container>
          </div>
        </div>
      </div>
    </motion.div>
  </div>
  );
}}
export default History;