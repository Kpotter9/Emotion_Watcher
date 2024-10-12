import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from matplotlib.pyplot import yscale

fig ,axs= plt.subplots(2,4)


def animate(i):
    df=pd.read_csv("Emotion.csv")
    for loop in axs:
        for i in loop:
            i.clear()
    for loop in axs:
        for i in loop:
            i.set_ylim([0,1000])
    axs[0,0].plot(df["anger"],color="red")
    axs[0, 1].plot(df["disgust"], color="green")
    axs[0, 2].plot(df["surprise"], color="orange")
    axs[0, 3].plot(df["sad"], color="blue")
    axs[1, 0].plot(df["happy"], color="yellow")
    axs[1, 1].plot(df["neutral"], color="gray")
    axs[1, 2].plot(df["fear"], color="purple")
    axs[1, 3].plot(df["attention"], color="black")
    axs[0, 0].set_xlabel("Anger", labelpad=-2, fontsize=10, color="red")
    axs[0, 1].set_xlabel("Disgust", labelpad=-2, fontsize=10, color="green")
    axs[0, 2].set_xlabel("Surprise", labelpad=-2, fontsize=10, color="orange")
    axs[0, 3].set_xlabel("Sad", labelpad=-2, fontsize=10, color="blue")
    axs[1, 0].set_xlabel("Happy", labelpad=-2, fontsize=10, color="yellow")
    axs[1, 1].set_xlabel("Neutral", labelpad=-2, fontsize=10, color="gray")
    axs[1, 2].set_xlabel("Fear", labelpad=-2, fontsize=10, color="purple")
    axs[1, 3].set_xlabel("Attention", labelpad=-2, fontsize=10, color="black")






ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()