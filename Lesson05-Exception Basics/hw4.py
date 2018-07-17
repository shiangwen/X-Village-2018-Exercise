# run me!
class RelationException(Exception):

    def __init__(self, err_msg):
        self.msg = err_msg
    def __str__(self):
        return  self.msg
   

try:
    a=input("Please input P1 ")
    b=input("Please input P2 ")
    raise RelationException(str(a)+str(b))

except RelationException as e:

    print("Are you sure that "+str(a)+" and "+str(b)+" are in love with each other?")
    