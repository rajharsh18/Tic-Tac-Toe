import pygame as pg
from pygame.locals import *
import time

X_O = 'X'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10,10,10)
T = [[None]*3,[None]*3,[None]*3]
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption("Tic Tac Toe")
opening = pg.image.load('tic_tac_opening.png')
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))


class TicTacToe:
    def game_opening():
        screen.blit(opening,(0,0))
        pg.display.update()
        time.sleep(1.5)
        screen.fill(white)
        pg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
        pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
        pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
        pg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)
        game_status.draw_status()


    def reset_game():
        global T, winner,X_O, draw
        time.sleep(1.5)
        X_O = 'X'
        draw = False
        TicTacToe.game_opening()
        winner=None
        T = [[None]*3,[None]*3,[None]*3]


 
class game_status:
    def draw_status():
        global draw
        if winner is None:
            message = X_O.upper() + "'s Turn"
        else:
            message = winner.upper() + " won!"
        if draw:
            message = 'Game Draw!'
        font = pg.font.Font(None, 30)
        text = font.render(message, 1, (255, 255, 255))
        screen.fill ((0, 0, 0), (0, 400, 500, 100))
        text_rect = text.get_rect(center=(width/2, 500-50))
        screen.blit(text, text_rect)
        pg.display.update()


    def check_win():
        global T, winner,draw
        for row in range (0,3):
            if ((T [row][0] == T[row][1] == T[row][2]) and(T [row][0] is not None)):

                winner = T[row][0]
                pg.draw.line(screen, (250,0,0), (0, (row + 1)*height/3 -height/6),\
                                  (width, (row + 1)*height/3 - height/6 ), 4)
                break

        for col in range (0, 3):
            if (T[0][col] == T[1][col] == T[2][col]) and (T[0][col] is not None):
                winner = T[0][col]
                pg.draw.line (screen, (250,0,0),((col + 1)* width/3 - width/6, 0),\
                              ((col + 1)* width/3 - width/6, height), 4)
                break

        if (T[0][0] == T[1][1] == T[2][2]) and (T[0][0] is not None):

            winner = T[0][0]
            pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)

        if (T[0][2] == T[1][1] == T[2][0]) and (T[0][2] is not None):

            winner = T[0][2]
            pg.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)

        if(all([all(row) for row in T]) and winner is None ):
            draw = True
        game_status.draw_status()



class Input:
    def drawXO(row,col):
        global T,X_O
        if row==1:
            posx = 30

        if row==2:
            posx = width/3 + 30

        if row==3:
            posx = width/3*2 + 30

        if col==1:
            posy = 30

        if col==2:
            posy = height/3 + 30

        if col==3:
            posy = height/3*2 + 30

        T[row-1][col-1] = X_O

        if(X_O == 'X'):
            screen.blit(x_img,(posy,posx))
            X_O= 'O'
        else:
            screen.blit(o_img,(posy,posx))
            X_O= 'X'
        pg.display.update()


    def userClick():
        x,y = pg.mouse.get_pos()
        if(x<width/3):
            col = 1
        elif (x<width/3*2):
            col = 2
        elif(x<width):
            col = 3
        else:
            col = None

        if(y<height/3):
            row = 1
        elif (y<height/3*2):
            row = 2
        elif(y<height):
            row = 3
        else:
            row = None

        if(row and col and T[row-1][col-1] is None):
            global X_O
            Input.drawXO(row,col)
            game_status.check_win()
        
        



# Main Function
TicTacToe.game_opening()
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
        elif event.type == MOUSEBUTTONDOWN:
            Input.userClick()
            if(winner or draw):
                TicTacToe.reset_game()
                
    pg.display.update()
    CLOCK.tick(fps)
