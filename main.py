#WALLPAPER CHANGER v2.0
#By AMLAN SAHA KUNDU

import ctypes, time, random

print(' '+'='*33+'\n'+' Welcome to WALLPAPER CHANGER v2.0 \n\t  by Amlan'+'\n'+' '+'='*33+'\n ')
print("Enter r for random choice OR any other key for systematic change")
uinp = input("Enter your Choice: ")
num = input("Enter Time Interval(sec): ")
if uinp == "r":
    while True:
        path = "C:\\Users\\amlan\\Desktop\\wp\\wp"+str(random.randint(1,10))+".jpg"
        print(path)
        ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
        time.sleep(int(num))
else:
    n = 1
    while n < 11:
        path = "C:\\Users\\amlan\\Desktop\\wp\\wp"+str(n)+".jpg"
        print(path)
        ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
        time.sleep(int(num))
        n=int(n)+1
        if n == 11:
            n = 1
