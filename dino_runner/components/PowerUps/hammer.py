from dino_runner.components.PowerUps.power_ups import PowerUp
from dino_runner.utils.constants import HAMMER_TYPE,HAMMER
import pygame

class Hammer(PowerUp):

    def __init__(self):
        self.type = HAMMER_TYPE
        super().__init__(self.type)
        
    
    def get_image(self):
        self.image = HAMMER
        return self.image
    
    
