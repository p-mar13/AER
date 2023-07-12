/* istanbul ignore file */
import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalFooter } from "reactstrap";
import axios from "axios";
export const API_URL="http://localhost:8000/api/textfile/";

// Implementation of removing results from table component FileList
class RemoveResult extends Component {
  // State determining whether window will be displayed
  state = {
    popup: false
  };
// Change state to its opposite value
  toggle = () => {
    this.setState(previous => ({
      popup: !previous.popup
    }));
  };
// Delete request using axios
  deleteResult = pk => {
      axios.delete(API_URL + pk).then(() => {this.props.resetState(); this.toggle();});
  };

  render() {
    return (
      <Fragment>
        <button class="btn btn-danger" 
         onClick={() => this.toggle()} >Remove</button>
        <Modal isOpen={this.state.popup} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>
            Do you wanna delete this entry?
          </ModalHeader>
          <ModalFooter>
          <Button
              type="button"
              color="primary"
              onClick={() => this.deleteResult(this.props.pk)}
            > Yes </Button>
            <Button  type="button" onClick={() => this.toggle()}>
              Cancel
            </Button>
          </ModalFooter>
        </Modal>
      </Fragment>
    );
  }
}
export default RemoveResult;