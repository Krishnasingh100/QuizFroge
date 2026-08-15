import fs from 'fs';
import path from 'path';
import mongoose from 'mongoose';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';

import Question from '../models/Question.js';

dotenv.config();


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

        // Validate and normalize questions to avoid aborting the entire seed
        const validDocs = [];
        let skipped = 0;

        for (const q of questions) {
          const hasQuestion = typeof q.question === 'string' && q.question.trim().length > 0;
          const hasOptions = Array.isArray(q.options) && q.options.length === 4 && q.options.every((o) => typeof o === 'string');
          const hasCorrect = Number.isInteger(q.correctAnswer) && q.correctAnswer >= 0 && q.correctAnswer <= 3;

          if (hasQuestion && hasOptions && hasCorrect) {
            validDocs.push({
              language,
              difficulty,
              question: q.question.trim(),
              options: q.options.map((o) => o.trim()),
              correctAnswer: q.correctAnswer,
              explanation: q.explanation || '',
            });
          } else {
            skipped += 1;
          }
        }

        if (validDocs.length > 0) {
          await Question.insertMany(validDocs, { ordered: false });
          totalInserted += validDocs.length;
        }

        console.log(
          `Inserted ${validDocs.length} questions -> ${language} / ${difficulty}` +
            (skipped > 0 ? ` (skipped ${skipped} invalid)` : '')
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