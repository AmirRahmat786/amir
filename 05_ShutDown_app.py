from tkinter import *
import os
def Restart():
    os.system("shutdown /r /s 1")
def Restart_Time():
    os.system("shutdown /r /s 2")     
def Log_out():    
    os.system("shutdown -1")
def ShutDown():
    os.system("shutdown 1")     
st = Tk()
st.title=("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")
r_button=Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button=Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Restart_Time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button=Button(st,text="Log_out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Log_out)
lg_button.place(x=150,y=270,height=50,width=200)

st_button=Button(st,text="ShutDown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=ShutDown)
st_button.place(x=150,y=370,height=50,width=200)
mainloop()