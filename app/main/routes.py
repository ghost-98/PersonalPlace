from flask import Blueprint, request, render_template, jsonify
from flask_login import login_required, current_user

from app.models.models import User, PlacesFolder, Place, PlaceInfo
from app import db

# root/__init__.py의 app.register_blueprint와 매핑
main = Blueprint('main', __name__)


# 초기 페이지
@main.route('/', methods=['GET'])
def home():
    # 메서드 GET일때
    if request.method == 'GET':
        return render_template('main/index.html')


# 초기 지도 페이지
@main.route('/maps_main', methods=['GET'])
@login_required
def maps_main():
    if request.method == 'GET':
        return render_template('main/maps_main.html')


# 내 장소 관리 페이지
@main.route('/my_places', methods=['GET'])
@login_required
def my_places():
    if request.method == 'GET':
        return render_template('main/my_places.html')


#### 내 장소 관리 페이지 기능 API들 ####
@main.route('/get_folders')
@login_required
def get_folders():
    user = current_user  # 현재 사용자

    folders = PlacesFolder.query.filter_by(owner_id=user.id).all()
    folder_data = [{'id': folder.id, 'name': folder.folder_name} for folder in folders]
    return jsonify({'folders': folder_data})


# 폴더 생성
@main.route('/create_folder', methods=['POST'])
@login_required
def create_folder():
    data = request.get_json()
    folder_name = data.get('name')

    user = current_user

    # 새 폴더 생성
    new_folder = PlacesFolder(owner_id=user.id, folder_name=folder_name)
    new_folder.save_to_db()

    return jsonify({'message': '폴더가 성공적으로 생성되었습니다'})


# 폴더 삭제
@main.route('/remove_folder/<int:folder_id>', methods=['DELETE'])
@login_required
def remove_folder(folder_id):
    folder = PlacesFolder.query.get(folder_id)
    if folder and folder.owner_id == current_user.id:
        db.session.delete(folder)
        db.session.commit()
        return jsonify({'message': '폴더가 삭제되었습니다'})
    return jsonify({'message': '폴더를 찾을 수 없습니다'}), 404


# 폴더의 장소 가져오기
@main.route('/get_places/<int:folder_id>', methods=['GET'])
@login_required
def get_places(folder_id):
    places = Place.query.filter_by(folder_id=folder_id).all()
    place_data = [{'id': place.id, 'name': place.place_name} for place in places]
    return jsonify({'places': place_data})


# 폴더에 장소 추가
@main.route('/add_place/<folder_id>', methods=['POST'])
@login_required
def add_place(folder_id):
    data = request.get_json()
    place_name = data.get('name')

    # 새 장소 생성
    new_place = Place(folder_id=folder_id, place_name=place_name)
    new_place.save_to_db()

    return jsonify({'message': '장소가 성공적으로 추가되었습니다'})


# 폴더에서 장소 삭제
@main.route('/remove_place/<int:place_id>', methods=['DELETE'])
@login_required
def remove_place(place_id):
    place = Place.query.get(place_id)
    if place:
        db.session.delete(place)
        db.session.commit()
        return jsonify({'message': '장소가 삭제되었습니다'})
    return jsonify({'message': '장소를 찾을 수 없습니다'}), 404


# 장소에 정보 추가 (이미지, 설명)
@main.route('/add_place_info/<int:place_id>', methods=['POST'])
@login_required
def add_place_info(place_id):
    data = request.get_json()
    place_image = data.get('image')
    place_desc = data.get('desc')

    # 장소에 대한 상세 정보 추가
    place_info = PlaceInfo(place_id=place_id, place_image=place_image, place_desc=place_desc)
    place_info.save_to_db()

    return jsonify({'message': '장소 정보가 성공적으로 추가되었습니다'})
