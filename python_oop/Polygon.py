class Polygon:
    def __init__(self,name,sides):
        self.name=name
        self.sides=sides
    def info(self):
        print("This is A polygon , A polygon is a closed shape constructed with straight lines")
    def perimeter(self):
        print("The perimeter of ",self.name,"is",sum(self.sides))
class Triangle(Polygon):
    def info(self):
        print("This is a Triangle, It is a polygon with three sides")
class Quadrilateral(Polygon):
    pass
triangle = Triangle("Triangle",[4,5,6])
triangle.info();
triangle.perimeter()
quadrilateral =Quadrilateral("Quadrilateral",[8,5,6,3])
quadrilateral.info()#since no info function in quadrilateral class , the info method in the polygon(parent) class will be executed
quadrilateral.perimeter()



