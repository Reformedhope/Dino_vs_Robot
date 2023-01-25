from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon  =   Weapon("Sword", 50) 
        

    def attack(self, dinosaur):
        if self.health > 0:
            dinosaur.health -= self.active_weapon.attack_power
            print (f'{self.name} attacked {dinosaur.name} for{self.active_weapon.attack_power}. Dinosaurs health is now {dinosaur.health}')



    
    