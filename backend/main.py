'''
# main.py (FastAPI 백엔드)
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from hand_tracking import HandTracker  # 손동작 추적 모듈

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket 경로
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    hand_tracker = HandTracker()  # 손동작 추적 객체 생성

    try:
        while True:
            # 손동작 데이터 감지
            data = hand_tracker.get_hand_position()  # 좌표 데이터 가져오기
            if data:
                await websocket.send_json({"type": "hand_position", "data": data})
            await asyncio.sleep(0.033)  # 약 30FPS로 데이터 전송
    except Exception as e:
        print(f"WebSocket 연결 종료: {e}")
        await websocket.close()
'''
# main.py (FastAPI 백엔드)
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from hand_tracking import HandTracker  # 손동작 추적 모듈

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 앱 URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    hand_tracker = HandTracker()

    try:
        while True:
            index_finger_position = hand_tracker.get_index_finger_position()
            if index_finger_position:
                await websocket.send_json({"type": "hand_position", "data": index_finger_position})
            # FPS를 자연스럽게 조정
            await asyncio.sleep(0.016)  # 약 60FPS
    except Exception as e:
        print(f"WebSocket 연결 종료: {e}")
        await websocket.close()

