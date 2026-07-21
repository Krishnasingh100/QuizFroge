import fs from 'fs';
import path from 'path';
import mongoose from 'mongoose';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';

import Question from '../models/Question.js';

dotenv.config();

// Recreate __dirname for ES Modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SEEDS_DIR = path.join(__dirname, '../seeds');
const DIFFICULTIES = ['easy', 'medium', 'hard'];

const seedQuestions = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URI);
    console.log('Connected to MongoDB');

    await Question.deleteMany({});
    console.log('Cleared old questions');

    const languages = fs
      .readdirSync(SEEDS_DIR, { withFileTypes: true })
      .filter((entry) => entry.isDirectory())
      .map((entry) => entry.name);

    let totalInserted = 0;

    for (const language of languages) {
      for (const difficulty of DIFFICULTIES) {
        const filePath = path.join(SEEDS_DIR, language, `${difficulty}.json`);

        if (!fs.existsSync(filePath)) {
          console.log(`Skipped missing file: ${language}/${difficulty}.json`);
          continue;
        }

        const raw = fs.readFileSync(filePath, 'utf-8');
        const questions = JSON.parse(raw);

        if (!Array.isArray(questions) || questions.length === 0) {
          console.log(`No questions in ${language}/${difficulty}.json`);
          continue;
        }

        const docs = questions.map((q) => ({
          language,
          difficulty,
          question: q.question,
          options: q.options,
          correctAnswer: q.correctAnswer,
          explanation: q.explanation || '',
        }));

        await Question.insertMany(docs);
        totalInserted += docs.length;

        console.log(
          `Inserted ${docs.length} questions -> ${language} / ${difficulty}`
        );
      }
    }

    console.log(`\nDone! Total questions seeded: ${totalInserted}`);
    process.exit(0);
  } catch (error) {
    console.error('Seed error:', error.message);
    process.exit(1);
  }
};

seedQuestions();