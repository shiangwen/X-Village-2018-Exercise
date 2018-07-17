



for i in range(1,51):

    
        
    if i==2:
        print(i,"是質數")
   
    for j in range(2,i):
       
        if (i%j)==0:
            
            break

        elif i%j!=0 and j+1==i :
            print(i,"是質數")
       
    
 

