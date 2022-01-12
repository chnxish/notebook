import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom';
import './App.css';

import Home from './pages/home';
import FPT from './pages/fpt';
import CE from './pages/ce';
import PE from './pages/pe';
import NotFound from './pages/notfound';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/filterable-product-table" element={<FPT />} />
        <Route path="/context-example" element={<CE />} />
        <Route path="/portal-example" element={<PE />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
