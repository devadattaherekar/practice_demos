import tkinter as tk

window=tk.Tk()
window.title("Calculate Application")
window.geometry("800x600")
window.configure(background="#9FE2BF")

label1=tk.Label(window,text="Enter First Number ",bg="pink")
label1.place(x=20,y=60)
label2=tk.Label(window,text="Enter Second Number ",bg="pink")
label2.place(x=20,y=120)
label3=tk.Label(window,text="Result ",bg="pink")
label3.place(x=20,y=180)


var1=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()


FirstEntry=tk.Entry(window,textvariable=var1,width=30)
FirstEntry.place(x=200,y=60)
SecondEntry=tk.Entry(window,textvariable=var2,width=30)
SecondEntry.place(x=200,y=120)
ThirdEntry=tk.Entry(window,textvariable=var3,width=30)
ThirdEntry.place(x=200,y=180)


def clearfunction():
    var1.set("")
    var2.set("")
    var3.set("")

def findtotal():
    var3.set(int(var1.get())+int(var2.get()))

Addbutton=tk.Button(window,text="ADD",width=30,bg="#abe6ff",command=findtotal)
Addbutton.place(x=500,y=60)
Clearbutton=tk.Button(window,text="CLEAR",width=30,bg="#fcd0ef",command=clearfunction)
Clearbutton.place(x=500,y=120)
ExitButton=tk.Button(window,text="EXIT",width=30,bg="#f44545",command=window.destroy)
ExitButton.place(x=500,y=180)



window.mainloop()

