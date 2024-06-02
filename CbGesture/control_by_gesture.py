import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time
import mode

last_gesture_time = time.time()
last_gesture = -1
start_time = None
display_text = ""

c_mode=0

# 손동작을 나타내는 딕셔너리를 정의합니다.
gesture = {
    0:'fist', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
    6:'six', 7:'rock', 8:'spiderman', 9:'yeah', 10:'ok',
    13:'thumbleft', 14:'thumbright', 15:'swiperight', 16:'swiperleft',17:'heart'
}

# MediaPipe 손 모델을 초기화합니다.
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# 손동작 인식 모델을 학습합니다.
file = np.genfromtxt('data/gesture_train_fy.csv', delimiter=',')
angle = file[:,:-1].astype(np.float32)
label = file[:, -1].astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(angle, cv2.ml.ROW_SAMPLE, label)

# 웹캠에서 영상을 캡처합니다.
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        continue

    # 이미지를 뒤집고, RGB로 변환합니다.
    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 손을 인식합니다.
    result = hands.process(img)

    # 이미지를 다시 BGR로 변환합니다.
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if result.multi_hand_landmarks is not None:
        for res in result.multi_hand_landmarks:
            # 각 관절의 위치를 저장합니다.
            joint = np.zeros((21, 3))
            for j, lm in enumerate(res.landmark):
                joint[j] = [lm.x, lm.y, lm.z]

            # 관절 간의 각도를 계산합니다.
            v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
            v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
            v = v2 - v1 # [20,3]
            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

            # 각도를 이용해 손동작을 인식합니다.
            angle = np.arccos(np.einsum('nt,nt->n',
                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]
            angle = np.degrees(angle) # Convert radian to degree
            data = np.array([angle], dtype=np.float32)
            ret, results, neighbours, dist = knn.findNearest(data, 3)
            idx = int(results[0][0])

            # 인식된 손동작에 따라 다른 동작을 수행합니다.
            current_time = time.time()
            #if current_time - last_gesture_time > 0.75:
            if   c_mode == 0:  # 모드 변경
                c_mode, last_gesture_time, last_gesture,text = mode.handle_mode0(c_mode, idx, last_gesture_time, last_gesture)
            elif c_mode == 1:  # 유튜브 모드
                c_mode, last_gesture_time, last_gesture,text= mode.handle_mode1(c_mode, idx, last_gesture_time, last_gesture)
            elif c_mode == 2:  # 웹서핑 모드
                c_mode, last_gesture_time, last_gesture,text= mode.handle_mode2(c_mode, idx, last_gesture_time, last_gesture)
            elif c_mode == 3:  # 모드3
               c_mode, last_gesture_time, last_gesture,text= mode.handle_mode3(c_mode, idx, last_gesture_time, last_gesture)
            

            # 현재 모드와 제스쳐 상태를 화면에 표시합니다.
            cv2.putText(img, 'Mode: ' + mode.mode_descriptions[c_mode], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(img, 'Gesture: ' + mode.gesture_descriptions[c_mode].get(idx, 'Unknown Gesture'), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            # 새로운 텍스트가 들어온 경우
            if text != display_text:
                start_time = time.time()  # 텍스트를 출력할 시작 시간을 업데이트합니다.
                display_text = text  # 출력할 텍스트를 업데이트합니다.

            # 현재 시간과 텍스트를 출력할 시작 시간의 차이가 0.5초 이하인 경우에만 텍스트를 출력합니다.
            if start_time is not None and time.time() - start_time <= 0.5:
                cv2.putText(img, display_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)
            else:
                display_text = ""  # 0.5초가 지난 후에는 출력할 텍스트를 지웁니다.
            # 손동작을 화면에 그립니다.
            mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

    # 이미지를 화면에 표시합니다.kkkk
    cv2.imshow('Game', img)
    if cv2.waitKey(1) == ord('q'):
        break