from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import GUN,HAMMER,SHIELD
import pygame

class PowerUp:

    Y_POS_POWER_UP = 125
    POWER_UP_DURATION = 5000
    IMAGES = [HAMMER, SHIELD, GUN]

    def __init__(self,type):
        self.image_index = 0
        self.image = self.IMAGES[self.image_index]
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = self.Y_POS_POWER_UP
        self.start_time = 0
        self.image_change_counter = 0
        self.time_up = 0
        self.used = False

    def update(self,game_speed,player):
        self.rect.x -= game_speed 
        if self.rect.colliderect(player.dino_rect):
            self.start_time = pygame.time.get_ticks()
            self.time_up = self.start_time + self.POWER_UP_DURATION
            self.used = True
        

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def image_change(self):
        self.image_change_counter += 1
        if self.image_change_counter >= 5:
            self.image_change_counter = 0
            self.image_index = (self.image_index + 1) % len(self.IMAGES)
            self.image = self.IMAGES[self.image_index]