#a-z ,0-9 , . , @ ,
while True:   
    import re
    email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    user=input("Enter Email: ")
    if re.search(email_condition,user):
        print("right email")
    else:
        print("wrong email")    

    ##### conditions sign #######
    """ sign for start with                (^) 
        sign for mearge other condition    (+)
        sign for search                    (\)
        sign works for availablity  
        which one or not                   (?) 
        sign for special chracter search   (\w)
        sign for search position of 
          any chracter or nomber           ({})                     
        sign for search from backward      ($)                    
                               """

        