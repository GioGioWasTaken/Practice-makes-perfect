class Teacher:
    def __init__(self,name, subject, salery, is_experienced):
        self.name=name
        self.subject=subject
        self.salery=salery
        self.is_experienced=is_experienced
        self.print_all=print(f"Name: {name}\nSubject: {subject}\nSalery:{salery}$\nIs experienced:{is_experienced}")
class multiple_question:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d