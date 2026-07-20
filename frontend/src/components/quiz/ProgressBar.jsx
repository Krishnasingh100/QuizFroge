const ProgressBar = ({ current, total }) => {
  const percent = (current / total) * 100;

  return (
    <div className="progress-wrap">
      <div className="progress-label">
        Question {current} of {total}
      </div>
      <div className="progress-track">
        <div className="progress-fill" style={{ width: `${percent}%` }} />
      </div>
    </div>
  );
};

export default ProgressBar;
