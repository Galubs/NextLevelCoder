import pygame

from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING, JUMPING, DUCKING, RUNNING_SHIELD, SHIELD_TYPE
from pygame.sprite import Sprite



DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
NUM_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_ING[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x =self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL

    def setup_stated(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not  self.dino_jump and not self.dino_duck:
            self.dino_duck = False
            self.dino_jump = False
            self.dino_run = True

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x =self.X_POS
        self.dno_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jumo_vel = self.JUMP_VEL

    def check_invicibility(self):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >= 0 and self.show_text:
                draw_message_component(
                    f"Shield enable for {time_to_show}", 
                    screen,
                    font_size = 18
                    pos_x_center = 500,
                    pos_y_center =
                 )
    
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def draw(self, screen, pygame.Surface):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

