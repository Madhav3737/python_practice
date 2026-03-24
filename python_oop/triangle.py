class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        perimeter=self.a+self.b+self.c
        return perimeter
triangle1= Triangle(4,5,6)
triangle2 = Triangle(6,7,8)
print("Perimeter of triangle is ",triangle1.perimeter())
print("Perimeter of triangle2 is ",triangle2.perimeter())