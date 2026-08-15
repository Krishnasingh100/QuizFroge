import { useEffect, useState } from 'react';
import { useNavigate, useParams, Link } from 'react-router-dom';
import { getLanguage, startQuiz } from '../services/api';
import { useQuiz } from '../context/QuizContext';
import DifficultySelector from '../components/quiz/DifficultySelector';
import Loader from '../components/common/Loader';
import LanguageIcon from '../components/common/LanguageIcon';

const LanguagePage = () => {
  const { slug } = useParams();
  const navigate = useNavigate();
  const { startQuizSession } = useQuiz();
  const [language, setLanguage] = useState(null);
  const [loading, setLoading] = useState(true);
  const [starting, setStarting] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchLanguage = async () => {
      try {
        const { data } = await getLanguage(slug);
        setLanguage(data.language);
      } catch (err) {
        setError('Language not found.');
      } finally {
        setLoading(false);
      }
    };
    fetchLanguage();
  }, [slug]);

  const handleSelectDifficulty = async (difficulty) => {
    setStarting(true);
    setError('');
    try {
      const { data } = await startQuiz(slug, difficulty);
      startQuizSession(slug, difficulty, data.questions);
      navigate(`/quiz/${slug}/${difficulty}`);
    } catch (err) {
      const message =
        err.response?.data?.message ||
        'Could not start quiz. Add questions and run seed script.';
      setError(message);
    } finally {
      setStarting(false);
    }
  };

  if (loading) return <Loader message="Loading language..." />;

  if (!language) {
    return (
      <div className="page error-page">
        <h2>{error || 'Language not found'}</h2>
        <Link to="/">Back to Home</Link>
      </div>
    );
  }

  return (
    <div className="page language-page">
      <header className="page-header">
        <span className="language-page-icon">
          <LanguageIcon slug={language.slug} name={language.name} />
        </span>
        <p>{language.description}</p>
      </header>

      <section className="difficulty-section">
        <h2>Select Difficulty</h2>
        <DifficultySelector onSelect={handleSelectDifficulty} loading={starting} />
        {starting && <p className="starting-text">Preparing your quiz...</p>}
        {error && <p className="error-text">{error}</p>}
      </section>

      <Link to="/" className="back-link">
        ← Back to languages
      </Link>
    </div>
  );
};

export default LanguagePage;