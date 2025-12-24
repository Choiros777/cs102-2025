import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.width = life.cols * cell_size
        self.height = life.rows * cell_size
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.paused = False

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                (0, y), (self.width, y))


    def draw_grid(self) -> None:
        screen = self.screen

        for i in range(self.life.rows):

            for j in range(self.life.cols):

                cell_value = self.life.curr_generation[i][j]

                if cell_value == 1:
                    cell_color = "green"
                else:
                    cell_color = "white"

                x_position = j * self.cell_size
                y_position = i * self.cell_size
                width = self.cell_size
                height = self.cell_size

                pygame.draw.rect(screen, cell_color,
                                 (x_position, y_position, width, height))


    def run(self) -> None:
        pygame.init()
        fps_controller = pygame.time.Clock()
        pygame.display.set_caption("Игра 'Жизнь'")
        self.screen.fill((255, 255, 255))

        pause_mode = False

        continue_game = True
        while continue_game:
            for current_event in pygame.event.get():
                if current_event.type == pygame.QUIT:
                    continue_game = False

                elif current_event.type == pygame.KEYDOWN:
                    # Клавиша P для паузы
                    if current_event.key == pygame.K_p:
                        pause_mode = not pause_mode

                elif current_event.type == pygame.MOUSEBUTTONDOWN:
                    # Только если на паузе
                    if pause_mode:
                        click_x, click_y = current_event.pos

                        cell_x = click_x // self.cell_size
                        cell_y = click_y // self.cell_size

                        self.life.curr_generation[cell_y][cell_x] = (self.life.curr_generation[cell_y][cell_x] + 1) % 2

            if not pause_mode:
                self.life.step()

            self.draw_lines()

            self.draw_grid()

            pygame.display.flip()

            fps_controller.tick(self.speed)

        pygame.quit()

