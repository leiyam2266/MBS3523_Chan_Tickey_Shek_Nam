import random
import cv2

capture = cv2.VideoCapture(0)

capture.set(3,640)
capture.set(4,480)

x = 0
dx = 1

y = 0
dy = 1

while True:
    success, img = capture.read()
    cv2.rectangle(img, (x, y), (x + 80, y + 80), (random.randint(0, 255) ,random.randint(0, 255) ,random.randint(0, 255) ), random.randint(1, 2))

    x = x + dx
    y = y + dy

    if x >= 590 or x <= 0:
        dx = dx * (-1)
    if y >= 590 or y <= 0:
            dy = dy * (-1)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == 32:
        break

capture.release()
cv2.destroyAllWindows()