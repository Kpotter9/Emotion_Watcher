from tkinter import *
from PIL import Image
from PIL.ImageChops import screen


root = Tk()

root.title("Cyberpunk")

root.iconbitmap('./images/Cyberpunk.png')

# root.bind("<Configure>", window_size)
screen_width = root.winfo_screenwidth()
window_width = int(screen_width * 1.0)
screen_height = root.winfo_screenheight()
window_height = int(screen_height * 1.0)
root.geometry(f"{window_width}x{window_height}+0+0")

def resize_img():
    img = Image.open("images/Cyberpunk.png")

    img = img.resize((window_width,window_height))

    img.save("images/img.png")

resize_img()
bg = PhotoImage(file = "images/img.png")

my_label = Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)


root.mainloop()