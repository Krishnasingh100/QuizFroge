import Button from '../common/Button';

const ScoreCard = ({ result, onRetry, onHome }) => {
  const { score, total, percentage, passed, language, difficulty } = result;

  return (
    <div className="score-card">
      <p className="score-label">Your Score</p>
      <h1 className={`score-value ${passed ? 'passed' : 'failed'}`}>
        {score}/{total}
      </h1>
      <p className="score-percent">{percentage}%</p>
      <p className="score-meta">
        {language} · {difficulty}
      </p>
      <p className={`score-status ${passed ? 'passed' : 'failed'}`}>
        {passed ? 'Great job! You passed.' : 'Keep practicing!'}
      </p>

      <div className="score-actions">
        <Button onClick={onRetry}>Try Again</Button>
        <Button variant="secondary" onClick={onHome}>
          Back to Home
        </Button>
      </div>
    </div>
  );
};

export default ScoreCard;
