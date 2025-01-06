import tkinter as tk
window = tk.Tk()
window.title("Cars Predict")
window.geometry("600x600")

label = tk.Label(window, text="Cars Predict")
label.place(x=265,y=10)


label = tk.Label(window, text="Symboling : ")
label.place(x=10,y=50)

box1=tk.Entry(window)
box1.place(x=80,y=50)


label = tk.Label(window, text="Car Name : ")
label.place(x=10,y=90)

box1=tk.Entry(window)
box1.place(x=80,y=90)

label = tk.Label(window, text="Fueltype : ")
label.place(x=10,y=130)

v = tk.IntVar()
tk.Radiobutton(window, text='Gas', variable=v, value=1).place(x=80,y=130)
tk.Radiobutton(window, text='Diesel', variable=v, value=2).place(x=150,y=130)

label = tk.Label(window, text="Aspiration : ")
label.place(x=10,y=170)

v = tk.IntVar()
tk.Radiobutton(window, text='Std', variable=v, value=1).place(x=80,y=170)
tk.Radiobutton(window, text='Turbo', variable=v, value=2).place(x=150,y=170)

label = tk.Label(window, text="Door Number : ")
label.place(x=10,y=210)

v = tk.IntVar()
tk.Radiobutton(window, text='Two', variable=v, value=1).place(x=80,y=210)
tk.Radiobutton(window, text='Four', variable=v, value=2).place(x=150,y=210)

label = tk.Label(window, text="Car Body : ")
label.place(x=10,y=250)
from tkinter import ttk
combo_box = ttk.Combobox(window, values=["Convertible", "Hatch Back", "Sedan","Wagon","Hard Top"])
combo_box.place(x=90,y=250)
combo_box.set("Selection")

label = tk.Label(window, text="Drive Wheel : ")
label.place(x=10,y=290)
from tkinter import ttk
combo_box = ttk.Combobox(window, values=["RWD", "FWD", "4WD"])
combo_box.place(x=90,y=290)
combo_box.set("Selection")


label = tk.Label(window, text="Engine Location : ")
label.place(x=10,y=330)
v = tk.IntVar()
tk.Radiobutton(window, text='Front', variable=v, value=1).place(x=120,y=330)
tk.Radiobutton(window, text='Rear', variable=v, value=2).place(x=190,y=330)

label = tk.Label(window, text="Wheel Base : ")
label.place(x=10,y=370)

box1=tk.Entry(window)
box1.place(x=80,y=370)

label = tk.Label(window, text="Car Length : ")
label.place(x=10,y=410)

box1=tk.Entry(window)
box1.place(x=80,y=410)

label = tk.Label(window, text="Car Width : ")
label.place(x=10,y=450)

box1=tk.Entry(window)
box1.place(x=80,y=450)

label = tk.Label(window, text="Car Height : ")
label.place(x=10,y=490)

box1=tk.Entry(window)
box1.place(x=80,y=490)

label = tk.Label(window, text="Curb Weight : ")
label.place(x=10,y=530)

box1=tk.Entry(window)
box1.place(x=80,y=530)

label = tk.Label(window, text="Engine Type : ")
label.place(x=350,y=40)
from tkinter import ttk
combo_box = ttk.Combobox(window, values=["DOHC", "OHCV", "OHC","L","ROTOR","OHCF","DOHCV"])
combo_box.place(x=430,y=40)
combo_box.set("Selection")

label = tk.Label(window, text="Cylinder Number : ")
label.place(x=330,y=80)
from tkinter import ttk
combo_box = ttk.Combobox(window, values=["TWO","THREE","FOUR", "FİVE", "SİX","EİGHT","TWELVE"])
combo_box.place(x=431,y=80)
combo_box.set("Selection")

label = tk.Label(window, text="Engine Size : ")
label.place(x=350,y=120)

box1=tk.Entry(window)
box1.place(x=430,y=120)

label = tk.Label(window, text="Fuel System : ")
label.place(x=350,y=160)
from tkinter import ttk
combo_box = ttk.Combobox(window, values=["MPFI","2BBL","MFI", "1BBL", "SPFI","4BBL","IDI","SPDI"])
combo_box.place(x=430,y=160)
combo_box.set("Selection")

label = tk.Label(window, text="Boreratio : ")
label.place(x=350,y=200)

box1=tk.Entry(window)
box1.place(x=430,y=200)

label = tk.Label(window, text="Stroke : ")
label.place(x=350,y=240)

box1=tk.Entry(window)
box1.place(x=430,y=240)

label = tk.Label(window, text="Compressionratio : ")
label.place(x=320,y=280)

box1=tk.Entry(window)
box1.place(x=430,y=280)

label = tk.Label(window, text="Horse Power : ")
label.place(x=350,y=320)

box1=tk.Entry(window)
box1.place(x=430,y=320)

label = tk.Label(window, text="Peak RPM : ")
label.place(x=350,y=360)

box1=tk.Entry(window)
box1.place(x=430,y=360)

label = tk.Label(window, text="City MPG : ")
label.place(x=350,y=400)

box1=tk.Entry(window)
box1.place(x=430,y=400)

label = tk.Label(window, text="High Way MPG : ")
label.place(x=340,y=440)

box1=tk.Entry(window)
box1.place(x=430,y=440)


button = tk.Button(window,text="Predict",width=25)
button.place(x=200,y=560)
window.mainloop()
