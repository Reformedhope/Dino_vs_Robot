from dinosaur import Dinosaur
from robot import Robot 
import random

class Battlefield:
    def __init__(self):
        self.robot = Robot('Lorenzo')
        self.dinosaur = Dinosaur('Frank', 50)
    
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        


    def display_welcome(self):
        print('Welcome to the heated battle battle, Only one side is able to take the prize')
    
    def battle_phase(self):
       
        while True:
            if self.dinosaur.health >= 99: 
                self.dinosaur.attack(self.robot)
                self.robot.attack(self.dinosaur)
            elif self.dinosaur.health == 0:
                break
            elif self.robot.health >= self.dinosaur.health:      
                break
            elif self.robot.health >= 49: 
                self.dinosaur.attack(self.robot)
            elif self.dinosaur.health == 0:
                break
            elif self.robot.health == 0:      
                break
                self.robot.attack(self.dinosaur)

    
            

    
      
    


    def display_winner(self):
        print( "The winner is {self.name} there health was {self.health}")
        