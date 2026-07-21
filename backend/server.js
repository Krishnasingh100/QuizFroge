import dotenv from 'dotenv';
import express from 'express';
import cors from 'cors';

import connectDB from './config/db.js';
import languageRoutes from './routes/languageRoutes.js';
import quizRoutes from './routes/quizRoutes.js';
import errorHandler from './middleware/errorHandler.js';

dotenv.config();

connectDB();

const app = express();

app.use(cors());
app.use(express.json());

app.get('/api/health', (req, res) => {
  res.json({
    status: 'ok',
    message: 'QuizForge API is running',
  });
});

app.use('/api/languages', languageRoutes);
app.use('/api/quiz', quizRoutes);

app.use(errorHandler);

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`QuizForge server running on http://localhost:${PORT}`);
});