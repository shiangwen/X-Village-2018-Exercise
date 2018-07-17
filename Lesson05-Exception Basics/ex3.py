
def func(a,b):
    try:
        
        if b==0:
            raise ZeroDivisionError("divisor cannot be zero!")
        else: 
            return a/b
    
    except Exception:
        print("I'm in except block!")
        return
    finally:
        print("do something")
        
func(5,0)
func(5,1)
