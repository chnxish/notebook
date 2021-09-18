import http from '../http-common';

const getName = () => {
  return http.get('/hello');
}

export default {
  getName
};
