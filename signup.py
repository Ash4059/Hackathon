from tkinter import *
from tkinter import messagebox
from tkinter import Tk
import random
import time
import datetime

def main():
    root=Tk()
    app=window1(root)


class window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Activity Tracker System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame=Frame(self.master,bg='powder blue')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()
        self.lblTitle=Label(self.frame,Text="Activity Tracker System",font=('arial',50,'bold'),bg='powder blue',fg='black')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)
        #==============================================================================
        self.LoginFrame1=Frame(self.frame,width=1350,height=600 ,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2=Frame(self.frame,width=1000,height=600 ,font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=20)
        self.LoginFrame2.grid(row=2,column=0)
#===================================Label and entry============================================
        self.lblUsername=Label(self.LoginFrame1,Text='Username',font=('arial',20,'bold'),bd=22,bg='Cadet blue',fg='Cornsilk')
        self.lblUsername.grid(row=0,column=0)
        self.lblUsername=Entry(self.LoginFrame1,font=('arial',20,'bold'))
        self.lblUsername.grid(row=0,column=1)

        self.lblPassword=Label(self.LoginFrame1,Text='Password',font=('arial',20,'bold'),bd=22,bg='Cadet blue',fg='Cornsilk')
        self.lblPassword.grid(row=1,column=0)
        self.lblPassword=Entry(self.LoginFrame1,font=('arial',20,'bold'))
        self.lblPassword.grid(row=1,column=1)
#===================================Buttons=====================================================
        self.btnLogin=Button(self.frame,text='Login',width=17,COMMAND=self.new_window)
        self.btnLogin.grid(row=3,column=0,pady=20,padx=8)
        self.btnReset=Button(self.frame,text='Reset',width=17,COMMAND=self.new_window)
        self.btnReset.grid(row=3,column=0,pady=20,padx=8)
        self.btnExit=Button(self.frame,text='Exit',width=17,COMMAND=self.new_window)
        self.btnExit.grid(row=3,column=0,pady=20,padx=8)
        
    def new_window(self):
        self.newwindow=Toplevel(self.master)
        self.app=window2(self.newwindow)


if __name__ == "__main__":
    main()