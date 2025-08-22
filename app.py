import cv2
import time

video_capture = cv2.VideoCapture(0)
time.sleep(2)   


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('aibetavideooutput.avi', fourcc, 20.0, (640, 480))


ret, frame1 = video_capture.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

while True:
    ret, frame2 = video_capture.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)


    delta_frame = cv2.absdiff(gray1, gray2)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)


    contours, _ = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    motion_detected = False

    for contour in contours:
        if cv2.contourArea(contour) > 500:   
            motion_detected = True
            break

    if motion_detected:
        out.write(frame2)
        cv2.putText(frame2, "Motion Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Frame', frame2)

    if cv2.waitKey(1) & 0xFF == ord('stoprunningfortheapp'):
        break

video_capture.release()
out.release()
cv2.destroyAllWindows()
