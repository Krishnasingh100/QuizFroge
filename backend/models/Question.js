import mongoose from 'mongoose';

const questionSchema = new mongoose.Schema(
  {
    language: {
      type: String,
      required: true,
      index: true,
    },
    difficulty: {
      type: String,
      required: true,
      enum: ['easy', 'medium', 'hard'],
      index: true,
    },
    question: {
      type: String,
      required: true,
    },
    options: {
      type: [String],
      required: true,
      validate: {
        validator: (options) => options.length === 4,
        message: 'Each question must have exactly 4 options',
      },
    },
    correctAnswer: {
      type: Number,
      required: true,
      min: 0,
      max: 3,
    },
    explanation: {
      type: String,
      default: '',
    },
  },
  {
    timestamps: true,
  }
);

questionSchema.index({ language: 1, difficulty: 1 });

const Question = mongoose.model('Question', questionSchema);

export default Question;