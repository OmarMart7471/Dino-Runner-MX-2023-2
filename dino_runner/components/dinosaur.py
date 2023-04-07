#IMPORTACIÓN DE LAS IMAGENES
import pygame
from dino_runner.components import text_utils
from dino_runner.utils.constants import (RUNNING,RUNNING_HAMMER,RUNNING_SHIELD,
JUMPING,JUMPING_HAMMER,JUMPING_SHIELD,DUCKING,DUCKING_HAMMER,DUCKING_SHIELD,
DEFAULT_TYPE,SHIELD_TYPE,HAMMER_TYPE,GUN_TYPE,DUCKING_GUN,JUMPING_GUN,RUNNING_GUN,
SCREEN_WIDTH,HAMMER
)
from dino_runner.components.PowerUps.hammer import Hammer
class Dinosaur:

    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 330
    JUMP_SPEED = 8.5

    def __init__(self):
        self.run_img = {
            DEFAULT_TYPE:RUNNING, 
            SHIELD_TYPE:RUNNING_SHIELD, 
            HAMMER_TYPE:RUNNING_HAMMER,
            GUN_TYPE:RUNNING_GUN
            }
        self.duck_img = {
            DEFAULT_TYPE:DUCKING, 
            SHIELD_TYPE:DUCKING_SHIELD, 
            HAMMER_TYPE:DUCKING_HAMMER,
            GUN_TYPE:DUCKING_GUN
            }
        self.jump_img = {
            DEFAULT_TYPE:JUMPING, 
            SHIELD_TYPE:JUMPING_SHIELD, 
            HAMMER_TYPE: JUMPING_HAMMER,
            GUN_TYPE:JUMPING_GUN
            }
        self.type= DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_SPEED
        self.dino_dead = False
        self.shield =  False
        self.hammer =  False
        self.gun =  False
        self.time_up_power_up = 0
        self.hammer_throw = False
        self.gun_shot= False
        self.gun_fire_position = (0,0)
        self.hammer_pos = self.dino_rect.x +100
        self.hammer_rect = HAMMER.get_rect()


    def run(self):
        self.image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img[self.type]
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
        self.image = self.duck_img[self.type][self.step_index // 5]
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
        elif (user_input[pygame.K_UP] or user_input[pygame.K_w])and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
        if self.step_index >=10:
            self.step_index = 0

        if user_input[pygame.K_SPACE] and self.hammer:
            self.hammer_throw = True

        if self.gun:
            self.gun_shot = True

          

        self.time_show()

    def time_show(self):
        if self.shield or self.hammer or self.gun:
            time_to_show=  round((self.time_up_power_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show < 0:
                self.reset()


    def draw(self,screen):
        screen.blit(self.image,self.dino_rect)
        if self.shield or self.hammer or self.gun:
            time_to_show=  round((self.time_up_power_up - pygame.time.get_ticks())/1000, 2)
            time = int(time_to_show)
            text, text_rect = text_utils.get_message(f'POWER UP TIME: {time}', 30,SCREEN_WIDTH//2,500)
            screen.blit(text, text_rect)
        if self.hammer_throw:
            self.draw_hammer(screen)
            self.hammer_throw = False

        if self.gun_shot:
            self.draw_aiming(screen)
            self.gun_shot = False


    def draw_aiming(self,screen):
        pygame.draw.line(screen,'Gold',(self.dino_rect.x+100,self.dino_rect.y+30),pygame.mouse.get_pos(),1)
        if pygame.mouse.get_pressed()[0]:
            print('clic derecho')
            self.gun_fire_position = pygame.mouse.get_pos()



    def draw_hammer(self,screen):
        self.hammer_rect = self.hammer_rect
        self.hammer_rect.x = self.hammer_pos
        self.hammer_rect.y = self.dino_rect.y
        if self.hammer:
            if self.hammer_pos < SCREEN_WIDTH:
                self.hammer_rect.x += 20
                self.hammer_pos +=20 
                screen.blit(HAMMER, self.hammer_rect)
                
            else:
                self.hammer = False
                self.reset()
                self.hammer_pos = self.dino_rect.x +100
        else:
            screen.blit(HAMMER, self.hammer_rect)


    def set_power_up(self,power_up):
        if power_up.type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
            self.shield = True
            self.time_up_power_up = power_up.time_up
        if power_up.type == HAMMER_TYPE:
            self.type = HAMMER_TYPE
            self.hammer = True
            self.time_up_power_up = power_up.time_up
        if power_up.type == GUN_TYPE:
            self.type = GUN_TYPE
            self.gun = True
            self.time_up_power_up = power_up.time_up

    def reset(self):
        self.type = DEFAULT_TYPE
        self.shield = False
        self.hammer =  False
        self.gun = False
        self.time_up_power_up = 0
        