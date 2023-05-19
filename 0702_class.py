# class
## static method, class method
## abstract class

class Calc:
    PI = 3.14
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 

    def __del__(self):
        print("Math Destroyed")

    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def div(x, y):
        if y > 0:
            return x / y
        else:
            print("hello")
            raise Exception("zero divied")
            return None

try:
    result = Calc.div(3, 5)
    print(result)
    result = Calc.div(3, 0)
    print(result)
except Exception as e:
    print(e)
finally:
    print("end")