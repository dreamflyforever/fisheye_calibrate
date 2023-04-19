import cv2
cap = cv2.VideoCapture(3)
i=0
while(1):
    ret,frame=cap.read()
    cv2.imshow('capture',frame)
    if cv2.waitKey(1)&0xFF==ord('s'):#按键盘q就停止拍照
        cv2.imwrite('./p/' + str(i) + ".jpg", frame)#将拍摄到的图片保存在data1文件夹中
    i=i+1
    if cv2.waitKey(1)&0xFF==ord('q'):#按键盘q就停止拍照
        break
cap.release()
cv2.destroyAllWindows()
