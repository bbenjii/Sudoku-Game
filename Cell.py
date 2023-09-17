import sys
import pygame

# colors
white = (255,255,255)
red = (255, 30, 70)
black = (0, 0, 0)

blue = (0, 102, 204)
grey = (121, 125, 127)
brown = (152, 82, 0)
beige = (255, 213, 164)

class Cell:
    def __init__(self, x, y, num):

        self.hidden = False
        self.found = False

        # square
        self.length = 80
        self.x = x
        self.y = y
        self.cell_rect = pygame.Rect(self.x*self.length+100,self.y*self.length+50, self.length, self.length)

        # number
        self.number= str(num)
        font = pygame.font.SysFont(None, self.cell_rect.width)
        self.number_img = font.render(self.number, True, black)
        self.number_rect = self.number_img.get_rect()
        self.number_rect.center = self.cell_rect.center

        self.highlighted = False

        self.test = ""

    def drawCell(self, screen):
        pygame.draw.rect(screen,white, self.cell_rect)
        pygame.draw.rect(screen, grey, self.cell_rect, 2)


        if self.hidden == False:
            screen.blit(self.number_img, self.number_rect)

        else:
            if self.found == True:

                font2 = pygame.font.SysFont(None, self.cell_rect.width)
                self.number_img2 = font2.render(str(self.number), True, blue)
                self.number_rect2 = self.number_img.get_rect()
                self.number_rect2.center = self.cell_rect.center
                screen.blit(self.number_img2, self.number_rect2)

            elif self.highlighted == True:

                font2 = pygame.font.SysFont(None, self.cell_rect.width)
                self.number_img2 = font2.render(str(self.test), True, (0, 0, 0))
                self.number_rect2 = self.number_img.get_rect()
                self.number_rect2.center = self.cell_rect.center

                pygame.draw.rect(screen, grey, self.cell_rect)
                screen.blit(self.number_img2, self.number_rect2)

