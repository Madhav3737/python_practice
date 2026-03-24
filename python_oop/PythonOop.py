class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def exam_results(self):
        if(self.marks>=40):
            print(self.name," is Pass")
        else:
            print(self.name," is Fail")

student1 = Student("Lakshman",65)
student2= Student("Mahesh",70)
student1.exam_results()
student2.exam_results()
#we can add attributes to an object from out side the class and those added so are only resembled in that object
student3 = Student("Madhav",40)
student3.class_room="cse-2"
print(student3.class_room)
#print(student2.class_room) // Throws error



    