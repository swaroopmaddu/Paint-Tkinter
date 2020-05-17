
from tkinter import messagebox
from tkinter import *
import webbrowser
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO


def about():
    messagebox.showinfo("About Tkinter Paint", "This is the newest version of the Pant application using Tkinter.\n Tkinter Paint v.1.00")


def callback(url):
    webbrowser.open_new(url)


def help():
    app_win = Tk()
    app_win.title('About Geek')
    app_win.geometry("500x500")
    app_win.maxsize(500, 500)
    app_win.minsize(500, 500)
    cv = Canvas(app_win, bg='white', width=500, height=500)
    cv.pack(expand=YES, fill=BOTH)

    options = """
                Available options
                1. Tools
                    * Pen
                        - Custom Size
                        - Custom Color
                    * Brush
                        - Custom Size
                        - Custom Color
                    * Shapes
                        - Rectange
                        - Circle
                        - Oval
                        - line
                2. Image
                    * You can add image to Paint.
                    * You can open image to Paint.
                    * You can Save image to desired location.
              """
    cv.create_text(240, 30, anchor=W, width=450, font=("Purisa", 18), text="Help")
    cv.create_text(10, 230, anchor=W, width=450, font=("Purisa", 8), text=options)


def author():
    app_win = Tk()
    app_win.title('About Geek')
    app_win.geometry("500x500")
    app_win.maxsize(500, 500)
    app_win.minsize(500, 500)

    URL = "https://pbs.twimg.com/profile_images/1151493893030068225/cBzeDrmJ_400x400.jpg"
    u = urlopen(URL)
    raw_data = u.read()
    u.close()

    im = Image.open(BytesIO(raw_data))
    im = im.resize((150, 150), Image.ANTIALIAS)
    cv = Canvas(app_win, bg='white', width=500, height=500)
    cv.pack(expand=YES, fill=BOTH)

    cv.image = ImageTk.PhotoImage(im, master=app_win)
    cv.create_image(250, 100, image=cv.image, anchor=CENTER)
    cv.pack()
    ab = "This application was built using Tkinter. Tkinter is a Python binding to the Tk GUI toolkit. That is a desktop software, like this one you are using right now. Drawing in Tkinter shows how to do a simple drawing. We can draw lines, shapes, text, and image on the canvas widget"
    cv.create_text(20, 280, anchor=W, width=480, font=("Purisa", 12), text=ab)
    link1 = Label(cv, text="About author", fg="blue", cursor="hand2")
    link1.pack()
    link1.place(x=180, y=450)
    link1.bind("<Button-1>", lambda e: callback("https://github.com/swaroopmaddu/"))

    app_win.mainloop()
