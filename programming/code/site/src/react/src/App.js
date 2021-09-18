import React, { useState } from 'react';
import Service from './services/service';
import './App.css';

function App() {
  const [name, setName] = useState('');

  Service.getName()
    .then(response => {
      setName(response.data['name']);
      console.log(response.data);
    })
    .catch(e => {
      console.log(e);
    })

  return (
    <div>
      <h1>Hello, World!</h1>
      <p style={{fontWeight:'500', fontSize:'2.2em'}}>My name is {name}.</p>
      <p>A primary school student in the programming world.</p>
    </div>
  );
}
