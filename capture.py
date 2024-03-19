import cv2
cap=cv2.VideoCapture(0 + cv2.CAP_ANY)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FPS, 25)

i=0
while(1):
    ret,frame=cap.read()
    cv2.imshow('capture',frame)
    if cv2.waitKey(1)&0xFF==ord('s'):# key 's' to  save 
        cv2.imwrite('./p/' + str(i) + ".jpg", frame) # save p directory
    i=i+1
    if cv2.waitKey(1)&0xFF==ord('q'):# key'q' to quit
        break
cap.release()
cv2.destroyAllWindows()
