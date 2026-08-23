import { useEffect, useState } from 'react';
import { getLanguages } from '../services/api';
import LanguageCard from '../components/home/LanguageCard';
import Loader from '../components/common/Loader';
import Button from '../components/common/Button';

const HomePage = () => {
  const [languages, setLanguages] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchLanguages = async () => {
      try {
        const { data } = await getLanguages();
        setLanguages(data.languages);
      } catch {
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

  const testimonials = [
    {
      id: 1,
      name: "Alex Johnson",
      role: "Full Stack Developer",
      thought: "QuizForge helped me master JavaScript in just 3 weeks. The difficulty progression is perfect!",
      avatar: "AJ"
    },
    {
      id: 2,
      name: "Sarah Chen",
      role: "DevOps Engineer",
      thought: "The breadth of languages covered is impressive. Great for keeping my skills sharp across multiple stacks.",
      avatar: "SC"
    },
    {
      id: 3,
      name: "Michael Rodriguez",
      role: "Backend Developer",
      thought: "I love how QuizForge provides immediate feedback. It's become my daily routine before coding sessions.",
      avatar: "MR"
    },
    {
      id: 4,
      name: "Emma Williams",
      role: "Frontend Developer",
      thought: "The React quizzes are spot-on. Helped me land my dream job at a top tech company!",
      avatar: "EW"
    }
  ];

  return (
    <div className="page home-page">
      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-left">
          <div className="hero-visual">
            <div className="visual-circle circle-1"></div>
            <div className="visual-circle circle-2"></div>
            <div className="visual-circle circle-3"></div>
            <div className="visual-element">
              <span className="visual-icon">💻</span>
            </div>
          </div>
        </div>
        <div className="hero-right">
          <div className="hero-content">
            <h1 className="hero-title">Master Programming Languages</h1>
            <p className="hero-subtitle">
              Challenge yourself with comprehensive quizzes across 20+ programming languages and tools. 
              Track your progress and become an expert coder.
            </p>
            <div className="hero-stats">
              <div className="stat">
                <span className="stat-number">{languages.length}+</span>
                <span className="stat-label">Languages</span>
              </div>
              <div className="stat">
                <span className="stat-number">1000+</span>
                <span className="stat-label">Questions</span>
              </div>
              <div className="stat">
                <span className="stat-number">3</span>
                <span className="stat-label">Difficulty Levels</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Languages Section */}
      <section id="languages-section" className="languages-section">
        <div className="section-header">
          <h2>Choose Your Language</h2>
          <p>Select a topic and test your programming knowledge</p>
        </div>

        <div className="language-grid">
          {languages.map((language) => (
            <LanguageCard key={language.slug} language={language} />
          ))}
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="testimonials-section">
        <div className="section-header">
          <h2>Our Users Love QuizForge</h2>
          <p>Join thousands of developers improving their skills every day</p>
        </div>

        <div className="testimonials-grid">
          {testimonials.map((testimonial) => (
            <div key={testimonial.id} className="testimonial-card">
              <div className="testimonial-header">
                <div className="user-avatar">{testimonial.avatar}</div>
                <div className="user-info">
                  <h4>{testimonial.name}</h4>
                  <p className="user-role">{testimonial.role}</p>
                </div>
              </div>
              <p className="testimonial-text">{testimonial.thought}</p>
              <div className="stars">★★★★★</div>
            </div>
          ))}
        </div>
      </section>

      {/* About Section */}
      <section className="about-section">
        <div className="section-header">
          <h2>About QuizForge</h2>
          <p>Learn more about our mission and features</p>
        </div>

        <div className="about-grid">
          <div className="about-card">
            <div className="about-icon">📚</div>
            <h3>Comprehensive Coverage</h3>
            <p>From fundamentals to advanced concepts, our quizzes cover all aspects of programming languages and modern development tools.</p>
          </div>

          <div className="about-card">
            <div className="about-icon">📊</div>
            <h3>Progressive Learning</h3>
            <p>Three difficulty levels (Easy, Medium, Hard) ensure you can progress at your own pace and challenge yourself appropriately.</p>
          </div>

          <div className="about-card">
            <div className="about-icon">⚡</div>
            <h3>Instant Feedback</h3>
            <p>Get immediate results and detailed explanations for each quiz question to understand your mistakes and improve faster.</p>
          </div>

          <div className="about-card">
            <div className="about-icon">🎯</div>
            <h3>Track Progress</h3>
            <p>Monitor your performance across different languages and topics. Identify your strengths and areas for improvement.</p>
          </div>

          <div className="about-card">
            <div className="about-icon">🏆</div>
            <h3>Competitive Spirit</h3>
            <p>Compete with other developers and see how you rank. Push yourself to become one of the top performers.</p>
          </div>

          <div className="about-card">
            <div className="about-icon">🚀</div>
            <h3>Industry-Relevant</h3>
            <p>Our questions are crafted by experienced developers to match real-world interview questions and practical scenarios.</p>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="cta-section">
        <div className="cta-content">
          <h2>Ready to Level Up Your Skills?</h2>
          <p>Start taking quizzes today and join thousands of developers who are mastering programming</p>
          <a href="#languages-section" className="cta-button">
            Start Learning Now
          </a>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
