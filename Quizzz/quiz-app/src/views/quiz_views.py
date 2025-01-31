from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from src.services.quiz_service import QuizService

quiz_views = Blueprint('quiz_views', __name__)
quiz_service = QuizService()

@quiz_views.route('/quizzes', methods=['GET'])
@login_required
def list_quizzes():
    quizzes = quiz_service.get_all_quizzes()
    return render_template('quiz.html', quizzes=quizzes)

@quiz_views.route('/quizzes/<int:quiz_id>', methods=['GET'])
@login_required
def attempt_quiz(quiz_id):
    quiz = quiz_service.get_quiz_by_id(quiz_id)
    if not quiz:
        flash('Quiz not found', 'danger')
        return redirect(url_for('quiz_views.list_quizzes'))
    return render_template('quiz.html', quiz=quiz)

@quiz_views.route('/quizzes/<int:quiz_id>/submit', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    answers = request.form.getlist('answers')
    score = quiz_service.calculate_score(quiz_id, answers)
    flash(f'Your score: {score}%', 'success')
    return redirect(url_for('quiz_views.list_quizzes'))

@quiz_views.route('/quizzes/leaderboard', methods=['GET'])
@login_required
def leaderboard():
    leaderboard_data = quiz_service.get_leaderboard()
    return render_template('leaderboard.html', leaderboard=leaderboard_data)