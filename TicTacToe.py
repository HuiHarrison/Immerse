import pygame, sys
import numpy as np

pygame.init()
 
 #Window
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


#Draw Circle and Cross
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


#set player to colour
def player_to_colour(player):
    if player == 1:
        return CIRCLE_BLACK
    elif player == 2:
        return CROSS_WHITE


#Winning and Restart Function
def check_win(player):
    #Vertical
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            pygame.draw.line(SCREEN, player_to_colour(player), (col * 200 + 100, 15), (col * 200 + 100, HEIGHT - 15), LINE_WIDTH)
            reset()

    #Horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            pygame.draw.line(SCREEN, player_to_colour(player), (15, row * 200 + 100), (WIDTH - 15, row * 200 + 100), LINE_WIDTH)
            reset()

    #Ascending Diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        pygame.draw.line(SCREEN, player_to_colour(player), (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH)
        reset()

    #Descending Diagonal
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        pygame.draw.line(SCREEN, player_to_colour(player), (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH)
        reset()

    #draw
    if is_board_full() == True:
        reset()


#Reset Board
def reset():
    pygame.display.update()
    pygame.time.wait(500)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

    SCREEN.fill(BG_BEIGE)
    drawing_lines()
    player = 1


#Main Function
def main():

    player = 1

    running = True
    while running:
        
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
                    draw_figures()
                    check_win(1)
                    player = 2

                elif player == 2:
                    mark_square(clicked_row, clicked_col, player)
                    draw_figures()
                    check_win(2)
                    player = 1
                    
        drawing_lines()

        pygame.display.update()


if __name__ == "__main__":
    main()
