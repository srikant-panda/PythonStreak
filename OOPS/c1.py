class Student:
    def __init__(self,name,age,regd_no):
        self.name = name
        self.age = age
        self.regd_no = regd_no

    def display(self):
        studentDict = {
            'Name' : self.name,
            'Age' : self.age,
            'Regd No' : self.regd_no,
        }
        
        print(studentDict)

s1 = Student('Srikanr', 19,2401204190)
s2 = Student('Chandan Kumar Dalai',19,2401204073)

s1.display()
s2.display()