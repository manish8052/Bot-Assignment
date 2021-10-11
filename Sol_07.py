p = input("Enter your password\n")
l, u, d, s = 0, 0, 0, 0

characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

if (len(p)>=6 and len(p)<=16):
    for i in p:
        if(i.islower()):
            l+=1
        if(i.isupper()):
            u+=1
        if(i.isdigit()):
            d+=1
        if i in characters or i=='"':
            s += 1
    #print(l,u,d,s)       
    if(l==0 or u==0 or d==0 or s==0):
        print("Oops!! Passward is Invalid ") 
    else:
        print("Paasward is valid")                
else:
    print("Oops!! Passward is Invalid ")
                      
            
        