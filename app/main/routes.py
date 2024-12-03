from flask import Blueprint, request, render_template

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
