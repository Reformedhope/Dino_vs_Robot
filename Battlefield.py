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
       
        while self.dinosaur.health > 0 and self.robot.health >0:
                self.dinosaur.attack(self.robot)
                self.robot.attack(self.dinosaur)
           
           

    
            

    
      
    


    def display_winner(self):
        if self.dinosaur.health<= 0:
            print(f'{self.dinosaur.name} has wont the battle')
        if self.robot.health <= 0:
            print(f'{self.robot.name} has won the battle')