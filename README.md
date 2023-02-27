<!-- Title Start -->
<div align="center">

# PCS - TVWebConsole
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=Flask&logoColor=white"/>
</div>
<!-- Title End -->

<!-- Body Start -->
<div align="left">

## Introduce
TV에 내장 되어 있는 브라우저 혹은 라즈베리파이를 이용하여 웹 서버에 접속하여 영상을 재생하고   
휴대폰이나 컴퓨터 등에서 TV 웹 콘솔에 접속하여 재생 중인 영상을 변경 할 수 있도록 만든 시스템입니다.    

## Installation
```
pip install -r requirements.txt
```

## Run
### Server(PC)
```bat
cd Server
py app.py
```
### Client(TV)
Server 콘솔 창에 있는 `http://*.*.*.*/` 으로 웹 브라우저를 실행하여 접속 할 수 있습니다.

## Update Video(PC, Mobile, etc...)
`http://*.*.*.*/console` 으로 접속하여 재생 중인 영상과 업로드 할 영상을 선택 할 수 있습니다.   
```
기초 아이디 : admin
기초 패스워드 : twc
```

</div>
<!-- Body End -->