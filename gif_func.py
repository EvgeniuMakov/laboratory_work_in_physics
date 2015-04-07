import time
from Tkinter import *

root = Tk()

imagelist = ["./image/1.gif","./image/2.gif","./image/3.gif","./image/4.gif",
"./image/5.gif","./image/6.gif","./image/7.gif",
"./image/8.gif","./image/9.gif","./image/10.gif",
"./image/11.gif","./image/12.gif","./image/13.gif",
"./image/14.gif","./image/15.gif","./image/16.gif",
"./image/17.gif","./image/18.gif","./image/19.gif",
"./image/20.gif","./image/21.gif","./image/22.gif",
"./image/23.gif","./image/24.gif","./image/25.gif","./image/26.gif"]

# extract width and height info
photo = PhotoImage(file=imagelist[0])
width = photo.width()
height = photo.height()
canvas = Canvas(width=width, height=height)
canvas.pack()

# create a list of image objects
giflist = []
for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)

# loop through the gif image objects for a while
for gif in giflist:
    canvas.delete(ALL)
    canvas.create_image(width/2.0, height/2.0, image=gif)
    canvas.update()
    time.sleep(0.2)

root.mainloop()
