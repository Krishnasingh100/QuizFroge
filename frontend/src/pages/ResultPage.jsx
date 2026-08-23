import { useNavigate } from 'react-router-dom';
import { useQuiz } from '../context/QuizContext';
import ScoreCard from '../components/result/ScoreCard';
import Loader from '../components/common/Loader';

const ResultPage = () => {
  const navigate = useNavigate();
  const { quizData, resetQuiz } = useQuiz();
  const { result, language } = quizData;

  if (!result) {
    return <Loader message="Loading results..." />;
  }

  const handleRetry = () => {
    resetQuiz();
    navigate(`/language/${language}`);
  };

  const handleHome = () => {
    resetQuiz();
    navigate('/');
  };

  return (
    <div className="page result-page">
      <ScoreCard result={result} onRetry={handleRetry} onHome={handleHome} />

      <section className="review-section">
        <h2>Review Answers</h2>
        <div className="review-list">
          {result.results.map((item, index) => (
            <div
              key={item.questionId}
              className={`review-item ${item.isCorrect ? 'correct' : 'wrong'}`}
            >
              <p className="review-question">
                {index + 1}. {item.question}
              </p>
              <p>
                Your answer: <strong>{item.options[item.userAnswer]}</strong>
              </p>
              {!item.isCorrect && (
                <p>
                  Correct answer: <strong>{item.options[item.correctAnswer]}</strong>
                </p>
              )}
              {item.explanation && <p className="review-explanation">{item.explanation}</p>}
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default ResultPage;
