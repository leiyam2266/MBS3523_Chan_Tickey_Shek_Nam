# Save this file as OpenCV-Ex2-BounceBox.py
import random
import cv2
#import numpy as np
#

# you may need to change the number inside () to 0 1 or 2,
# depending on which webcam you are using
capture = cv2.VideoCapture(1)
# Below 2 lines are used to set the webcam window size
capture.set(3,640) # 3 is the width of the frame
capture.set(4,480) # 4 is the height of the frame

x = 0
dx = 12

y = 0
dy = 12

Blue = random.randint(0, 255)
Green = random.randint(0, 255)
Red = random.randint(0, 255)
thickness = random.randint(1, 2)


# Start capturing and show frames on window named 'Frame'

while True:

    x_1 = x
    y_1 = y

    x_2 = x + 80
    y_2 = y + 80

    success, img = capture.read()

    cv2.rectangle(img, (x_1, y_1), (x_2, y_2), (Blue, Green, Red), thickness)

    x = x + dx
    y = y + dy

    if x >= 560 or x <= 0:
        dx = dx * (-1)
    elif y >= 400 or y <= 0:
        dy = dy * (-1)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == 32:
            break

capture.release()
cv2.destroyAllWindows()
