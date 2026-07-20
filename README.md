# QuizForge

A full-stack MERN quiz application for programming languages and tools.

## Tech Stack

- **Frontend:** React 19 + Vite + React Router + Axios
- **Backend:** Node.js + Express 5 + Mongoose
- **Database:** MongoDB Atlas

## Project Structure

```
QuizForge/
├── backend/     # Express API, models, seeds
└── frontend/    # React UI
```

## Setup

### 1. MongoDB Atlas

1. Create a free cluster on MongoDB Atlas
2. Add your IP in Network Access
3. Create a database user
4. Copy the connection string

### 2. Backend

**Where:** `backend`

1. Copy `.env.example` to `.env`
2. Put your MongoDB URI in `.env`
3. Add questions in `seeds/<language>/<difficulty>.json`
4. Run:

```bash
npm run seed
npm run dev
```

Backend runs on `http://localhost:5000`

### 3. Frontend

**Where:** `frontend`

```bash
npm run dev
```

Frontend runs on `http://localhost:5173`

## API Endpoints (Postman)

| Method | URL |
|--------|-----|
| GET | `http://localhost:5000/api/health` |
| GET | `http://localhost:5000/api/languages` |
| GET | `http://localhost:5000/api/quiz/start?language=javascript&difficulty=easy` |
| POST | `http://localhost:5000/api/quiz/submit` |

## Question JSON Format

```json
{
  "question": "Your question?",
  "options": ["A", "B", "C", "D"],
  "correctAnswer": 0,
  "explanation": "Optional"
}
```

`correctAnswer` is the index: 0 = first option, 1 = second, etc.

## Languages

c, cpp, python, javascript, java, html, css, nodejs, react, go, rust, git, github, sql
