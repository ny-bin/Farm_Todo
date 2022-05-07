import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './app/store';
import App from './App';
import reportWebVitals from './reportWebVitals';
import './index.css';
import { QueryClient, QueryClientProvider } from 'react-query';
import {ReactQueryDevtools} from "react-query/devtools"
import ReactDOM from 'react-dom';

const queryClient = new QueryClient({
  defaultOptions:{
    queries:{
      retry:false,
      refetchOnWindowFocus:false
    }
  }
})


ReactDOM.render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>

    <Provider store={store}>
      <App />
    </Provider>
    <ReactQueryDevtools initialIsOpen={false}/>
    </QueryClientProvider>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
