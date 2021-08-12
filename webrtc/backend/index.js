const express = require('express');
const app = express();
const PORT = 8080;
const routes = require('./src/routes');
 
const cors = require('cors');
app.use(cors());

const connect = require('./config/database');

app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.use(express.json());
app.use('/api', routes);

app.listen(PORT, ()=> console.log(`이 서버는 ${PORT}로 동작합니다.`));

module.exports = app;