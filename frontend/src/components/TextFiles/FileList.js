/* istanbul ignore file */
import React, { Component } from "react";
import Styles from "../../styles/HistoryPage/HistoryPage.module.css";
import { Table } from "reactstrap";
import RemoveResult from './RemoveResult.js'
var fileDownload = require('js-file-download');

// Table of results that will be displayed in history page
class FileList extends Component {
  // Downloading of file with results, where e input is of type blob
  handlePDFDownload = (e) => {
        fileDownload(e, 'result.txt');
};
render() {
  const files = this.props.files;
  return (
        <div class={Styles.tableData}>
        <Table>
          <thead>
            <tr>
              <th class={Styles.headerTable}>Title</th>
              <th class={Styles.headerTable}>Created</th>
              <th class={Styles.headerTable}>Type</th>
              <th class={Styles.headerTable}></th>
            </tr>
          </thead>
          <tbody>
            {!files || files.length <= 0 ? (
              <tr>
                <td colSpan="5" align="center">
                  <b class={Styles.noFiles}>Ops, no files here yet</b>
                  <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
                </td>
              </tr>
            ) : (
              files.map(file => (
                <tr key={file.id}>
                  <td align='center'>{file.title}</td>
                  <td align='center'>{file.created}</td>
                  <td align='center'>{file.data_type}</td>
                  <div class={Styles.Liner}><td>
                  <button align='center' class="btn btn-secondary"
                  onClick={() => this.handlePDFDownload(file.content)}>Download
                  </button></td><td>
                  <RemoveResult align='center'
                    pk={file.id}
                    resetState={this.props.resetState}
                  />
                  </td>
                  </div>
                </tr>
              ))
            )}
          </tbody>
        </Table>
        <br></br>
        </div>
      );
    }
  }
  
  export default FileList;