// Kakao Maps API 초기화
var mapContainer = document.getElementById('map'); // 지도를 표시할 영역
var mapOptions = {
    center: new kakao.maps.LatLng(37.566535, 126.977969), // 기본 중심 좌표 (서울 시청)
    level: 3 // 확대 레벨
};
var map = new kakao.maps.Map(mapContainer, mapOptions); // 지도 생성

// Kakao Places API를 사용한 장소 검색
var ps = new kakao.maps.services.Places();

var markers = []; // 생성된 마커를 관리하는 배열
var bounds = new kakao.maps.LatLngBounds(); // 검색 결과를 모두 포함하도록 지도의 범위를 설정

function searchPlaces() {
    var keyword = document.getElementById('keyword').value.trim();
    if (!keyword) {
        alert('검색어를 입력하세요.');
        return;
    }

    ps.keywordSearch(keyword, function (data, status) {
        var resultsContainer = document.getElementById('search-results');
        resultsContainer.innerHTML = ''; // 기존 결과 제거

        if (status === kakao.maps.services.Status.OK) {
            removeAllMarkers(); // 이전 검색 결과의 마커 제거
            bounds = new kakao.maps.LatLngBounds(); // 새로운 범위 초기화

            data.forEach(place => {
                var item = document.createElement('div');
                item.className = 'result-item';
                item.innerHTML = `
                    <strong>${place.place_name}</strong><br>
                    ${place.address_name || '주소 정보 없음'}<br>
                    ${place.phone || '전화번호 정보 없음'}<br>
                    ${place.place_url}
                    <button class="btn btn-sm btn-primary mt-2" onclick="showFolderSelectModal(${place.id}, '${place.place_name}')">추가</button>

                `;
                item.onclick = function () {
                    focusOnPlace(place); // 클릭 시 해당 장소로 줌인 및 마커 제거
                };
                resultsContainer.appendChild(item);

                // 마커 생성 및 지도에 추가
                createMarker(place);
            });

            // 모든 마커가 보이도록 지도 범위 설정
            map.setBounds(bounds);
        } else {
            resultsContainer.innerHTML = '<p>검색 결과가 없습니다.</p>';
        }
    });
}

// 마커 생성 함수
function createMarker(place) {
    var position = new kakao.maps.LatLng(place.y, place.x);
    var marker = new kakao.maps.Marker({
        position: position,
        map: map
    });
    markers.push(marker); // 마커를 배열에 저장

    // 마커 위에 이름 표시
    var infowindow = new kakao.maps.InfoWindow({
        content: `<div style="padding:5px;">${place.place_name}</div>`
    });
    infowindow.open(map, marker);

    // 마커 위치를 지도의 범위에 포함
    bounds.extend(position);
}

// 모든 마커 제거
function removeAllMarkers() {
    markers.forEach(marker => marker.setMap(null)); // 지도에서 마커 제거
    markers = []; // 배열 초기화
}

// 특정 장소로 줌인 및 나머지 마커 제거
function focusOnPlace(place) {
    removeAllMarkers(); // 기존 마커 제거
    var position = new kakao.maps.LatLng(place.y, place.x);

    // 단일 마커 생성
    var marker = new kakao.maps.Marker({
        position: position,
        map: map
    });
    markers.push(marker); // 단일 마커를 배열에 추가

    // 지도 줌인 및 중심 이동
    map.setCenter(position);
    map.setLevel(3); // 지도 레벨(확대 정도) 설정

    // 장소 상세 정보 가져오기

}

function showFolderSelectModal(placeId, placeName) {
    fetch('/get_folders')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const folderList = document.getElementById('folder-list');
            folderList.innerHTML = '';

            data.folders.forEach(folder => {
                // 각 폴더 항목 생성
                const folderItem = document.createElement('li');
                folderItem.className = 'list-group-item d-flex justify-content-between align-items-center';

                folderItem.innerHTML = `
                    ${folder.name}
                    <button class="btn btn-sm btn-${folder.contains_place ? 'danger' : 'primary'}"
                        onclick="togglePlaceInFolder(${placeId}, '${placeName}', ${folder.id}, ${folder.contains_place})">
                        ${folder.contains_place ? '삭제' : '추가'}
                    </button>
                `;
                folderList.appendChild(folderItem);
            });

            // 모달 창 열기
            const modal = new bootstrap.Modal(document.getElementById('folder-modal'));
            modal.show();
        });
}

function togglePlaceInFolder(placeId, placeName, folderId, isContained) {
    const url = isContained ? `/remove_place/${folderId}` : `/add_place/${folderId}`;
    const method = isContained ? 'DELETE' : 'POST';

    fetch(url, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: placeName })
    }).then(response => response.json())
      .then(data => alert(data.message));
}

function createNewFolder() {
    const folderName = document.getElementById('new-folder-name').value.trim();
    if (!folderName) {
        alert('폴더 이름을 입력하세요.');
        return;
    }

    fetch('/create_folder', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: folderName })
    }).then(response => response.json())
      .then(data => {
          alert(data.message);
          showFolderSelectModal(); // 새로고침하여 폴더 목록 업데이트
      });
}

