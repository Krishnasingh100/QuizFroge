const Loader = ({ message = 'Loading...' }) => {
  return (
    <div className="loader-wrap">
      <div className="loader" />
      <p>{message}</p>
    </div>
  );
};

export default Loader;
