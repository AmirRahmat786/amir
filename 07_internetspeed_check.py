from tkinter import *
import speedtest 

def speedcheck():
    sp=speedtest.Speedtest() 
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+" mbps"  #sp.download() / 1024 /1024
    up = str(round(sp.upload()/(10**6),3))+" mbps"    #sp.upload() /1024/1024
    lab_down.config(text=down)
    lab_up.config(text=up) 

sp = Tk() 
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="White")

lab =Label(sp,text="Internet Speed Test",font=("Time New Roman",20,"bold"),bg="Blue",fg="Red")
lab.place(x=90,y=30,height=50,width=300)

lab =Label(sp,text="Download Speed",font=("Time New Roman",20,"bold"))
lab.place(x=90,y=130,height=50,width=300)

lab_down =Label(sp,text="00",font=("Time New Roman",20,"bold"))
lab_down.place(x=90,y=200,height=50,width=300)

lab =Label(sp,text="Upload Speed",font=("Time New Roman",20,"bold"))
lab.place(x=90,y=290,height=50,width=300)

lab_up =Label(sp,text="00",font=("Time New Roman",20,"bold"))
lab_up.place(x=90,y=360,height=50,width=300)

button = Button(sp,text="Check Speed",font=("Time New Roman",20,"bold"),relief=RAISED,bg="Red",command=speedcheck())
button.place(x=90,y=460,height=50,width=300)


sp.mainloop()