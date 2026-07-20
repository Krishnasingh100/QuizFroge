const DifficultySelector = ({ onSelect, loading }) => {
  const levels = [
    { key: 'easy', label: 'Easy', color: 'easy' },
    { key: 'medium', label: 'Medium', color: 'medium' },
    { key: 'hard', label: 'Hard', color: 'hard' },
  ];

  return (
    <div className="difficulty-grid">
      {levels.map((level) => (
        <button
          key={level.key}
          type="button"
          className={`difficulty-btn difficulty-${level.color}`}
          onClick={() => onSelect(level.key)}
          disabled={loading}
        >
          <span>{level.label}</span>
        </button>
      ))}
    </div>
  );
};

export default DifficultySelector;
