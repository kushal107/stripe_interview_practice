import myclass2 as myc
class Human:
    def __init__(self,name,age):
        self.name1 = name
        self.age1 = age

    def jump(self,city):
        print(f"please jump {self.name1} and you age is {self.age1} and {city}")

    
#instantiate the class Human
human1 = Human('Kushal',33)
human1.jump('Ranchi')

#Inherit the Human class
class Superhuman(Human):
    def __init__(self,name2, age2):
        super().__init__(name2,age2)
    
    def jump(self,city2):
        print(f"You are a superhuman {self.name1} with age {self.age1} and city {city2}")

superhuman1 = Superhuman('Kush',1)
superhuman1.jump('Delhi')

inst_class = myc.Mobile()
inst_class.var1 = 100
inst_class.var2 = 200
inst_class.showvar()
    