#IMPORTACIÓN DE LAS IMAGENES
import pygame
from dino_runner.utils.constants import RUNNING,RUNNING_HAMMER,RUNNING_SHIELD,JUMPING,JUMPING_HAMMER,JUMPING_SHIELD,DUCKING,DUCKING_HAMMER,DUCKING_SHIELD

class Dinosaur:

    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 330
    JUMP_SPEED = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_SPEED
        self.dino_dead = False


    def run(self):
        self.image = RUNNING[0] if self.step_index <5 else RUNNING[1]
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            #SUBE
            self.dino_rect.y -= self.jump_vel * 4
            #BAJA
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_SPEED

    def duck(self):
        self.image = DUCKING[0] if self.step_index <5 else DUCKING[1]
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def update(self,user_input):

        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()

        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif (user_input[pygame.K_UP] or user_input[pygame.K_SPACE])and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
        if self.step_index >=10:
            self.step_index = 0


    def draw(self,screen):
        screen.blit(self.image,self.dino_rect)