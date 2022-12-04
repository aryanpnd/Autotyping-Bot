try:
    from tkinter import *
    from tkinter import messagebox
    import window1
    import window2
except ModuleNotFoundError:
    messagebox.showerror("BOT error","Some modules are not found on you device or directory \nTry installing following using PIP command in your terminal or powershell: \n• TKinter \n• PyautoGUI \n• Time")



aryanMain = Tk()
aryanMain.title("aryan window")
aryanMain.geometry('495x159')
aryanMain.maxsize(height=159,width=495)
aryanMain.minsize(height=159,width=495)
aryanMain.configure(background ="black")


def open1():
    window1.autoTypeBot()
def close1():
    window1.autoTypeBotDestroy()
    # Toplevel.destroy()


def open2():
    window2.randomTextSpamBot()
def close2():
    window2.randomTextSpamBotDestroy()


def showDev():
    messagebox.showinfo("Developer Info","This Bot was Developed by ARYAN \n\n  Language and Modules used: \n• Python \n• TKinter \n• PyautoGUI \n• Time")


lbl1 = Label(aryanMain, text="Auto Text Typing Bot",
          fg='#fc6f03', bg='black', font="arial 18 bold")
lbl1.grid(padx=10,pady=10,row=1,column=0)
btn1 = Button(aryanMain, text="Open",command=open1,bg='lime',font=(50))
btn1.grid(padx=10,pady=10,row=1,column=1)
btn2 = Button(aryanMain, text="Close",command=close1,bg='red',font=(50))
btn2.grid(padx=10,pady=10,row=1,column=2)

lbl2 = Label(aryanMain, text="Random Text Spamming Bot",
          fg='#fc6f03', bg='black', font="arial 18 bold")
lbl2.grid(padx=10,pady=10,row=3,column=0)
btn3 = Button(aryanMain, text="Open",command=open2,bg='lime',font=(50))
btn3.grid(padx=10,pady=10,row=3,column=1)
btn4 = Button(aryanMain, text="Close",command=close2,bg='red',font=(50))
btn4.grid(padx=10,pady=10,row=3,column=2)

devBtn = Button(aryanMain, text="Developer",command=showDev, bg='#9c275d',fg="white",activebackground="black",activeforeground="white", font="arial 12 bold")
devBtn.grid(ipadx=30,padx=50,pady=10)

aryanMain.mainloop()