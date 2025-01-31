def generate_random_quiz_questions(questions, num_questions):
    import random
    return random.sample(questions, min(num_questions, len(questions)))

def calculate_score(correct_answers, total_questions):
    if total_questions == 0:
        return 0
    return (correct_answers / total_questions) * 100

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02}:{seconds:02}"

def sanitize_input(user_input):
    from werkzeug.utils import escape
    return escape(user_input)

def get_difficulty_label(difficulty):
    difficulty_labels = {
        'easy': 'Easy',
        'medium': 'Medium',
        'hard': 'Hard'
    }
    return difficulty_labels.get(difficulty, 'Unknown')