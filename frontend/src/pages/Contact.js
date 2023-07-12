/* istanbul ignore file */
import React, { Component } from "react";
import axios from 'axios';
import Styles from "../styles/ContactPage/ContactPage.module.css";
import {Link} from "react-router-dom";
import Background from "../assets/images/bg_cont.jpg"; 
import Image from "../assets/logo/linkedin.png"; 
import { motion } from "framer-motion";

// Page where info about app's author and message form are displayed
class Contact extends Component {
  // Message info stores in states
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      email: '',
      message: ''
    }
  }

  handleSubmit(e) {
    e.preventDefault();
    // POST method in axios to send message
    axios({
      method: "POST",
      url:"http://127.0.0.1:8000/api/email/",
      data:  this.state
    }).then((response)=>{
      this.resetForm();
      if (response.data.status === 'SUCCESS') {
        alert("Message Sent.");
      } else if(response.data.status === 'ERROR') {
        alert("Message failed to send.")
      }
    })
  }
  resetForm(){
    this.setState({name: '', email: '', message: ''})
  }
  render() {
    return(
      <div style={{ backgroundImage:`url(${Background})`,backgroundRepeat:"repeat",height:685,width:1535 }}>
        <div class={Styles.border}>
          <div class={Styles.app}>
            <motion.div
              className="container text-center"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 1 }}>
                <div class={Styles.row}>
                  <div class={Styles.column1}>
                    <p class={Styles.intro}>Hi, I'm Paulina Markiewicz! I'm the creator of AER web application.</p>
                    <p class={Styles.blackText}></p>&nbsp;
                    <p>If you encounter any issues or simply have a question regarding implementation of AER app, do not hesitate to contact me.</p><br/><br/>
                      <p>
                        <div class={Styles.contactForm}>
                          <div class={Styles.header}>
                            Additional contact info:
                          </div>
                          E-mail: paulina.markiewicz@stud.pw.edu.pl&nbsp;
                          Linked<img class={Styles.logo} src={Image} alt="Linkedin Logo"></img>: 
                          <Link to ='https://www.linkedin.com/in/paulina-markiewicz-88a708216/'>link to profile</Link>&nbsp;&nbsp;
                          </div>
                        </p>
                    </div>
                    <div class={Styles.column2}>
                      <div class={Styles.info}>
                        <div class={Styles.header}>
                          <p>Contact form:</p>
                        </div>
                      <div class={Styles.form}>
                        <div className="App">
                          <form id="contact-form" onSubmit={this.handleSubmit.bind(this)} method="POST">
                            <div className="form-group">
                              <label htmlFor="name">Name</label>
                              <input type="text" className="form-control" value={this.state.name} onChange={this.onNameChange.bind(this)} />
                            </div>
                          <div className="form-group">
                            <label htmlFor="exampleInputEmail1">Email address</label>
                            <input type="email" className="form-control" aria-describedby="emailHelp" value={this.state.email} onChange={this.onEmailChange.bind(this)} />
                          </div>
                          <div className="form-group">
                            <label htmlFor="message">Message</label>
                            <textarea className="form-control" rows="5" value={this.state.message} onChange={this.onMessageChange.bind(this)} />
                          </div>
                          <div class={Styles.button}>
                            <button type="submit" className="btn btn-primary">Submit</button>
                          </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </div>
  );}

  onNameChange(event) {
	  this.setState({name: event.target.value})
  }
  onEmailChange(event) {
	  this.setState({email: event.target.value})
  }
  onMessageChange(event) {
	  this.setState({message: event.target.value})
    
  }} export default Contact;
