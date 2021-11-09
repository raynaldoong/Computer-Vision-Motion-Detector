import cv2, time, pandas
from datetime import datetime

first_frame=None
status_list = [None, None] #reason being that in the first iteration, list have no [-2] hence will cause error
times = [] #only records the time of start and the exit when object moves into frame
df = pandas.DataFrame(columns=["Start", "End"]) #will be used to convert time recorded to csv 

video = cv2.VideoCapture(0)


while True:
    check, frame = video.read() #check returns boolean to check if webcam works, captures the first frame when webcam turns on
    status = 0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0) #makes frame blury

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray) #calculates the difference in first frame and all following frame
    thresh_frame = cv2.threshold(delta_frame, 30,255,cv2.THRESH_BINARY)[1] #determines the threshold frame when the difference in first frame and following frame is more than 30
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2) #smoothens the big white area from the background
    
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts: #detect changes and make a rectangle, the lower the more sensitive
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1 #status changes when detect object moving
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    
    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0: #time when object comes in
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1: #time when object exits
        times.append(datetime.now())


    
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key = cv2.waitKey(1)
    if key==ord("q"):
        if status == 1:
            times.append(datetime.now()) #to track the time of last frame if object is still moving
        break



for i in range(0, len(times),2):
    df=df.append({"Start":times[i], "End":times[i+1]},ignore_index=True) #
df.to_csv("Times.Csv")
video.release()
cv2.destroyAllWindows