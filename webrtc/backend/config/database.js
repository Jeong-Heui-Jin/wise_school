const mysql = require('mysql2');
//const mysql = require('promise-mysql');

const dbConfig = {
    host: 'i5a205.p.ssafy.io',
    port: '3306',
    user: 'i5a205',
    password: '1234',
    database: 'dingcho',
    connectionLimit: 10,
    waitForConnection : true
};

const conn = mysql.createConnection(dbConfig);

module.exports = conn;