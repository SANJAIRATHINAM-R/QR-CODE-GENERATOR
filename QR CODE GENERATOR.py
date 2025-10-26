from tkinter import *
import pyqrcode
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
app=Tk()
app.geometry("350x350")
app.title('QR Code Generator')
get_image=None

def create_code():
    save_path=filedialog.asksaveasfilename(title="save",defaultextension=".png",
                                         filetype=(("PNG File","*.png"),
                                         ("All Files","*.*")))

    if save_path:
        get_code=pyqrcode.create(ent.get())
        get_code.png(save_path,scale=10)
        global get_image
        get_image=ImageTk.PhotoImage(Image.open(save_path))
        lab.config(image=get_image)
    else:
        messagebox.showerror(title="Error",message="Something went wrong")

def reset():
    ent.delete(0,END)
    lab.config(image='')
ent=Entry(app,font="20")
ent.pack(pady=20)
btn1=Button(app,text="Generate",command=create_code)
btn1.pack(pady=20)
btn2=Button(app,text="Reset",command=reset)
btn2.pack()
lab=Label(app,text='')
lab.pack()
app.mainloop()
