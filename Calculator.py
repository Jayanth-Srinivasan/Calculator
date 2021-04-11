from tkinter import *
win=Tk()
win.title("Calculator")
EnterNum=""
TxtInp=StringVar()
def Clicked(num):
    global EnterNum
    EnterNum = EnterNum + str(num)
    #print(EnterNum)
    TxtInp.set(EnterNum)
def ClearClick():
    global EnterNum
    TxtInp.set("")
    EnterNum=""
def EqualClick():
    global EnterNum
    Ans=str(eval(EnterNum))
    TxtInp.set(Ans)
    EnterNum=""
def fact():
    global EnterNum
    f=1
    for i in range (1,int(eval(EnterNum))+1):
        f*=i
    Ans = str(f)
    TxtInp.set(Ans)
    EnterNum=""
TxtDisp= Entry(win,font=('Segoe UI Semibold',20,'bold'))
TxtDisp.config(textvariable=TxtInp,bd=20,width=20,bg="orange",justify="right")
TxtDisp.grid(columnspan=4)
B1=Button(win,text='7',bd=5,padx=20,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked(7),relief="ridge")
B1.grid(row=1,column=0)
B2=Button(win,text='8',bd=5,padx=20,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked(8),relief="ridge")
B2.grid(row=1,column=1)
B3=Button(win,text='9',bd=5,padx=23,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked(9),relief="ridge")
B3.grid(row=1,column=2)
B4=Button(win,text='+',bd=5,padx=20,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked("+"),relief="ridge")
B4.grid(row=1,column=3)
B5=Button(win,text='4',bd=5,padx=20,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked(4),relief="ridge")
B5.grid(row=2,column=0)
B6=Button(win,text='5',bd=5,padx=20,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked(5),relief="ridge")
B6.grid(row=2,column=1)
B7=Button(win,text='6',bd=5,padx=23,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked(6),relief="ridge")
B7.grid(row=2,column=2)
B8=Button(win,text='*',bd=5,padx=20,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked('*'),relief="ridge")
B8.grid(row=2,column=3)
B9=Button(win,text='1',bd=5,padx=20,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked(1),relief="ridge")
B9.grid(row=3,column=0)
B10=Button(win,text='2',bd=5,padx=20,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked(2),relief="ridge")
B10.grid(row=3,column=1)
B11=Button(win,text='3',bd=5,padx=23,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked(3),relief="ridge")
B11.grid(row=3,column=2)
B12=Button(win,text='/',bd=5,padx=20,fg="white",font=("new times roman",22,"bold"),bg="black",command=lambda:Clicked("/"),relief="ridge")
B12.grid(row=3,column=3)
B13=Button(win,text='0',bd=5,padx=20,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked(0),relief="ridge")
B13.grid(row=4,column=0)
B14=Button(win,text='c',bd=5,padx=20,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:ClearClick(),relief="ridge")
B14.grid(row=4,column=1)
B15=Button(win,text='-',bd=5,padx=23,fg="white",font=("new times roman",20,"bold"),bg="black",command=lambda:Clicked("-"),relief="ridge")
B15.grid(row=4,column=2)
B16=Button(win,text='=',bd=5,padx=20,fg="white",font=("new times roman",18,"bold"),bg="black",command=lambda:EqualClick(),relief="ridge")
B16.grid(row=4,column=3)
B17=Button(win,width=5,text='.',bd=5,padx=6,fg="white",font=("new times roman",15,"bold"),bg="black",command=lambda:Clicked("."),relief="ridge")
B17.grid(row=5,column=0)
B18=Button(win,text='POW',bd=5,padx=19,pady=8,fg="white",font=("new times roman",10,"bold"),bg="black",command=lambda:Clicked("**"),relief="ridge")
B18.grid(row=5,column=1)
B19=Button(win,text='SQRT',bd=5,padx=19,pady=8,fg="white",font=("new times roman",10,"bold"),bg="black",command=lambda:Clicked("**0.5"),relief="ridge")
B19.grid(row=5,column=2)
B20=Button(win,text='!',bd=5,padx=30,pady=8,fg="white",font=("new times roman",10,"bold"),bg="black",command=lambda:fact(),relief="ridge")
B20.grid(row=5,column=3)
win.mainloop()

