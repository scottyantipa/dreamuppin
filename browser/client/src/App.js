import React, { Component } from 'react';
import './App.css';

// Takes a dreamup app url as input and renders the app generated from the backend
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      urlText: undefined,
      html: undefined
    }
  }

  handleSubmit = () => {
    fetch("http://127.0.0.1:5000", {
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        url: this.state.urlText
      })
    })
      .then((res) => {
        if (res.ok) {
          res.text().then((html) => {
            this.setState({ html });
          })
        } else {
          console.log('failure: ', res);
        }
      })
      .catch((e) => {
        console.log(e);
      })
  }

  render() {
    return (
      <div className="App">
        <div className="search-control">
          <input
            type="text"
            value={this.state.urlText}
            onChange={(e) => {
              this.setState({ urlText: e.target.value })
            }}
            onKeyUp={(e) => {
              const keyCode = e.keyCode || e.which;
              if (keyCode === 13) {
                this.handleSubmit();
              }
            }}
          />
          <button
            type="button"
            onClick={this.handleSubmit}
          >
            dream
          </button>
        </div>
        <div className="divider" />
        <div>
          {
            this.state.html ? (
              <div dangerouslySetInnerHTML={{ __html: this.state.html }} />
            ) : null
          }
        </div>
      </div>
    );
  }
}

export default App;
