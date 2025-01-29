class Director:
    def description(self) ->str:
        print("Soy el director del colegio")

class Teacher:
    def description(self) -> str:
        print("Soy el que enseña")

def descriptionPerson(person):
    person.description()

objeto1 = Teacher()
descriptionPerson(objeto1)