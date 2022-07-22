import pygame, sys
import numpy as np

pygame.init()
 
WIDTH, HEIGHT = 600, 600
BOARD_ROWS = 3
BOARD_COLS = 3


#Graphic
CIRCLE_BLACK = (16, 15, 15)
CROSS_WHITE = (241, 241, 241)
BG_BEIGE = (226, 220, 200)
LINE_GREEN = (15, 61, 62)
LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55


#Screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
SCREEN.fill(BG_BEIGE)


#Board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


#Lines
def drawing_lines():
    #horizontal 1
    pygame.draw.line(SCREEN, LINE_GREEN, (0, 200), (600, 200), LINE_WIDTH)
    
    #horizontal 2
    pygame.draw.line(SCREEN, LINE_GREEN, (0, 400), (600, 400), LINE_WIDTH)
    
    #vertical 1
    pygame.draw.line(SCREEN, LINE_GREEN, (200, 0), (200, 600), LINE_WIDTH)
    
    #vertical 2
    pygame.draw.line(SCREEN, LINE_GREEN, (400, 0), (400, 600), LINE_WIDTH)


#Square
def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            
            #draw circle (PLAYER 1)
            if board[row][col] == 1:
                pygame.draw.circle(SCREEN, CIRCLE_BLACK, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)

            #draw cross (PLAYER 2)
            elif board[row][col] == 2:
                pygame.draw.line(SCREEN, CROSS_WHITE, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(SCREEN, CROSS_WHITE, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


#Winning and Restart Function
def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line()

def draw_vertical_winning_line(col, player):
    pass

def draw_horizontal_winning_line(row, player):
    pass

def draw_asc_diagonal(player):
    pass

def draw_desc_diagonal(player):
    pass

def restart():
    pass





def main():

    player = 1

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


       

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                
                if player == 1:
                    mark_square(clicked_row, clicked_col, player)
                    player = 2
                    print(board)

                elif player == 2:
                    mark_square(clicked_row, clicked_col, player)
                    player = 1
                    print(board)

                draw_figures()



        drawing_lines()



        pygame.display.update()



if __name__ == "__main__":
    main()
