# ControlByGesture
mouse move, scroll and push shortcut key by gesture with MediaPipe
# 손동작 인식을 통한 제어 시스템(Hand Gesture Recognition with MediaPipe)

이 프로젝트는 MediaPipe와 OpenCV를 사용하여 손동작을 인식하고, 인식된 동작에 따라 다양한 작업을 수행하는 시스템입니다. YouTube 제어, 웹 서핑, 자동 스크롤 모드 등의 기능을 포함하고 있습니다.
This project is a hand gesture recognition system using MediaPipe and OpenCV. The system can detect various hand gestures and perform corresponding actions such as controlling YouTube, web surfing, and auto-scrolling modes.

## 설치 방법(Installation)   

필요한 라이브러리를 설치하려면 아래 명령어를 실행하세요:
To install the necessary dependencies, run the following command:
```bash
pip install opencv-python mediapipe numpy pyautogui   

# 사용 방법(Usage)

메인 파이썬 스크립트 control_by_gesture.py 를 실행하여 프로젝트를 사용합니다:

웹캠이 정상적으로 연결되어 있어야 합니다.
Ensure that you have a working webcam connected to your system.

## 설명(Description)
이 프로젝트는 MediaPipe를 이용하여 손 관절을 인식하고, OpenCV를 사용하여 웹캠 이미지를 캡처합니다. 인식된 손동작은 사전에 준비된 동작 데이터를 바탕으로 K-Nearest Neighbor(KNN) 모델을 사용하여 분류됩니다. 인식된 동작에 따라 다양한 모드와 작업이 수행됩니다.

모드
모드 변경 (0): 다양한 동작 모드로 변경합니다.
YouTube 모드 (1): YouTube 재생을 손동작으로 제어합니다.
웹 서핑 모드 (2): 웹 페이지를 탐색하고 상호작용합니다.
자동 스크롤 모드 (3): 웹 페이지를 자동으로 스크롤합니다.
손동작
모드 변경: 주먹, OK, Rock
YouTube 모드: 재생/정지, 볼륨 업/다운, 전체화면, 다음 동영상, 앞으로/뒤로 건너뛰기
웹 서핑 모드: 스크롤 업/다운, 마우스 커서 이동, 클릭, 이전 페이지
자동 스크롤 모드: 스크롤 업/다운, 정지, 이전 페이지
기능
메인 스크립트 main.py는 다음과 같은 기능을 포함합니다:

OpenCV를 사용하여 웹캠 이미지 캡처
MediaPipe를 사용하여 손 관절 인식
학습된 KNN 모델을 기반으로 손동작 인식
인식된 동작과 현재 모드에 따라 작업 수행
mode.py 스크립트는 다양한 모드와 해당 손동작의 로직을 처리합니다.

예제 코드
다음은 YouTube 모드에서 손동작을 처리하는 예제입니다:

python
코드 복사
def handle_mode1(mode, idx, last_gesture_time, last_gesture):
    text=''
    current_time = time.time()
    if idx != last_gesture:
        last_gesture = idx
        last_gesture_time = current_time
    elif idx == last_gesture:
        if current_time - last_gesture_time > 0.5 and idx in {7, 8, 13, 14}:  # 'volumeup', 'volumedown', 'skipforward', 'skipbackward'
            last_gesture_time = current_time  # Update the last_gesture_time
            if idx == 7:  # 'volumeup' gesture
                pyautogui.press('up')
            elif idx == 8:  # 'volumedown' gesture
                pyautogui.press('down')
            elif idx == 13:  # 'skipbackward' gesture
                pyautogui.press('left')
            elif idx == 14:  # 'skipforward' gesture
                pyautogui.press('right')
        elif current_time - last_gesture_time > 0.75 and idx in {9, 0, 10, 6}:
            last_gesture_time = current_time  # Update the last_gesture_time
            if idx == 9:  # 'fullscreen' gesture
                pyautogui.press('f')
            elif idx == 0:  # 'play/stop' gesture
                pyautogui.press('k')
            elif idx == 10:  # 'nextvideo' gesture
                pyautogui.hotkey('shift','n')
            elif idx == 6:  # 'prevpage' gesture
                pyautogui.hotkey('alt','left')
        elif current_time - last_gesture_time >= 2:
            last_gesture_time = current_time
            if idx==5:
                mode = 0
    return mode, last_gesture_time, last_gesture,text
라이선스
이 프로젝트는 MIT 라이선스에 따라 배포됩니다.

감사의 말
Google의 MediaPipe
이미지 처리를 위한 OpenCV
UI 자동화를 위한 PyAutoGUI
