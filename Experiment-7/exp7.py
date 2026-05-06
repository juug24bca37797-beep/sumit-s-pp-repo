# Aim: Demonstrate OOP concepts (Inheritance types)

# -------- SINGLE INHERITANCE --------
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

class Student(Person):
    def display(self):
        print("Student class derived from Person")

# -------- MULTIPLE INHERITANCE --------
class Sports:
    def sport(self):
        print("Playing sports")

class Result(Student, Sports):
    def result(self):
        print("Result class using multiple inheritance")

# -------- MULTILEVEL INHERITANCE --------
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B derived from A")

class C(B):
    def showC(self):
        print("Class C derived from B")

# -------- HIERARCHICAL INHERITANCE --------
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

# -------- MAIN PROGRAM --------
print("Single Inheritance:")
s = Student("Sumit")
s.show()
s.display()

print("\nMultiple Inheritance:")
r = Result("Rahul")
r.show()
r.sport()
r.result()

print("\nMultilevel Inheritance:")
c = C()
c.showA()
c.showB()
c.showC()

print("\nHierarchical Inheritance:")
d = Dog()
d.speak()
d.bark()

c = Cat()
c.speak()
c.meow()
