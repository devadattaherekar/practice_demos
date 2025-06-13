import tkinter as tk

window=tk.Tk()
window.title("My First UI")
x=window.winfo_screenwidth()
y=window.winfo_screenheight()
print(x,y)
window.geometry("800x600")
window.configure(background="#9FE2BF")
name_label=tk.Label(window,text="Enter your name ")
name_label.place(x=20,y=100)
# geometry layout manager / widget manager
# choose one of the 3 widget managers pack() / grid() / place()
#name_label.pack(padx=1,pady=10,ipadx=20,ipady=20,fill="y",expand=True)
#name_label.grid(row=0,column=0)
# city_label=tk.Label(window,text="Enter your city ")
# city_label.grid(row=1,column=0,sticky="w")

city_label=tk.Label(window,text="Enter your city ")
city_label.place(x=20,y=200)
#city_label.grid(row=0,column=0)

def greetuser():
    label2=tk.Label(text="Hello hrishikesh",bg="yellow",fg="red")
    label2.pack()

def farewelluser():
    label2=tk.Label(text="Good Bye hrishikesh",bg="light blue",fg="green")
    label2.pack()

greet_button=tk.Button(window,text="Greet Me",command=greetuser)
greet_button.pack()

farewell_button=tk.Button(window,text="Farewell Me",command=farewelluser)
farewell_button.pack()

window.mainloop()

