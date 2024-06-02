import pyautogui
import time



# 각 모드와 제스처에 대한 설명을 담은 딕셔너리를 만듭니다.
mode_descriptions = {
    0: 'Mode Change',
    1: 'YouTube Mode',
    2: 'Web Surfing Mode',
    3: 'auto scroll Mode'
}

gesture_descriptions = {
    0: {
        0: 'fist',
        1: 'One Finger',
        3: 'Three Fingers',
        4:'four', 5:'five',
        6:'six', 7:'rock(1,2,5)', 8:'spiderman(2,5)', 9:'v', 10:'ok',
        13:'thumbleft', 14:'thumbright',17:'heart'

        # 필요한 만큼 추가합니다.
    },
    1: {
        # YouTube Mode에서의 제스처 설명을 추가합니다.
        9:'fullscreen',
        0:'play/stop',
        7:'volumeup',
        8:'volumedown',
        5: 'modechange',
        13:'skipbackward',
        14:'skipforward',
        10:'right-nextvideo',
        6:'prevpage',
        
    },
    2: {
        # Websurfing Mode에서의 제스처 설명을 추가합니다.
        0:'scrolldown',
        4:'stop',
        5:'modechange',
        6:'scrollup',
        7:'mousecursor up',
        8:'mousecursor down',
        9:'prevpage',
        10:'click',
        13:'mousecursor left',
        14:'mousecursor right',
        17:'nextwebtoon(for naver)'
        





    },
    3: {
        #autoscrollmode 에서의 제스처 설명을 추가합니다.
        4: 'stop',
        5: 'modechange',
        9: 'prevpage',
        10: 'scrollup',
        17: 'modechange'
    }
}






def handle_mode0(mode, idx, last_gesture_time, last_gesture):
    # 현재 시간을 가져옵니다.
    current_time = time.time()
    text=''

    # 제스처가 변경되었거나, 2초 이상 동일한 제스처가 유지되었는지 확인합니다.
    if idx != last_gesture:
            last_gesture = idx
            last_gesture_time = current_time
    elif idx == last_gesture and current_time - last_gesture_time >= 2:
        if idx == 4:
            mode = 1
        elif idx == 10:
            mode = 2
        elif idx == 7:
           mode = 3

    return mode, last_gesture_time, last_gesture,text

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

def handle_mode2(mode, idx, last_gesture_time, last_gesture):
    text=''
    current_time = time.time()
    if idx != last_gesture:
        last_gesture = idx
        last_gesture_time = current_time
    elif idx == last_gesture:
        if current_time - last_gesture_time > 0.1 and idx in {7, 8,6,0, 13, 14}:  # 'volumeup', 'volumedown', 'skipforward', 'skipbackward'
            last_gesture_time = current_time  # Update the last_gesture_time
            if idx == 7:  # '2,5up' gesture
                pyautogui.move(0, -30)  # Move the mouse up
            elif idx == 8:  # '1,2,5up' gesture
                pyautogui.move(0, 30)  # Move the mouse down
            elif idx == 13:  # 'thumbleft' gesture
                pyautogui.move(-30, 0)  # Move the mouse left
            elif idx == 14:  # 'thumbright' gesture
                pyautogui.move(30, 0)  # Move the mouse right
            elif idx == 6:  # 'six' gesture
                pyautogui.scroll(200)  # Scroll up
            elif idx == 0:  # 'fist' gesture
                pyautogui.scroll(-200)  # Scroll down
            elif idx==4:
                pass
            
        elif current_time - last_gesture_time > 0.75 and idx in {10, 9, 17}:
            last_gesture_time = current_time  # Update the last_gesture_time
            
            if idx == 10:  # 'ok' gesture
                pyautogui.click() #click
            elif idx == 9:  # 'prevpage' gesture
                pyautogui.hotkey('alt','left')
            elif idx==17:
                pyautogui.click(1510,115)  # 다음화 for naver webtoon
        elif current_time - last_gesture_time >= 2:
            last_gesture_time = current_time
            if idx==5:
                mode = 0
    
        
    return mode, last_gesture_time, last_gesture,text

def handle_mode3(mode, idx, last_gesture_time, last_gesture):
    text=''
    current_time = time.time()
    speed=150

    if idx != last_gesture:
        last_gesture = idx
        last_gesture_time = current_time

    elif idx == last_gesture:
        if current_time - last_gesture_time > 0.1 and idx in {0,10,4}:  # 'volumeup', 'volumedown', 'skipforward', 'skipbackward'
            last_gesture_time = current_time  # Update the last_gesture_time
            if idx==0:
                pass
            elif idx==10:
                pyautogui.scroll(speed)

        elif current_time - last_gesture_time > 1.5 and idx in{9,17}:
            last_gesture_time = current_time
            
            if idx == 9:  # 'prevpage' gesture
                pyautogui.hotkey('alt','left')
            #elif idx==17:
            #   pyautogui.click(1510,115)  # 다음화 for naver webtoon
            
        elif current_time - last_gesture_time >= 2:
            last_gesture_time = current_time
            if idx==5:
                mode = 0

    if idx != 4 and idx !=10:  # 제스처가 4번이 아니면
        pyautogui.scroll(-(speed))  # 아래로 스크롤
    return mode, last_gesture_time, last_gesture, text