import pygame
from random import randint

pygame.init()
pygame.font.init()

width = 800
height = 600

pong_display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong, 1v1")
clock = pygame.time.Clock()




Svart = (0,0,0)
Hvit = (255,255,255)




def scoring(skaaring,x,y):
    font = pygame.font.Font(None, 64)
    scoreBlit = font.render(str(skaaring), 1, (R, G, B))
    pong_display.blit(scoreBlit,(x,y))




def brett(x,y):
    pygame.draw.rect(pong_display, (R, G, B), (x, y, 8, 64))



def brett2(x,y):
    pygame.draw.rect(pong_display, (R, G, B), (x, y, 8, 64))



def ball(x,y):
    pygame.draw.rect(pong_display, (R, G, B), (x, y, 8, 8))


def spill_loop():
    x = width-width+5
    y = height/2.15
    x_2 = width/1.02
    y_2 = height/2.15
    x_ball = width/2
    y_ball = height/2.15

    y_endring = 0
    y_2endring = 0

    slutt_spill = False
    UP = False
    DOWN = False
    q = False
    a = False

    ballfart = 7
    retnforandring = 3

    ball_ret_x = -5
    ball_ret_y = 0
    score1 = 0
    score2 = 0
    global R
    global G
    global B
    R = 255
    G = 255
    B = 255




    while not slutt_spill:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                slutt_spill = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    UP = True

                if event.key == pygame.K_DOWN:
                    DOWN = True

            if event.type == pygame.KEYUP:
                if UP and event.key == pygame.K_UP:
                    UP = False
                if DOWN and event.key == pygame.K_DOWN:
                    DOWN = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    q = True

                if event.key == pygame.K_a:
                    a = True

            if event.type == pygame.KEYUP:
                if q and event.key == pygame.K_q:
                    q = False
                if a and event.key == pygame.K_a:
                    a = False

        if UP and DOWN:
            y_2endring  *= 1
        elif UP:
            y_2endring  = -9
        elif DOWN:
            y_2endring  = 9
        else:
            y_2endring  = 0

        if q and a:
            y_endring  *= 1
        elif q:
            y_endring  = -9
        elif a:
            y_endring  = 9
        else:
            y_endring  = 0





        if (x-4)<x_ball<(x+4) and (y-0.6)<y_ball<(y+25):

            ball_ret_x = ballfart
            ball_ret_y = -(retnforandring)


        if (x-4)<x_ball<(x+4) and (y+25)<y_ball<(y+40):

            ball_ret_x = ballfart
            ball_ret_y = 0

        if (x-4)<x_ball<(x+4) and (y+40)<y_ball<(y+64.1):

            ball_ret_x = ballfart
            ball_ret_y = retnforandring


        if (x_2-4)<x_ball<(x_2+4) and (y_2-0.6)<y_ball<(y_2+25):

            ball_ret_x = -ballfart
            ball_ret_y = -(retnforandring)


        if (x_2-4)<x_ball<(x_2+4) and (y_2+25)<y_ball<(y_2+40):

            ball_ret_x = -ballfart
            ball_ret_y = 0

        if (x_2-4)<x_ball<(x_2+4) and (y_2+40)<y_ball<(y_2+64.1):

            ball_ret_x = -ballfart
            ball_ret_y = retnforandring

        if y_ball>height:
            ball_ret_y = -(retnforandring)

        if y_ball<0:
            ball_ret_y = retnforandring



        if y_2 > height-64:
            y_2 = height-64

        elif y_2 < 0:
            y_2 = 0


        if y > height-64:
            y = height-64

        elif y < 0:
            y = 0

        if ballfart > 10:
            ballfart = 10

        x_ball += ball_ret_x
        y_ball += ball_ret_y
        y_2 += y_2endring
        y += y_endring
        pong_display.fill(Svart)
        ball(x_ball,y_ball)
        scoring(score1,32, 16)
        scoring(score2,height+92,16)
        brett(x,y)
        brett2(x_2,y_2)
        ballfart+=0.02
        R -= 1
        if R < 20:
            randint(80,255)

        if R < 90:
            G = randint(80,255)


        if G < 90:
            B = randint(80,255)

        if R < 10 or G < 10 or B < 10:
            R = randint(35,255)
            G = randint(35,255)
            B = randint(35,255)



        pygame.display.update()
        clock.tick(60)

        if x_ball < 0:
            score2+=1
            x_ball = width/2
            y_ball = height/2.15
            ball_ret_x = -6
            ball_ret_y = 0




        if x_ball > width:
            score1+=1
            x_ball = width/2
            y_ball = height/2.15
            ball_ret_x = -6
            ball_ret_y = 0









        if score1 == 3 or score2 == 3:
            if score1 == 3:
                scoring("Spiller 1 vant!!!",300,400)
            if score2 == 3:
                scoring("Spiller 2 vant!!!",300,400)

spill_loop()
pygame.quit()
quit()
