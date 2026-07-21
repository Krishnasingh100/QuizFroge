import express from 'express';
import {
  startQuiz,
  submitQuiz,
  getStats,
} from '../controllers/quizController.js';

const router = express.Router();

router.get('/start', startQuiz);
router.post('/submit', submitQuiz);
router.get('/stats', getStats);

export default router;