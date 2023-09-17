import pygame
import sys
from Sudoku import Sudoku

class Game:
    def __init__(self):
        # setting screen
        screen_dim = (1200, 800)
        pygame.init()
        self.screen = pygame.display.set_mode(screen_dim)
        pygame.display.set_caption("Ben's ChessGame")

        self.bg_color = (225, 225, 225)
        self.screen.fill(self.bg_color)

        self.sudoku = Sudoku()

        self.active = False


    def mainScreen(self):
        while self.active ==False:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return False
                    # self.play()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    break


                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        break
            pygame.display.flip()

    def play(self):

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    self.sudoku.move(mouse_position)

                elif event.type == pygame.KEYDOWN:
                    k_input = event.key
                    self.sudoku.enterNum(k_input)

                    if event.key == pygame.K_RETURN:
                        self.sudoku.checkNum()

            self.sudoku.displayBoard(self.screen)
            pygame.display.flip()


