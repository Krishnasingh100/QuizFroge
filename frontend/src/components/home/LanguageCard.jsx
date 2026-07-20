import { Link } from 'react-router-dom';
import LanguageIcon from '../common/LanguageIcon';

const LanguageCard = ({ language }) => {
  return (
    <Link to={`/language/${language.slug}`} className="language-card">
      <span className="language-icon">
        <LanguageIcon slug={language.slug} name={language.name} />
      </span>
      <h3>{language.name}</h3>
      <p>{language.description}</p>
      <span className="language-cta">Start Quiz →</span>
    </Link>
  );
};

export default LanguageCard;
