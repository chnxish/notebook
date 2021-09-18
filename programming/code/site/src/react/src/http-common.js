import axios from 'axios';

export default axios.create({
  baseURL: 'http://ip:8000/api',
  headers: {
    'content-type': 'application/json'
  }
});
