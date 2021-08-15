const express = require('express');
const router = express.Router();

const postAttendaance = require('./postAttendance');
router.use('/attendance', postAttendaance);

const getAttendaance = require('./getAttendance');
router.use('/attendance', getAttendaance);

module.exports = router;