import cv2
import numpy as np
import mediapipe as mp
import time

cap = cv2.VideoCapture('Drowsiness video/istockphoto-1212121078-640_adpp_is.mp4')
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

lmList = []
rEyeId = [362, 398, 384, 385, 386, 387, 388, 466, 263, 249,
         390, 373, 374, 380, 381, 382]
lEyeId = [33, 246, 161, 160, 159, 158, 157, 173, 133, 155,
          154, 153, 145, 144, 163, 7]
timer = 0

while True:
    rEyeX = []
    rEyeY = []
    success, img = cap.read()
    imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imageRGB)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS,
                                  drawSpec, drawSpec)

            for id, lm in enumerate(faceLms.landmark):
                ih, iw, ic = img.shape
                x, y = int(lm.x*iw), int(lm.y*ih)
                # print(x,y)
                lmList.append([x,y])

                for i in rEyeId:
                    if id == i:
                        cv2.circle(img, (x,y), 1, (255, 0, 255), cv2.FILLED)
                        rEyeX.append(x)
                        rEyeY.append(y)

                for i in lEyeId:
                    if id == i:
                        cv2.circle(img, (x,y), 1, (255, 0, 255), cv2.FILLED)

    rEyeArea = 0.5*np.abs(np.dot(rEyeX,np.roll(rEyeY,1))-np.dot(rEyeY,np.roll(rEyeX,1)))
    print('Area of the eye:',rEyeArea)

    if rEyeArea < 50:
        timer = timer + 1
        print('Frame counter:',timer)
        if timer >= 10:
            print('Alert Driver')
            cv2.putText(img, f'Alert Drowsing', (200, 300), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 0, 255), 2)
    else:
        timer = 0

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (10, 30), cv2.FONT_HERSHEY_PLAIN, 1.5,
                (255, 0, 255), 2)

    cv2.imshow('Image', img)
    cv2.waitKey(1)