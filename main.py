#Use Better coments for a better expereince <3 
import pygame, sys, random

#! Functions 
#? Ball animations
def ball_animation():
    #* Speed
    global ball_speed_x, ball_speed_y, general_speed
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screenWidth:
        ball_speed_x = 7
        general_speed = -2
        ball_restart()
    #* Collitions
    if ball.colliderect(player) or ball.colliderect(opponent):
        if ball_speed_x == -14:
            general_speed = -1
        ball_speed_x *= general_speed

#? Player animations
def player_animation():
    #* Speed
    player.y += player_speed
    #* Collitions
    if player.top <= 0:
        player.top = 0 
    if player.bottom >= screenHeight:
        player.bottom = screenHeight 

#? Opponent animations
def opponent_animation():
     #* Speed
    opponent.y += opponent_speed
    #* Collitions
    if opponent.top <= 0:
        opponent.top = 0 
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight 
    # #* Opponent Follow the Ball (BOT AI)
    # if opponent.top < ball.y:
    #     opponent.top += opponent_speed
    # if opponent.bottom > ball.y:
    #     opponent.bottom -= opponent_speed
#? Center ball to the center when his x <= 0 or x <= width
def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = center
    ball_speed_y *= random.choice((1,-1))


pygame.init()
clock = pygame.time.Clock()


#! Display window
screenWidth = 1368
screenHeight = 700
screen = pygame.display.set_mode((screenWidth, screenHeight))
#? Tittle
pygame.display.set_caption('My fisrt Videogame')

#? icon
icon = pygame.image.load('icon-export.png') 
pygame.display.set_icon(icon)


#! Positions
center_x = screenWidth/2
center_y = screenHeight/2
center = (center_x, center_y)


#! Define Rectangles   (x_position, y_position,  width, heigth)
#? Ball Reactangle
ball = pygame.Rect(center_x-15,center_y-15,30,30)

#? Players Rectangles 
player = pygame.Rect(screenWidth-20,center_y-70,  10,140)
opponent = pygame.Rect(10,center_y-70,  10, 140)

#? Colors
opponent_color = pygame.Color('brown')
player_color = pygame.Color('steelblue1')
ball_color = pygame.Color('darkorchid1')
background_color = pygame.Color('grey12')
grey = (200, 200, 200)

#! Define speed
#? Ball_speeds
ball_speed_x = 7
ball_speed_y = 7
general_speed = -2

#? PLayer_speed
player_speed = 0

#? Opponent_speed
opponent_speed = 0


running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            #? Player
            if event.key == pygame.K_DOWN:
                player_speed += 7            
            if event.key == pygame.K_UP:
                player_speed -= 7  
            #? Opponent
            if event.key == pygame.K_s:
                opponent_speed += 7            
            if event.key == pygame.K_w:
                opponent_speed -= 7  
        if event.type == pygame.KEYUP:
             #? Player
            if event.key == pygame.K_DOWN:
                player_speed -= 7            
            if event.key == pygame.K_UP:
                player_speed += 7
            #? Opponent
            if event.key == pygame.K_s:
                opponent_speed -= 7            
            if event.key == pygame.K_w:
                opponent_speed += 7  
        #?
    #! Call the Functions
    ball_animation()
    player_animation()
    opponent_animation()

    #! visuals (from top to bottom)
    #? Backgoud  (color)                     
    screen.fill(background_color)     
    #*                                   top: x,y | bottom: x,     y      
    pygame.draw.aaline(screen, grey,  (center_x,0), (center_x, screenHeight))
    #? Draw Rectangles (screen, color, Rectangle)
    pygame.draw.rect(screen,opponent_color, opponent)
    pygame.draw.ellipse(screen,ball_color, ball)
    pygame.draw.rect(screen,player_color, player)
    

    #update de window (fps)
    pygame.display.flip()
    clock.tick(60)
