import pygame
from dino_runner.utils.constants  import SCREEN_WIDTH

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self,game_speed,player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            if not player.shield:
                player.dino_dead = True
        if self.rect.colliderect(player.hammer_rect):
            return 1
        if self.rect.collidepoint((player.gun_fire_position[0], player.gun_fire_position[1])):
            return 1


    def get_rect(self):
        return self.rect

    def draw(self,screen):
        screen.blit(self.image,self.rect)