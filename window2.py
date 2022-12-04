import time
from tkinter import*
from types import TracebackType
import pyautogui
from tkinter import messagebox
from tkinter import ttk
import random    



def randomTextSpamBot():

    global randomTextSpamBotDestroy
    def randomTextSpamBotDestroy():
        aryan2.destroy()

    aryan2 = Toplevel()
    aryan2.title("Auto Typing Bot")
    aryan2.geometry('413x618')
    aryan2.minsize(width=413,height=618)
    aryan2.maxsize(width=413,height=618)
    # aryan2.configure(background="black")




    # sb = Scrollbar(aryan)  
    # sb.pack(side = RIGHT, fill = Y)  

    def bot():
        
        try:

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
                    arr = Text.split(',')

                    lid = e1.get()
                    lid2 = int(lid)
                    time.sleep(lid2)

                    result3 = str(c22.get())
                    result4 = str(".")
                    result5 = str(c33.get()).zfill(2)
                    tsiSTR = result3+result4+result5
                    TypingSpeedInterval = tsiSTR

                    
                    pyautogui.write(arr, interval=TypingSpeedInterval)

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

        except ValueError:
            messagebox.showwarning("BOT error","Please Enter Value Or \nCheck The Values you Entered")    
        except:
            messagebox.showerror("BOT error","BOT has Stopped \nCursor moved to 0-axis")


        # else:
        #     messagebox.showwarning("BOT Warning","Enter only Numbers \nOr Type ENDLESS (in capitals) for infinity loop ")


    def TextBoxClear():
        a1.delete(1.0, END)



    a = ttk.Label(aryan2, text="Text")
    a.pack()
    a1 = Text(aryan2, height=10, width=1000, padx=5, pady=5)
    a2 = ttk.Button(aryan2, text="Clear",command=TextBoxClear)
    a1.pack(padx=10, pady=0)
    a2.pack(padx=10, pady=0,ipadx=200)

    b = ttk.Label(aryan2, text="Bot's Start Timing")
    b.pack()
    b1 = ttk.Spinbox(aryan2, from_=0, to=60)
    b1.pack(padx=10, pady=10)


    c = ttk.Label(aryan2, text="Characters Typing Speed Delay")

    c2 = ttk.Label(aryan2, text="Seconds")
    c22 = Spinbox(aryan2, from_=0, to=60)

    c3 = ttk.Label(aryan2, text="Milliseconds")
    c33 = Spinbox(aryan2, from_=0, to_=99)

    c.pack()
    c2.pack()
    c22.pack()
    c3.pack()
    c33.pack()





    d = ttk.Label(aryan2, text="Bot Loop")
    d.pack()
    d1 = ttk.Label(aryan2, text ="(**type 'ENDLESS' for infinity OR select numbers**)")
    d1.pack()
    d2 = ttk.Spinbox(aryan2, from_=1, to=9999999999)
    d2.pack(padx=10, pady=10)

    e= ttk.Label(aryan2, text="Loop Interval Delay (in seconds)")
    e.pack(pady=5)
    e1 = ttk.Spinbox(aryan2, from_=0, to=9999)
    e1.pack(pady=5)


    btn = ttk.Button(aryan2, text="Start",command=bot)
    btn.pack(ipadx=200,ipady=10,padx=50,pady=10)
    # btn.pack(padx=10,pady=10)
    # btn1 = Button(aryan2, text="exit", command=aryan2.destroy, bg='red', font="arial 12 bold")
    # btn1.pack(ipadx=200,padx=50)
    # btn1.pack(padx=10,pady=10)


    aryan2.mainloop()


