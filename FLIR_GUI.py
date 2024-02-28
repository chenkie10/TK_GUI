import tkinter as tk
from tkinter import ttk

import random
# info of window
window=tk.Tk()
window.title("FLIR Camera GUI")
window.geometry("600x600")
window.resizable(False,False)

canvas = tk.Canvas(window, width=500, height=450, bg="white")
canvas.place(x=30,y=10)


label_1 = tk.Label(window, text="Zoom")
label_1.place(x=520,y=400)

label_2=tk.Label(window, text="")
label_2.place(x=480,y=10)

signals = ["Signal 1", "Signal 2", "Signal 3", "Signal 4"]

label_3=tk.Label(window, text=f"Selcet {signals[0]}")
label_3.place(x=200,y=450)

#button for connect cam
def connect():
    pass


def image():
    canvas.create_rectangle(10, 30, 480, 430, fill="green")

def on_slider_change(value):
    label_1.config(text=f"Zoom: x{int(int(value)/20)}")

def FPS_measure():
    if checkbox_var.get():
        label_2.config(text="FPS:"+str(random.randint(10,40)),fg='red')
    else:
        label_2.config(text="  ")
        window.update()
def select_signals(event):
    selected_value=combobox.get()
    label_3.config(text=f"Select {selected_value}")




button_connect=tk.Button(window,text="Connect",command=connect)
button_connect.place(x=50,y=480)
image_button = tk.Button(window, text="Imaging", command=image)
image_button.place(x=120,y=480)
#Functions Line 1
button_fun1=tk.Button(window,text='Function1')
button_fun1.place(x=50,y=520)
button_fun2=tk.Button(window,text='Function2')
button_fun2.place(x=130,y=520)
button_fun3=tk.Button(window,text='Function3')
button_fun3.place(x=210,y=520)
#Functions Line 2
button_fun4=tk.Button(window,text='Function4')
button_fun4.place(x=50,y=550)
button_fun5=tk.Button(window,text='Function5')
button_fun5.place(x=130,y=550)
button_fun6=tk.Button(window,text='Function6')
button_fun6.place(x=210,y=550)
#Snapshot
button_snapshot=tk.Button(window,text="SnapShot")
button_snapshot.place(x=400,y=530)


slider = tk.Scale(window, from_=0, to=100, orient=tk.VERTICAL, command=on_slider_change,length=300)
slider.place(x=520,y=60)
checkbox_var=tk.IntVar()
checkbox = tk.Checkbutton(window, text="FPS on", variable=checkbox_var, command=FPS_measure)
checkbox.place(x=450,y=480)
combobox = ttk.Combobox(window, values=signals)
combobox.place(x=200,y=480)
combobox.set(signals[0])  
combobox.bind("<<ComboboxSelected>>", select_signals)

window.mainloop()