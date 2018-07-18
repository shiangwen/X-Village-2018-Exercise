

def eightqueen(test):   
    queen_x =[]  
    for i in test:
        queen_x += i

    print(queen_x)
    #print(queen_x[0])
    
    new_queen_x1 = []
    for i in range(0,len(queen_x),2):
        #print(queen_x[i])
        new_queen_x1.append(queen_x[i])
    print(new_queen_x1)
    
    new_queen_x2 = []
    for i in range(1,len(queen_x),2):
        #print(queen_x[i])
        new_queen_x2.append(queen_x[i])
    print(new_queen_x2)

    add = [a+b for a, b in zip(new_queen_x1,new_queen_x2)]
    less = [a+b for a, b in zip(new_queen_x1,new_queen_x2)]
  
    if len(set(new_queen_x1))!=8:
        print(False) 
    elif len(set(new_queen_x2))!=8:
        print(False) 
    elif len(set(add))!=8:
        return (False)
    elif len(set(less)))!=8:
        return (False)
    else:
        print(True)

eightqueen([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]])


