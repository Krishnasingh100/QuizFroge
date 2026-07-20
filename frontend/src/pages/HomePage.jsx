import { useEffect, useState } from 'react';
import { getLanguages } from '../services/api';
import LanguageCard from '../components/home/LanguageCard';
import Loader from '../components/common/Loader';

const HomePage = () => {
  const [languages, setLanguages] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchLanguages = async () => {
      try {
        const { data } = await getLanguages();
        setLanguages(data.languages);
      } catch (err) {
        setError('Failed to load languages. Make sure backend is running.');
      } finally {
        setLoading(false);
      }
    };

    fetchLanguages();
  }, []);

  if (loading) return <Loader message="Loading languages..." />;

  if (error) {
    return (
      <div className="page error-page">
        <h2>Something went wrong</h2>
        <p>{error}</p>
      </div>
    );
  }

  return (
    <div className="page home-page">
      <header className="page-header">
        <h1>Choose Your Language</h1>
        <p>Select a topic and test your programming knowledge</p>
      </header>

      <div className="language-grid">
        {languages.map((language) => (
          <LanguageCard key={language.slug} language={language} />
        ))}
      </div>
    </div>
  );
};

export default HomePage;
