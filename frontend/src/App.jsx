import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { QuizProvider } from './context/QuizContext';
import Navbar from './components/common/Navbar';
import HomePage from './pages/HomePage';
import LanguagePage from './pages/LanguagePage';
import QuizPage from './pages/QuizPage';
import ResultPage from './pages/ResultPage';

function App() {
  return (
    <QuizProvider>
      <BrowserRouter>
        <div className="app">
          <Navbar />
          <main className="main-content">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/language/:slug" element={<LanguagePage />} />
              <Route path="/quiz/:slug/:difficulty" element={<QuizPage />} />
              <Route path="/result" element={<ResultPage />} />
            </Routes>
          </main>
        </div>
      </BrowserRouter>
    </QuizProvider>
  );
}

export default App;
