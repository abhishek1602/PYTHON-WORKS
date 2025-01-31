from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from src.services.user_service import UserService

user_views = Blueprint('user_views', __name__)
user_service = UserService()

@user_views.route('/profile')
@login_required
def profile():
    user = user_service.get_user(current_user.id)
    return render_template('profile.html', user=user)

@user_views.route('/leaderboard')
def leaderboard():
    top_users = user_service.get_leaderboard()
    return render_template('leaderboard.html', users=top_users)

@user_views.route('/bookmark/<int:question_id>', methods=['POST'])
@login_required
def bookmark_question(question_id):
    user_service.bookmark_question(current_user.id, question_id)
    flash('Question bookmarked successfully!', 'success')
    return redirect(url_for('quiz_views.quiz', question_id=question_id))

@user_views.route('/bookmarks')
@login_required
def bookmarks():
    bookmarked_questions = user_service.get_bookmarked_questions(current_user.id)
    return render_template('bookmarks.html', questions=bookmarked_questions)