import tkinter as tk
from tkinter import *
from tkinter import ttk


def convert(a):
    return a * 1.8+32

print(convert(10))
a = tk.StringVar
root=tk.Tk()
root.title("Convert Temperature")
input_frame=ttk.Frame(root, padding=(10,10,10,10))
input_frame.pack()
temp_name_c=ttk.Label(input_frame, text='Temp in C')
temp_name_c.grid(padx=(2, 2), row=0, column=0)
temp_entery=ttk.Entry(input_frame, floatvariable = a)
a = Entry.get()
temp_entery.grid(row=0, column=1)
convert_temp=convert(a)
button_com=ttk.Button(input_frame, text="Convert", command= convert_temp)
button_com.grid(padx=(2, 2), row=1, column=1)
temp_name_f=ttk.Label(input_frame, text=str(convert_temp))
temp_name_f.grid(padx=(2, 2), row=0, column=1)

root.mainloop()

