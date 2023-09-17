from random import randint
from Cell import Cell
import sys
import pygame
class Sudoku:

    def __init__(self):
        self.board = [[0 for x in range(9)] for y in range(9)]
        self.occurences = 0
        self.generateBoard(0,0)
        self.printBoard()
        print(self.occurences)

        self.gameBoard = [[Cell(x,y,self.board[y][x]) for x in range(9)] for y in range(9)]
        self.hideCells(35)

        self.waiting = False
        self.highlighted_cell = Cell(0,0,0)


    def move(self, mousePosition):
        #reset
        self.highlighted_cell.highlighted = False
        self.waiting = False

        # go through each cell detect if a cell was clicked
        for x in range(9):
            for y in range(9):
                if self.gameBoard[x][y].cell_rect.collidepoint(mousePosition):
                    self.waiting = True
                    self.highlighted_cell = self.gameBoard[x][y]
                    self.highlighted_cell.highlighted = True
                    print(self.highlighted_cell.number)


    def enterNum(self, k_input):
        if k_input == pygame.K_1:
            self.highlighted_cell.test = "1"

        elif k_input == pygame.K_2:
            self.highlighted_cell.test = "2"

        elif k_input == pygame.K_3:
            self.highlighted_cell.test = "3"

        elif k_input == pygame.K_4:
            self.highlighted_cell.test = "4"

        elif k_input == pygame.K_5:
            self.highlighted_cell.test = "5"

        elif k_input == pygame.K_6:
            self.highlighted_cell.test = "6"

        elif k_input == pygame.K_7:
            self.highlighted_cell.test = "7"

        elif k_input == pygame.K_8:
            self.highlighted_cell.test = "8"

        elif k_input == pygame.K_9:
            self.highlighted_cell.test = "9"


    def checkNum(self):
        if self.waiting == True:
            if self.highlighted_cell.test == self.highlighted_cell.number:
                self.highlighted_cell.found = True
                print("True")
            else:
                print("Incorrect")


    def hideCells(self, num):

        cells = []
        for i in range(81):
            cells.append(i)

        for i in range (81):
            r = randint(0, i)

            exch = cells[i]
            cells[i] = cells[r]
            cells[r] = exch

        for i in range(num):
            cell = cells[i]
            x = int(cell/9)
            y = cell - 9*x

            self.gameBoard[x][y].hidden = True


    def displayBoard(self, screen):
        for i in range(9):
            for z in range(9):
                self.gameBoard[i][z].drawCell(screen)

    def generateBoard(self, x, y):
        self.occurences += 1
        # if self.turns > 100: return False
        # print(self.turns)


        #generate random order of numbers 1-9
        list1 = self.randomList()

        for i in range(9):
            # check if number is legal
            if (self.checkRow(x, list1[i])== False and self.checkColumn(y, list1[i]) == False
                and self.checkSquare(x, y, list1[i]) == False):
                # if number works, place in board
                self.board[x][y] = list1[i]


                #repeat in following cell

                #if current cell is regular
                if y < 8:
                    if self.generateBoard(x, y+1) == True: return True
                    else: self.board[x][y] = 0

                #if current cell is an edge cell and
                elif y==8 and x < 8:
                    if self.generateBoard(x+1, 0) == True: return True
                    else:
                        self.board[x][y] = 0


                else: return True

        return False


    def randomList(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        #shuffle list
        for i in range (9):
            r = randint(0, i)

            exch = numbers[i]
            numbers[i] = numbers[r]
            numbers[r] = exch

        return numbers


    def printBoard(self):
        # function to display the board in terminal
        b = ""

        for x in range(1,10):
            for y in range(1,10):
                b = b + str(self.board[x-1][y-1]) + " "
                if y%3 == 0 and y != 9:
                    b = b + "| "

            b = b+ "\n"
            if x % 3 == 0 and x != 9:
                for z in range(21):
                    b = b+ "-"
                b = b + "\n"
        print(b)


    def checkRow(self, row, num):
        # function that returns True if a given number is present in a given row

        for y in range(9):
            if num == self.board[row][y] :

                return True

        return False

    def checkColumn(self, column, num):
        # function that returns True if a given number is present in a given column
        for x in range(9):
            if num == self.board[x][column] :
                return True

        return False

    def checkSquare(self, x, y, num):
        equal = False
        if x >=0 and x <3:
            if y >= 0 and y < 3:
                for i in range (0,3):
                    for z in range(0,3):
                        if self.board[i][z] == num:
                            return True

            elif y >= 3 and y < 6:
                for i in range (0,3):
                    for z in range(3,6):
                        if self.board[i][z] == num:
                            return True

            elif y >= 6 and y < 9:
                for i in range (0,3):
                    for z in range(6,9):
                        if self.board[i][z] == num:
                            return True

        elif x >= 3 and x < 6:
            if y >= 0 and y < 3:
                for i in range(3,6):
                    for z in range(0, 3):
                        if self.board[i][z] == num:
                            return True

            elif y >= 3 and y < 6:
                for i in range(3,6):
                    for z in range(3, 6):
                        if self.board[i][z] == num:
                            return True

            elif y >= 6 and y < 9:
                for i in range(3,6):
                    for z in range(6, 9):
                        if self.board[i][z] == num:
                            return True



        elif x >= 6 and x < 9:
            if y >= 0 and y < 3:
                for i in range(6,9):
                    for z in range(0, 3):
                        if self.board[i][z] == num:
                            return True

            elif y >= 3 and y < 6:
                for i in range(6,9):
                    for z in range(3, 6):
                        if self.board[i][z] == num:
                            return True

            elif y >= 6 and y < 9:
                for i in range(6,9):
                    for z in range(6, 9):
                        if self.board[i][z] == num:
                            return True

        return equal
