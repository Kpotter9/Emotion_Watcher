import sys

from PIL import Image,ImageTk
from PIL.ImageChops import screen
import customtkinter
from customtkinter import CTkFont
import tkinter as tk
from tkinter import PhotoImage, Label, Canvas ,font
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import asyncio
from multiprocessing import Process, Pool
import cv2
import pandas as pd
import os
import Background

from tensorflow.python.distribute.multi_process_lib import multiprocessing

from Scan import Scan

matplotlib.use("TkAgg")
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import subprocess

# import Video


class Guiy:

    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        root = customtkinter.CTk()
        root.title("Big Brother")

        width = root.winfo_screenwidth()
        halfWidthScreen = (int)((1 / 2) * width)

        # thirdWidth = (int)((1 / 3) * width)

        length = root.winfo_screenheight()
        # heightThing = (int)((2 / 3) * length)

        root.geometry(f"{halfWidthScreen}x{length}+0+0")
        root.iconbitmap("./images/Cyberpunk.png")

        img = Image.open("images/Cyberpunk.png")
        img = img.resize((width,length))
        img.save("images/img.png")
        bg = PhotoImage(file="images/img.png")

        my_canvas = Canvas(root,width = width ,height = length)

        my_canvas.pack(fill = "both",expand = True)
        my_canvas.create_image(0,0,image=bg,anchor = "nw")

        '''
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=50, fill="both", expand=True)
        '''
        label = customtkinter.CTkLabel(
            master=root, text="Big Brother's Always Watching"
        )
        label.pack(pady=12, padx=10)

        # time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # test = [23, 41, 32, 67, 83, 56, 93, 12, 7, 57]

        # graphOne = Figure(figsize=(5, 5), dpi=100)
        # sub = graphOne.add_subplot(111)
        # sub.plot(time, test)

        def terminal():
            print("Stop")
            exit()
        def kyle_event():
            begin(1)
        def button_event():
            begin(0)
        def begin(cam):
            print("Pressed")
            button.pack_forget()
            kylesButton.pack_forget()

            graphFrame = customtkinter.CTkFrame(master=my_canvas, width= int(halfWidthScreen*1.8))
            graphFrame.pack(pady=40, padx=0)

            # graph, ax = plt.subplots()
            # ax.plot(time, test)

            # plt.show()
            fig, axs = plt.subplots(2, 4)
            fig.patch.set_facecolor('#313030')
            def animate(i):
                df = pd.read_csv("Emotion.csv")
                for loop in axs:
                    for i in loop:
                        i.clear()
                for loop in axs:
                    for i in loop:
                        i.set_ylim([0, 1000])
                        i.patch.set_facecolor('#313030')
                        i.set_yticklabels([])
                axs[0, 0].plot(
                    df["anger"],
                    color="red",
                )
                axs[0, 1].plot(df["disgust"], color="green")
                axs[0, 2].plot(df["surprise"], color="orange")
                axs[0, 3].plot(df["sad"], color="blue")
                axs[1, 0].plot(df["happy"], color="yellow")
                axs[1, 1].plot(df["neutral"], color="gray")
                axs[1, 2].plot(df["fear"], color="purple")
                axs[1, 3].plot(df["attention"], color="black")
                axs[0, 0].set_xlabel("Anger", labelpad=-2, fontsize=10, color="red")
                axs[0, 1].set_xlabel("Disgust", labelpad=-2, fontsize=10, color="green")
                axs[0, 2].set_xlabel(
                    "Surprise", labelpad=-2, fontsize=10, color="orange"
                )
                axs[0, 3].set_xlabel("Sad", labelpad=-2, fontsize=10, color="blue")
                axs[1, 0].set_xlabel("Happy", labelpad=-2, fontsize=10, color="yellow")
                axs[1, 1].set_xlabel("Neutral", labelpad=-2, fontsize=10, color="gray")
                axs[1, 2].set_xlabel("Fear", labelpad=-2, fontsize=10, color="purple")
                axs[1, 3].set_xlabel(
                    "Attention", labelpad=-2, fontsize=10, color="black"
                )

            ani = animation.FuncAnimation(fig, animate, interval=1000)

            graphCanvas = FigureCanvasTkAgg(fig, master=graphFrame)

            graphCanvas.draw()
            graphCanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            # graphCanvas.get_tk_widget().configure(thirdWidth, heightThing)
            # graphCanvas.get_tk_widget().pack(side=root.winfo_toplevel, fill="both", expand=True)

            proc = sys.path
            subprocess.Popen([sys.executable, "Video.py",str(cam)])

            stopButton = customtkinter.CTkButton(
                master=my_canvas, text="Terminate", font=helvia,command=terminal,border_width=-5, bg_color="blue"
            )
            stopButton.pack(pady=20, padx=0)

        img = Image.open("images/Cyberpunk.png")
        img = img.resize((1,1))
        img.save("images/img1.png")
        bg1 =PhotoImage(file="images/img1.png")
        img_label=Label(image=bg1)
        helvia=CTkFont(family="Helvetica",size=30)
        button = customtkinter.CTkButton(
            font=helvia,
            master=my_canvas,text="Internal Monitor",fg_color="#a82218",text_color="black",hover_color="#4f0f0a", border_width=-10, command=button_event
        )
        button.pack(pady=40, padx=0)

        kylesButton = customtkinter.CTkButton(
            master=my_canvas, font=helvia,text="External Surveillance", fg_color="#a82218",text_color="black", hover_color="#4f0f0a",border_width=-10, command=kyle_event
        )
        kylesButton.pack(pady=40, padx=20)

        root.mainloop()


if __name__ == "__main__":
    Guiy()
