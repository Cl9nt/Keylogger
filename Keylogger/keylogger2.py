####### KEYLOGGER = DISPLAY KEY ( PRESSED AND RELEASED )

import pynput.keyboard as Keyboard

def on_press(key):

    # callback whenever a key is pressed 

    try:

        print((f'Key {key.char} pressed!'))
    
    except AttributeError:

        print(f'Special Key {key} pressed!')

def on_release(key):

    print(f'Key {key} released')

    if key == Keyboard.Key.esc:

        # stop the listener 

        return False

with Keyboard.Listener(on_press=on_press, on_release=on_release) as listener:

    listener.join()
