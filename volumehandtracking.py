import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


###################
wcam,hcam=640,480
###################
cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector=htm.handDetector()


devices = AudioUtilities.GetSpeakers()
interface=  devices. Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER (IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMaster VolumeLevel()
volRange = volume.GetVolumeRange()

minvol=volRange[0]
maxvol=volRange[1]
volBar=0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPostion(img, draw=False)
    if len(lmList) != 0:
        #print(lmList[4],lmList[8])

        x1 , y1 = lmList[4][1],lmList[4][2]
        x2, y2 = lmList[8][1],lmList[8][2]
        cx,cy= (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1), 8, (225, 0, 225), cv2.FILLED)
        cv2.circle(img, (x2, y2), 8, (225, 0, 225), cv2.FILLED)
        cv2.circle(img, (cx, cy), 8, (225, 0, 225), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (225, 0, 225), 3)

        length = math.hypot(x2-x1, y2-y1)
        #print(length)

        # Hand range 30 - 250
        # Volume range -65 - 0

        vol = np.interp(length, [30,250],[minvol,maxvol])
        volBar = np.interp(length, [30,250],[400,150])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)


        if length<30:
            cv2.circle(img, (cx, cy), 8, (0, 225, 0), cv2.FILLED)
        elif length>250:
            cv2.circle(img, (cx, cy), 8, (0, 0, 255), cv2.FILLED)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
