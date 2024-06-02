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
```


## 사용 방법(Usage)
메인 파이썬 스크립트 control_by_gesture.py 를 실행하여 프로젝트를 사용합니다:

웹캠이 정상적으로 연 결되어 있어야 합니다.   
Ensure that you have a working webcam connected to your system.


## 설명(Description)

이 프로젝트는 MediaPipe를 이용하여 손 관절을 인식하고, OpenCV를 사용하여 웹캠 이미지를 캡처합니다. 인식된 손동작은 사전에 준비된 동작 데이터를 바탕으로 K-Nearest Neighbor(KNN) 모델을 사용하여 분류됩니다. 인식된 동작에 따라 다양한 모드와 작업이 수행됩니다.   
This project utilizes MediaPipe for hand landmark detection and OpenCV for capturing webcam images. The detected hand gestures are classified using a K-Nearest Neighbors (KNN) model trained on pre-recorded gesture data. Based on the recognized gestures, different modes and actions are triggered.

## 모드와 제스쳐(Modes and Gesture)
### Gesture and their code number   
![thumbleft](https://github.com/starvvolf/ControlByGesture/assets/118524918/9afec3d1-df53-4282-b6d5-44aff8cd8907)   
13:thumbleft    
![thumbright](https://github.com/starvvolf/ControlByGesture/assets/118524918/d2bdb9ce-fabb-4b1d-9b2e-84084bdf1a14)  
14:thumbright   
![v](https://github.com/starvvolf/ControlByGesture/assets/118524918/17820310-0f34-4f5e-beab-333341a46b3e)
9:v   
![ok](https://github.com/starvvolf/ControlByGesture/assets/118524918/da6a6b6e-5abe-4cac-a840-91126df4d343)
10:ok   
![six](https://github.com/starvvolf/ControlByGesture/assets/118524918/049d5cff-1f12-486b-80bb-9d487a5cd113)
6:six   
![fist](https://github.com/starvvolf/ControlByGesture/assets/118524918/dd0cfabf-9b11-42be-b5eb-dd14d9f28def)
0:fist   
![spiderman](https://github.com/starvvolf/ControlByGesture/assets/118524918/7835bc16-f96e-419f-9290-ae35b33a64a5)
8:spiderman(2,5)   
![rock](https://github.com/starvvolf/ControlByGesture/assets/118524918/928a5b66-bf4e-430a-91f9-c5ba852c7d4e)
7:rock(1,2,5)   
![five](https://github.com/starvvolf/ControlByGesture/assets/118524918/b0688c3c-64e6-4943-af84-245aa8f7c9bb)
5:five   
![four](https://github.com/starvvolf/ControlByGesture/assets/118524918/7816cf33-1da3-492f-adc0-60f3ec7c4270)
4:four   

### Mode0-ModeChange
At first we are in the ModeChange mode(mode 0)   
   
ModeChange 에서는 세 개의 제스쳐가 있습니다. 같은 제스쳐를 2초 유지하면 각 모드로 넘어갑니다.   
4(주먹)-YouTube 모드 : YouTube 재생을 손동작으로 제어합니다.   
10(OK)- 웹 서핑 모드 : 웹 페이지를 탐색하고 상호작용합니다.   
7(Rock-1,2,5번 손가락만 펴기)- 자동 스크롤 모드 : 웹 페이지를 자동으로 스크롤합니다.   

### Mode1-YoutubeMode   
   
YouTubeMode에서는 9개의 제스쳐가 있습니다.    
9(V)-전체화면   
0(주먹)-재생/일시정지   
10(OK)-다음 비디오   
6(six-새끼만 펴기)-이전페이지   
7(Rock-1,2,5펴기)- 볼륨 업   
8(Spiderman-2,5펴기)-볼륨 다운   
13(thumbleft-엄지 펴고 주먹쥔 상태로 손 왼쪽으로 돌리기 )-이전으로 스킵   
14(thumbright-엄지 펴고 주먹쥔 상태로 손 오른쪽으로 돌리기 )-다음으로 스킵   
5(전부펴기,손바닥보여주기)-2초이상 유지하면 ModeChange로 넘어감.   

### Mode2-WebsurfingMode   

WebsurfingMode에서는 10개의 제스쳐가 있습니다.     
#### 마우스조종       
7(Rock-1,2,5펴기)- 마우스 커서 업     
8(Spiderman-2,5펴기)-마우스 커서 다운      
13(thumbleft-엄지 펴고 주먹쥔 상태로 손 왼쪽으로 돌리기 )-마우스 커서 왼쪽으로      
14(thumbright-엄지 펴고 주먹쥔 상태로 손 오른쪽으로 돌리기 )-마우스 커서 오른쪽으로     
10(OK)-클릭      

#### 스크롤   
0(주먹)-스크롤 다운      
6(six-새끼만 펴기)-스크롤 업      
9(V)-이전페이지      

17(손하트,1번 2번만 펴서 서로 크로스)-네이버 웹툰 FHD전체화면 기준 웹툰 다음화로 넘기기 버튼 좌표 클릭     
5(전부펴기,손바닥보여주기)-2초이상 유지하면 ModeChange로 넘어감.   

### Mode3- AutoScrollMode      
AutoScrollMode 손이 인식되는 한 자동으로 스크롤을 내립니다.   
4(four)-스크롤 내리던 걸 멈춥니다.   
10(OK)-스크롤을 올립니다.   
9(V)-1.5초이상 유지시 이전페이지로   
5(전부펴기,손바닥보여주기)-2초이상 유지하면 ModeChange로 넘어감.   


## 기능 구성
OpenCV를 사용하여 웹캠 이미지 캡처   
MediaPipe를 사용하여 손 관절 인식   
학습된 KNN 모델을 기반으로 손동작 인식   
인식된 동작과 현재 모드에 따라 작업 수행
mode.py 스크립트는 다양한 모드와 해당 손동작의 로직을 처리합니다.   

## 예제 코드
다음은 YouTube 모드에서 손동작을 처리하는 예제입니다:

```
    python
    
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

```
## Demo
https://github.com/starvvolf/ControlByGesture/assets/118524918/b5f34129-018a-46a1-b092-b45cec8ea091


## if somethingwrong
제스쳐 인식이 제대로 되지 않는다면, gatherdataset.py를 이용해 자신의 손에 맞게 데이터셋을 수집할 수 있습니다.
code by: https://github.com/kairess/Rock-Paper-Scissors-Machine






## Reference   
Google MediaPipe   
https://github.com/kairess/Rock-Paper-Scissors-Machine   
https://github.com/ntu-rris/google-mediapipe  
github Copilot

