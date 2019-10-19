#WALLPAPER CHANGER v2.1
#By AMLAN SAHA KUNDU

import ctypes, time, random

print(' '+'='*33+'\n'+' Welcome to WALLPAPER CHANGER v2.1 \n\t  by Amlan'+'\n'+' '+'='*33+'\n ')
print("Enter r for random choice OR any other key for systematic change")
uinp = input("Enter your Choice: ")
val = input("Enter no. of Wallpapers: ")
num = input("Enter Time Interval(sec): ")
if uinp == "r":
    while True:
        path = "C:\\Users\\amlan\\Desktop\\wp\\wp"+str(random.randint(1,int(val)))+".jpg"
        print(path)
        ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
        time.sleep(int(num))
else:
    n = 1
    while n < int(val)+1:
        path = "C:\\Users\\amlan\\Desktop\\wp\\wp"+str(n)+".jpg"
        print(path)
        ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
        time.sleep(int(num))
        n=int(n)+1
        if n == int(val)+1:
            n = 1
