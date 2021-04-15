# swiftStock_Server
주린이 앱에서 종목코드를 request로 받아서 받은 종목코드에 대하 주식 정보(시가, 고가, 저가, 종가, 거래량)을 response로 앱으로 보내는 기능을 함.

## 중계 서버 환경
1. flask - REST API 를 이용해 백엔드 서버 생성
2. pandas_datareader - 실시가 주식 정보를 받아오는 게 사실사 불가능해서 python 라이브러리에서 제공하는 api에 요청을 보내 주식 정보를 가져옴.

## 종목 코드 데이터 베이스
1. FirebaseDatabase 이용


