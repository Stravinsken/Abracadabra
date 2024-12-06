/*
// App.js (React 프론트엔드)
import React, { useEffect, useRef } from "react";

const App = () => {
  const canvasRef = useRef(null);
  const socketRef = useRef(null);

  useEffect(() => {
    // WebSocket 연결
    socketRef.current = new WebSocket("ws://127.0.0.1:8000/ws");

    // WebSocket 메시지 수신
    socketRef.current.onmessage = (event) => {
      const message = JSON.parse(event.data);
      if (message.type === "hand_position") {
        drawHandPosition(message.data);
      }
    };

    // WebSocket 연결 해제
    return () => {
      if (socketRef.current) {
        socketRef.current.close();
      }
    };
  }, []);

  const drawHandPosition = (positions) => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    // 캔버스 초기화
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 손 좌표 그리기
    positions.forEach((pos) => {
      ctx.beginPath();
      ctx.arc(pos.x, pos.y, 5, 0, 2 * Math.PI); // x, y 좌표에 원 그리기
      ctx.fillStyle = "black";
      ctx.fill();
    });
  };

  return (
    <div>
      <h1>Hand Drawing App</h1>
      <canvas
        ref={canvasRef}
        width={800}
        height={600}
        style={{ border: "1px solid black" }}
      ></canvas>
    </div>
  );
};

export default App;
*/
import React, { useEffect, useRef } from "react";

const App = () => {
  const canvasRef = useRef(null);
  const socketRef = useRef(null);
  const previousPositionRef = useRef(null); // 이전 좌표를 저장하는 Ref

  useEffect(() => {
    // WebSocket 연결
    socketRef.current = new WebSocket("ws://127.0.0.1:8000/ws");

    socketRef.current.onmessage = (event) => {
      const message = JSON.parse(event.data);
      if (message.type === "hand_position") {
        drawLine(message.data); // 선 그리기 함수 호출
      }
    };

    return () => {
      if (socketRef.current) {
        socketRef.current.close();
      }
    };
  }, []);

  const drawLine = (currentPosition) => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    // 이전 좌표가 없으면 현재 좌표를 저장하고 종료
    if (!previousPositionRef.current) {
      previousPositionRef.current = currentPosition;
      return;
    }

    // 선 그리기
    ctx.beginPath();
    ctx.moveTo(previousPositionRef.current.x, previousPositionRef.current.y); // 이전 좌표에서 시작
    ctx.lineTo(currentPosition.x, currentPosition.y); // 현재 좌표로 선 그리기
    ctx.strokeStyle = "blue"; // 선 색깔
    ctx.lineWidth = 2; // 선 두께
    ctx.stroke();

    // 현재 좌표를 이전 좌표로 저장
    previousPositionRef.current = currentPosition;
  };

  return (
    <div>
      <h1>Hand Drawing App</h1>
      <canvas
        ref={canvasRef}
        width={800}
        height={600}
        style={{ border: "1px solid black" }}
      ></canvas>
    </div>
  );
};

export default App;

