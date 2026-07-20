import { createContext, useContext, useState } from 'react';

const QuizContext = createContext(null);

const shuffleArray = (array) => {
  const items = [...array];
  for (let i = items.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [items[i], items[j]] = [items[j], items[i]];
  }
  return items;
};

export const QuizProvider = ({ children }) => {
  const [quizData, setQuizData] = useState({
    language: '',
    difficulty: '',
    questions: [],
    answers: {},
    result: null,
  });

  const startQuizSession = (language, difficulty, questions) => {
    setQuizData({
      language,
      difficulty,
      questions: shuffleArray(questions),
      answers: {},
      result: null,
    });
  };

  const setAnswer = (questionId, optionIndex) => {
    setQuizData((prev) => ({
      ...prev,
      answers: {
        ...prev.answers,
        [questionId]: optionIndex,
      },
    }));
  };

  const setResult = (result) => {
    setQuizData((prev) => ({
      ...prev,
      result,
    }));
  };

  const resetQuiz = () => {
    setQuizData({
      language: '',
      difficulty: '',
      questions: [],
      answers: {},
      result: null,
    });
  };

  return (
    <QuizContext.Provider
      value={{
        quizData,
        startQuizSession,
        setAnswer,
        setResult,
        resetQuiz,
      }}
    >
      {children}
    </QuizContext.Provider>
  );
};

export const useQuiz = () => {
  const context = useContext(QuizContext);
  if (!context) {
    throw new Error('useQuiz must be used inside QuizProvider');
  }
  return context;
};
