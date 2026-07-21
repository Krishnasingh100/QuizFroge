const LANGUAGES = [
  { slug: 'c', name: 'C', description: 'Core C programming concepts' },
  { slug: 'cpp', name: 'C++', description: 'Object-oriented C++ fundamentals' },
  { slug: 'python', name: 'Python', description: 'Python syntax, logic, and libraries' },
  { slug: 'javascript', name: 'JavaScript', description: 'JS basics, DOM, and ES6+' },
  { slug: 'java', name: 'Java', description: 'Java OOP, collections, and JVM' },
  { slug: 'html', name: 'HTML', description: 'HTML tags, semantics, and forms' },
  { slug: 'css', name: 'CSS', description: 'CSS layout, flexbox, and styling' },
  { slug: 'nodejs', name: 'Node.js', description: 'Node runtime, modules, and APIs' },
  { slug: 'react', name: 'React.js', description: 'Components, hooks, and state' },
  { slug: 'go', name: 'Go', description: 'Go syntax, goroutines, and packages' },
  { slug: 'rust', name: 'Rust', description: 'Ownership, borrowing, and safety' },
  { slug: 'git', name: 'Git', description: 'Version control commands and workflow' },
  { slug: 'github', name: 'GitHub', description: 'Repos, PRs, and collaboration' },
  { slug: 'sql', name: 'SQL', description: 'Queries, joins, and database design' },
  { slug: 'typescript', name: 'TypeScript', description: 'Typed JavaScript with interfaces and generics' },
  { slug: 'php', name: 'PHP', description: 'Server-side scripting and web development' },
  { slug: 'ruby', name: 'Ruby', description: 'Elegant syntax, metaprogramming, and Rails' },
  { slug: 'swift', name: 'Swift', description: 'Apple ecosystem, safety, and performance' },
  { slug: 'kotlin', name: 'Kotlin', description: 'Concise syntax, null safety, and Android' },
  { slug: 'csharp', name: 'C#', description: '.NET framework, LINQ, and async programming' },
  { slug: 'docker', name: 'Docker', description: 'Containerization, images, and orchestration' },
  { slug: 'mongodb', name: 'MongoDB', description: 'NoSQL document database and queries' },
  { slug: 'redis', name: 'Redis', description: 'In-memory data store, caching, and pub/sub' },
  { slug: 'bash', name: 'Bash', description: 'Shell scripting, automation, and CLI tools' },
  { slug: 'tailwind', name: 'Tailwind CSS', description: 'Utility-first CSS framework and design' },
]
const getLanguages = async (req, res) => {
  res.json({ languages: LANGUAGES });
};

const getLanguageBySlug = async (req, res) => {
  const language = LANGUAGES.find((item) => item.slug === req.params.slug);

  if (!language) {
    return res.status(404).json({ message: 'Language not found' });
  }

  res.json({ language });
};

module.exports = {
  getLanguages,
  getLanguageBySlug,
};