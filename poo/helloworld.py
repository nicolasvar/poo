from datetime import date 

class helloworld:
    def __init__(self):
        self.name:str =''
        self.birthDate:date= None
    def say_hello(self) -> str:
        return f"Hello, World {self.name}"
    def __privateMethod(self) -> str:
        return "This is a private method"
    
    
object1 = helloworld()
object1.name = "Nicolas"
print(object1.say_hello())

object2 = helloworld()
object2.name= "Dario"
var2 = object2.say_hello()
print(object2.__privateMethod())