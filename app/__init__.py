from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy가 flask에서
from flask_migrate import Migrate  # flask_migrate 라이브러리에서 마이그레이션 기능 가져오기
from flask_login import LoginManager

from .config import DBConfig

# SQLAlchemy로 데이터베이스 객체 생성
db = SQLAlchemy()
migrate = Migrate()

# 로그인 관리 초기화
login_manager = LoginManager()


def create_app():
    # Flask 앱 객체 생성
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'  # ??
    app.config.from_object(DBConfig)  # DB 설정 적용?

    # Flask 애플리케이션에 secret_key 설정??
    app.config['SECRET_KEY'] = 'your-unique-and-secret-key'

    ## Flask 앱의 설정, DB, URL 정의
    # config 앱 설정 적용되는 코드

    # DB와 Flask 앱 연결
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)  # 로그인 매니저

    # 로그인 후 리다이렉트할 URL 설정
    login_manager.login_view = 'auth.login'  # 로그인 페이지로 리다이렉트
    login_manager.login_message_category = 'info'

    # 모델 임포트 (app에 migrate 반영 위해)
    from app.models.models import User, UserProfile
    # DB에서 user 객체 반환
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Blueprint로 url 계층화 매핑
    from app.auth.routes import auth
    from app.main.routes import main

    app.register_blueprint(auth, url_prefix='/auth')  # 회원가입 관련 URL은 /auth로 시작
    app.register_blueprint(main)  # 주요 기능 관련 URL은 기본 경로 사용

    return app
