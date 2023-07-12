import ProgressBar from 'react-bootstrap/ProgressBar';
import React, { Component } from "react";

// Implementation of animated progress bar
class AnimatedBar extends Component {
    render() {
      const { percent } = this.props;
      return (
        <ProgressBar
          now={percent} // Current progress in percents
          animated
          label={`${percent}%`}
        />
      );
    }
  } 
export default AnimatedBar;