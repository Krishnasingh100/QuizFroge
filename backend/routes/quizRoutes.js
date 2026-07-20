const express = require('express');
const { startQuiz, submitQuiz, getStats } = require('../controllers/quizController');

const router = express.Router();

router.get('/start', startQuiz);
router.post('/submit', submitQuiz);
router.get('/stats', getStats);

module.exports = router;
