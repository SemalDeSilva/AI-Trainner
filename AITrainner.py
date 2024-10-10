import cv2
import numpy as np
import time
import PoseModule as pm


cap = cv2.VideoCapture("curls.mp4")
# cap = cv2.VideoCapture(0)


detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    # img = cv2.imread("test.jpg")
    img = detector.findPose(img, False)
    lmlist = detector.findPosition(img, False)
    # print(lmlist)

    if len(lmlist) != 0:

        # right arm
        # detector.findAngle(img,12,14,16)

        # left arm
        angle = detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))

        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)

        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)

        # Draw "Reps: {count}" with smaller text and better alignment
        cv2.rectangle(img, (10, 500), (350, 600), (0, 255, 0),
                      cv2.FILLED)  # Adjusted rectangle size
        cv2.putText(img, f"Reps:{int(count)}/6", (30, 570),
                    # Adjusted text size
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f"fps:{str(int(fps))}", (50, 100), cv2.FONT_HERSHEY_PLAIN, 4,
                    (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
