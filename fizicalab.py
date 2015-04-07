from Tkinter import *
import tkMessageBox, sys, random
import tkFont, time, gif
from PIL import Image, ImageTk

root = Tk()
root.title(b"Fizika")
root.geometry('280x250')
image=Image.open('.\zxc.jpg')
background_image = ImageTk.PhotoImage(image)
l = Label(root, image = background_image)
l.pack(fill=BOTH, expand=YES)
l.bind('<Configure>')
l.pack()

def gift():
    gif.func()

def Re(p_g, r, t, L, q):
    return float( p_g*L**2/t/q)

def n_():
    global struct
    x = 0
    for i in range(len(struct)):
        s = struct[i]
        x += s[2]
    x/=len(struct)
    return x

def dn():
    global struct
    dx = 0.0
    sz = len(struct)
    for i in range(len(struct)):
        s = struct[i]
        dx += n_()**2
    if(len(struct)!=1):
        dx = (dx/(sz*(sz-1)))**0.5
    else:
        dx = (dx/(sz))**0.5
    return 2.8*dx

def radius_time(p_m, p_g, k, L):
    root.geometry('280x385')
    global struct
    height = L
    struct = []
    next_ = True
    go = True
    Lb1 = Listbox(root, height=10, width=50)
    for i in range(k):
        r = random.uniform(2, 3)
        r/=2
        r*=(height/0.5)
        print("Radius:", r)
        if(r<=2/2):
            t = random.uniform(7, 7.5)
        elif(r<=2.5/2):
            t = random.uniform(6, 7)
        elif(r<3/2):
            t = random.uniform(4.5, 6)
        elif(r>=3/2):
            t = random.uniform(3.75, 4.25)
        t*=(height/0.5)
        print("Time:", t)
        print()
        string = ""
        string = str(i+1) +"   Time:"+str(t)+ "  Radius:"+str( r)
        Lb1.insert(i+1, string)
        Lb1.pack()
        Lb1.place(x = 5, y = 235, height = 120, width = 265)
        minus = p_m-p_g
        q = 2*minus*r*r*(10**-6)*9.8*t/9/L
        if next_:
            if go :
                s = tkMessageBox.askokcancel(title = "Quesions", message = "Do work GIF?")
            if not s:
                next_ = False
                go = False
            else:
                gift()
                next_op = tkMessageBox.askokcancel(title = "Quesions", message = "Do visible next?")
                if not next_op:
                    s = False
                go = False
        struct.append([t, r, q])
    #Lb1.pack()
    #Lb1.place(x = 5, y = 235, height = 120, width = 265)
    str_dn = "dn = "+str(dn())
    label_dn = Label( root, text=str_dn)
    label_dn.pack()
    label_dn.place(x = 5, y = 360, height = 20, width = 265)
    print_main()

def inp_plotnosty():
    global struct
    global pl
    struct = []
    pl = []
    h = 20
    w = 90
    
    label = Label( root, text="Density material")
    label.pack()
    label.place(x = 10, y = 5, height = h, width = w)
    e1=Entry(root, width=30)
    e1.bind('<space>')
    e1.pack()
    e1.place(x = 115, y = 5, height = h, width = 150)

    label1 = Label( root, text="Density liquid")
    label1.pack()
    label1.place(x = 10, y = 35, height = h, width = w)
    e2=Entry(root,width=30)
    e2.bind('<space>')
    e2.pack()
    e2.place(x = 115, y = 35, height = h, width = 150)

    labeln = Label( root, text="Number of\n experiments (N)")
    labeln.pack()
    labeln.place(x = 10, y = 70, height = h+h, width = w)
    e3=Entry(root,width=30)
    e3.bind('<space>')
    e3.pack()
    e3.place(x = 115, y = 70+5, height = h, width = 150)

    labelL = Label( root, text="Height (L)")
    labelL.pack()
    labelL.place(x = 10, y = 75+45, height = h, width = w)
    e4=Entry(root,width=30)
    e4.bind('<space>')
    e4.pack()
    e4.place(x = 115, y = 75+45, height = h, width = 150)
    
    global p_m
    global L
    global p_g
    global k
    p_m = 0.0   
    p_g = 0.0    
    k = 0    
    L = 0.0
    
    def callback():
        if (not(e1.get()=="") and not(e2.get()=="") and not(e3.get()=="") and not(e4.get()=="")):
            if (e1.get() == e2.get()):
                tkMessageBox.showinfo("Error", "Please write true data")
            else:
                global p_m
                global p_g
                global k
                global L
                            
                p_m = p_m + float(e1.get())        
                p_g = p_g + float(e2.get())        
                k   = k + int(e3.get())        
                L   = L + float(e4.get())
                radius_time(p_m, p_g, k, L)
        else:
            tkMessageBox.showinfo("Error", "Please write data")

    
    b = Button(root, text="Get", width=30, command=callback)
    b.pack()
    b.place(x = 65, y = 165, height = h, width = 150)

    def pr_m_if():
        if(not(e1.get()=="")):
            print_main()
        else:
            tkMessageBox.showinfo("Error", "Please write data")
    
    ex = Button(root, text="Exit", width=30, command=root.quit)
    ex.pack()
    ex.place(x = 65, y = 205, height = h, width = 150)
    return

