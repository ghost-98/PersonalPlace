import os


class DBConfig:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # 현재 파일의 절대 경로
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
