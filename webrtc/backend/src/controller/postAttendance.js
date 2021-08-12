const express = require('express');
const router = express.Router();
const connect = require('../../config/database');

var mmt = require('moment');
require('moment-timezone');
mmt.tz.setDefault("Asia/Seoul");

router.post('/', async (req, res) => {
    const attendance_query = 'INSERT INTO student_manage_attendance (status, registertime, student_id, classroom_id) VALUES (?)';
    
    const {student_id, classroom_id} = req.body;
    const now_at = mmt().format("yyyy-MM-DD hh:mm:ss");
    var attendance_data = {
        status: '1',
        registertime: now_at,
        student_id: student_id,
        classroom_id: classroom_id
    }

    connect.query(attendance_query, attendance_data,(error, result) => {
        if(error) throw error;
        console.log(result);
        res.render("logic", {type:"attendance", result:true});

    })
    


});


module.exports = router;