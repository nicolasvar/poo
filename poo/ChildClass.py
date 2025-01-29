from ParentClass import ParentClass

class ChildClass(ParentClass):
    def __init__(self,address:str) -> None:
        ParentClass.__init__(self)
        self.address = address

    def calculate_birth_date(self) -> str:
        return f'{str(super().calculate_birth_date())} en clase hija y vive en {self.address}'
    
object1= ChildClass("Calle Lima")
object1.address="Lima"
object1.birth_date=2004
data = object1.calculate_birth_date()
print(data)

    
