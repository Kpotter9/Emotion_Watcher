import cv2
import pandas as pd
from Scan import Scan
import sys
import numpy as np




def camera(cam):
    scan = Scan()
    val=0
    if(cam.isalnum()):
       val=int(cam)
    webcam = cv2.VideoCapture(val)
    if not webcam.isOpened():
        webcam = cv2.VideoCapture(0)

    data=[[],[],[],[],[],[],[],[]]
    loops=0

    add={"anger":0,"disgust":0,"fear":0,"happy":0,"sad":0,"surprise":0,"neutral":0,"attention" :0}
    df = pd.DataFrame(columns=["anger", "disgust", "fear", "happy", "sad", "surprise", "neutral", "attention"])



    while True:

        scan.get_scan(webcam)
        cv2.imshow("Camera Cap",scan.frame )
        temp=scan.emotion_data
        temp.append(scan.attention)
        #print(temp)
        loops = loops + 1
        add["anger"]+=scan.emotion_data[0]
        add["disgust"] += scan.emotion_data[1]
        add["fear"] += scan.emotion_data[2]
        add["happy"] += scan.emotion_data[3]
        add["sad"] += scan.emotion_data[4]
        add["surprise"] += scan.emotion_data[5]
        add["neutral"] += scan.emotion_data[6]
        add["attention"] += scan.attention
        if loops%10==0:
            df=df._append(add,ignore_index=True)
            df = df.sort_index()
            add = {"anger": 0, "disgust": 0, "fear": 0, "happy": 0, "sad": 0, "surprise": 0, "neutral": 0,
                   "attention": 0}
            df.to_csv("Emotion.csv",index=True)



        if cv2.waitKey(1) == 27 or not cv2.getWindowProperty("Camera Cap", cv2.WND_PROP_VISIBLE) >= 1:
            break




    # plt.plot(data[0], label="anger")
    # plt.plot(data[1], label="disgust")
    # plt.plot(data[2], label="fear")
    # plt.plot(data[3], label="happy")
    # plt.plot(data[4], label="sad")
    # plt.plot(data[5], label="surprise")
    # plt.plot(data[6], label="neutral")
    # plt.plot(data[7], label="attention")
    #plt.legend()

    #farah

    webcam.release()
    cv2.destroyAllWindows()
    # end farah

camera(sys.argv[1])








