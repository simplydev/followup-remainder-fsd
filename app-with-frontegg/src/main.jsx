import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

import { FronteggProvider } from '@frontegg/react';

const contextOptions = {
  baseUrl: 'https://followup-dev.frontegg.com',
  clientId: '560c6ea6-f026-4b8b-b43a-86f2c15c7f58',
  appId: '47eed79c-fd8d-4913-8637-b3b962a5eec6'
};

ReactDOM.render(
  <FronteggProvider contextOptions={contextOptions}>
    <App />
  </FronteggProvider>,
  document.getElementById('root')
);