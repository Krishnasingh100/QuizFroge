const QuestionCard = ({ question, options, selectedAnswer, onSelect }) => {
  return (
    <div className="question-card">
      <h2>{question}</h2>
      <div className="options-grid">
        {options.map((option, index) => (
          <button
            key={index}
            type="button"
            className={`option-btn ${selectedAnswer === index ? 'selected' : ''}`}
            onClick={() => onSelect(index)}
          >
            <span className="option-letter">{String.fromCharCode(65 + index)}</span>
            <span>{option}</span>
          </button>
        ))}
      </div>
    </div>
  );
};

export default QuestionCard;
