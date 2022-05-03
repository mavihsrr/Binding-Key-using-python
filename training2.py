import keyboard
import time
s=0
maxi = 100
print(s)
while True:
    press = keyboard.is_pressed('u')
    if press and s<maxi:
        time.sleep(0.1)
        s += 1
        print(s)
    else:
        time.sleep(0.1)
        if s <= 0 or (s == maxi and press):
            pass
        else:
            s -= 1
            print(s)

