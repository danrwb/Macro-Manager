import ctypes
import keyboard
import time
import pyautogui as pag

def round_to_dp(num, dp):
    return int(num * (10*dp)) / (10*dp)

def d_left_click():
    if ctypes.windll.user32.GetKeyState(0x01):
        return True
    return False

def d_right_click():
    if ctypes.windll.user32.GetKeyState(0x02):
        return True
    return False

def d_mouse_move():
    global prev_pos
    if prev_pos != pag.position():
        prev_pos = pag.position()
        return pag.position()
    return False

def keys(event):
    global keys_down
    if event.name in keys_down:
        keys_down.remove(event.name)
        keys_released.append(event.name)
    else:
        keys_down.append(event.name)
        keys_pressed.append(event.name)

def d_keys_pressed():
    global keys_pressed
    kp = keys_pressed
    keys_pressed = []
    if len(kp)> 0:
        return kp
    return False


def d_keys_released():
    global keys_released
    kr = keys_released
    keys_released = []
    if len(kr)> 0:
        return kr
    return False
    
   

keyboard.hook(keys)
actions = []

prev_keys_down = []
keys_down = []
keys_pressed = []
keys_released = []
prev_pos = (-1,-1)


while not keyboard.is_pressed('['):
    pass

start = time.time()

while not keyboard.is_pressed(']'):
    action = {}
    lc = d_left_click()
    rc = d_right_click()
    mm = d_mouse_move()
    kp = d_keys_pressed()
    kr = d_keys_released()
    if lc == '1':
        action['left click'] = True
    if rc == '1':
        action['right click'] = True
    if mm != False:
        action['move'] = mm
    if kp != False:
        action['press'] = kp
    if kr != False:
        action['release'] = kr
    if len(action) > 0:
        time_action = time.time() - start
        action['time'] = time_action
        actions.append(action)
    # time.sleep(0.1)

print(actions)



        
