import datetime,ctypes,time
x = datetime.datetime.now()
#CURRENT TIME
CH=int(x.strftime("%H"))
CM=int(x.strftime("%M"))
CS=int(x.strftime("%S"))
CMonth = int(x.strftime("%m"))
#Starting Hr Calculation
if CMonth <=3 or CMonth >=9:
    startH = 2
else:
    startH = 3
#TIME FROM Starting Hour
if CH >= startH:
    calH = CH-startH
else:
    calH = CH+24-startH
upSec = calH*3600+CM*60+CS
startSec = int(upSec//169.4)
print(startSec)
val = 510
num = 169.
n = startSec%510
while n < int(val)+1:
    path = "C:\\Users\\amlan\\Desktop\\mojave\\wp"+str(n)+".jpg"
    y = datetime.datetime.now()
    print(path,y)
    ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
    time.sleep(int(num))
    n=int(n)+1
    if n == int(val)+1:
        n = 1
