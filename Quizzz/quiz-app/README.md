# Quiz Application

This is a comprehensive quiz application built using Flask and PostgreSQL. The application allows admins to create, update, delete, and read quizzes, while normal users can attempt the quizzes. 

## Features

- **User Authentication**: Secure login and registration for users and admins.
- **Multiple-Choice Questions**: Supports various subjects including Python, Java, C#, etc.
- **Random Question Selection**: Questions are randomly selected based on the chosen subject.
- **Category Filtering**: Users can filter quizzes by category.
- **Difficulty Levels**: Quizzes can be categorized by difficulty (easy, medium, hard).
- **Detailed Explanations**: Each question includes an explanation for the correct answer.
- **Leaderboard**: Displays top users based on their scores.
- **Timer**: A 60-second timer per question to enhance the challenge.
- **Final Score**: Users receive a score as a percentage after completing the quiz.
- **Hints and Lifelines**: Options for hints, 50-50, and skipping questions.
- **Bookmarking**: Users can tag questions for later review.
- **Media Support**: Supports image-based and audio-based questions.
- **Responsive Design**: Built with Jinja templates for a dynamic user experience.

## Project Structure

```
quiz-app
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── repositories
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── mcq_repository.py
│   │   └── user_repository.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── quiz_service.py
│   │   └── user_service.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── quiz.html
│   │   ├── result.html
│   │   └── leaderboard.html
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   ├── js
│   │   │   └── scripts.js
│   │   └── images
│   ├── types
│   │   └── __init__.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   └── helpers.py
│   ├── views
│   │   ├── __init__.py
│   │   ├── auth_views.py
│   │   ├── quiz_views.py
│   │   └── user_views.py
│   ├── unit_of_work.py
│   └── database.py
├── tests
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_quiz.py
│   └── test_user.py
├── migrations
│   ├── versions
│   │   └── __init__.py
│   └── alembic.ini
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd quiz-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Configure your database settings in the `.env` file.
   - Run migrations using Alembic.

5. Start the application:
   ```
   python src/app.py
   ```

## Usage

- Access the application in your web browser at `http://localhost:5000`.
- Admins can manage quizzes through the admin panel.
- Users can register, log in, and attempt quizzes.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.