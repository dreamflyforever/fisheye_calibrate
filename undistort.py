import cv2
import numpy as np

cap=cv2.VideoCapture(0 + cv2.CAP_ANY)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cap.set(cv2.CAP_PROP_FPS, 25)

def undistort(frame,K,D,DIM,scale=1.0,imshow=False):
    img = frame
    Knew = K.copy()
    if scale:#change fov
        Knew[(0,1), (0,1)] = scale * Knew[(0,1), (0,1)]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), Knew, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    if imshow:
        cv2.imshow("undistorted", undistorted_img)
    return undistorted_img

if __name__ == "__main__":

	while (1):
		ret, img = cap.read()
		K=np.array([[380.3025881264698, 0.0, 835.7633212578959], [0.0, 380.3560307871331, 648.708948996112], [0.0, 0.0, 1.0]])
		D=np.array([[-0.03261472548785381], [0.011062003883309286], [-0.02407978291132735], [0.014817956840343545]])
		img_size = (640, 360)

		result_img = undistort(img, K, D, img_size)
		cv2.imshow('img_distort', result_img)
		if cv2.waitKey(1)&0xFF==ord('q'):# key'q' to quit
	        	break
	cap.release()
	cv2.destroyAllWindows()
	
