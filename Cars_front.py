import tkinter as tk
def data():
    import Cars_Linear as ml
    try:
        symboling=int(box1.get())
        carname=str(box2.get())
        fueltype=str(v1.get())
        aspiration=str(v2.get())
        doornumber=str(v3.get())
        carbody=str(combo_box1.get())
        drivewheel=str(combo_box2.get())
        engineloc=str(v4.get())
        wheelbase=float(box3.get())
        carlenght=float(box4.get())
        carwidth=float(box5.get())
        carheight=float(box6.get())
        curbweight=int(box7.get())
        engintype=str(combo_box3.get())
        cylindernumber=str(combo_box4.get())
        enginsize=int(box8.get())
        fuelsystem=str(combo_box5.get())
        borerotio=float(box9.get())
        stoke=float(box10.get())
        compressinrata=float(box11.get())
        horse_power=int(box12.get())
        peak=int(box13.get())
        city=int(box14.get())
        high_way=int(box15.get())
    except ValueError:
        tk.Message.showerror("Error", "Please enter a valid value")
    user_predict=[symboling,carname.lower(),fueltype.lower(),aspiration.lower(),doornumber.lower(),carbody.lower(),drivewheel.lower(),engineloc.lower(),wheelbase,carlenght,carwidth,carheight,
             curbweight,engintype.lower(),cylindernumber.lower(),enginsize,fuelsystem.lower(),borerotio,stoke,compressinrata,horse_power,peak,city,high_way]

    file=open("CarPrice_Assignment.csv","a")
    file.write(user_predict)
    file.close()
    ml()

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

box2=tk.Entry(window)
box2.place(x=80,y=90)

label = tk.Label(window, text="Fueltype : ")
label.place(x=10,y=130)

v1 = tk.IntVar()
tk.Radiobutton(window, text='Gas', variable=v1, value=1).place(x=80,y=130)
tk.Radiobutton(window, text='Diesel', variable=v1, value=2).place(x=150,y=130)

label = tk.Label(window, text="Aspiration : ")
label.place(x=10,y=170)

v2 = tk.IntVar()
tk.Radiobutton(window, text='Std', variable=v2, value=1).place(x=80,y=170)
tk.Radiobutton(window, text='Turbo', variable=v2, value=2).place(x=150,y=170)

label = tk.Label(window, text="Door Number : ")
label.place(x=10,y=210)

v3 = tk.IntVar()
tk.Radiobutton(window, text='Two', variable=v3, value=1).place(x=80,y=210)
tk.Radiobutton(window, text='Four', variable=v3, value=2).place(x=150,y=210)

label = tk.Label(window, text="Car Body : ")
label.place(x=10,y=250)
from tkinter import ttk
combo_box1 = ttk.Combobox(window, values=["Convertible", "Hatch Back", "Sedan","Wagon","Hard Top"])
combo_box1.place(x=90,y=250)
combo_box1.set("Selection")

label = tk.Label(window, text="Drive Wheel : ")
label.place(x=10,y=290)
from tkinter import ttk
combo_box2 = ttk.Combobox(window, values=["RWD", "FWD", "4WD"])
combo_box2.place(x=90,y=290)
combo_box2.set("Selection")


label = tk.Label(window, text="Engine Location : ")
label.place(x=10,y=330)
v4 = tk.IntVar()
tk.Radiobutton(window, text='Front', variable=v4, value=1).place(x=120,y=330)
tk.Radiobutton(window, text='Rear', variable=v4, value=2).place(x=190,y=330)

label = tk.Label(window, text="Wheel Base : ")
label.place(x=10,y=370)

box3=tk.Entry(window)
box3.place(x=80,y=370)

label = tk.Label(window, text="Car Length : ")
label.place(x=10,y=410)

box4=tk.Entry(window)
box4.place(x=80,y=410)

label = tk.Label(window, text="Car Width : ")
label.place(x=10,y=450)

box5=tk.Entry(window)
box5.place(x=80,y=450)

label = tk.Label(window, text="Car Height : ")
label.place(x=10,y=490)

box6=tk.Entry(window)
box6.place(x=80,y=490)

label = tk.Label(window, text="Curb Weight : ")
label.place(x=10,y=530)

box7=tk.Entry(window)
box7.place(x=80,y=530)

label = tk.Label(window, text="Engine Type : ")
label.place(x=350,y=40)
from tkinter import ttk
combo_box3 = ttk.Combobox(window, values=["DOHC", "OHCV", "OHC","L","ROTOR","OHCF","DOHCV"])
combo_box3.place(x=430,y=40)
combo_box3.set("Selection")

label = tk.Label(window, text="Cylinder Number : ")
label.place(x=330,y=80)
from tkinter import ttk
combo_box4 = ttk.Combobox(window, values=["TWO","THREE","FOUR", "FİVE", "SİX","EİGHT","TWELVE"])
combo_box4.place(x=431,y=80)
combo_box4.set("Selection")

label = tk.Label(window, text="Engine Size : ")
label.place(x=350,y=120)

box8=tk.Entry(window)
box8.place(x=430,y=120)

label = tk.Label(window, text="Fuel System : ")
label.place(x=350,y=160)
from tkinter import ttk
combo_box5 = ttk.Combobox(window, values=["MPFI","2BBL","MFI", "1BBL", "SPFI","4BBL","IDI","SPDI"])
combo_box5.place(x=430,y=160)
combo_box5.set("Selection")

label = tk.Label(window, text="Boreratio : ")
label.place(x=350,y=200)

box9=tk.Entry(window)
box9.place(x=430,y=200)

label = tk.Label(window, text="Stroke : ")
label.place(x=350,y=240)

box10=tk.Entry(window)
box10.place(x=430,y=240)

label = tk.Label(window, text="Compressionratio : ")
label.place(x=320,y=280)

box11=tk.Entry(window)
box11.place(x=430,y=280)

label = tk.Label(window, text="Horse Power : ")
label.place(x=350,y=320)

box12=tk.Entry(window)
box12.place(x=430,y=320)

label = tk.Label(window, text="Peak RPM : ")
label.place(x=350,y=360)

box13=tk.Entry(window)
box13.place(x=430,y=360)

label = tk.Label(window, text="City MPG : ")
label.place(x=350,y=400)

box14=tk.Entry(window)
box14.place(x=430,y=400)

label = tk.Label(window, text="High Way MPG : ")
label.place(x=340,y=440)

box15=tk.Entry(window)
box15.place(x=430,y=440)


button = tk.Button(window,text="Predict",width=25,command=data())
button.place(x=200,y=560)
window.mainloop()
