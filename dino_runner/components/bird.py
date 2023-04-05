import random 
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.Y_POS = random.choice([200, 150, 300]) 
        self.rect.y = self.Y_POS
        self.image_change_counter = 0

    def fly(self):
        self.rect.y = self.Y_POS
        self.image_change_counter += 1
        if self.image_change_counter >= 7:
            self.image_change_counter = 0
            self.image = BIRD[1] if self.image == BIRD[0] else BIRD[0]
    
    
        
    