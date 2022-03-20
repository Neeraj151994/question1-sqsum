class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqSum(self):
        return self.x**2+self.y**2+self.z**2
    
obj_sqSum=point(2,3,4)        
print(obj_sqSum.sqSum())