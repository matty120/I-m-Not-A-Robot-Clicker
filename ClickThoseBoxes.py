from PIL import ImageGrab
import cv2
import numpy as np
import ctypes
from matplotlib import pyplot as plt
from ctypes import windll, Structure, c_ulong, byref
from time import sleep

class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}




img3 = ImageGrab.grab()
img3.save('temp.png')

def findInScreen(template,writeFile=True):
    out = []
    img_rgb = cv2.imread('temp.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, (pt[0], pt[1]), (pt[0] + w, pt[1] + h), (0,0,255), 2)
        out.append(pt[0])
        out.append(pt[1])
        out.append(pt[0] + w)
        out.append(pt[1] + h)
    if writeFile:
        cv2.imwrite('res.png',img_rgb)
    return out

template = cv2.imread('find.png',0)
output = findInScreen(template)
i = 0
xmin = []
ymin = []
xmax = []
ymax = []
print(output)
print(len(output))
while i <= len(output):
    xmin.append(output[i])
    ymin.append(output[i+1])
    xmax.append(output[i+2])
    ymax.append(output[i+3])
    if i+4 != len(output):
        i = i+4
    else:
        break
print(xmin,ymin,xmax,ymax)
template = cv2.imread('find2.png',0)
output = findInScreen(template)
i = 0
xmin1 = []
ymin1 = []
xmax1 = []
ymax1 = []
print(output)
print(len(output))
while i <= len(output):
    xmin1.append(output[i])
    ymin1.append(output[i+1])
    xmax1.append(output[i+2])
    ymax1.append(output[i+3])
    if i+4 != len(output):
        i = i+4
    else:
        break
print(xmin1,ymin1,xmax1,ymax1)
checking = True
i = 0
while checking:
    if xmin1[i] > xmin[i] and ymin1[i] > ymin[i] and xmax1[i] < xmax[i] and ymax1[i] < ymax[0]:
        value = i
        print("I Found A Vaild CheckBox No: "+str(i))
        checking = False
        break
    else:
        if i != len(xmin):
            i = i+1
#pos = queryMousePosition()
#print(pos)

#curx = int(str(pos['x']).split('L')[0])
#cury = int(str(pos['y']).split('L')[0])
#print(curx,cury)
xP =xmin1[value] + ( xmax1[value] - xmin1[value] )/2
yP =ymin1[value] + ( ymax1[value] - ymin1[value] )/2
ctypes.windll.user32.SetCursorPos(xP,yP)
ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
sleep(0.25)
ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
sleep(1)
ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
sleep(0.25)
ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up


