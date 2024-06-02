# ControlByGesture
mouse move, scroll and push shortcut key by gesture with MediaPipe
# Hand Gesture Recognition with MediaPipe

This project is a hand gesture recognition system using MediaPipe and OpenCV. The system can detect various hand gestures and perform corresponding actions such as controlling YouTube, web surfing, and auto-scrolling modes.

## Demo
https://github.com/starvvolf/ControlByGesture/assets/118524918/b5f34129-018a-46a1-b092-b45cec8ea091


## Installation
   
To install the necessary dependencies, run the following command:   
```bash
pip install opencv-python mediapipe numpy pyautogui
```


## Usage
The project consists of the following files: `data/gesture_train_fy.py` (Dataset), `control_by_gesture.py` (Main), and `mode.py` (Mode settings).
To use the project, run the main Python script `control_by_gesture.py`:

웹캠이 정상적으로 연결되어 있어야 합니다.   
Ensure that you have a working webcam connected to your system.


## Description
  
This project utilizes MediaPipe for hand landmark detection and OpenCV for capturing webcam images. The detected hand gestures are classified using a K-Nearest Neighbors (KNN) model trained on pre-recorded gesture data. Based on the recognized gestures, different modes and actions are triggered.

## Modes and Gesture
### Gesture and their code number    
****
13:thumbleft    
![thumbleft](https://github.com/starvvolf/ControlByGesture/assets/118524918/9afec3d1-df53-4282-b6d5-44aff8cd8907)   
****
14:thumbright      
![thumbright](https://github.com/starvvolf/ControlByGesture/assets/118524918/d2bdb9ce-fabb-4b1d-9b2e-84084bdf1a14)  
****
9:v  
![v](https://github.com/starvvolf/ControlByGesture/assets/118524918/17820310-0f34-4f5e-beab-333341a46b3e)   
****
10:ok  
![ok](https://github.com/starvvolf/ControlByGesture/assets/118524918/da6a6b6e-5abe-4cac-a840-91126df4d343)
****  
6:six   
![six](https://github.com/starvvolf/ControlByGesture/assets/118524918/049d5cff-1f12-486b-80bb-9d487a5cd113)
****
0:fist   
![fist](https://github.com/starvvolf/ControlByGesture/assets/118524918/dd0cfabf-9b11-42be-b5eb-dd14d9f28def)
****  
8:spiderman(2,5)   
![spiderman](https://github.com/starvvolf/ControlByGesture/assets/118524918/7835bc16-f96e-419f-9290-ae35b33a64a5)
****   
7:rock(1,2,5)   
![rock](https://github.com/starvvolf/ControlByGesture/assets/118524918/928a5b66-bf4e-430a-91f9-c5ba852c7d4e)
****   
5:five   
![five](https://github.com/starvvolf/ControlByGesture/assets/118524918/b0688c3c-64e6-4943-af84-245aa8f7c9bb)
**** 
4:four   
![four](https://github.com/starvvolf/ControlByGesture/assets/118524918/7816cf33-1da3-492f-adc0-60f3ec7c4270)
****

### Mode0-ModeChange
At first we are in the ModeChange mode(mode 0)    
   
In ModeChange mode, there are three gestures. If you maintain the same gesture for 2 seconds, you will switch to each respective mode.   
4 (Fist) - YouTube Mode: Controls YouTube playback using gestures.     
10 (OK) - Web Surfing Mode: Navigates and interacts with web pages..     
7 (Rock - only extend fingers 1, 2, and 5) - Auto Scroll Mode: Automatically scrolls through web pages.   

### Mode1-YoutubeMode   
   
In YouTube Mode, there are 9 gestures.   

9 (V) - Fullscreen   
0 (Fist) - Play/Pause   
10 (OK) - Next Video   
6 (Six - only extend the pinky finger) - Previous Page   
7 (Rock - only extend fingers 1, 2, and 5) - Volume Up   
8 (Spiderman - only extend fingers 2 and 5) - Volume Down   
13 (Thumbleft - extend thumb and rotate fist to the left) - Skip Backward   
14 (Thumbright - extend thumb and rotate fist to the right) - Skip Forward   
5 (Extend all fingers, showing palm) - If held for more than 2 seconds, switches to ModeChange.   

### Mode2-WebsurfingMode   

In Websurfing Mode, there are 10 gestures.
#### Mouse Control       
7 (Rock - only extend fingers 1, 2, and 5) - Move mouse cursor up   
8 (Spiderman - only extend fingers 2 and 5) - Move mouse cursor down   
13 (Thumbleft - extend thumb and rotate fist to the left) - Move mouse cursor left   
14 (Thumbright - extend thumb and rotate fist to the right) - Move mouse cursor right   
10 (OK) - Click     

#### 스크롤   
0 (Fist) - Scroll down   

6 (Six - only extend the pinky finger) - Scroll up   

9 (V) - Previous page   

17 (Hand heart, cross fingers 1 and 2) - Click the next episode button on Naver Webtoon (FHD fullscreen mode)   

5 (Extend all fingers, showing palm) - If held for more than 2 seconds, switches to ModeChange.   

### Mode3- AutoScrollMode      
In Auto Scroll Mode, the page scrolls down automatically as long as a hand is detected.   

4 (Four) - Stop scrolling down   
10 (OK) - Scroll up   
9 (V) - If held for more than 1.5 seconds, goes to the previous page   
5 (Extend all fingers, showing palm) - If held for more than 2 seconds, switches to ModeChange.   


## Features

1. Capture webcam images using OpenCV   
2. Recognize hand landmarks using MediaPipe   
3. Recognize hand gestures based on a trained KNN model   
4. Perform tasks based on the recognized gestures and current mode   

## If Something Goes Wrong   

If gesture recognition does not work properly, you can collect a dataset tailored to your hand using `gatherdataset.py`.   
Code by: https://github.com/kairess/Rock-Paper-Scissors-Machine   






## Reference   
Google MediaPipe   
https://github.com/kairess/Rock-Paper-Scissors-Machine   
https://github.com/ntu-rris/google-mediapipe  
github Copilot

