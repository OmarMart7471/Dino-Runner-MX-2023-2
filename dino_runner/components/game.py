import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,CLOUD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.Obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_c1 = 700
        self.y_pos_c1 = 50
        self.x_pos_c2 = 300
        self.y_pos_c2 = 90
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        else:
            self.screen.fill((94,129,162))
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed,self.player)
        if self.player.dino_dead: self.playing = False

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        cloud1 = CLOUD
        cloud2 = CLOUD

        test_font = pygame.font.Font(None,40)
        current_time = int(pygame.time.get_ticks()/10)
        score_surf = test_font.render(f'Score : {current_time}',False,(64,64,64))
        score_rect = score_surf.get_rect(center = (990,50))
        self.screen.blit(score_surf,score_rect)

        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.x_pos_c1 -= 2
        self.x_pos_c2 -= 5
        if self.x_pos_c1 < -100: self.x_pos_c1 = 1500
        if self.x_pos_c2 < -100: self.x_pos_c2 = 1000
        self.screen.blit(cloud1,(self.x_pos_c1,self.y_pos_c1))
        self.screen.blit(cloud2,(self.x_pos_c2,self.y_pos_c2))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg < -image_width :
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
