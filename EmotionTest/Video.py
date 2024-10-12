import cv2
from Scan import Scan





def camera():
    scan = Scan()
    webcam = cv2.VideoCapture(0)
    while True:

        print(scan.get_scan(webcam))
        cv2.imshow("Camera Cap",scan.frame )
        if cv2.waitKey(1) == 27 or not cv2.getWindowProperty("Camera Cap", cv2.WND_PROP_VISIBLE) >= 1:
            break

    webcam.release()
    cv2.destroyAllWindows()
camera()

