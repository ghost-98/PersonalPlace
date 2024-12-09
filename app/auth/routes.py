from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from app.models.models import User, UserProfile

from werkzeug.security import generate_password_hash, check_password_hash  # 비밀번호 해시화 라이브러리

from datetime import datetime

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])  # get은 렌더링html 반환
def signup():
    if request.method == 'GET':
        return render_template('auth/signup.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 비밀번호 일치는 FE 로직
        confirm_password = request.form['confirm_password']
        name = request.form['name']
        gender = request.form['gender']
        birth_date = request.form['birth_date']
        phone_number = f"{request.form['phone_number_1']}-{request.form['phone_number_2']}-{request.form['phone_number_3']}"

        # 비밀번호 해시화 (sha256)
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # db에 맞게 str -> date
        birth_date_obj = datetime.strptime(birth_date, '%Y-%m-%d').date()

        # User 객체 생성
        new_user = User(
            username=username,
            password=hashed_password,
            name=name,
            gender=gender,
            birth_date=birth_date_obj,
            phone_number=phone_number,
            created_time=datetime.now(),
        )

        new_user.save_to_db()

        new_user_profile = UserProfile(user_id=new_user.id)
        new_user_profile.save_to_db()

    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            user = User.query.filter_by(username=username).first()

            if user and check_password_hash(user.password, password):
                login_user(user)  # 로그인 처리
                flash('로그인 성공!', 'success')
                return redirect(url_for('main.home'))

            else:
                flash('로그인 실패! 아이디 혹은 비밀번호를 확인하세요.', 'danger')
                return redirect(url_for('auth.login'))

        except Exception as e:
            print(f"Error during login: {e}")
            flash('로그인 처리 중 문제가 발생했습니다. 다시 시도해주세요.', 'danger')
            return redirect(url_for('auth.login'))

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required  # 로그인된 사용자만 접근 가능, 순서 라우팅보다 밑에
def logout():
    logout_user()  # 로그아웃 처리
    flash('로그아웃 되었습니다.', 'info')
    return redirect(url_for('auth.login'))
