# MCQ Application

## Overview
The MCQ Application is a web-based platform designed for users to attempt multiple-choice questions (MCQs) across various categories and difficulty levels. The application supports two types of user roles: Admin and User. Admins have additional functionalities such as managing users and uploading MCQs in bulk.

## Features
- **User Roles**: 
  - Admin: Manage users and upload MCQs in bulk.
  - User: Attempt MCQs, view history, and select MCQ types.
  
- **MCQ Management**:
  - Search and filter MCQs by category and difficulty level.
  - Randomized question selection for users.
  - Detailed explanations for correct and incorrect answers.
  - Question tagging/bookmarking for later review.

- **User Interaction**:
  - Attempt a customizable number of MCQs.
  - Timer set to 60 seconds per question.
  - Lifelines: 50-50 and skip options.
  - Hints available for questions.
  - Leaderboard to track top scorers.

- **History Tracking**: Users can view their attempt history and scores.

## Tech Stack
- **Backend**: Python, FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Frontend**: Jinja2 for templating

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/mcq-application.git
   cd mcq-application
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Update the `.env` file with your database credentials.
   - Run the database initialization script:
     ```
     python -m app.db.init_db
     ```

5. Start the application:
   ```
   uvicorn app.main:app --reload
   ```

## Usage
- Access the application at `http://localhost:8000`.
- Admin users can manage MCQs and users through the admin panel.
- Regular users can attempt MCQs and view their history.

## Docker
To build and run the application using Docker, use the following commands:
1. Build the Docker image:
   ```
   docker build -t mcq-application .
   ```

2. Run the Docker container:
   ```
   docker run -d -p 8000:8000 mcq-application
   ```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.