from tkinter import *
from PIL import ImageGrab
from tkinter import messagebox


global count
count =0
class App(): 
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')
        
    def start(self):
        global count
        count=0
        self.start_timer()
    
    def start_timer(self):
        global count
        self.timer()
    def stop(self):
        global count
        count=1
     
        
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s
            
            
            self.t.set(self.d)
            if(count==0):
                self.root.after(930,self.start_timer)
    def callback(self):
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            def Screenshot(self):
                Image=ImageGrab.grab()   
                Image.save(r"C:\Users\jaisw\OneDrive\Desktop\python\Hackathon\screen.png")
            self.root.destroy()
        
        
    def __init__(self):
        self.root=Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("Stop Watch")
        self.root.geometry("600x500")
        self.t = StringVar()
        self.t.set("00:00:00")
        self.root.configure(background='blue')
        self.lb = Label(self.root,textvariable=self.t)
        self.lb.config(font=("Courier 40 bold"))                
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Courier 12 bold"))
        self.bt2 = Button(self.root,text="Stop",command=self.stop,font=("Courier 12 bold"))
        self.bt3 = Button(self.root,text="Reset",command=self.reset,font=("Courier 12 bold"))
        self.lb.place(x=160,y=10)
        self.bt1.place(x=130,y=100)
        self.bt2.place(x=255,y=100)
        self.bt3.place(x=370,y=100)
        self.root.mainloop()
    


a = App()