const express = require('express');
const router = express.Router();
//const db = require('../module/pool');
const connect = require('../../config/database');

router.get('/', async (req, res) => {
    const AttendanceData = 'select * from student_manage_attendance';
    let data = new Array();
    connect.query(AttendanceData, (error, rows) => {
        if (error) throw error;

        for(let i=0;i<rows.length;i++){
            let temp = {
                status: '',
                registertime: '',
                student_id: '',
                classroom_id: ''
            }
            temp.status = rows[i].status;
            temp.registertime = rows[i].registertime;
            temp.student_id = rows[i].student_id;
            temp.classroom_id = rows[i].classroom_id;
    
            data.push(temp);
        }

        if (data) {
            res.status(200).send({
            message: "success",
            data: data
            });
        } else {
            res.status(405).send({
            error: "Get sensing data fail"
            });
        }
    });



});


module.exports = router;