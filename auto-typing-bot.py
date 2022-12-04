from tkinter import *
import pyautogui
import random
import time
from tkinter import messagebox


# print(random.choice(mylist))


aryan = Tk()
aryan.title("Auto Typing Bot")
aryan.geometry('413x618')
aryan.minsize(width=413,height=618)
aryan.maxsize(width=413,height=618)
aryan.configure(background="black")


# sb = Scrollbar(aryan)  
# sb.pack(side = RIGHT, fill = Y)  

def bot():

    result1 = b1.get()
    botStartTime = int(result1)
    time.sleep(botStartTime)

    loopResult = d2.get()

    # bst1 = c44.get()
    # lid = e1.get()
    

    if loopResult == "ENDLESS":
        while True:


            result2 = a1.get(1.0, END)
            Text = str(result2)

            lid = e1.get()
            lid2 = int(lid)
            time.sleep(lid2)

            result3 = str(c22.get())
            result4 = str(".")
            result5 = str(c33.get()).zfill(2)
            tsiSTR = result3+result4+result5
            TypingSpeedInterval = tsiSTR

            
            pyautogui.write(Text, interval=TypingSpeedInterval)

    else:
        for i in range(int(loopResult)):

            lid3 = e1.get()
            lid4 = int(lid3)
            time.sleep(lid4)

            result2 = a1.get(1.0, END)
            Text = str(result2)

            result3 = str(c22.get())
            result4 = str(".")
            result5 = str(c33.get()).zfill(2)
            tsiSTR = result3+result4+result5
            TypingSpeedInterval = tsiSTR

            pyautogui.write(Text, interval=TypingSpeedInterval)

    messagebox.showinfo("BOT","Task Completed")    

    # else:
    #     messagebox.showwarning("BOT Warning","Enter only Numbers \nOr Type ENDLESS (in capitals) for infinity loop ")


def TextBoxClear():
    a1.delete(1.0, END)


a = Label(aryan, text="Text", fg='#8403fc', bg='black', font="arial 18 bold")
a.pack()
a1 = Text(aryan, height=5, width=1000, padx=5, pady=5,
          bg="white", fg="black", font="arial 15")
a2 = Button(aryan, text="Clear", command=TextBoxClear, bg='#28327a', font="arial 10 bold")
a1.pack(padx=10, pady=0)
a2.pack(padx=10, pady=0,ipadx=200)

b = Label(aryan, text="Bot's Start Timing",
          fg='#fc6f03', bg='black', font="arial 18 bold")
b.pack()
b1 = Spinbox(aryan, from_=0, to=60, bg="#d3d0d6",
             fg="black", font="arial 13 bold")
b1.pack(padx=10, pady=10)


c = Label(aryan, text="Characters Typing Speed Delay",
          fg='#fcec03', bg='black', font="arial 18 bold")

c2 = Label(aryan, text="Seconds", fg='white', bg='black')
c22 = Spinbox(aryan, from_=0, to=60, bg="#d3d0d6",
              fg="black", font="arial 13 bold")

c3 = Label(aryan, text="Milliseconds", fg='white', bg='black')
c33 = Spinbox(aryan, from_=0, to_=99, bg="#d3d0d6",
              fg="black", font="arial 13 bold")

c.pack()
c2.pack()
c22.pack()
c3.pack()
c33.pack()





d = Label(aryan, text="Bot Loop", fg='#03fce3',
          bg='black', font="arial 18 bold")
d.pack()
d1 = Label(aryan, text ="(**type 'ENDLESS' for infinity OR select numbers**)",fg='red',bg='black')
d1.pack()
d2 = Spinbox(aryan, from_=1, to=9999999999, bg="#d3d0d6",
             fg="black", font="arial 13 bold")
d2.pack(padx=10, pady=10)

e= Label(aryan, text="Loop Interval Delay (in seconds)", fg='#a103fc', bg='black', font="arial 18 bold")
e.pack(pady=5)
e1 = Spinbox(aryan, from_=0, to=9999, bg="#d3d0d6",fg="black", font="arial 13 bold")
e1.pack(pady=5)


btn = Button(aryan, text="Start", command=bot, bg='lime', font="arial 12 bold")
btn.pack(ipadx=200,padx=50,pady=10)
# btn.pack(padx=10,pady=10)
# btn1 = Button(aryan, text="exit", command=aryan.destroy, bg='red', font="arial 12 bold")
# btn1.pack(ipadx=200,padx=50)
# btn1.pack(padx=10,pady=10)


aryan.mainloop()
