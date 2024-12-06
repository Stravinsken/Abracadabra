'''
# hand_tracking.py
import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)  # 웹캠 초기화

    def get_hand_position(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        positions = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = frame.shape
                    x, y = int(lm.x * w), int(lm.y * h)
                    positions.append({"x": x, "y": y})
        
        return positions
'''
import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,  # 실시간으로 연속된 프레임 처리
            max_num_hands=1,         # 한 손만 추적
            min_detection_confidence=0.5,  # 손 검출 임계값
            min_tracking_confidence=0.5    # 추적 성공 임계값
        )
        self.cap = cv2.VideoCapture(0)  # 웹캠 초기화
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 해상도 축소
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def get_index_finger_position(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        # 해상도 축소로 처리 속도 향상
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_tip = hand_landmarks.landmark[8]
                h, w, _ = frame.shape
                x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                return {"x": x, "y": y}
        return None
