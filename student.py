class Student:
    def __init__(self, name:str, notes:list = []):
        self.name = name
        self.notes = notes

    def add_note(self, note:int):
        self.notes.append(note)

    def find_notes(self):
        return f'Voici les notes de {self.name} : {self.notes}'
    
    def moy_notes(self):
        return f'La moyenne de {self.name} est de {sum(self.notes)/len(self.notes)}'


enzo = Student("Enzo")
enzo.add_note(16)
enzo.add_note(11)
enzo.add_note(5)
print(enzo.find_notes())
print(enzo.moy_notes())