# class
## class-variable, instance-variable(member-variable)
## constructor, destructor, method
## magic method
## inheritance, mro, super
## overriding
## 접근제어자(public, protected, private), getter / setter

class Animal:
    # 클래스 변수
    type = "Animal"

    # 생성자
    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    # 소멸자
    def __del__(self):
        print(f"{Animal.type}: {self.name} destroyed")

    # magic method
    def __str__(self):
        return f"{self.name} is {self.age}"

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name_):
        self.__name = name_

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age_):
        self.__age = age_

    #method
    def walk(self):
        print(f"{self.name} is walking!!!")

    def say(self):
        print(f"{self.name} say ...")


class Cat(Animal):
    type = "Cat"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"{Cat.type}: {self.name} destroyed")

    def __str__(self):
        return f"{self.name} is {self.age}"

    def walk(self):
        print("f{self.name} walk slowly")
    
    def say(self):
        print("Meow Meow")

animal_var = Animal("ahn", 4)
cat_var = Cat("mho", 2)

print(animal_var)
print(cat_var)

print(f"animal.name: {animal_var.name}")
print(f"animal.age: {animal_var.age}")
print(f"cat.name: {cat_var.name}")
print(f"cat.age: {cat_var.age}")

animal_var.say()
cat_var.say()
    
