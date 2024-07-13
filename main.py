class Warrior():
        def __init__(self, name, power,endurance,hair_color):
            self.name = name
            self.power = power
            self.endurance = endurance
            self.hair_color = hair_color
        def  sleep(self):
            print(f"{self.name} is resting.")
            self.endurance+=2
        def eat(self):
            print(f"{self.name} is eating.")
            self.power+=1
        def hit(self):
            print(f"{self.name} is hitting.")
            self.endurance-=6
        def walk(self):
            print(f"{self.name} is walking.")
        def info(self):
            print(f"имя воина - {self.name}")
            print(f"сила воина - {self.power}")
            print(f"выносливость воина - {self.endurance}")
            print(f"цвет волос воина - {self.hair_color}")
war1=Warrior("Stiven",76,54,"brown")
war2=Warrior("Egor",45,23,"blond")
print(war1.info())
print(war1.endurance)
war1.sleep()
print(war1.endurance)