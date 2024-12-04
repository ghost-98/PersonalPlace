from flask import Blueprint, request, render_template, jsonify

from app import db
from app.models.models import User, PlacesFolder, Place, PlaceInfo

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
def maps_main():
    if request.method == 'GET':
        return render_template('main/maps_main.html')


# 내 장소 관리 페이지
@main.route('/my_places', methods=['GET'])
def my_places():
    if request.method == 'GET':
        return render_template('main/my_places.html')


#### 내 장소 관리 페이지 기능 API들 ####
@main.route('/get_folders')
def get_folders():
    user = User.query.first()  # 현재 사용자 (로그인된 사용자로 변경 필요)
    folders = PlacesFolder.query.filter_by(owner_id=user.id).all()
    folder_data = [{'id': folder.id, 'name': folder.folder_name} for folder in folders]
    return jsonify({'folders': folder_data})


# 폴더 생성
@main.route('/create_folder', methods=['POST'])
def create_folder():
    data = request.get_json()
    folder_name = data.get('name')

    user = User.query.first()  # 현재 사용자 (로그인된 사용자로 변경 필요)

    # 새 폴더 생성
    new_folder = PlacesFolder(owner_id=user.id, folder_name=folder_name)
    new_folder.save_to_db()

    return jsonify({'message': '폴더가 성공적으로 생성되었습니다'})


# 장소 추가
@main.route('/add_place/<folder_id>', methods=['POST'])
def add_place(folder_id):
    data = request.get_json()
    place_name = data.get('name')

    # 새 장소 생성
    new_place = Place(folder_id=folder_id, place_name=place_name)
    new_place.save_to_db()

    return jsonify({'message': '장소가 성공적으로 추가되었습니다'})


# 장소에 정보 추가 (이미지, 설명)
@main.route('/add_place_info/<int:place_id>', methods=['POST'])
def add_place_info(place_id):
    data = request.get_json()
    place_image = data.get('image')
    place_desc = data.get('desc')

    # 장소에 대한 상세 정보 추가
    place_info = PlaceInfo(place_id=place_id, place_image=place_image, place_desc=place_desc)
    place_info.save_to_db()

    return jsonify({'message': '장소 정보가 성공적으로 추가되었습니다'})
