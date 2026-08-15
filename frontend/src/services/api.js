import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "/api",
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getLanguages = () => api.get('/languages');

export const getLanguage = (slug) => api.get(`/languages/${slug}`);

export const startQuiz = (language, difficulty) =>
  api.get('/quiz/start', { params: { language, difficulty } });

export const submitQuiz = (data) => api.post('/quiz/submit', data);

export const getStats = () => api.get('/quiz/stats');

export default api;
