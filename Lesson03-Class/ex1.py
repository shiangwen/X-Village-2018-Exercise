


class triangle:
    def set_number(self,n):
        self.number=n
        i=1
        j=1
        while i<=self.number:
            while j<=self.number:
                print("*",end="")
                j+=1
            print("")
            i+=1
            j=i
    

tri=triangle()       
tri.set_number(3)