def print_main():
    global struct
    global pl
    global p_m
    global p_g
    global k
    global L

    lb_colom7 = Listbox(root, width=30)
    lb_colom1 = Listbox(root, width=30)
    lb_colom2 = Listbox(root, width=30)
    lb_colom3 = Listbox(root, width=30)
    lb_colom4 = Listbox(root, width=30)
    lb_colom5 = Listbox(root, width=30)
    lb_colom6 = Listbox(root, width=30)
    root.geometry('1145x390')
    if(lb_colom1.size()!=0 and lb_colom2.size()!=0 and lb_colom3.size()!=0 and lb_colom4.size()!=0 and lb_colom5.size()!=0 and lb_colom6.size()!=0 and lb_colom7.size()!=0):
        lb_colom1.delete(0, END)
        lb_colom2.delete(0, END)
        lb_colom3.delete(0, END)
        lb_colom4.delete(0, END)
        lb_colom5.delete(0, END)
        lb_colom6.delete(0, END)
        lb_colom7.delete(0, END)
        struct = []

    lb_colom1.insert(1, "N")
    lb_colom2.insert(1, "r")
    lb_colom3.insert(1, "t")
    lb_colom4.insert(1, "n")
    lb_colom5.insert(1, "dn")
    lb_colom6.insert(1, "dn^2")
    lb_colom7.insert(1, "Re")
    
    for i in range(len(struct)):
        s = struct[i]
        lb_colom1.insert(i+2, str(i+1))
        lb_colom2.insert(i+2, str(s[1]))
        lb_colom3.insert(i+2, str(s[0]))
        lb_colom4.insert(i+2, str(s[2]))
        lb_colom5.insert(i+2, str(n_()-s[2]))
        lb_colom6.insert(i+2, str((n_()-s[2])**2))
        lb_colom7.insert(i+2, str(Re(p_g, s[1], s[0], L, s[2])))

    r = 120
    o = 375
    lb_colom1.pack()
    lb_colom1.place(x = 5+280, y = 10, height = o, width = r)
    lb_colom2.pack()
    lb_colom2.place(x = 5+r+280, y = 10, height = o, width = r)
    lb_colom6.pack()
    lb_colom6.place(x = 5+r*2+280, y = 10, height = o, width = r)
    lb_colom5.pack()
    lb_colom5.place(x = 5+r*3+280, y = 10, height = o, width = r)
    lb_colom4.pack()
    lb_colom4.place(x = 5+r*4+280, y = 10, height = o, width = r)
    lb_colom3.pack()
    lb_colom3.place(x = 5+r*5+280, y = 10, height = o, width = r)
    lb_colom7.pack()
    lb_colom7.place(x = 5+r*6+280, y = 10, height = o, width = r)


    
global struct
global pl

inp_plotnosty()
root.mainloop()
