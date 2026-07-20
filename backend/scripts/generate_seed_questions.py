import json
import random
from pathlib import Path
from string import Formatter

ROOT = Path(__file__).resolve().parent.parent
SEEDS_DIR = ROOT / 'seeds'

LANGUAGE_META = {
    'c': {
        'name': 'C',
        'ext': '.c',
        'comment': '//',
        'const_keyword': 'const',
        'bool_true': '1',
        'bool_false': '0',
        'equality': '==',
        'import_example': '#include <stdio.h>',
        'function_definition': 'int main()',
    },
    'cpp': {
        'name': 'C++',
        'ext': '.cpp',
        'comment': '//',
        'const_keyword': 'const',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '==',
        'import_example': '#include <iostream>',
        'function_definition': 'int main()',
    },
    'java': {
        'name': 'Java',
        'ext': '.java',
        'comment': '//',
        'const_keyword': 'final',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '==',
        'import_example': 'import java.util.*;',
        'function_definition': 'public static void main(String[] args)',
    },
    'go': {
        'name': 'Go',
        'ext': '.go',
        'comment': '//',
        'const_keyword': 'const',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '==',
        'import_example': 'import "fmt"',
        'function_definition': 'func main()',
    },
    'rust': {
        'name': 'Rust',
        'ext': '.rs',
        'comment': '//',
        'const_keyword': 'const',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '==',
        'import_example': 'use std::io;',
        'function_definition': 'fn main()',
    },
    'javascript': {
        'name': 'JavaScript',
        'ext': '.js',
        'comment': '//',
        'const_keyword': 'const',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '===',
        'import_example': 'import React from "react";',
        'function_definition': 'function example() {}',
        'print_example': 'console.log("Hello")',
    },
    'python': {
        'name': 'Python',
        'ext': '.py',
        'comment': '#',
        'const_keyword': 'None',
        'bool_true': 'True',
        'bool_false': 'False',
        'equality': '==',
        'import_example': 'import math',
        'function_definition': 'def main():',
        'print_example': 'print("Hello")',
    },
    'nodejs': {
        'name': 'Node.js',
        'ext': '.js',
        'comment': '//',
        'const_keyword': 'const',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '===',
        'import_example': 'const fs = require("fs");',
        'function_definition': 'function main() {}',
        'print_example': 'console.log("Hello")',
    },
    'html': {
        'name': 'HTML',
        'ext': '.html',
    },
    'css': {
        'name': 'CSS',
        'ext': '.css',
    },
    'react': {
        'name': 'React',
        'ext': '.jsx',
    },
    'git': {
        'name': 'Git',
    },
    'github': {
        'name': 'GitHub',
    },
    'sql': {
        'name': 'SQL',
    },
    'typescript': {
        'name': 'TypeScript',
        'ext': '.ts',
        'comment': '//',
        'const_keyword': 'const',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '===',
        'import_example': 'import useState from "react";',
        'function_definition': 'function example(): void {}',
    },
    'php': {
        'name': 'PHP',
        'ext': '.php',
        'comment': '//',
        'const_keyword': 'const',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '==',
        'import_example': "include 'file.php';",
        'function_definition': 'function example() {}',
        'print_example': 'echo "Hello";',
    },
    'ruby': {
        'name': 'Ruby',
        'ext': '.rb',
        'comment': '#',
        'const_keyword': 'CONST',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '==',
        'import_example': "require 'json'",
        'function_definition': 'def example; end',
        'print_example': 'puts "Hello"',
    },
    'swift': {
        'name': 'Swift',
        'ext': '.swift',
        'comment': '//',
        'const_keyword': 'let',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '==',
        'import_example': 'import Foundation',
        'function_definition': 'func example() {}',
        'print_example': 'print("Hello")',
    },
    'kotlin': {
        'name': 'Kotlin',
        'ext': '.kt',
        'comment': '//',
        'const_keyword': 'val',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '==',
        'import_example': 'import kotlin.random.Random',
        'function_definition': 'fun main() {}',
        'print_example': 'println("Hello")',
    },
    'csharp': {
        'name': 'C#',
        'ext': '.cs',
        'comment': '//',
        'const_keyword': 'const',
        'bool_true': 'true',
        'bool_false': 'false',
        'equality': '==',
        'import_example': 'using System;',
        'function_definition': 'static void Main(string[] args) {}',
        'print_example': 'Console.WriteLine("Hello");',
    },
}

PROGRAMMING_CONTEXTS = [
    'source code', 'header files', 'library imports', 'loop logic', 'conditional logic',
    'function definitions', 'data types', 'memory management', 'input/output', 'error handling',
]

GIT_CONTEXTS = [
    'local repository', 'remote repository', 'staging area', 'branch history', 'working tree',
    'feature branch', 'main branch', 'merge conflicts', 'stash area', 'commit history',
]

GITHUB_CONTEXTS = [
    'repository', 'project board', 'workflow', 'documentation', 'security settings',
    'package registry', 'collaboration tools', 'issue tracker', 'pull requests', 'release notes',
]

HTML_CONTEXTS = [
    'web page', 'document head', 'content section', 'paragraph', 'table row',
    'link', 'image', 'list', 'navigation', 'form',
]

CSS_CONTEXTS = [
    'container', 'header', 'footer', 'main', 'nav',
    'card', 'form', 'button', 'image', 'content',
]

REACT_CONTEXTS = [
    'components', 'hooks', 'props', 'state', 'rendering',
    'context', 'memoization', 'event handling', 'lists', 'effects',
]

DOCKER_CONTEXTS = [
    'container', 'image', 'registry', 'Dockerfile', 'compose service',
    'network', 'volume', 'build cache', 'deployment', 'runtime',
]

MONGODB_CONTEXTS = [
    'document', 'collection', 'query', 'aggregation', 'index',
    'replica set', 'shard', 'schema', 'pipeline', 'cursor',
]

REDIS_CONTEXTS = [
    'cache', 'key-value store', 'pub/sub channel', 'memory', 'expiration',
    'hash', 'list', 'set', 'sorted set', 'database',
]

BASH_CONTEXTS = [
    'terminal', 'shell script', 'command line', 'environment variable',
    'pipe', 'redirection', 'file path', 'process', 'job control', 'argument',
]

TAILWIND_CONTEXTS = [
    'utility class', 'responsive layout', 'hover state', 'spacing',
    'typography', 'background', 'border', 'flexbox', 'grid', 'animation',
]

HTML_TAGS = ['div', 'span', 'p', 'a', 'section', 'article', 'nav', 'header', 'footer', 'img']
CSS_PROPERTIES = ['color', 'margin', 'padding', 'display', 'font-size', 'background', 'border', 'width', 'height', 'opacity']
REACT_HOOKS = ['useState', 'useEffect', 'useMemo', 'useCallback', 'useContext']
GIT_COMMANDS = ['git init', 'git clone', 'git add', 'git commit', 'git push', 'git pull', 'git branch', 'git checkout', 'git merge', 'git status']
GITHUB_FEATURES = ['Pull Request', 'Issue', 'Fork', 'Gist', 'Actions', 'Pages', 'Wiki', 'Release', 'Repository', 'Project']

RANDOM_ANSWERS = [
    'true', 'false', 'None', '0', '1', '===', '==', '!=', 'const', 'let', 'final', 'import',
    'class', 'def', 'function', 'for', 'while', 'if', 'public', 'private', 'static',
]


formatter = Formatter()

def format_fields(text, variant):
    parsed = list(formatter.parse(text))
    has_named = any(field_name for _, field_name, _, _ in parsed if field_name)
    return text.format(**variant) if has_named else text


def shuffle_options(correct, wrongs):
    options = wrongs.copy()
    options.append(correct)
    random.shuffle(options)
    correct_index = options.index(correct)
    return options, correct_index


def build_questions(lang, difficulty):
    meta = LANGUAGE_META[lang]
    name = meta['name']

    if lang == 'sql':
        return build_sql_questions(name, difficulty)
    if lang == 'git':
        return build_git_questions(name, difficulty)
    if lang == 'github':
        return build_github_questions(name, difficulty)
    if lang == 'html':
        return build_html_questions(name, difficulty)
    if lang == 'css':
        return build_css_questions(name, difficulty)
    if lang == 'react':
        return build_react_questions(name, difficulty)
    if lang == 'docker':
        return build_docker_questions(name, difficulty)
    if lang == 'mongodb':
        return build_mongodb_questions(name, difficulty)
    if lang == 'redis':
        return build_redis_questions(name, difficulty)
    if lang == 'bash':
        return build_bash_questions(name, difficulty)
    if lang == 'tailwind':
        return build_tailwind_questions(name, difficulty)

    return build_programming_questions(name, difficulty, meta)


