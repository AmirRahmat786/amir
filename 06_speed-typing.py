import random as r
from time import *

def mistake(paratest,usertest): 
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
              error = error + 1
        except:
            error = error + 1
    return error        

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s 
    time_r =round(time_delay,2)
    speed =len(userinput)/time_r 
    return round(speed) 
while True:
    check=input("Are you ready :yes / no:")
    if check == "yes" :
        test=["amir is a new coder and making try to become the best.","i have two friends both are the best",
            "which one is our teacher and best coder","2nd one is the official employee in a jinahh complex"]
        test1 = r.choice(test) 
        print(" ****** typing speed ****** ")
        print(test1)
        print()
        print()
        time_1 = time()
        practice = input(" Enter: ") 
        time_2 =time()
        print("speed :",speed_time(time_1,time_2,practice),"w/sec")
        print("Error :",mistake(test1,practice))
    elif check== "no":
        print("thank you")
        break
    
    else:
        print("wrong input")


        
















































































































































































































































































































































