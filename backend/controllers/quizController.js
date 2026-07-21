import Question from '../models/Question.js';
import QuizAttempt from '../models/QuizAttempt.js';

const QUESTIONS_PER_QUIZ = 10;

const VALID_LANGUAGES = [
  'c', 'cpp', 'python', 'javascript', 'java', 'html', 'css',
  'nodejs', 'react', 'go', 'rust', 'git', 'github', 'sql',
  'typescript', 'php', 'ruby', 'swift', 'kotlin', 'csharp',
];

export const startQuiz = async (req, res, next) => {
  try {
    const { language, difficulty } = req.query;

    if (!language || !difficulty) {
      return res.status(400).json({
        message: 'language and difficulty are required',
      });
    }

    if (!VALID_LANGUAGES.includes(language)) {
      return res.status(400).json({
        message: 'Invalid language',
      });
    }

    if (!['easy', 'medium', 'hard'].includes(difficulty)) {
      return res.status(400).json({
        message: 'Invalid difficulty',
      });
    }

    const count = await Question.countDocuments({
      language,
      difficulty,
    });

    if (count === 0) {
      return res.status(404).json({
        message: `No questions found for ${language} (${difficulty}). Add questions to seeds and run npm run seed.`,
      });
    }

    const sampleSize = Math.min(QUESTIONS_PER_QUIZ, count);

    const questions = await Question.aggregate([
      { $match: { language, difficulty } },
      { $sample: { size: sampleSize } },
      {
        $project: {
          question: 1,
          options: 1,
          language: 1,
          difficulty: 1,
        },
      },
    ]);

    res.json({
      language,
      difficulty,
      total: questions.length,
      questions,
    });
  } catch (error) {
    next(error);
  }
};

export const submitQuiz = async (req, res, next) => {
  try {
    const { language, difficulty, answers, timeTaken } = req.body;

    if (!language || !difficulty || !answers || typeof answers !== 'object') {
      return res.status(400).json({
        message: 'language, difficulty, and answers are required',
      });
    }

    const questionIds = Object.keys(answers);

    if (questionIds.length === 0) {
      return res.status(400).json({
        message: 'No answers provided',
      });
    }

    const questions = await Question.find({
      _id: { $in: questionIds },
    });

    let score = 0;

    const results = questions.map((q) => {
      const userAnswer = answers[q._id.toString()];
      const isCorrect = userAnswer === q.correctAnswer;

      if (isCorrect) score++;

      return {
        questionId: q._id,
        question: q.question,
        options: q.options,
        userAnswer,
        correctAnswer: q.correctAnswer,
        isCorrect,
        explanation: q.explanation,
      };
    });

    const total = questions.length;
    const percentage = Math.round((score / total) * 100);

    await QuizAttempt.create({
      language,
      difficulty,
      score,
      totalQuestions: total,
      percentage,
      timeTaken: timeTaken || 0,
    });

    res.json({
      language,
      difficulty,
      score,
      total,
      percentage,
      passed: percentage >= 60,
      results,
    });
  } catch (error) {
    next(error);
  }
};

export const getStats = async (req, res, next) => {
  try {
    const totalQuestions = await Question.countDocuments();
    const totalAttempts = await QuizAttempt.countDocuments();

    res.json({
      totalQuestions,
      totalAttempts,
      questionsPerQuiz: QUESTIONS_PER_QUIZ,
    });
  } catch (error) {
    next(error);
  }
};