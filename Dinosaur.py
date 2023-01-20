from weapon import Weapon
class Dinosaur:
    def __init__(self,name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):
        robot.health -= self.attack_power
        print (f' {self.name} attacked {robot.name} for{self.attack_power}. Robots health is now {robot.health}')