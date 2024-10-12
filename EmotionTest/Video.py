import cv2
from tensorflow.python.ops.functional_ops import scan_v2

from Scan import Scan
from matplotlib import pyplot as plt
import numpy as np




def camera():
    scan = Scan()
    webcam = cv2.VideoCapture(0)
    data=[[],[],[],[],[],[],[],[]]
    loops=0

    add=[0,0,0,0,0,0,0,0]



    while True:

        scan.get_scan(webcam)
        cv2.imshow("Camera Cap",scan.frame )
        temp=scan.emotion_data
        temp.append(scan.attention)
        #print(temp)
        loops = loops + 1
        if loops%20==0:
            for i in range(8):
                data[i].append(add[i])
            add = [0, 0, 0, 0, 0, 0, 0, 0]


        else:
            for i in range(8):
                add[i]+=temp[i]

        if cv2.waitKey(1) == 27 or not cv2.getWindowProperty("Camera Cap", cv2.WND_PROP_VISIBLE) >= 1:
            break

    print(data)
    print(loops)
    plt.title("Graph")
    plt.xlabel("idk")
    plt.ylabel("idk")

    plt.plot(data[0], label="anger")
    plt.plot(data[1], label="disgust")
    plt.plot(data[2], label="fear")
    plt.plot(data[3], label="happy")
    plt.plot(data[4], label="sad")
    plt.plot(data[5], label="surprise")
    plt.plot(data[6], label="neutral")
    plt.plot(data[7], label="attention")
    plt.legend()

    #farah
    plt.draw()
#end farah
    plt.show()
    webcam.release()
    cv2.destroyAllWindows()
camera()


