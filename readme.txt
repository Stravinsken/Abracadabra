1. project_root라는 상위 폴더를 만든다.
2. 그 안에 각 파일 압축 푼다. (project_root 안에 frontend와 backend 폴더 존재)
3. 그다음 vs code로 터미널 실행하여 project root 경로에서 
python -m venv venv
를 실행하여 가상공간 환경을 다운로드 한다.
4. pip install uvicorn[standard]
WebSocket 라이브러리 설치
uvicorn에서 WebSocket을 지원하도록 필수 라이브러리를 설치해야 한다.
5. venv\Scripts\activate
로 가상공간 활성화한다. (경로의 앞에 venv가 붙으면 성공)
6. pip install -r requirements.txt
로 의존성 파일 다운
7. uvicorn main:app --reload
로 백엔드 서버 실행
8. frontend 경로에서 npm start 하면 웹이 실행
9. 검지 손가락을 웹캠에 인식시켜 선이 그려지는지 확인
