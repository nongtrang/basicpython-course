#GUI-calculator.py

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวนปลารถ')
GUI.geometry('700x600')

bg = PhotoImage(file='car.png')
BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='กรอกจำนวนปลา (กิโลกรัม)',font=(None,20))
L.pack()

v_quantity = StringVar() # เป็นตัวแปรใช้เก็บข้อความเมื้อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack(ipadx=20,ipady=10)

f_price = StringVar() # เป็นตัวแปรเก็บราคาปลา
E2 = ttk.Entry(GUI, textvariable=f_price, font=(None,20))
E2.pack(ipadx=20,ipady=10,pady=20)

def Cal():
    try:
        quan = float(v_quantity.get())
        fprice = float(f_price.get())
        calc = quan * fprice #39 บาทต่อกิโล * จำนวนปลาที่กรอกมา
        messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc))
        v_quantity.set('')
        E1.focus()
    except:
            messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
            v_quantity.set('1')

B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20,pady=20) #ipadx ขยายความกว้าง x/y

GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา

