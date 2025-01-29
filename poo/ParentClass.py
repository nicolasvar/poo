class ParentClass:
    def __init__(self) -> None:
        self.name="";
        self.last_name="";
        self.birth_date=None
    def calculate_birth_date(self):
        return 2025-self.birth_date
    
object1 = ParentClass()
object1.name="Nicolas"
object1.last_name="Vargas"
object1.birth_date = 2004
age=object1.calculate_birth_date()
print(age)