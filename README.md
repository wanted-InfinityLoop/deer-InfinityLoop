# 🎊 Wanted X Wecode PreOnBoarding Backend Course | 무한루프 팀

원티드 3주차 기업 과제 :  Deer Corporation Assignment Project
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

| 이름 | 담당 기능 | 블로그 |
| :---: | :---: | :---: | 
| 공통 | 초기환경 설정, DB 모델링, postman api 문서 작성, README.md 작성, 배포, UnitTest | X |
| [유동헌](https://github.com/dhhyy) | 킥보드 대여 기능| |
| [하예준](https://github.com/TedJunny) | 유저 인증 기능, 서비스 지역 생성 기능 ||
| [송치헌](https://github.com/Oraange) |킥보드 반납 및 요금 정책에 따른 요금 계산 기능|
| [오지윤(팀장)](https://github.com/Odreystella) | 할인/벌금 수정 기능, 지역에 추가되는 할인/벌금 수정 기능 | |
| [손희정](https://github.com/heejung-gjt) | 할인/벌금 추가 기능, 지역에 추가되는 할인/벌금 추가 기능 |  |

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

- 킥보드 반납 및 요금 정책에 따른 요금 계산 API
- 서비스 지역 생성 API
- 킥보드 대여 API
- 할인/벌금 요금 추가 API
- 할인/벌금 요금 수정 API
- 지역에 추가되는 할인/벌금 추가 API
- 지역에 추가되는 할인/벌금 수정 API

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

![디어db](https://user-images.githubusercontent.com/64240637/142769570-d1caee18-1668-4f19-b92a-e00a70e5261d.png)

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

### 👉 킥보드 대여 기능

1. 로그인 한 유저가 대여할 킥보드를 요청한다.
2. 로그인 한 유저의 유효성 검증 후 존재하지 않는 유저의 경우 에러 메시지를 반환한다.
3. 존재하지 않는 킥보드시 에러 메시지를 반환한다. 

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

### 👉 서비스 지역 추가 기능


- Method: POST

```
http://3.38.118.39:8000/areas/service/f48d910f42cd487c89921fa6f8fee579
```

<br>

- header : Bearer token
- parameter : request_body


```
{
    "name": "여의도_2",
    "boundary": [
        [
            126.9191962480545,
            37.52151216125405
        ],
        [
            126.9208323955536,
            37.52151216125405
        ],
        [
            126.9208323955536,
            37.52279280068019
        ],
        [
            126.9191962480545,
            37.52279280068019
        ],
        [
            126.9191962480545,
            37.52151216125405
        ]
    ],
    "center": [
        126.92001700401306,
        37.52213333794024
    ],
    "code": []
}
```

<br>

- response

```

```

<br>

### 👉 할인/벌금 요금 조건 추가기능

[할인요금 추가]

1. 관리자가 할인 요금 조건을 추가하기 위해 요청한다.
2. 관리자 외 유저가 요금을 추가할 시 에러를 반환한다.
3. 할인요금 코드형식이 다를 시 에러를 반환한다.
4. 이미 존재하는 할인요금시 에러를 반환한다.

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
    "code": "D-P-7",
    "number": 10,
    "description": "파킹 할인 유형7"
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

[벌금요금 추가]

1. 관리자가 벌금요금 조건을 추가하기 위해 요청한다.
2. 관리자 외 유저가 요금을 추가할 시 에러를 반환한다.
3. 벌금요금 코드형식이 다를 시 에러를 반환한다.
4. 이미 존재하는 벌금요금시 에러를 반환한다.

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
    "code": "P-P-19",
    "number": 1000,
    "description": "파킹 벌금 유형1"
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

### 👉 할인/벌금 요금 조건 수정기능

[할인요금 수정]

1. 관리자가 할인 요금 조건을 수정하기 위해 요청한다.
2. 관리자 외 유저가 요금 수정 시 에러를 반환한다.
3. 할인조건에 대한 id가 없을 시 에러를 반환한다.

<br>

- Method: POST
```
http://3.38.118.39:8000/charges/discount/D-P-1
```

<br>

- header : Bearer token
- parameter : request_body
- path parameter : 요금code


```
{
    "number" : 30,
    "description" : "주차존 반납"
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

[벌금요금 수정]

1. 관리자가 벌금 요금 조건을 수정하기 위해 요청한다.
2. 관리자 외 유저가 요금 수정 시 에러를 반환한다.
3. 벌금조건에 대한 id가 없을 시 에러를 반환한다.

<br>

- Method: POST
```
http://3.38.118.39:8000/charges/penalty/P-P-1
```

<br>

- header : Bearer token
- parameter : request_body
- path parameter : 요금code


```
{
    "number" : 6000,
    "description" : "반납금지지역 반납"
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


### 👉 서비스 지역에 할인/벌금 요금 추가

1. 관리자가 지역에 할인/벌금요금을 추가하기 위해 요청한다.
2. 관리자 외 유저가 요금 추가 시 에러를 반환한다.
3. 할인/벌금조건에 대한 id가 없을 시 에러를 반환한다.
4. 존재하지 않은 요금 코드시 에러를 반환한다.
5. 존재하지 않은 지역시 에러를 반환한다.

<br>

- Method: POST

```
http://3.38.118.39:8000/areas/event?region=강남  
```

<br>

- header : Bearer token
- parameter : request_body
- query parameter : 지역 name


```
{
    "code": "P-P-5"
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


### 👉 서비스 지역에 할인/벌금 요금 수정

1. 관리자가 지역에 할인/벌금요금을 수정하기 위해 요청한다.
2. 관리자 외 유저가 요금 수정 시 에러를 반환한다.
3. 할인/벌금조건에 대한 id가 없을 시 에러를 반환한다.
4. 존재하지 않은 요금 코드시 에러를 반환한다.
5. 존재하지 않은 지역시 에러를 반환한다.

<br>

- Method: POST

```
http://3.38.118.39:8000/areas/ 
```

<br>

- header : Bearer token
- parameter : request_body
- query parameter : 지역 name


```
{
    "code": "P-P-5"
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


- Method: POST

```
http://3.38.118.39:8000/charges/<str:vehicle_id>  
```

<br>

- header : Bearer token
- parameter : request_body
- path parameter : 킥보드 id


```
{
    "code": "P-P-5"
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
<br>

# ➕ 기능 구현 추가설명

### [111111]

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



