from dino_runner.components.cactus import Cactus
from dino_runner.components.bird import Bird
import random

class ObstacleManager:
    class_list = [Cactus,Bird]
    
    def __init__(self):
        self.obstacles = []

    def update(self,game_speed,player):
        if len(self.obstacles) == 0:
            random_class = random.choice(self.class_list)
            self.obstacles.append(random_class())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.pop()
            if isinstance(obstacle,Bird):obstacle.fly()
            if obstacle.update(game_speed,player) == 1:
               self.obstacles.remove(obstacle)
   

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
