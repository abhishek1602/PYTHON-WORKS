def generate_random_mcqs(mcqs, count):
    import random
    return random.sample(mcqs, min(count, len(mcqs)))

def calculate_score(correct_answers, user_answers):
    score = sum(1 for correct, user in zip(correct_answers, user_answers) if correct == user)
    percentage = (score / len(correct_answers)) * 100 if correct_answers else 0
    return score, percentage

def paginate(items, page, page_size):
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end]

def filter_mcqs(mcqs, category=None, difficulty=None):
    filtered = mcqs
    if category:
        filtered = [mcq for mcq in filtered if mcq.category == category]
    if difficulty:
        filtered = [mcq for mcq in filtered if mcq.difficulty == difficulty]
    return filtered

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02}:{seconds:02}"