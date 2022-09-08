import cv2
import time
import os

# line a
ax1 = 70
ay = 90
ax2 = 230
# line b
bx1 = 15
by = 125
bx2 = 225


def Speed_Cal(time):

    try:
        Speed = (9.144/1000)/(time/3600)
        return Speed
    except ZeroDivisionError:
        print("can not devide by zero")


# car num
i = 1
start_time = time.time()
# video ....
cap = cv2.VideoCapture('cars.mp4')
car_cascade = cv2.CascadeClassifier('./cars.xml')

while True:
    ret, img = cap.read()
    if(type(img) == type(None)):
        break
    # bluring to have exacter detection
    blurred = cv2.blur(img, ksize=(15, 15))
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 2)

    # line a #i know road has got
    cv2.line(img, (ax1, ay), (ax2, ay), (255, 0, 0), 2)
    # line b
    cv2.line(img, (bx1, by), (bx2, by), (255, 0, 0), 2)
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0), 2)
        # cv2.circle(img,(int((x+w)/2),int((y+h)/2)),1,(0,255,0),-1)

        while int(ay) == int((y + y+h)/2):
            start_time = time.time()
            break
        while int(ay) <= int((y+y+h)/2):
            # if int(by) <= int((y+y+h)/2) & int (by +10) >= int(( y + y+h)
            cv2.line(img, (bx1, by), (bx2, by), (0, 255, 0), 2)
            Speed = Speed_Cal(time.time() - start_time)
            print("Car Number "+str(i)+"  Speed:  "+str(Speed)+"KM/H")
            i = i+1
            break
        # else :
        # cv2.putText(img, "Calculing", (100,200), cv2.FONT_HERSHEY_S:
        # break
        cv2.imshow('video', img)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        if cv2.waitKey(33) == 27:
            break
cap.release()
cv2.destroyAllWindows()
