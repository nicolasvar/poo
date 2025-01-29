from ChildClass import ChildClass

class ThirdClass(ChildClass):
    def __init__(self):
        super().__init__('Vive en Lima')

    def calculate_birth_date(self):
        return f'{super().calculate_birth_date()} {self.address}'
    
object1= ThirdClass()
object1.birth_date = 2004
print(object1.calculate_birth_date())