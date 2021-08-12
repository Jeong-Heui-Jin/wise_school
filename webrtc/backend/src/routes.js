const express = require('express');
const router = express.Router();

const attendance = require('./controller/app_routes');
router.use('/', attendance);

module.exports = router;