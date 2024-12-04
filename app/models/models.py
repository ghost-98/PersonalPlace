from sqlalchemy.sql import func
from flask_login import UserMixin  # UserMixin을 상속받아 필요한 메서드 구현

from app import db


# User, UserProfile은 username으로 관계
class User(db.Model, UserMixin):  # UserMixin 상속받기
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=True)
    created_time = db.Column(db.DateTime, nullable=False, server_default=func.now())

    # profile = db.relationship('UserProfile', back_populates='user', uselist=False)

    # 사용할 orm 메서드 정의
    def get_id(self):
        return self.id

    # db 추가 후 커밋을 하나의 메서드로 정의
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


# 보유 장소 리스트와 테이블 연결
class UserProfile(db.Model):
    __tablename__ = 'user_profile'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    nickname = db.Column(db.String(20), unique=True, nullable=True)
    profile_image = db.Column(db.String(255), nullable=True)
    active_area = db.Column(db.String(30), nullable=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class PlacesFolder(db.Model):
    __tablename__ = 'places_folder'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    folder_name = db.Column(db.String(20), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Place(db.Model):
    __tablename__ = 'place'

    id = db.Column(db.Integer, primary_key=True)
    folder_id = db.Column(db.Integer, db.ForeignKey('places_folder.id'), nullable=False)
    place_name = db.Column(db.String(50), nullable=False)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class PlaceInfo(db.Model):
    __tablename__ = 'place_info'

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)
    place_image = db.Column(db.String(255), nullable=True)
    place_desc = db.Column(db.String(255), nullable=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
