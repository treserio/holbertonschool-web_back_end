// Express.Router setup for routes to functions
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');
const express = require('express');
const router = express.Router();

router.get('/students/:major', StudentsController.getAllStudentsByMajor);
router.get('/students', StudentsController.getAllStudents);
router.get('/', AppController.getHomepage);

module.exports = router;
