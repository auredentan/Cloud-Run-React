import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
class App extends Component {

  launchTask = () => {
    axios.get('/api/task').then(resp => {
      console.log('Response is ', resp);
    })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <div>
          <button onClick={this.launchTask}>Click me</button>
          </div>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React Prod kk
          </a>
        </header>
      </div>
    );
  }
}

export default App;
