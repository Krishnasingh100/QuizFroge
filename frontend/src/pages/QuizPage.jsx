import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { submitQuiz } from '../services/api';
import { useQuiz } from '../context/QuizContext';
import ProgressBar from '../components/quiz/ProgressBar';
import QuestionCard from '../components/quiz/QuestionCard';
import Button from '../components/common/Button';
import Loader from '../components/common/Loader';

const QuizPage = () => {
  const { slug, difficulty } = useParams();
  const navigate = useNavigate();
  const { quizData, setAnswer, setResult } = useQuiz();
  const [currentIndex, setCurrentIndex] = useState(0);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  const { questions, answers } = quizData;

  useEffect(() => {
    if (questions.length === 0) {
      navigate(`/language/${slug}`);
    }
  }, [questions, slug, navigate]);

  if (questions.length === 0) {
    return <Loader message="Loading quiz..." />;
  }

  const currentQuestion = questions[currentIndex];
  const questionId = currentQuestion._id;
  const selectedAnswer = answers[questionId];
  const isLastQuestion = currentIndex === questions.length - 1;

  const handleSelectOption = (questionId, optionIndex) => {
    setAnswer(questionId, optionIndex);
    if (!isLastQuestion) {
      setTimeout(() => {
        setCurrentIndex((prev) => Math.min(prev + 1, questions.length - 1));
      }, 250);
    }
  };

  const handleSubmit = async () => {
    setSubmitting(true);
    setError('');
    try {
      const { data } = await submitQuiz({
        language: slug,
        difficulty,
        answers,
      });
      setResult(data);
      navigate('/result');
    } catch {
      setError('Failed to submit quiz. Please try again.');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="page quiz-page">
      <ProgressBar current={currentIndex + 1} total={questions.length} />
      <QuestionCard
        question={currentQuestion.question}
        options={currentQuestion.options}
        selectedAnswer={selectedAnswer}
        onSelect={(index) => handleSelectOption(questionId, index)}
      />
      <div className="quiz-actions">
        {isLastQuestion ? (
          <Button
            onClick={handleSubmit}
            disabled={selectedAnswer === undefined || submitting}
          >
            {submitting ? 'Submitting...' : 'Submit Quiz'}
          </Button>
        ) : null}
      </div>
      {error && <p className="error-text">{error}</p>}
    </div>
  );
};

export default QuizPage;