#should be in=(len,isalpha,@,.,)
#should not be in= (space,upper isalpha)
while True: 
    k,m,n=0,0,0
    email = input("Enter email: ")
    if len(email)>=6:  
        if email[0].isalpha():
            if ("@"in email) and email.count("@")==1:
                if ("."in email) and (email[-4]=="." ):
                    for i in email:
                        if i==i.isspace():
                            k=1
                        elif i.isalpha():
                            if i==i.upper():
                                m=1
                        elif i.isdigit():
                            continue 
                        elif i=="_" or i=="@" or i==".": 
                            continue
                        else:
                            n=1
                    if k==1 or m==1 or n==1:
                        print("wrong email 5")
                    else:
                        print("right email")
                else:
                    print("wrong email 4")
            else:
                print("wrng email 3")
        else:
            print("wrong email 2")    
    else:
        print("wrong email 1")    