import pygame
from dino_runner.components.dinosaur import Dinosaur
from obstacles.obstacle_manager import ObstaclesManager

from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

FONT_STYLE = 'freessansbold.ttf'

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.points = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.unning:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.update_score()
        self.player.check_inbicibility()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.player.update()

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
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                
            if event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255)) #change color
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2


        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE)
            text = font.render("Press any key to start", True, (0,0,0)) #change color
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
        elif self.death_count > 0:
            pass

        self.screen.blit(RUNNING[0], (half_screen_width - 20, half_screen_height - 140))

        pygame.display.update()
        self.handle_key_events_on_menu()

    def draw_score(self):
        draw_message_component(
            f"Points: {self.points}",
            self.screen,
            font_size=22,
        )