def build_programming_questions(name, difficulty, meta):
    easy_templates = [
        (
            'Which file extension is standard for {name} {table}?',
            meta['ext'],
            ['.txt', '.md', '.json'],
        ),
        (
            'Which symbol begins a single-line comment in {name} {table}?',
            meta['comment'],
            [c for c in ['//', '#', '/* */', '<!-- -->'] if c != meta['comment']][:3],
        ),
        (
            'Which keyword declares a constant value in {name} {table}?',
            meta['const_keyword'],
            ['let', 'var', 'static'],
        ),
        (
            'Which value is commonly used for true in {name} {table}?',
            meta['bool_true'],
            [b for b in ['true', 'false', 'True', 'False', '0', '1'] if b != meta['bool_true']][:3],
        ),
        (
            'Which operator checks equality in {name} {table}?',
            meta['equality'],
            [o for o in ['==', '===', '=', '!='] if o != meta['equality']][:3],
        ),
        (
            'Which phrase describes the main function signature in {name} {table}?',
            meta['function_definition'],
            ['main()', 'function main() {}', 'def main():'],
        ),
        (
            'Which keyword begins a loop in {name} {table}?',
            'for',
            ['while', 'loop', 'repeat'],
        ),
        (
            'Which value represents false in {name} {table}?',
            meta['bool_false'],
            [b for b in ['true', 'false', 'True', 'False', '0', '1'] if b != meta['bool_false']][:3],
        ),
        (
            'Which sign is used to assign values in {name} {table}?',
            '=',
            ['==', ':=', '=>'],
        ),
        (
            'Which statement imports libraries or packages in {name} {table}?',
            meta['import_example'],
            ['require("lib")', 'include <lib>', 'use lib;'],
        ),
        (
            'Which code line prints "Hello" in {name} {table}?',
            meta.get('print_example', 'print("Hello")'),
            ['console.log("Hello")', 'echo "Hello";', 'puts "Hello"'],
        ),
        (
            'What is the result of 3 + 4 in {name} {table}?',
            '7',
            ['34', 'Error', '0'],
        ),
        (
            'Which code line correctly declares a constant in {name} {table}?',
            meta['const_keyword'],
            ['let', 'var', 'static'],
        ),
        (
            'Which value is produced by 2 * 5 in {name} {table}?',
            '10',
            ['25', '2', '0'],
        ),
        (
            'Which code line uses string concatenation in {name} {table}?',
            '"Hello" + "World"',
            ['"Hello" . "World"', 'concat("Hello", "World")', 'join("Hello", "World")'],
        ),
        (
            'Which option fills the blank in {name} {table}: {const_keyword} x = 5; x = 10; // __? ',
            'assignment',
            ['declaration', 'comparison', 'iteration'],
        ),
        (
            'What is the result of 8 - 3 in {name} {table}?',
            '5',
            ['3', '8', '2'],
        ),
        (
            'Which concept describes reusable code blocks in {name} {table}?',
            'functions',
            ['classes', 'variables', 'comments'],
        ),
        (
            'Which keyword is used to exit a loop early in {name} {table}?',
            'break',
            ['continue', 'return', 'stop'],
        ),
    ]

    medium_templates = [
        (
            'Which keyword declares a function in {name} {table}?',
            'def' if name == 'Python' else 'function' if name in ['JavaScript', 'Node.js'] else 'public static void' if name == 'Java' else 'func' if name == 'Go' else 'fn' if name == 'Rust' else 'int',
            ['class', 'var', 'const'],
        ),
        (
            'Which keyword starts a conditional expression in {name} {table}?',
            'if',
            ['when', 'switch', 'case'],
        ),
        (
            'Which operator is used to compare two values in {name} {table}?',
            meta['equality'],
            [o for o in ['==', '===', '!=', '<>'] if o != meta['equality']][:3],
        ),
        (
            'Which structure is often used for repeated execution in {name} {table}?',
            'for',
            ['if', 'switch', 'case'],
        ),
        (
            'Which keyword defines a function or method name in {name} {table}?',
            'function' if name in ['JavaScript', 'Node.js', 'React'] else 'def' if name == 'Python' else 'pub fn' if name == 'Rust' else 'func' if name == 'Go' else 'void' if name == 'Java' else 'int',
            ['class', 'struct', 'module'],
        ),
        (
            'Which line represents a valid import or include in {name} {table}?',
            meta['import_example'],
            ['include <sys>', 'import module', 'require("module")'],
        ),
        (
            'Which term often describes a collection of values in {name} {table}?',
            'array',
            ['object', 'class', 'function'],
        ),
        (
            'Which keyword in {name} creates a new variable in {table}?',
            'var' if name in ['JavaScript', 'Node.js'] else 'let' if name == 'Go' else 'int' if name in ['C', 'C++', 'Java'] else 'def' if name == 'Python' else 'let',
            ['const', 'static', 'class'],
        ),
        (
            'Which operator in {name} is used for string concatenation in {table}?',
            '+' if name not in ['Python'] else '+',
            ['&', '||', '##'],
        ),
        (
            'Which keyword in {name} indicates a return value from a function in {table}?',
            'return',
            ['yield', 'break', 'exit'],
        ),
        (
            'Which value is the result of 4 * 2 in {name} {table}?',
            '8',
            ['6', '16', '2'],
        ),
        (
            'Which term describes a variable whose value cannot change after assignment in {name} {table}?',
            'immutable',
            ['dynamic', 'mutable', 'temporary'],
        ),
        (
            'Which line represents a correct function definition in {name} {table}?',
            meta['function_definition'],
            ['main() {}', 'function main', 'def main'],
        ),
        (
            'Which concept means solving a problem by calling the same function inside itself in {name} {table}?',
            'recursion',
            ['iteration', 'compilation', 'optimization'],
        ),
    ]

    hard_templates = [
        (
            'Which statement best describes memory management in {name} {table}?',
            'manual allocation and free' if name in ['C', 'C++'] else 'automatic garbage collection',
            ['implicit typing', 'runtime binding', 'syntax highlighting'],
        ),
        (
            'Which feature is commonly used for concurrency in {name} applications in {table}?',
            'threads' if name in ['Java', 'C', 'C++'] else 'async/await' if name in ['JavaScript', 'Python', 'Node.js'] else 'goroutines' if name == 'Go' else 'async tasks',
            ['closures', 'generics', 'inheritance'],
        ),
        (
            'Which keyword indicates an immutable value in {name} code in {table}?',
            meta['const_keyword'],
            ['var', 'let', 'mutable'],
        ),
        (
            'Which statement checks for equality in {name} {table}?',
            meta['equality'],
            ['=', '=>', ':='],
        ),
        (
            'Which concept ensures a variable keeps its state across function calls in {name} {table}?',
            'static',
            ['volatile', 'dynamic', 'transient'],
        ),
        (
            'Which keyword defines a class in {name} {table}?',
            'class' if name in ['Java', 'Python'] else 'struct' if name in ['C', 'C++', 'Rust'] else 'function',
            ['module', 'package', 'namespace'],
        ),
        (
            'Which mechanism helps avoid null reference errors in {name} {table}?',
            'optional types' if name in ['Swift', 'Rust', 'Java'] else 'None handling',
            ['global variables', 'inheritance', 'exceptions'],
        ),
        (
            'Which term describes code reuse through a function call in {name} {table}?',
            'modularity',
            ['polymorphism', 'encapsulation', 'abstraction'],
        ),
        (
            'Which relationship lets one type inherit behavior from another in {name} {table}?',
            'inheritance',
            ['composition', 'aggregation', 'delegation'],
        ),
        (
            'Which data structure is fastest for random access by index in {name} {table}?',
            'array',
            ['linked list', 'stack', 'queue'],
        ),
    ]

    variants = [
        {
            'index': i,
            'table': PROGRAMMING_CONTEXTS[i % len(PROGRAMMING_CONTEXTS)],
            'property': CSS_PROPERTIES[i % len(CSS_PROPERTIES)],
            'tag': HTML_TAGS[i % len(HTML_TAGS)],
            'hook': REACT_HOOKS[i % len(REACT_HOOKS)],
            'command': GIT_COMMANDS[i % len(GIT_COMMANDS)],
            'feature': GITHUB_FEATURES[i % len(GITHUB_FEATURES)],
            'name': name,
            **meta,
        }
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_sql_questions(name, difficulty):
    easy_questions = [
        ('What does the SQL SELECT statement do?', 'Retrieve data from a table', ['Delete rows from a table', 'Create a new table', 'Insert data into a table']),
        ('Which SQL keyword deletes rows from a table?', 'DELETE', ['DROP', 'REMOVE', 'TRUNCATE']),
        ('Which SQL clause filters rows using a condition?', 'WHERE', ['GROUP BY', 'ORDER BY', 'HAVING']),
        ('Which SQL statement inserts new rows into a table?', 'INSERT INTO', ['SELECT', 'UPDATE', 'DELETE']),
        ('Which SQL clause orders rows in a query result?', 'ORDER BY', ['GROUP BY', 'WHERE', 'LIMIT']),
        ('Which SQL clause limits the number of returned rows?', 'LIMIT', ['OFFSET', 'TOP', 'FETCH']),
        ('Which SQL keyword updates existing rows in a table?', 'UPDATE', ['ALTER', 'SET', 'MODIFY']),
        ('Which SQL clause groups rows that share common values?', 'GROUP BY', ['ORDER BY', 'WHERE', 'UNION']),
        ('Which SQL statement creates a new table?', 'CREATE TABLE', ['INSERT TABLE', 'ADD TABLE', 'MAKE TABLE']),
        ('Which SQL keyword removes a table completely?', 'DROP TABLE', ['DELETE TABLE', 'TRUNCATE TABLE', 'REMOVE TABLE']),
        ('Which SQL keyword returns only unique values from a column?', 'DISTINCT', ['ALL', 'UNIQUE', 'SAME']),
        ('Which SQL operator checks for equality between values?', '=', ['!=', '<>', 'LIKE']),
        ('Which SQL function counts the number of rows?', 'COUNT()', ['SUM()', 'AVG()', 'MAX()']),
        ('Which SQL clause specifies the source table for a SELECT query?', 'FROM', ['WHERE', 'JOIN', 'SELECT']),
        ('Which SQL keyword is used to match a pattern in text data?', 'LIKE', ['MATCH', 'IN', 'BETWEEN']),
        ('Which SQL keyword adds a new column to an existing table?', 'ADD COLUMN', ['CREATE COLUMN', 'ALTER ROW', 'INSERT COLUMN']),
        ('Which SQL keyword changes the structure of a table?', 'ALTER TABLE', ['UPDATE TABLE', 'DROP TABLE', 'CREATE TABLE']),
        ('Which SQL keyword removes all rows from a table but keeps the structure?', 'TRUNCATE TABLE', ['DELETE FROM', 'DROP TABLE', 'REMOVE TABLE']),
        ('Which SQL keyword starts a transaction block?', 'BEGIN', ['START', 'OPEN', 'INIT']),
        ('Which SQL command saves changes made in a transaction?', 'COMMIT', ['ROLLBACK', 'SAVE', 'END']),
        ('Which SQL command undoes changes made since the last COMMIT?', 'ROLLBACK', ['COMMIT', 'SAVEPOINT', 'REVERT']),
        ('Which SQL operator combines conditions requiring both to be true?', 'AND', ['OR', 'NOT', 'XOR']),
        ('Which SQL operator combines conditions where either may be true?', 'OR', ['AND', 'NOT', 'XOR']),
        ('Which SQL clause renames a column in query results?', 'AS', ['ALIAS', 'RENAME', 'LABEL']),
        ('Which SQL clause sets the output order to descending?', 'DESC', ['ASC', 'ORDER BY', 'REVERSE']),
        ('Which SQL keyword prevents null values in a column?', 'NOT NULL', ['UNIQUE', 'DEFAULT', 'CHECK']),
        ('Which SQL function returns the greater of two values?', 'GREATEST()', ['MAX()', 'LARGEST()', 'HIGHEST()']),
        ('Which SQL keyword creates a view?', 'CREATE VIEW', ['CREATE TABLE', 'CREATE INDEX', 'CREATE DATABASE']),
        ('Which SQL type stores whole numbers?', 'INTEGER', ['VARCHAR', 'TEXT', 'FLOAT']),
        ('Which SQL keyword changes the name of a column?', 'ALTER TABLE ... RENAME COLUMN', ['ALTER TABLE ... ADD COLUMN', 'RENAME COLUMN', 'UPDATE COLUMN']),
        ('Which SQL keyword retrieves only matching rows from two tables?', 'INNER JOIN', ['LEFT JOIN', 'RIGHT JOIN', 'FULL JOIN']),
        ('Which SQL keyword tests whether a value is within a list?', 'IN', ['BETWEEN', 'LIKE', 'EXISTS']),
        ('Which SQL value represents missing or unknown data?', 'NULL', ['NONE', '0', 'EMPTY']),
        ('Which SQL clause filters groups after aggregation?', 'HAVING', ['WHERE', 'ORDER BY', 'GROUP BY']),
        ('Which SQL keyword creates an index on a column?', 'CREATE INDEX', ['ALTER INDEX', 'ADD INDEX', 'INDEX COLUMN']),
        ('Which SQL type stores variable-length text?', 'VARCHAR', ['INT', 'TEXT', 'CHAR']),
        ('Which SQL keyword deletes rows while keeping the table?', 'DELETE FROM', ['TRUNCATE TABLE', 'DROP TABLE', 'REMOVE TABLE']),
        ('Which SQL keyword gives a column a default value?', 'DEFAULT', ['SET', 'ASSIGN', 'VALUE']),
        ('Which SQL function returns string length?', 'LENGTH()', ['SIZE()', 'COUNT()', 'LEN()']),
        ('Which SQL keyword removes an index?', 'DROP INDEX', ['DELETE INDEX', 'REMOVE INDEX', 'ALTER INDEX']),
        ('Which SQL keyword defines a foreign key relationship?', 'FOREIGN KEY', ['PRIMARY KEY', 'CHECK', 'UNIQUE']),
        ('Which SQL clause orders rows in ascending order?', 'ASC', ['DESC', 'ORDER BY', 'REVERSE']),
        ('Which SQL statement creates a new database?', 'CREATE DATABASE', ['CREATE SCHEMA', 'CREATE TABLE', 'CREATE VIEW']),
        ('Which SQL statement removes a database?', 'DROP DATABASE', ['DELETE DATABASE', 'REMOVE DATABASE', 'TRUNCATE DATABASE']),
        ('Which SQL keyword combines results and removes duplicates?', 'UNION', ['UNION ALL', 'INTERSECT', 'EXCEPT']),
        ('Which SQL keyword preserves duplicate rows in combined results?', 'UNION ALL', ['UNION', 'INTERSECT', 'EXCEPT']),
        ('Which SQL keyword starts a common table expression?', 'WITH', ['FROM', 'JOIN', 'INTO']),
        ('Which SQL keyword creates a temporary table for the session?', 'CREATE TEMPORARY TABLE', ['CREATE TABLE', 'CREATE GLOBAL TEMPORARY TABLE', 'CREATE PERMANENT TABLE']),
        ('Which SQL function returns the current date?', 'CURRENT_DATE', ['NOW()', 'TODAY()', 'SYSDATE']),
        ('Which SQL function returns the current date and time?', 'NOW()', ['CURRENT_DATE', 'TODAY()', 'SYSDATE']),
        ('Which SQL keyword defines a unique value in a column?', 'UNIQUE', ['PRIMARY KEY', 'NOT NULL', 'CHECK']),
        ('Which SQL clause creates a join condition?', 'ON', ['WHERE', 'USING', 'HAVING']),
        ('Which SQL clause compares values against a range?', 'BETWEEN', ['IN', 'LIKE', 'EXISTS']),
        ('Which SQL keyword checks if a value is null?', 'IS NULL', ['= NULL', 'IS NOT NULL', 'NULL']),
        ('Which SQL statement removes a column from a table?', 'ALTER TABLE ... DROP COLUMN', ['ALTER TABLE ... ADD COLUMN', 'DROP TABLE', 'DELETE COLUMN']),
        ('Which SQL keyword calculates distinct row counts?', 'COUNT(DISTINCT column)', ['COUNT(column)', 'SUM(column)', 'AVG(column)']),
        ('Which SQL keyword creates a sequence for unique values?', 'CREATE SEQUENCE', ['CREATE INDEX', 'CREATE TABLE', 'CREATE VIEW']),
        ('Which SQL clause groups rows before aggregation?', 'GROUP BY', ['HAVING', 'WHERE', 'ORDER BY']),
        ('Which SQL keyword defines a primary key?', 'PRIMARY KEY', ['UNIQUE', 'FOREIGN KEY', 'CHECK']),
        ('Which SQL statement changes a table column to have a default value?', 'ALTER TABLE ... ALTER COLUMN', ['ALTER TABLE ... CHANGE COLUMN', 'ALTER TABLE ... ADD COLUMN', 'ALTER TABLE ... MODIFY COLUMN']),
    ]

    medium_questions = [
        ('Which SQL join returns only rows with matching values in both tables?', 'INNER JOIN', ['LEFT JOIN', 'RIGHT JOIN', 'FULL OUTER JOIN']),
        ('Which SQL join returns all rows from the left table and matching rows from the right?', 'LEFT JOIN', ['INNER JOIN', 'RIGHT JOIN', 'FULL OUTER JOIN']),
        ('Which SQL join returns all rows from the right table and matching rows from the left?', 'RIGHT JOIN', ['INNER JOIN', 'LEFT JOIN', 'FULL OUTER JOIN']),
        ('Which SQL join returns matching rows plus unmatched rows from both tables?', 'FULL OUTER JOIN', ['INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN']),
        ('Which SQL join combines rows from every row in two tables?', 'CROSS JOIN', ['INNER JOIN', 'LEFT JOIN', 'FULL OUTER JOIN']),
        ('Which SQL join automatically matches columns with the same names?', 'NATURAL JOIN', ['INNER JOIN', 'USING', 'RIGHT JOIN']),
        ('Which SQL clause specifies join conditions between tables?', 'ON', ['USING', 'WHERE', 'HAVING']),
        ('Which SQL clause simplifies joins using common column names?', 'USING', ['ON', 'WHERE', 'JOIN']),
        ('Which SQL clause filters groups after aggregation?', 'HAVING', ['WHERE', 'ORDER BY', 'GROUP BY']),
        ('Which SQL clause groups rows before aggregation?', 'GROUP BY', ['ORDER BY', 'WHERE', 'HAVING']),
        ('Which SQL clause orders results by one or more columns?', 'ORDER BY', ['GROUP BY', 'WHERE', 'HAVING']),
        ('Which SQL keyword removes duplicate rows from a result set?', 'DISTINCT', ['UNION', 'ALL', 'UNIQUE']),
        ('Which SQL keyword keeps duplicate rows when combining queries?', 'UNION ALL', ['UNION', 'INTERSECT', 'EXCEPT']),
        ('Which SQL keyword returns rows common to two queries?', 'INTERSECT', ['UNION', 'EXCEPT', 'JOIN']),
        ('Which SQL keyword returns rows from the first query that are not in the second?', 'EXCEPT', ['UNION', 'INTERSECT', 'MINUS']),
        ('Which SQL clause compares a value to a range?', 'BETWEEN', ['IN', 'LIKE', 'EXISTS']),
        ('Which SQL keyword checks if a value is null?', 'IS NULL', ['= NULL', 'IS NOT NULL', 'NULL']),
        ('Which SQL keyword checks if a value is not null?', 'IS NOT NULL', ['IS NULL', '= NULL', 'NOT NULL']),
        ('Which SQL operator tests for the existence of rows from a subquery?', 'EXISTS', ['IN', 'BETWEEN', 'ANY']),
        ('Which SQL keyword tests if any row satisfies a subquery?', 'ANY', ['ALL', 'IN', 'EXISTS']),
        ('Which SQL keyword tests if all rows satisfy a subquery?', 'ALL', ['ANY', 'EXISTS', 'IN']),
        ('Which SQL expression chooses values based on conditions?', 'CASE WHEN', ['IF', 'SWITCH', 'SELECT CASE']),
        ('Which SQL function converts a value to a different type?', 'CAST()', ['CONVERT()', 'FORMAT()', 'TO_CHAR()']),
        ('Which SQL function returns the first non-null value?', 'COALESCE', ['NVL', 'IFNULL', 'ISNULL']),
        ('Which SQL function returns NULL when two values are equal?', 'NULLIF', ['COALESCE', 'IFNULL', 'CASE WHEN']),
        ('Which SQL function counts distinct values in a column?', 'COUNT(DISTINCT column)', ['COUNT(column)', 'SUM(column)', 'AVG(column)']),
        ('Which SQL keyword creates a new index on a table?', 'CREATE INDEX', ['ADD INDEX', 'INDEX TABLE', 'MAKE INDEX']),
        ('Which SQL keyword deletes an existing index?', 'DROP INDEX', ['DELETE INDEX', 'REMOVE INDEX', 'ALTER INDEX']),
        ('Which SQL statement adds a new column to a table?', 'ALTER TABLE ... ADD COLUMN', ['INSERT COLUMN', 'CREATE COLUMN', 'ALTER TABLE ... CHANGE COLUMN']),
        ('Which SQL statement removes a column from a table?', 'ALTER TABLE ... DROP COLUMN', ['ALTER TABLE ... ADD COLUMN', 'DROP COLUMN', 'DELETE COLUMN']),
        ('Which SQL statement renames a column in a table?', 'ALTER TABLE ... RENAME COLUMN', ['RENAME COLUMN', 'ALTER COLUMN ... RENAME', 'CHANGE COLUMN']),
        ('Which SQL keyword creates a sequence for generating unique values?', 'CREATE SEQUENCE', ['CREATE INDEX', 'CREATE TABLE', 'CREATE VIEW']),
        ('Which SQL statement creates a stored procedure?', 'CREATE PROCEDURE', ['CREATE FUNCTION', 'CREATE TRIGGER', 'CREATE VIEW']),
        ('Which SQL statement creates a stored function?', 'CREATE FUNCTION', ['CREATE PROCEDURE', 'CREATE TRIGGER', 'CREATE VIEW']),
        ('Which SQL statement shows table definitions in MySQL?', 'DESCRIBE', ['SHOW', 'EXPLAIN', 'SELECT']),
        ('Which SQL statement explains the execution plan for a query?', 'EXPLAIN', ['DESCRIBE', 'ANALYZE', 'SHOW PLAN']),
        ('Which SQL statement lists tables in the current database?', 'SHOW TABLES', ['LIST TABLES', 'DESCRIBE TABLES', 'SELECT FROM INFORMATION_SCHEMA']),
        ('Which SQL statement creates a temporary table for a session?', 'CREATE TEMPORARY TABLE', ['CREATE TABLE', 'CREATE GLOBAL TEMPORARY TABLE', 'CREATE PERMANENT TABLE']),
        ('Which SQL command creates a savepoint inside a transaction?', 'SAVEPOINT', ['COMMIT', 'ROLLBACK', 'SET TRANSACTION']),
        ('Which SQL command rolls back to a savepoint?', 'ROLLBACK TO SAVEPOINT', ['ROLLBACK', 'SAVEPOINT', 'COMMIT']),
        ('Which SQL keyword creates a new trigger on a table?', 'CREATE TRIGGER', ['CREATE PROCEDURE', 'CREATE FUNCTION', 'CREATE EVENT']),
        ('Which SQL keyword creates a read-only view?', 'CREATE VIEW', ['CREATE TABLE', 'CREATE INDEX', 'CREATE SCHEMA']),
        ('Which SQL keyword starts a common table expression?', 'WITH', ['FROM', 'JOIN', 'INTO']),
        ('Which SQL function returns the current date and time?', 'NOW()', ['CURRENT_DATE', 'CURRENT_TIMESTAMP', 'SYSDATE']),
        ('Which SQL function returns the current date?', 'CURRENT_DATE', ['NOW()', 'CURRENT_TIMESTAMP', 'TODAY()']),
        ('Which SQL function returns the current timestamp?', 'CURRENT_TIMESTAMP', ['NOW()', 'CURRENT_DATE', 'SYSDATE']),
        ('Which SQL function removes whitespace from both ends of a string?', 'TRIM()', ['RTRIM()', 'LTRIM()', 'CLEAN()']),
        ('Which SQL function returns a substring from a string?', 'SUBSTRING()', ['LEFT()', 'RIGHT()', 'MID()']),
        ('Which SQL function concatenates strings?', 'CONCAT()', ['JOIN()', 'MERGE()', 'ADDSTR()']),
        ('Which SQL function rounds a numeric value?', 'ROUND()', ['FLOOR()', 'CEIL()', 'TRUNC()']),
        ('Which SQL clause filters rows inside an aggregate function?', 'FILTER', ['HAVING', 'WHERE', 'GROUP BY']),
        ('Which SQL statement changes a table column definition?', 'ALTER TABLE', ['UPDATE TABLE', 'MODIFY TABLE', 'CHANGE TABLE']),
        ('Which SQL keyword defines a primary key?', 'PRIMARY KEY', ['UNIQUE', 'FOREIGN KEY', 'CHECK']),
        ('Which SQL keyword enforces a range constraint on a column?', 'CHECK', ['UNIQUE', 'NOT NULL', 'DEFAULT']),
        ('Which SQL keyword defines a foreign key constraint?', 'FOREIGN KEY', ['PRIMARY KEY', 'UNIQUE', 'CHECK']),
    ]

    hard_questions = [
        ('Which SQL keyword returns rows that exist in one query but not another?', 'EXCEPT', ['UNION', 'INTERSECT', 'MINUS']),
        ('Which SQL operator checks whether a value matches a pattern using wildcards?', 'LIKE', ['IN', 'BETWEEN', 'MATCH']),
        ('Which SQL keyword tests whether a value exists in a list?', 'IN', ['LIKE', 'EXISTS', 'BETWEEN']),
        ('Which SQL operator tests for the existence of rows in a subquery?', 'EXISTS', ['IN', 'ANY', 'SOME']),
        ('Which SQL function returns the first non-null value from its arguments?', 'COALESCE', ['IFNULL', 'NULLIF', 'NVL']),
        ('Which SQL statement creates a temporary table for the session?', 'CREATE TEMPORARY TABLE', ['CREATE TABLE', 'CREATE TEMP TABLE', 'CREATE GLOBAL TEMPORARY TABLE']),
        ('Which SQL keyword sets a column to reject null values?', 'NOT NULL', ['NULL', 'DEFAULT', 'UNIQUE']),
        ('Which SQL statement adds a primary key constraint to a table?', 'ALTER TABLE ... ADD PRIMARY KEY', ['ALTER TABLE ... ADD UNIQUE', 'CREATE TABLE ... PRIMARY KEY', 'ALTER TABLE ... ADD CONSTRAINT']),
        ('Which SQL keyword enforces that values in a column are unique?', 'UNIQUE', ['PRIMARY KEY', 'NOT NULL', 'CHECK']),
        ('Which SQL constraint links a column to another table\'s primary key?', 'FOREIGN KEY', ['PRIMARY KEY', 'UNIQUE', 'CHECK']),
        ('Which SQL clause sorts results in descending order?', 'DESC', ['ASC', 'ORDER BY', 'SORT BY']),
        ('Which SQL clause sorts results in ascending order?', 'ASC', ['DESC', 'ORDER BY', 'SORT BY']),
        ('Which SQL statement removes a database?', 'DROP DATABASE', ['DELETE DATABASE', 'REMOVE DATABASE', 'TRUNCATE DATABASE']),
        ('Which SQL keyword prevents duplicate rows in a combined result?', 'UNION', ['UNION ALL', 'INTERSECT', 'EXCEPT']),
        ('Which SQL keyword preserves duplicate rows in a combined result?', 'UNION ALL', ['UNION', 'INTERSECT', 'EXCEPT']),
        ('Which SQL command reverts all changes in the current transaction?', 'ROLLBACK', ['COMMIT', 'SAVEPOINT', 'END TRANSACTION']),
        ('Which SQL keyword defines a constraint that a value must be within a range?', 'CHECK', ['UNIQUE', 'NOT NULL', 'DEFAULT']),
        ('Which SQL statement creates a new stored procedure?', 'CREATE PROCEDURE', ['CREATE FUNCTION', 'CREATE TRIGGER', 'CREATE VIEW']),
        ('Which SQL keyword allows a query to refer to the same table twice?', 'SELF JOIN', ['CROSS JOIN', 'NATURAL JOIN', 'INNER JOIN']),
        ('Which SQL function returns the current date and time?', 'NOW()', ['CURRENT_DATE', 'SYSDATE', 'GETDATE()']),
        ('Which SQL statement renames a table?', 'ALTER TABLE ... RENAME TO', ['RENAME TABLE', 'CHANGE TABLE', 'MODIFY TABLE']),
        ('Which SQL clause is used to limit rows for pagination in MySQL?', 'LIMIT', ['OFFSET', 'FETCH', 'TOP']),
        ('Which SQL keyword creates a compound primary key?', 'PRIMARY KEY', ['UNIQUE', 'FOREIGN KEY', 'CHECK']),
        ('Which SQL clause defines an alias for a table?', 'AS', ['ALIAS', 'RENAME', 'LABEL']),
        ('Which SQL keyword defines a row-level security policy?', 'POLICY', ['SECURITY', 'RULE', 'CONSTRAINT']),
        ('Which SQL command creates a stored function in MySQL?', 'CREATE FUNCTION', ['CREATE PROCEDURE', 'CREATE TRIGGER', 'CREATE VIEW']),
        ('Which SQL clause is used to order rows before applying OFFSET?', 'ORDER BY', ['WHERE', 'GROUP BY', 'LIMIT']),
        ('Which SQL keyword is used to create a read-only view?', 'CREATE VIEW', ['CREATE TABLE', 'CREATE INDEX', 'CREATE SCHEMA']),
        ('Which SQL clause is used to compare pattern-matching conditions?', 'LIKE', ['IN', 'BETWEEN', 'EXISTS']),
        ('Which SQL statement removes only rows that meet a condition?', 'DELETE', ['DROP', 'TRUNCATE', 'REMOVE']),
        ('Which SQL keyword defines a foreign key reference in a table?', 'FOREIGN KEY', ['PRIMARY KEY', 'UNIQUE', 'CHECK']),
        ('Which SQL expression adds a label for an expression in query output?', 'AS', ['LABEL', 'NAME', 'ALIAS']),
        ('Which SQL keyword forces a join to include all rows from both tables?', 'FULL OUTER JOIN', ['INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN']),
        ('Which SQL function converts a string to uppercase?', 'UPPER()', ['LOWER()', 'INITCAP()', 'TITLE()']),
        ('Which SQL function extracts part of a string?', 'SUBSTRING()', ['TRIM()', 'CONCAT()', 'LENGTH()']),
        ('Which SQL clause defines a window for analytic functions?', 'OVER', ['PARTITION BY', 'ORDER BY', 'GROUP BY']),
        ('Which SQL statement removes a constraint from a table?', 'ALTER TABLE ... DROP CONSTRAINT', ['ALTER TABLE ... REMOVE CONSTRAINT', 'DROP CONSTRAINT', 'DELETE CONSTRAINT']),
        ('Which SQL keyword creates a unique index?', 'CREATE UNIQUE INDEX', ['CREATE INDEX', 'CREATE TABLE', 'CREATE CONSTRAINT']),
        ('Which SQL function returns the integer part of a number?', 'FLOOR()', ['ROUND()', 'CEIL()', 'TRUNC()']),
        ('Which SQL statement refreshes a materialized view?', 'REFRESH MATERIALIZED VIEW', ['ALTER MATERIALIZED VIEW', 'UPDATE MATERIALIZED VIEW', 'REBUILD MATERIALIZED VIEW']),
        ('Which SQL clause defines a recursive common table expression?', 'WITH RECURSIVE', ['WITH', 'WITH CTE', 'WITH REPEAT']),
        ('Which SQL keyword indicates that a column value is generated automatically?', 'GENERATED ALWAYS AS IDENTITY', ['AUTO_INCREMENT', 'SERIAL', 'IDENTITY']),
        ('Which SQL keyword creates a materialized view?', 'CREATE MATERIALIZED VIEW', ['CREATE VIEW', 'CREATE TABLE', 'CREATE TEMP TABLE']),
        ('Which SQL keyword is used to merge rows from a source into a target table?', 'MERGE', ['UPDATE', 'INSERT', 'UPSERT']),
        ('Which SQL clause produces subtotal rows for grouped data?', 'ROLLUP', ['GROUP BY', 'CUBE', 'GROUPING SETS']),
        ('Which SQL clause produces all combinations of grouping columns?', 'CUBE', ['ROLLUP', 'GROUP BY', 'GROUPING SETS']),
        ('Which SQL clause specifies subsets of groupings?', 'GROUPING SETS', ['ROLLUP', 'CUBE', 'GROUP BY']),
        ('Which SQL function aggregates rows into a JSON array?', 'JSON_AGG()', ['ARRAY_AGG()', 'GROUP_CONCAT()', 'JSON_ARRAYAGG()']),
        ('Which SQL function aggregates rows into an array?', 'ARRAY_AGG()', ['JSON_AGG()', 'LISTAGG()', 'GROUP_CONCAT()']),
        ('Which SQL function concatenates strings from grouped rows?', 'STRING_AGG()', ['CONCAT()', 'GROUP_CONCAT()', 'LISTAGG()']),
        ('Which SQL clause filters within an aggregate function?', 'FILTER', ['HAVING', 'WHERE', 'GROUP BY']),
        ('Which SQL function returns the difference between two timestamps?', 'AGE()', ['DATEDIFF()', 'TIMEDIFF()', 'DATE_DIFF()']),
        ('Which SQL function truncates a date to a specified precision?', 'DATE_TRUNC()', ['TRUNC()', 'TRUNCATE()', 'DATE_TRUNCATE()']),
        ('Which SQL clause defines a partition for window functions?', 'PARTITION BY', ['ORDER BY', 'OVER', 'GROUP BY']),
        ('Which SQL statement creates a trigger to respond to table events?', 'CREATE TRIGGER', ['CREATE PROCEDURE', 'CREATE FUNCTION', 'CREATE EVENT']),
    ]

    questions_source = easy_questions if difficulty == 'easy' else medium_questions if difficulty == 'medium' else hard_questions
    questions = []
    for question, correct, wrongs in questions_source:
        options, correct_index = shuffle_options(correct, wrongs)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_git_questions(name, difficulty):
    easy_templates = [
        ('Which {name} command initializes a new repository in {table}?', 'git init', ['git clone', 'git add', 'git pull']),
        ('Which {name} command makes a copy of a remote repository locally in {table}?', 'git clone', ['git init', 'git push', 'git fetch']),
        ('Which {name} command adds changes to the staging area in {table}?', 'git add', ['git commit', 'git push', 'git checkout']),
        ('Which {name} command saves staged changes as a new commit in {table}?', 'git commit', ['git add', 'git push', 'git status']),
        ('Which {name} command shows the status of working tree changes in {table}?', 'git status', ['git log', 'git diff', 'git push']),
        ('Which {name} command creates a new branch in {table}?', 'git branch', ['git checkout', 'git merge', 'git pull']),
        ('Which {name} command switches to another branch in {table}?', 'git checkout', ['git branch', 'git merge', 'git pull']),
        ('Which {name} command uploads commits to a remote repository from {table}?', 'git push', ['git pull', 'git fetch', 'git commit']),
        ('Which {name} command downloads changes from a remote repository into {table}?', 'git pull', ['git push', 'git fetch', 'git merge']),
        ('Which {name} command shows differences between commits in {table}?', 'git diff', ['git log', 'git status', 'git show']),
    ]

    medium_templates = [
        ('Which {name} command creates a new commit with a message in {table}?', 'git commit -m', ['git add -m', 'git save -m', 'git push -m']),
        ('Which {name} command fetches changes from the remote without merging in {table}?', 'git fetch', ['git pull', 'git push', 'git merge']),
        ('Which {name} command merges another branch into the current branch in {table}?', 'git merge', ['git rebase', 'git pull', 'git push']),
        ('Which {name} command creates a local branch and switches to it in {table}?', 'git checkout -b', ['git branch -b', 'git switch -c', 'git create -b']),
        ('Which {name} command lists existing branches in {table}?', 'git branch', ['git list', 'git show-branch', 'git branch -a']),
        ('Which {name} command discards unstaged changes in the working tree in {table}?', 'git checkout --', ['git reset --hard', 'git stash', 'git clean']),
        ('Which {name} command stores local changes temporarily in {table}?', 'git stash', ['git commit', 'git push', 'git branch']),
        ('Which {name} command shows commit history in {table}?', 'git log', ['git status', 'git diff', 'git show']),
        ('Which {name} command removes a tracked file from the index in {table}?', 'git rm', ['git remove', 'git delete', 'git reset']),
        ('Which {name} command applies stashed changes back to the working tree in {table}?', 'git stash pop', ['git stash apply', 'git pop', 'git apply']),
    ]

    hard_templates = [
        ('Which {name} command resets the working tree to the last commit and discards changes in {table}?', 'git reset --hard', ['git revert', 'git stash pop', 'git clean']),
        ('Which {name} command rewrites commits on top of another base branch in {table}?', 'git rebase', ['git merge', 'git reset', 'git checkout']),
        ('Which {name} command compares two branches for differences in {table}?', 'git diff branch1..branch2', ['git log branch1..branch2', 'git status branch1..branch2', 'git compare branch1..branch2']),
        ('Which {name} command lists all remote repositories in {table}?', 'git remote -v', ['git remotes', 'git repo -v', 'git ls-remote']),
        ('Which {name} command restores deleted files from the index in {table}?', 'git checkout --', ['git restore --', 'git add --', 'git reset --']),
        ('Which {name} command creates a tag at the current commit in {table}?', 'git tag', ['git label', 'git mark', 'git release']),
        ('Which {name} command removes untracked files from the working tree in {table}?', 'git clean -f', ['git rm -f', 'git reset --hard', 'git stash clear']),
        ('Which {name} command shows a graphical commit history in {table}?', 'git log --graph', ['git diff --graph', 'git show --graph', 'git status --graph']),
        ('Which {name} command rewrites the commit message for the last commit in {table}?', 'git commit --amend', ['git amend', 'git rebase -i', 'git reset --soft']),
        ('Which {name} command clones a repository and checks out a branch in {table}?', 'git clone -b', ['git clone --branch', 'git clone -c', 'git checkout -b']),
    ]

    variants = [
        {'table': GIT_CONTEXTS[i % len(GIT_CONTEXTS)], 'name': name}
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_github_questions(name, difficulty):
    easy_templates = [
        ('Which GitHub feature is used to request code changes in {table}?', 'Pull Request', ['Issue', 'Wiki', 'Release']),
        ('Which GitHub feature tracks work items and bugs in {table}?', 'Issue', ['Pull Request', 'Fork', 'Gist']),
        ('Which GitHub feature creates a personal copy of a repository in {table}?', 'Fork', ['Branch', 'Clone', 'Mirror']),
        ('Which GitHub feature stores reusable code snippets in {table}?', 'Gist', ['Issue', 'Release', 'Action']),
        ('Which GitHub page shows the repository source code in {table}?', 'Code', ['Actions', 'Issues', 'Wiki']),
        ('Which GitHub feature publishes documentation or websites in {table}?', 'Pages', ['Issues', 'Projects', 'Releases']),
        ('Which GitHub feature manages workflows and automation in {table}?', 'Actions', ['Issues', 'Wiki', 'Releases']),
        ('Which GitHub feature stores project planning boards in {table}?', 'Projects', ['Actions', 'Wiki', 'Issues']),
        ('Which GitHub feature documents a project in {table}?', 'Wiki', ['Pages', 'Issues', 'Actions']),
        ('Which GitHub feature publishes a release package in {table}?', 'Releases', ['Issues', 'Projects', 'Wiki']),
    ]

    medium_templates = [
        ('Which GitHub feature runs CI/CD workflows in {table}?', 'GitHub Actions', ['GitHub Pages', 'GitHub Issues', 'GitHub Packages']),
        ('Which GitHub feature lets you propose, review, and merge changes in {table}?', 'Pull Request', ['Issue', 'Fork', 'Wiki']),
        ('Which GitHub page contains repository settings and permissions in {table}?', 'Settings', ['Insights', 'Code', 'Actions']),
        ('Which GitHub feature stores binary builds and packages in {table}?', 'Packages', ['Actions', 'Pages', 'Releases']),
        ('Which GitHub tool helps visualize repository activity in {table}?', 'Insights', ['Issues', 'Wiki', 'Projects']),
        ('Which GitHub feature is used for collaborative documentation in {table}?', 'Wiki', ['Issues', 'Actions', 'Pages']),
        ('Which GitHub feature provides temporary pull request environments in {table}?', 'Environments', ['Pages', 'Gists', 'Actions']),
        ('Which GitHub feature tracks repository contributions and commits in {table}?', 'Contributors', ['Issues', 'Pull Requests', 'Actions']),
        ('Which GitHub page displays open pull requests in {table}?', 'Pull requests', ['Issues', 'Actions', 'Wiki']),
        ('Which GitHub section handles code review comments in {table}?', 'Pull requests', ['Issues', 'Discussions', 'Projects']),
    ]

    hard_templates = [
        ('Which GitHub feature automates build and test pipelines in {table}?', 'Actions', ['Pages', 'Issues', 'Projects']),
        ('Which GitHub feature helps publish a compiled application or library in {table}?', 'Packages', ['Actions', 'Wiki', 'Releases']),
        ('Which GitHub term refers to a copy of a repository you can modify independently in {table}?', 'Fork', ['Branch', 'Clone', 'Mirror']),
        ('Which GitHub page lists published version history in {table}?', 'Releases', ['Issues', 'Pull requests', 'Actions']),
        ('Which GitHub feature keeps track of security alerts and vulnerabilities in {table}?', 'Security', ['Issues', 'Wiki', 'Actions']),
        ('Which GitHub feature allows contributors to discuss changes before merging in {table}?', 'Pull Request', ['Issue', 'Wiki', 'Pages']),
        ('Which GitHub feature is used to manage feedback and feature requests in {table}?', 'Issues', ['Projects', 'Actions', 'Pages']),
        ('Which GitHub feature stores custom workflow definitions in YAML in {table}?', 'Actions', ['Pages', 'Releases', 'Wiki']),
        ('Which GitHub page shows code scanning results and alerts in {table}?', 'Security', ['Insights', 'Settings', 'Actions']),
        ('Which GitHub feature lets you keep code and documentation together in {table}?', 'Wiki', ['Pages', 'Issues', 'Actions']),
    ]

    variants = [
        {'table': GITHUB_CONTEXTS[i % len(GITHUB_CONTEXTS)], 'name': name}
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_docker_questions(name, difficulty):
    easy_templates = [
        ('Which {name} file defines container configuration in {table}?', 'Dockerfile', ['docker-compose.yml', 'Dockerfile.dev', '.dockerignore']),
        ('Which {name} command builds an image from a Dockerfile in {table}?', 'docker build', ['docker run', 'docker compose', 'docker push']),
        ('Which {name} command lists running containers in {table}?', 'docker ps', ['docker images', 'docker ls', 'docker top']),
        ('Which {name} command downloads an image from a registry in {table}?', 'docker pull', ['docker upload', 'docker push', 'docker fetch']),
        ('Which {name} file is used to define multi-container setups in {table}?', 'docker-compose.yml', ['Dockerfile', 'compose.yml', 'dockerfile.yml']),
        ('Which {name} command starts a container from an image in {table}?', 'docker run', ['docker start', 'docker exec', 'docker create']),
        ('Which {name} option maps a host port to a container port in {table}?', '-p', ['-v', '--name', '-d']),
        ('Which {name} term describes a lightweight standalone package in {table}?', 'container', ['image', 'volume', 'network']),
        ('Which {name} command removes stopped containers in {table}?', 'docker rm', ['docker rmi', 'docker prune', 'docker clean']),
        ('Which {name} command shows logs for a container in {table}?', 'docker logs', ['docker inspect', 'docker stats', 'docker ps']),
    ]

    medium_templates = [
        ('Which {name} command removes an image by name in {table}?', 'docker rmi', ['docker rm', 'docker delete', 'docker remove']),
        ('Which {name} flag runs a container in detached mode in {table}?', '-d', ['-it', '-p', '--rm']),
        ('Which {name} option mounts a host directory into a container in {table}?', '-v', ['-p', '-e', '--mount']),
        ('Which {name} object stores persistent data outside containers in {table}?', 'volume', ['container', 'network', 'image']),
        ('Which {name} command displays resource usage for containers in {table}?', 'docker stats', ['docker top', 'docker ps', 'docker inspect']),
        ('Which {name} file defines build stages for an image in {table}?', 'Dockerfile', ['docker-compose.yml', 'docker.stack', '.dockerignore']),
        ('Which {name} command executes a command inside a running container in {table}?', 'docker exec', ['docker run', 'docker start', 'docker attach']),
        ('Which {name} command shows detailed information about a container in {table}?', 'docker inspect', ['docker info', 'docker logs', 'docker stats']),
        ('Which {name} command removes unused images and containers in {table}?', 'docker system prune', ['docker prune', 'docker clean', 'docker rm -f']),
        ('Which {name} command logs into a registry in {table}?', 'docker login', ['docker auth', 'docker connect', 'docker push']),
    ]

    hard_templates = [
        ('Which {name} feature groups services in a file for orchestration in {table}?', 'Docker Compose', ['Dockerfile', 'Swarm', 'Kubernetes']),
        ('Which {name} command builds an image with a specific tag in {table}?', 'docker build -t', ['docker tag -t', 'docker create -t', 'docker run -t']),
        ('Which {name} network mode connects containers directly to the host network in {table}?', 'host', ['bridge', 'overlay', 'none']),
        ('Which {name} command upgrades the compose project in {table}?', 'docker compose up', ['docker compose build', 'docker compose start', 'docker compose run']),
        ('Which {name} object isolates networking between containers in {table}?', 'network', ['volume', 'container', 'image']),
        ('Which {name} command saves an image to a tar archive in {table}?', 'docker save', ['docker export', 'docker load', 'docker push']),
        ('Which {name} command loads an image from a tar archive in {table}?', 'docker load', ['docker import', 'docker pull', 'docker save']),
        ('Which {name} feature lets services restart automatically in {table}?', 'restart policy', ['health check', 'entrypoint', 'command']),
        ('Which {name} file uses a version field for compose configuration in {table}?', 'docker-compose.yml', ['Dockerfile', '.dockerignore', 'dockerfile.yml']),
        ('Which {name} driver provides secure network isolation in {table}?', 'bridge', ['host', 'overlay', 'none']),
    ]

    variants = [
        {'table': DOCKER_CONTEXTS[i % len(DOCKER_CONTEXTS)], 'name': name}
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_mongodb_questions(name, difficulty):
    easy_templates = [
        ('Which {name} structure stores JSON-like data in {table}?', 'document', ['row', 'record', 'tuple']),
        ('Which {name} concept groups documents in {table}?', 'collection', ['table', 'database', 'schema']),
        ('Which {name} operation finds documents in a collection in {table}?', 'find()', ['select()', 'search()', 'query()']),
        ('Which {name} command inserts a document into a collection in {table}?', 'insertOne()', ['insert()', 'addOne()', 'push()']),
        ('Which {name} field type stores nested objects in {table}?', 'embedded document', ['foreign key', 'column', 'array']),
        ('Which {name} index type improves search speed in {table}?', 'single field index', ['multi field index', 'hash index', 'tree index']),
        ('Which {name} option returns documents in {table}?', 'toArray()', ['toList()', 'toJSON()', 'fetch()']),
        ('Which {name} keyword updates a document in {table}?', 'updateOne()', ['modifyOne()', 'setOne()', 'changeOne()']),
        ('Which {name} feature allows multiple servers to provide redundancy in {table}?', 'replica set', ['sharding', 'indexing', 'aggregation']),
        ('Which {name} component distributes data across shards in {table}?', 'shard', ['replica', 'collection', 'index']),
    ]

    medium_templates = [
        ('Which {name} stage allows grouping documents in {table}?', '$group', ['$match', '$project', '$sort']),
        ('Which {name} stage filters documents in aggregation in {table}?', '$match', ['$filter', '$group', '$project']),
        ('Which {name} function returns the first matching document in {table}?', 'findOne()', ['find()', 'queryOne()', 'getOne()']),
        ('Which {name} option adds a field to the output document in {table}?', '$addFields', ['$project', '$match', '$sort']),
        ('Which {name} stage transforms document structure in {table}?', '$project', ['$sort', '$group', '$match']),
        ('Which {name} concept controls how data is split across servers in {table}?', 'sharding', ['replication', 'indexing', 'caching']),
        ('Which {name} object stores a sequence of results in {table}?', 'cursor', ['pipeline', 'collection', 'document']),
        ('Which {name} feature prevents schema changes from breaking read operations in {table}?', 'schema validation', ['schema-free', 'lazy schema', 'dynamic schema']),
        ('Which {name} method deletes one document in {table}?', 'deleteOne()', ['removeOne()', 'dropOne()', 'delete()']),
        ('Which {name} method deletes all matching documents in {table}?', 'deleteMany()', ['removeMany()', 'dropMany()', 'deleteAll()']),
    ]

    hard_templates = [
        ('Which {name} feature provides a high-performance in-memory cache in {table}?', 'in-memory storage engine', ['disk storage engine', 'replica set', 'sharded cluster']),
        ('Which {name} structure stores related documents together in {table}?', 'embedded document', ['separate collection', 'foreign document', 'reference']),
        ('Which {name} option ensures a write is acknowledged by the majority in {table}?', 'majority', ['w1', 'w2', 'unacknowledged']),
        ('Which {name} command starts replication in {table}?', 'rs.initiate()', ['rs.start()', 'rs.replicate()', 'rs.begin()']),
        ('Which {name} index type supports text search in {table}?', 'text index', ['hash index', 'geo index', 'regular index']),
        ('Which {name} feature executes multiple operations atomically in {table}?', 'transactions', ['bulk writes', 'index builds', 'replication']),
        ('Which {name} stage sorts documents in aggregation in {table}?', '$sort', ['$group', '$project', '$match']),
        ('Which {name} command adds a new shard to the cluster in {table}?', 'sh.addShard()', ['sh.addNode()', 'sh.addReplica()', 'sh.addCluster()']),
        ('Which {name} feature lets you define document validation rules in {table}?', 'schema validation', ['dynamic schema', 'relaxed schema', 'flex schema']),
        ('Which {name} option forces a query to use an index in {table}?', 'hint()', ['forceIndex()', 'useIndex()', 'index()']),
    ]

    variants = [
        {'table': MONGODB_CONTEXTS[i % len(MONGODB_CONTEXTS)], 'name': name}
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_redis_questions(name, difficulty):
    easy_templates = [
        ('Which {name} data structure stores key/value pairs in {table}?', 'string', ['hash', 'list', 'set']),
        ('Which {name} command sets a value for a key in {table}?', 'SET', ['GET', 'ADD', 'PUT']),
        ('Which {name} command retrieves the value of a key in {table}?', 'GET', ['SET', 'DELETE', 'MGET']),
        ('Which {name} structure stores multiple ordered values in {table}?', 'list', ['set', 'hash', 'sorted set']),
        ('Which {name} structure stores unique values in {table}?', 'set', ['list', 'hash', 'sorted set']),
        ('Which {name} command removes a key in {table}?', 'DEL', ['REMOVE', 'DELETE', 'UNSET']),
        ('Which {name} command sets an expiration on a key in {table}?', 'EXPIRE', ['TTL', 'SETEX', 'EXPIRETIME']),
        ('Which {name} command returns the time to live of a key in {table}?', 'TTL', ['EXPIRE', 'PTTL', 'TIME']),
        ('Which {name} structure stores field/value pairs in {table}?', 'hash', ['list', 'set', 'string']),
        ('Which {name} structure stores elements ordered by score in {table}?', 'sorted set', ['set', 'list', 'hash']),
    ]

    medium_templates = [
        ('Which {name} command adds one or more members to a set in {table}?', 'SADD', ['SET', 'ADD', 'LADD']),
        ('Which {name} command retrieves all members of a set in {table}?', 'SMEMBERS', ['GETMEMBERS', 'MGET', 'HGETALL']),
        ('Which {name} command pushes a value onto the end of a list in {table}?', 'RPUSH', ['LPUSH', 'PUSH', 'APPEND']),
        ('Which {name} command removes and returns the first element of a list in {table}?', 'LPOP', ['RPOP', 'POP', 'PULL']),
        ('Which {name} command increments the integer value of a key in {table}?', 'INCR', ['ADD', 'INCREMENT', 'SET']),
        ('Which {name} command returns a hash by key in {table}?', 'HGETALL', ['HGET', 'HMGET', 'GETALL']),
        ('Which {name} command adds an element to a sorted set in {table}?', 'ZADD', ['SADD', 'ADD', 'HSET']),
        ('Which {name} command gets the score of a member in {table}?', 'ZSCORE', ['ZGET', 'SCORE', 'GETSCORE']),
        ('Which {name} command deletes one or more hash fields in {table}?', 'HDEL', ['DEL', 'REMOVE', 'DELETE']),
        ('Which {name} command returns the number of elements in a set in {table}?', 'SCARD', ['SCOUNT', 'SIZE', 'COUNT']),
    ]

    hard_templates = [
        ('Which {name} command creates a pub/sub channel in {table}?', 'PUBLISH', ['SUBSCRIBE', 'CONNECT', 'OPEN']),
        ('Which {name} command subscribes to messages in a channel in {table}?', 'SUBSCRIBE', ['CONNECT', 'LISTEN', 'JOIN']),
        ('Which {name} feature stores data in memory for low-latency access in {table}?', 'in-memory storage', ['disk persistence', 'database storage', 'cloud storage']),
        ('Which {name} command copies keys from one database to another in {table}?', 'DUMP', ['COPY', 'MIGRATE', 'SAVE']),
        ('Which {name} command atomically increments a field in a hash in {table}?', 'HINCRBY', ['HINCR', 'INCRBY', 'HSET']),
        ('Which {name} command adds members to a sorted set with scores in {table}?', 'ZADD', ['SADD', 'ADD', 'HSET']),
        ('Which {name} command retrieves a range of members from a sorted set in {table}?', 'ZRANGE', ['ZRANK', 'ZREM', 'ZSCORE']),
        ('Which {name} command creates a persistent snapshot on disk in {table}?', 'BGSAVE', ['SAVE', 'PERSIST', 'SNAPSHOT']),
        ('Which {name} feature limits the lifetime of a key in {table}?', 'TTL', ['EXPIRE', 'TIMEOUT', 'LIFETIME']),
        ('Which {name} structure is optimized for fast lookups by key in {table}?', 'hash', ['list', 'set', 'sorted set']),
    ]

    variants = [
        {'table': REDIS_CONTEXTS[i % len(REDIS_CONTEXTS)], 'name': name}
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_bash_questions(name, difficulty):
    easy_templates = [
        ('Which {name} command lists files in the current directory in {table}?', 'ls', ['cd', 'pwd', 'dir']),
        ('Which {name} command prints the current working directory in {table}?', 'pwd', ['ls', 'cd', 'echo']),
        ('Which {name} command changes directories in {table}?', 'cd', ['ls', 'pwd', 'mv']),
        ('Which {name} operator redirects output to a file in {table}?', '>', ['|', '>>', '<']),
        ('Which {name} symbol runs a command in the background in {table}?', '&', ['|', ';', '&&']),
        ('Which {name} command shows the first lines of a file in {table}?', 'head', ['tail', 'cat', 'less']),
        ('Which {name} command shows the last lines of a file in {table}?', 'tail', ['head', 'cat', 'less']),
        ('Which {name} command concatenates files and prints to standard output in {table}?', 'cat', ['echo', 'print', 'type']),
        ('Which {name} command searches text using patterns in {table}?', 'grep', ['find', 'search', 'look']),
        ('Which {name} command creates a new directory in {table}?', 'mkdir', ['touch', 'rmdir', 'cp']),
    ]

    medium_templates = [
        ('Which {name} command copies files in {table}?', 'cp', ['mv', 'copy', 'duplicate']),
        ('Which {name} command moves or renames files in {table}?', 'mv', ['cp', 'move', 'rename']),
        ('Which {name} command changes file permissions in {table}?', 'chmod', ['chown', 'chgrp', 'permit']),
        ('Which {name} command changes file ownership in {table}?', 'chown', ['chmod', 'chgrp', 'owner']),
        ('Which {name} command shows running processes in {table}?', 'ps', ['top', 'jobs', 'proc']),
        ('Which {name} command pauses output one screen at a time in {table}?', 'less', ['more', 'cat', 'head']),
        ('Which {name} command displays environment variables in {table}?', 'env', ['export', 'set', 'printenv']),
        ('Which {name} command removes empty directories in {table}?', 'rmdir', ['rm', 'del', 'remove']),
        ('Which {name} operator runs the next command only if the previous command succeeded in {table}?', '&&', ['||', ';', '&']),
        ('Which {name} syntax defines a variable in {table}?', 'VAR=value', ['set VAR=value', 'export VAR value', 'VAR := value']),
    ]

    hard_templates = [
        ('Which {name} command searches for files by name in {table}?', 'find', ['grep', 'locate', 'search']),
        ('Which {name} command displays the difference between files in {table}?', 'diff', ['cmp', 'compare', 'delta']),
        ('Which {name} command reads a file backwards page by page in {table}?', 'tac', ['cat', 'tail', 'rev']),
        ('Which {name} operator redirects both stdout and stderr to a file in {table}?', '&>', ['>', '2>', '>>']),
        ('Which {name} command substitutes text in a stream in {table}?', 'sed', ['awk', 'grep', 'perl']),
        ('Which {name} command processes text with patterns and actions in {table}?', 'awk', ['sed', 'grep', 'perl']),
        ('Which {name} command creates a new file or updates timestamp in {table}?', 'touch', ['mkfile', 'create', 'newfile']),
        ('Which {name} shell builtin exits the shell in {table}?', 'exit', ['quit', 'logout', 'close']),
        ('Which {name} command prints the first column of each line in {table}?', 'cut', ['awk', 'grep', 'paste']),
        ('Which {name} command runs multiple programs in a pipeline in {table}?', '|', ['&&', ';', '||']),
    ]

    variants = [
        {'table': BASH_CONTEXTS[i % len(BASH_CONTEXTS)], 'name': name}
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_tailwind_questions(name, difficulty):
    easy_templates = [
        ('Which {name} class sets margin in {table}?', 'm-4', ['p-4', 'text-center', 'bg-blue-500']),
        ('Which {name} class sets padding in {table}?', 'p-4', ['m-4', 'pt-4', 'px-4']),
        ('Which {name} class sets text color in {table}?', 'text-red-500', ['bg-red-500', 'text-blue-500', 'border-red-500']),
        ('Which {name} class sets a background color in {table}?', 'bg-blue-500', ['text-blue-500', 'border-blue-500', 'hover:bg-blue-500']),
        ('Which {name} class makes text bold in {table}?', 'font-bold', ['text-bold', 'font-semibold', 'font-medium']),
        ('Which {name} class centers text in {table}?', 'text-center', ['text-left', 'text-right', 'text-justify']),
        ('Which {name} class sets display to flex in {table}?', 'flex', ['grid', 'block', 'inline-flex']),
        ('Which {name} class makes a container full width in {table}?', 'w-full', ['w-auto', 'max-w-full', 'h-full']),
        ('Which {name} class applies rounded corners in {table}?', 'rounded', ['rounded-full', 'rounded-none', 'rounded-lg']),
        ('Which {name} class sets a border in {table}?', 'border', ['border-0', 'border-gray-500', 'border-solid']),
    ]

    medium_templates = [
        ('Which {name} class sets horizontal padding in {table}?', 'px-4', ['py-4', 'p-4', 'mx-4']),
        ('Which {name} class sets vertical padding in {table}?', 'py-4', ['px-4', 'p-4', 'my-4']),
        ('Which {name} class sets margin on all sides in {table}?', 'm-4', ['mt-4', 'mb-4', 'mx-4']),
        ('Which {name} class adds a hover background color in {table}?', 'hover:bg-blue-700', ['hover:text-blue-700', 'hover:border-blue-700', 'focus:bg-blue-700']),
        ('Which {name} class sets text size to large in {table}?', 'text-lg', ['text-xl', 'text-base', 'text-sm']),
        ('Which {name} class sets a max-width container in {table}?', 'max-w-screen-lg', ['container', 'max-w-full', 'max-w-md']),
        ('Which {name} class places items in a row inside a flex container in {table}?', 'flex-row', ['flex-col', 'items-center', 'justify-center']),
        ('Which {name} class enables responsive grid columns in {table}?', 'grid-cols-3', ['grid-cols-2', 'grid-cols-4', 'grid-cols-none']),
        ('Which {name} class sets a shadow effect in {table}?', 'shadow-lg', ['shadow-md', 'shadow-sm', 'shadow-none']),
        ('Which {name} class sets a custom height in {table}?', 'h-16', ['h-12', 'h-full', 'h-auto']),
    ]

    hard_templates = [
        ('Which {name} class makes an element sticky at the top in {table}?', 'sticky top-0', ['fixed top-0', 'absolute top-0', 'relative top-0']),
        ('Which {name} class sets a responsive gap between grid items in {table}?', 'gap-4', ['gap-2', 'space-x-4', 'space-y-4']),
        ('Which {name} class applies a gradient background in {table}?', 'bg-gradient-to-r', ['bg-gradient-to-l', 'bg-blue-500', 'bg-gradient']),
        ('Which {name} class makes an element invisible in {table}?', 'invisible', ['hidden', 'opacity-0', 'sr-only']),
        ('Which {name} class makes text uppercase in {table}?', 'uppercase', ['capitalize', 'lowercase', 'normal-case']),
        ('Which {name} class applies a ring around an element in {table}?', 'ring', ['border', 'outline', 'shadow']),
        ('Which {name} class sets grid columns automatically in {table}?', 'grid-cols-none', ['grid-cols-1', 'grid-cols-2', 'grid-cols-3']),
        ('Which {name} class makes an element partially transparent in {table}?', 'opacity-75', ['opacity-50', 'opacity-100', 'opacity-25']),
        ('Which {name} class adds margin on the right side in {table}?', 'mr-4', ['ml-4', 'mx-4', 'm-4']),
        ('Which {name} class sets a custom min-height in {table}?', 'min-h-screen', ['h-screen', 'min-h-full', 'max-h-screen']),
    ]

    variants = [
        {'table': TAILWIND_CONTEXTS[i % len(TAILWIND_CONTEXTS)], 'name': name}
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_html_questions(name, difficulty):
    easy_templates = [
        ('Which file extension is used for {name} documents in {table}?', '.html', ['.css', '.js', '.txt']),
        ('Which tag wraps the main content of a {name} page in {table}?', '<body>', ['<head>', '<footer>', '<section>']),
        ('Which tag defines a paragraph in {name} on {table}?', '<p>', ['<div>', '<span>', '<h1>']),
        ('Which syntax marks a comment in {name} on {table}?', '<!-- -->', ['//', '#', '/* */']),
        ('Which tag is used to represent a hyperlink in {name} on {table}?', '<a>', ['<link>', '<href>', '<url>']),
        ('Which element embeds an image in {name} on {table}?', '<img>', ['<image>', '<figure>', '<picture>']),
        ('Which tag defines the page head in {name} on {table}?', '<head>', ['<body>', '<html>', '<title>']),
        ('Which tag defines a list item in {name} on {table}?', '<li>', ['<ul>', '<ol>', '<dl>']),
        ('Which tag defines a table row in {name} on {table}?', '<tr>', ['<td>', '<table>', '<th>']),
        ('Which attribute sets the link destination in {name} on {table}?', 'href', ['src', 'alt', 'title']),
    ]

    medium_templates = [
        ('Which element defines a section in {name} on {table}?', '<section>', ['<div>', '<article>', '<aside>']),
        ('Which attribute sets alternative text for an image in {name} on {table}?', 'alt', ['title', 'src', 'href']),
        ('Which tag groups form controls in {name} on {table}?', '<fieldset>', ['<form>', '<div>', '<section>']),
        ('Which tag defines the biggest heading in {name} on {table}?', '<h1>', ['<h2>', '<title>', '<header>']),
        ('Which tag defines an ordered list in {name} on {table}?', '<ol>', ['<ul>', '<li>', '<dl>']),
        ('Which element is used for inline text in {name} on {table}?', '<span>', ['<div>', '<p>', '<section>']),
        ('Which tag embeds a video in {name} on {table}?', '<video>', ['<media>', '<clip>', '<iframe>']),
        ('Which attribute names the language of the document in {name} on {table}?', 'lang', ['type', 'charset', 'rel']),
        ('Which tag defines table header cells in {name} on {table}?', '<th>', ['<td>', '<tr>', '<thead>']),
        ('Which attribute specifies the URL of an image in {name} on {table}?', 'src', ['href', 'alt', 'title']),
    ]

    hard_templates = [
        ('Which tag defines navigation links in {name} on {table}?', '<nav>', ['<menu>', '<section>', '<header>']),
        ('Which tag defines a self-closing line break in {name} on {table}?', '<br>', ['<lb>', '<hr>', '<break>']),
        ('Which HTML5 element represents a standalone piece of content on {table}?', '<article>', ['<section>', '<div>', '<aside>']),
        ('Which tag is used to define a caption for a table in {name} on {table}?', '<caption>', ['<title>', '<label>', '<summary>']),
        ('Which attribute is used to specify a stylesheet URL in {name} on {table}?', 'href', ['src', 'action', 'type']),
        ('Which tag defines a row of table header cells in {name} on {table}?', '<thead>', ['<tbody>', '<tr>', '<tfoot>']),
        ('Which element defines the visible title of a document on {table}?', '<title>', ['<h1>', '<header>', '<meta>']),
        ('Which tag defines a clickable button in {name} on {table}?', '<button>', ['<input>', '<a>', '<div>']),
        ('Which attribute changes the display text of a link in {name} on {table}?', 'title', ['href', 'alt', 'rel']),
        ('Which tag defines a list of definitions in {name} on {table}?', '<dl>', ['<ul>', '<ol>', '<dt>']),
    ]

    variants = [
        {'table': HTML_CONTEXTS[i % len(HTML_CONTEXTS)], 'name': name}
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_css_questions(name, difficulty):
    easy_templates = [
        ('Which file extension is used for {name} stylesheets in {table}?', '.css', ['.html', '.js', '.scss']),
        ('Which syntax selects elements with a class name in {name} on {table}?', '.class', ['#class', 'class', '*class']),
        ('Which property changes text color in {name} on {table}?', 'color', ['font-size', 'margin', 'padding']),
        ('Which syntax is a valid comment in {name} on {table}?', '/* */', ['//', '#', '<!-- -->']),
        ('Which property changes the background color in {name} on {table}?', 'background-color', ['color', 'border', 'display']),
        ('Which value sets the display type to block in {name} on {table}?', 'display: block', ['position: absolute', 'float: left', 'visibility: hidden']),
        ('Which selector targets an element by id in {name} on {table}?', '#id', ['.id', 'id', '*id']),
        ('Which property adds space inside an element in {name} on {table}?', 'padding', ['margin', 'border', 'opacity']),
        ('Which property changes the font size in {name} on {table}?', 'font-size', ['line-height', 'color', 'width']),
        ('Which property hides an element in {name} on {table}?', 'display: none', ['visibility: hidden', 'opacity: 0', 'position: absolute']),
    ]

    medium_templates = [
        ('Which property sets the spacing between flex items in {name} on {table}?', 'gap', ['margin', 'padding', 'space']),
        ('Which selector matches the first child element in {name} on {table}?', ':first-child', ['.first', '#first', ':nth-child(1)']),
        ('Which property controls the stacking order in {name} on {table}?', 'z-index', ['opacity', 'order', 'visibility']),
        ('Which property changes text alignment in {name} on {table}?', 'text-align', ['align-items', 'justify-content', 'display']),
        ('Which property makes an element flexible in {name} on {table}?', 'flex', ['display', 'float', 'position']),
        ('Which rule applies a grid layout in {name} on {table}?', 'display: grid', ['display: flex', 'position: grid', 'layout: grid']),
        ('Which property changes the width of an element in {name} on {table}?', 'width', ['height', 'margin', 'padding']),
        ('Which property adds a shadow to an element in {name} on {table}?', 'box-shadow', ['text-shadow', 'border-shadow', 'shadow']),
        ('Which value makes a CSS property transparent in {name} on {table}?', 'rgba(0,0,0,0)', ['transparent', 'none', 'inherit']),
        ('Which syntax is used for a CSS class selector in {name} on {table}?', '.class', ['#class', 'class', '*class']),
    ]

    hard_templates = [
        ('Which CSS property controls horizontal overflow in {name} on {table}?', 'overflow-x', ['overflow-y', 'overflow', 'position']),
        ('Which property sets the gap between grid rows in {name} on {table}?', 'row-gap', ['grid-gap', 'column-gap', 'gap']),
        ('Which property lets content wrap onto a new line in {name} on {table}?', 'flex-wrap', ['flex-direction', 'align-items', 'justify-content']),
        ('Which selector matches an element by id in {name} on {table}?', '#main', ['.main', 'main', '*main']),
        ('Which property sets the distance between the element and its border in {name} on {table}?', 'padding', ['margin', 'border', 'outline']),
        ('Which property controls how white space is handled in {name} on {table}?', 'white-space', ['text-overflow', 'overflow', 'line-height']),
        ('Which property defines the stacking order of positioned elements in {name} on {table}?', 'z-index', ['opacity', 'order', 'visibility']),
        ('Which property sets a background image in {name} on {table}?', 'background-image', ['background', 'image', 'url']),
        ('Which value makes a flex container use row layout in {name} on {table}?', 'flex-direction: row', ['display: flex', 'align-items: center', 'justify-content: flex-start']),
        ('Which property changes the opacity in {name} on {table}?', 'opacity', ['visibility', 'filter', 'display']),
    ]

    variants = [
        {'table': CSS_CONTEXTS[i % len(CSS_CONTEXTS)], 'name': name}
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def build_react_questions(name, difficulty):
    easy_templates = [
        ('Which {hook} hook manages state in {name} on {table}?', 'useState', ['useEffect', 'useMemo', 'useCallback']),
        ('Which {hook} hook is used for side effects in {name} on {table}?', 'useEffect', ['useState', 'useReducer', 'useContext']),
        ('Which property passes data into components in {name} on {table}?', 'props', ['state', 'context', 'refs']),
        ('Which syntax creates JSX elements in {name} on {table}?', '<div>Hello</div>', ['[div]Hello[/div]', '{{div}}Hello', '<div>Hello>']),
        ('Which file extension is common for {name} components on {table}?', '.jsx', ['.js', '.css', '.html']),
        ('Which {hook} hook memoizes a callback in {name} on {table}?', 'useCallback', ['useMemo', 'useState', 'useEffect']),
        ('Which {hook} hook memoizes a value in {name} on {table}?', 'useMemo', ['useState', 'useEffect', 'useContext']),
        ('Which prop is used to track a unique element in a list in {name} on {table}?', 'key', ['id', 'className', 'ref']),
        ('Which {hook} hook accesses context in {name} on {table}?', 'useContext', ['useState', 'useReducer', 'useEffect']),
        ('Which statement returns the UI tree from a component in {name} on {table}?', 'return', ['render', 'output', 'yield']),
        ('Which value represents a React component property in {name} on {table}?', 'props', ['state', 'context', 'hooks']),
        ('Which hook is used for memoizing expensive calculations in {name} on {table}?', 'useMemo', ['useCallback', 'useState', 'useEffect']),
        ('Which hook is used to access context values in {name} on {table}?', 'useContext', ['useState', 'useEffect', 'useRef']),
        ('Which keyword defines a function component in {name} on {table}?', 'function', ['class', 'const', 'let']),
        ('Which React concept lets data flow down from parent to child in {name} on {table}?', 'props', ['state', 'hooks', 'context']),
    ]

    medium_templates = [
        ('Which hook runs when dependencies change in {name} on {table}?', 'useEffect', ['useState', 'useCallback', 'useMemo']),
        ('Which React feature splits the UI into reusable pieces in {name} on {table}?', 'components', ['hooks', 'props', 'state']),
        ('Which prop in {name} passes values from parent to child on {table}?', 'props', ['state', 'hooks', 'context']),
        ('Which hook keeps a mutable value without rerendering in {name} on {table}?', 'useRef', ['useState', 'useReducer', 'useMemo']),
        ('Which hook manages form fields and values in {name} on {table}?', 'useState', ['useEffect', 'useRef', 'useCallback']),
        ('Which React API prevents a component from rerendering when props do not change on {table}?', 'React.memo', ['useMemo', 'useCallback', 'PureComponent']),
        ('Which React concept tracks component data over time in {name} on {table}?', 'state', ['props', 'render', 'context']),
        ('Which hook runs cleanup code when components unmount in {name} on {table}?', 'useEffect', ['useState', 'useMemo', 'useCallback']),
        ('Which keyword creates a function component in {name} on {table}?', 'function', ['class', 'const', 'let']),
        ('Which feature allows React to manage UI updates efficiently on {table}?', 'virtual DOM', ['real DOM', 'shadow DOM', 'server DOM']),
    ]

    hard_templates = [
        ('Which hook returns a memoized value in {name} on {table}?', 'useMemo', ['useState', 'useEffect', 'useCallback']),
        ('Which hook returns a memoized callback in {name} on {table}?', 'useCallback', ['useMemo', 'useEffect', 'useState']),
        ('Which React feature lets you render elements conditionally on {table}?', 'conditional rendering', ['hooks', 'props', 'state']),
        ('Which hook lets you manage local component state in {name} on {table}?', 'useState', ['useEffect', 'useReducer', 'useContext']),
        ('Which hook runs after render and can clean up in {name} on {table}?', 'useEffect', ['useMemo', 'useCallback', 'useRef']),
        ('Which prop identifies unique items in a list in {name} on {table}?', 'key', ['id', 'className', 'name']),
        ('Which React feature lets you share values without passing props down manually on {table}?', 'context', ['state', 'hooks', 'refs']),
        ('Which concept should be pure for predictable rendering in {name} on {table}?', 'render', ['componentDidMount', 'useEffect', 'setState']),
        ('Which React hook is useful for expensive calculations that should not rerun every render on {table}?', 'useMemo', ['useEffect', 'useState', 'useContext']),
        ('Which hook is often used to handle user input and form state in {name} on {table}?', 'useState', ['useMemo', 'useEffect', 'useRef']),
    ]

    variants = [
        {
            'hook': REACT_HOOKS[i % len(REACT_HOOKS)],
            'table': REACT_CONTEXTS[i % len(REACT_CONTEXTS)],
            'name': name,
        }
        for i in range(10)
    ]

    templates = easy_templates if difficulty == 'easy' else medium_templates if difficulty == 'medium' else hard_templates
    questions = []
    for idx in range(100):
        template, correct, wrongs = templates[idx % len(templates)]
        variant = variants[idx // len(templates)]
        question = format_fields(template, variant)
        correct_text = format_fields(correct, variant)
        wrong_texts = [format_fields(w, variant) for w in wrongs]
        options, correct_index = shuffle_options(correct_text, wrong_texts)
        questions.append({
            'question': question,
            'options': options,
            'correctAnswer': correct_index,
            'explanation': f"The correct answer is '{correct_text}' for {name}.",
        })

    random.shuffle(questions)
    return questions


def dedupe_questions(questions):
    seen = set()
    unique_questions = []
    for question in questions:
        key = question['question'].strip()
        if key not in seen:
            seen.add(key)
            unique_questions.append(question)
    return unique_questions


def build_questions_for_file(lang, difficulty):
    questions = build_questions(lang, difficulty)
    questions = dedupe_questions(questions)
    return questions[:50]


def main():
    random.seed(42)
    for lang in sorted(LANGUAGE_META):
        lang_dir = SEEDS_DIR / lang
        lang_dir.mkdir(parents=True, exist_ok=True)
        for difficulty in ['easy', 'medium', 'hard']:
            questions = build_questions_for_file(lang, difficulty)
            file_path = lang_dir / f'{difficulty}.json'
            file_path.write_text(json.dumps(questions, indent=2, ensure_ascii=False), encoding='utf-8')
            print(f'Wrote {len(questions)} questions to {file_path}')

if __name__ == '__main__':
    main()
