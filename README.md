# PersonalPlace

### 1. 주제 소개
- 가봤거나 가보고 싶은 장소들을 다양한 카테고리에 따라 나만의 명칭으로 관리하고자 만들게 되었습니다. 
- 로그인 후 자유로이 장소 폴더를 생성 삭제등 관리하고 원하는 장소를 자유롭게 담을 수 있습니다.

### 2. 주요 기능
- 세션 기반의 회원가입, 로그인, 로그아웃 기능을 만들었습니다
- Kakao maps API를 가져와서 장소 검색 및 장소 정보를 가져와 저장했습니다
- DB(SQLITE)에 유저의 정보와 폴더, 장소 정보등을 저장했습니다

### 3. 화면 설명

<hr/>

* 최초 메인 화면 <br/>
  <img src="./Image/메인 화면.png" width="300px" height="200px" alt="main page"></img><br/>
  - 네비게이션 바가 있고, PersonalPlace 로고를 누르면 지금의 메인화면으로 리다이렉트 하고, 로그인이 되어있을때는 {사용자 이름}님 안녕하세요 인삿말과 로그아웃 버튼이 있고, 로그인이 안되어있으면 로그인과 회원가입 버튼만 있고 아래의 지도 보기와 내 장소 보기를 클릭해 이동하려고 할 시 로그인 화면으로 이동함
  - 로그인 후 지도 보기와 내 장소 보기 버튼을 누르면 각각의 화면으로 이동함


* 로그인 화면 <br/>
  <img src="./Image/로그인 화면.png" width="300px" height="200px" alt="login page"></img><br/>
  - 로그인이 되어있으면 페이지 어느 곳에서도 로그인 화면으로 이동할 수 있는 버튼이 뜨지 않음
  - 네비게이션 바와 로그인 페이지 하단에 회원가입 버튼이 있고 정보 입력 후 로그인 버튼을 누르면 로그인 된 상태로 메인 화면으로 이동, 정보가 틀리면 그에 맞는 경고 창이 뜸
  - 왼쪽 상단에 PersonalPlace 버튼을 누르면 메인 화면으로 이동


* 회원가입 화면 <br/>
  <img src="./Image/회원가입 화면.png" width="300px" height="200px" alt="signup page"></img><br/>
  - 네비게이션 오른쪾과 페이지 하단에 로그인 페이지로 이동 가능한 버튼이 있음
  - 정보 작성 후 회원가입 버튼 누르면 성공 시 로그인 페이지로 이동
  - 아이디 혹은 전화번호가 중복 될 시 회원가입이 되지 않음


* 지도 화면 <br/>
  <img src="./Image/지도 화면.png" width="300px" height="150px" alt="maps page"></img><br/>
  - 네비게이션바 오른쪽에 유저 인삿말, 내장소 관리로 이동 가능한 버튼과 로그아웃 버튼이 존재 (로그인 된 상태에서만 접근 가능한 화면임)
  - 기본 장소 검색 화면이 있고 내 폴더를 누르면 내가 가진 폴더의 리스트가 뜸


* 지도 검색 화면 <br/>
  <img src="./Image/검색 화면.png" width="300px" height="150px" alt="maps search page"></img><br/>
  - 장소 검색시 검색된 장소를 모두 포함한 배율로 지도가 표시되고, 장소들의 이름과 마커가 다 표시됨. 장소 검색 창 밑에는 검색 결과와 해당하는 상세정보들이 뜸
  - 다수의 검색 결과 장소 중 하나를 클릭하면 그것만 남고 지도에서도 그 장소만 확대해서 마커 표시함


* 장소 추가 화면 <br/>
  <img src="./Image/장소 추가 화면.png" width="300px" height="150px" alt="add place page"></img><br/>
  - 검색된 장소 오른쪽에 뜨는 추가 버튼을 누르면 내가 가진 폴더에 장소를 저장할 수 있는 모달 창이 뜸
  - 내가 가지고 있는 폴더 중에 추가도 가능하고, 새 폴더를 생성해서 추가하는 것도 가능함
  - 추가 시 모달 창은 자동으로 사라짐


* 지도에서 내 폴더 확인 화면 <br/>
  <img src="./Image/지도 화면에서 내폴더 확인.png" width="300px" height="150px" alt="my folder in maps page"></img><br/>
  - 네비게이션 바 밑의 내 폴더 버튼을 누르면 내가 가진 폴더 리스트 화면으로 바뀜   


* 내 장소 관리 화면 <br/>
  <img src="./Image/내 장소 관리 화면.png" width="300px" height="150px" alt="my place management page"></img><br/>
  - 네비게이션 바 오른쪽에 지도 페이지로 넘어갈 수 있는 버튼이 있음
  - 새로운 폴더를 생성 가능하고, 기존에 내 폴더들을 관리 가능함
  - 기존 폴더의 이름 변경, 폴더 삭제, 폴더의 장소 목록 확인 가능   


* 내 장소 관리 폴더 화면 <br/>
  <img src="./Image/내 장소 관리 세부 화면.png" width="300px" height="150px" alt="my place management folder page"></img><br/>
  - 폴더 클릭시 폴더 안에 있는 장소 목록이 스크롤 됨
  - 원하는 장소들을 중복 체크해서 삭제 가능


### 4. 라이 센스 및 레포지터리 주소
- 라이센스 : MIT License
- 레포지터리 주소 : https://github.com/ghost-98/PersonalPlace.git
