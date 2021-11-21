# 🎊 Wanted X Wecode PreOnBoarding Backend Course | 무한루프 팀

원티드 3주차 기업 과제 : Deer Corporation Assignment Project
✅ 디어코퍼레이션 기업 과제입니다.

- [디어코퍼레이션 사이트](https://web.deering.co/)
- [디어코퍼레이션 채용공고 링크](https://www.wanted.co.kr/wd/59051)

<br>
<br>

# 🔖 목차

- Team 소개
- 과제 내용
- 기술 환경 및 tools
- 모델링 ERD
- API 명세서
- 기능 구현 추가설명
- 설치 및 실행 방법

<br>
<br>

# 🧑‍🤝‍🧑 Team 소개

|                      이름                      |                                    담당 기능                                    | 블로그 |
| :--------------------------------------------: | :-----------------------------------------------------------------------------: | :----: |
|                      공통                      | 초기환경 설정, DB 모델링, postman api 문서 작성, README.md 작성, 배포, UnitTest |   X    |
|       [유동헌](https://github.com/dhhyy)       |                                킥보드 대여 기능                                 |        |
|     [하예준](https://github.com/TedJunny)      |                      유저 인증 기능, 서비스 지역 생성 기능                      |        |
|      [송치헌](https://github.com/Oraange)      |                 킥보드 반납 및 요금 정책에 따른 요금 계산 기능                  |
| [오지윤(팀장)](https://github.com/Odreystella) |            할인/벌금 수정 기능, 지역에 추가되는 할인/벌금 수정 기능             |        |
|    [손희정](https://github.com/heejung-gjt)    |            할인/벌금 추가 기능, 지역에 추가되는 할인/벌금 추가 기능             |        |

<br>
<br>

# 📖 과제 내용

> 디어는 사용자의 요금을 계산하기 위해 다양한 상황을 고려합니다.

### **[필수 포함 사항]**

- README 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

### **[개발 요구 사항]**

- 지역별로 다양한 요금제 적용 기능
- 다양한 할인/벌금 조건 추가 기능
- 킥보드 고장시 1분 이내 요금 청구되지 않는 기능

- 확장성을 고려한 시스템 설계 및 구현
- 새로운 할인이나 벌금 조건이 쉽게 추가될 수 있는 기능

### **[기능 개발]**

✔️ **REST API 기능**

- 유저 Auth

  - 회원가입 API
  - 로그인 API

- 할인 / 벌금 CRUD

  - 할인 조건 추가 API
  - 벌금 조건 추가 API
  - 할인 조건 변경 API
  - 벌금 조건 변경 API

- 킥보드 대여 및 반납

  - 킥보드 대여 API
  - 킥보드 반납 요금 정책에 따른 요금 계산 API

- 위치 정보 CRUD
  - 서비스 지역 생성 API
  - 지역에 추가되는 할인 / 벌금 추가 API
  - 지역에 추가되는 할인 / 벌금 삭제 API

<br>
<br>

# ➡️ Build(AWS EC2)

API URL : http://3.38.118.39:8000

<br>
<br>

# ⚒️ 기술 환경 및 tools

- Back-End: Python 3.9.7, Django 3.2.9
- Deploy: AWS EC2, RDS
- ETC: Git, Github, Postman

<br>
<br>

# 📋 모델링 ERD

[Aquerytool URL](https://aquerytool.com/aquerymain/index/?rurl=d7b4f6b6-8da4-4af4-9d3c-fa27b6ed3b26&)  
Password : 70pd61

![디어db](https://user-images.githubusercontent.com/77820352/142776533-9e4fbb89-2037-4da2-9f50-fa0a141027f7.png)

<br>
<br>

# 🌲 디렉토리 구조

```
├── areas
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── charges
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── CONVENTION.md
├── core
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── utils.py
│   ├── validation.py
│   └── views.py
├── manage.py
├── my_settings.py
├── PULL_REQUEST_TEMPLATE.md
├── README.md
├── requirements.txt
├── users
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── vehicles
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

<br>
<br>

# 🔖 API 명세서

[Postman API Document 보러가기](https://documenter.getpostman.com/view/14348138/UVJWqfGC)

<br>

### 👉 회원가입/로그인

[회원가입]

1. 유저 인증 처리를 위해 회원가입 API
2. 유저의 이름과 이메일, 휴대폰 번호를 요청 본문에 담으면 가입된다.

- Method: POST

```
http://3.38.118.39:8000/users/signup
```

<br>

- parameter : request_body

```
{
    "name": "관리자2",
    "email": "hayejun10@server.co.kr",
    "phone_number": "010-2222-3333"
}
```

<br>

- response

```
{
    "message": "SUCCUESS"
}
```

<br>

[로그인]

1. 유저의 이메일과 휴대폰 번호를 통해서 User Auth 검증 한다.
2. 로그인 성공 시, user_id 정보를 담은 access_token을 반환한다.

- Method: POST

```
http://3.38.118.39:8000/users/signin
```

<br>

- parameter : request_body

```
{
    "email": "hayejun1013@naver.com",
    "phone_number": "010-2723-4713"
}
```

<br>

- response

```
{
    "message": "Success",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiOWNlZjllMDItMTA2ZC00MjQ4LWIyMTItMzUyMjc1OTBlYzFjIn0.8ubSxYVGeyGAjgGkb1DxCsc9uw2i27ihhksFBhlJ3Mg"
}
```

<br>

### 👉 할인 / 벌금 조건 추가 기능

[할인 조건 추가]

1. 관리자가 할인 조건을 추가하기 위해 요청한다.
1. 벌금 퍼센트와 벌금 코드를 body에 담아 요청합니다.
1. 관리자 외 유저가 추가할 시 에러를 반환한다.
1. 할인 코드형식(D-P-1)이 다를 시 에러를 반환한다.
1. 이미 존재하는 할인시 에러를 반환한다.

<br>

- Method: POST

```
http://3.38.118.39:8000/charges/discount
```

<br>

- header : Bearer token
- parameter : request_body

```
{
    "code": "D-P-1",
    "number": 30,
    "description": "주차구역 반납"
}
```

<br>

- response

```
{
    "message": "SUCCESS"
}
```

<br>

[벌금 조건 추가]

1. 관리자가 벌금 조건을 추가하기 위해 요청한다.
1. 벌금 퍼센트와 벌금요금 코드를 body에 담아 요청합니다
1. 관리자 외 유저가 추가할 시 에러를 반환한다.
1. 벌금 코드형식(D-P-1)이 다를 시 에러를 반환한다.
1. 이미 존재하는 벌금시 에러를 반환한다.

<br>

- Method: POST

```
http://3.38.118.39:8000/charges/penalty
```

<br>

- header : Bearer token
- parameter : request_body

```
{
    "code": "P-A-1",
    "number": 10000,
    "description": "서비스 지역 이탈 요금 부과"
}
```

<br>

- response

```
{
    "message": "SUCCESS"
}
```

<br>

### 👉 할인 / 벌금 조건 변경 기능

[할인 조건 변경]

1. 관리자만이 할인 조건 변경할 수 있다.
1. 패스 파라미터로 변경할 할인의 코드를 보낸다.
1. 할인 조건에 대한 금액과 설명을 body에 담아 요청한다.
1. 관리자 외 유저가 수정 시 에러를 반환한다.
1. 할인 조건에 대한 id가 없을 시 에러를 반환한다.

<br>

- Method: PUT

```
http://3.38.118.39:8000/charges/discount/D-P-1
```

<br>

- header : Bearer token
- parameter : request_body
- path parameter : 요금code

```
{
    "number" : 20,
    "description" : "주차구역 반납"
}
```

<br>

- response

```
{
    "message": "SUCCESS"
}
```

<br>

[벌금 조건 변경]

1. 관리자만이 벌금 조건 변경할 수 있다.
1. 패스 파라미터로 변경할 벌금의 코드를 보낸다.
1. 벌금 조건에 대한 금액과 설명을 body에 담아 요청한다.
1. 관리자 외 유저가 수정 시 에러를 반환한다.
1. 벌금 조건에 대한 id가 없을 시 에러를 반환한다.

<br>

- Method: PUT

```
http://3.38.118.39:8000/charges/penalty/P-A-1
```

<br>

- header : Bearer token
- parameter : request_body
- path parameter : 요금code

```
{
    "number" : 6000,
    "description" : "서비스 지역 이탈 요금 부과"
}
```

<br>

- response

```
{
    "message": "SUCCESS"
}
```

<br>

### 👉 킥보드 대여 기능

1. 패스 파라미터로 킥보드 아이디를 받아 킥보드 대여를 시작한다.
2. 대여가 됨과 동시에 유저 아이디를 통해 사용자를 확인한다.
3. 만약 킥보드가 이미 사용 중일 경우 에러를 발생한다.
4. 만약 킥보드 아이디가 잘 못 전달되면 에러를 발생한다.

<br>

- Method: POST

```
http://3.38.118.39:8000/vehicles/lend
```

<br>

- header : Bearer token
- parameter : request_body

```
{
    "deer_name": "씽씽이"
}
```

<br>

- response

```
{
    "message": "SUCCESS"
}
```

<br>

### 👉 킥보드 반납 기능

1. 킥보드를 반납할 시 요금 계산 하는 API
1. 킥보드를 반납할 경우, Path Parameter에 vehicle_id를 받는다.
1. 킥보드 반납 지점에 대해 end_lat(위도), end_lng(경도)를 Payload Body로 값을 전달 받고, API 호출시 반납 시간이 자동으로 저장된다.
1. 반납 지점이 지역을 이탈하여 주차하면, 거리에 비례하여 요금을 계산한다.
1. 주차 금지 구역에 반납하면 일정 금액 벌금을 추가한다.
1. 파킹존에 반납하면, 일정 금액 할인이 적용되고 이용 시간에 따라 금액이 책정된다.

<br>

- Method: PATCH

```
http://3.38.118.39:8000/vehicles/return/50cc196d-3f0b-4b2c-9052-c61af5c35505
```

<br>

- header : Bearer token
- parameter : request_body

```
{
    "end_lat": 37.507649215664735,
    "end_lng": 126.88256263732909
}
```

<br>

- response

```
{
    "message": "UPDATED"
}
```

<br>

### 👉 서비스 지역 추가 기능

```
 # DB에 생성된 할인/벌금 Object
 "D-P-1" - 파킹존 주차 할인
 "P-A-1" - 지역 이탈 벌금
 "P-P-1" - 금지 구역에 주차
```

1. 서비스 지역 데이터를 추가할 수 있는 API
1. 추가하고자 하는 지역의 이름을 name으로 전달한다.
1. boundary에 이중 리스트 형식의 위도, 경도 데이터를 보내면 polygon 데이터로 바뀌어서 서비스 지역 영역이 저장된다.
1. Polygon 형태의 데이터로 저장하기 위해서는 첫 번째로 들어온 위도, 경도와 마지막으로 들어온 위도, 경도 데이터가 같아야 한다.
1. 서비스 지역 영역의 중심 Point 정보는 center로 보낸다.
1. 서비스 지역을 생성하면서 해당 지역의 할인 / 벌금 조건을 연결 시킬 수 있다.
1. code에 리스트로 할인 / 벌금 객체의 ID를 전달한다.

- Method: POST

```
http://3.38.118.39:8000/areas/service/b1d96ffe56cd441bb12e789199f419de
```

<br>

- header : Bearer token
- parameter : request_body

```
{
    "name": "신도림_3",
    "boundary": [
        [
            126.88183307647704,
            37.515121399458664
        ],
        [
            126.87754154205322,
            37.51101945039516
        ],
        [
            126.87490224838255,
            37.50712153887425
        ],
        [
            126.87981605529784,
            37.50303617298528
        ],
        [
            126.89022302627565,
            37.51027052249435
        ],
        [
            126.88659667968751,
            37.512534304312624
        ],
        [
            126.88183307647704,
            37.515121399458664
        ]
    ],
    "center": [
        26.8819327474983,
        37.5091695751726
    ],
    "code": [
        "D-P-5",
        "P-A-3",
        "P-P-2"
    ]
}
```

<br>

- response

```
{
  "message": "신도림_1_ALREADY_REGISTERED"
}

```

<br>

### 👉 서비스 지역에 할인 / 벌금 추가

1. 관리자가 지역에 할인 / 벌금을 추가하기 위해 요청한다.
2. 관리자 외 유저가 추가 시 에러를 반환한다.
3. 할인 / 벌금에 대한 id가 없을 시 에러를 반환한다.
4. 존재하지 않은 코드시 에러를 반환한다.
5. 존재하지 않은 지역시 에러를 반환한다.

<br>

- Method: POST

```
http://3.38.118.39:8000/areas/service
```

<br>

- header : Bearer token
- parameter : request_body
- query parameter : 지역 name

```
{
    "code": "P-P-7",
    "region": "강남"

```

<br>

- response

```
{
    "message": "SUCCESS"
}
```

<br>

### 👉 서비스 지역에 할인 / 벌금 삭제

1. 관리자가 지역에 할인 / 벌금을 삭제하기 위해 요청한다.
2. 관리자 외 유저가 삭제시 에러를 반환한다.
3. 할인 / 벌금에 대한 id가 없을 시 에러를 반환한다.
4. 존재하지 않은 코드시 에러를 반환한다.
5. 존재하지 않은 지역시 에러를 반환한다.

<br>

- Method: DELETE

```
http://3.38.118.39:8000/areas/service
```

<br>

- header : Bearer token
- parameter : request_body
- query parameter : 지역 name

```
{
    "region" : "신도림_1",
    "code" : "D-P-1"
}
```

<br>

- response

```
{
    "message": "SUCCESS"
}
```

<br>

# ➕ 기능 구현 추가설명

### [111111]

![query](https://user-images.githubusercontent.com/77820352/142777685-1a752bf3-8fd9-42a3-9ccb-b31c164daf82.png)
<br>

### [222222]

<br>

# 🔖 설치 및 실행 방법

### 로컬 및 테스트용

1. 해당 프로젝트를 clone하고, 프로젝트로 들어간다.

```
https://github.com/wanted-InfinityLoop/deer-InfinityLoop.git .
cd deer
```

2. 가상환경으로 miniconda를 설치한다. [Go](https://docs.conda.io/en/latest/miniconda.html)

```
conda create -n deer python=3.9
conda actvate deer
```

3. 가상환경 생성 후, requirements.txt를 설치한다.

```
pip install -r requirements.txt

Django==3.2.9
django-cors-headers==3.10.0
gunicorn==20.1.0
mysqlclient==2.1.0
PyMySQL==1.0.2
bcrypt==3.2.0
PyJWT==2.3.0

```

4. migrate 후 로컬 서버 가동

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
