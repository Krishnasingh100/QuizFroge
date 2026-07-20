require('dotenv').config();
const express = require('express');
const cors = require('cors');
const connectDB = require('./config/db');
const languageRoutes = require('./routes/languageRoutes');
const quizRoutes = require('./routes/quizRoutes');
const errorHandler = require('./middleware/errorHandler');

connectDB();

const app = express();

app.use(cors());
app.use(express.json());

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', message: 'QuizForge API is running' });
});

app.use('/api/languages', languageRoutes);
app.use('/api/quiz', quizRoutes);

app.use(errorHandler);

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`QuizForge server running on http://localhost:${PORT}`);
});
