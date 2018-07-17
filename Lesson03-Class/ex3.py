
class Map:
    
    def set_map(self,n):
        
        for i in range(n):
            for k in range(n):
                print("*",end="   ")
                k+=1
            i+=1
            print("\n")
    def set_pattern(self,k):
        if k==1:
            a="*"
            b="0"
            self.result=[(a*5),(a*1+b*3+a*1),(a*1+b*1+a*3),(a*2+b*1+a*2),(a*5)]
       
    def display(self):
        print(self.result)



my_map = Map()
my_map.set_pattern(1) # p=1, 設置 Glider 圖案在地圖中央
my_map.display() # 展示有 Glider 圖案的地圖
        
    

 #建立 instance object
my_map.set_map(6) # n=5, 代表地圖為 5x5 大小
#my_map.display() #印出 5x5 地圖