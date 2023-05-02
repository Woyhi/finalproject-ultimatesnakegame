import pygame
import time
import random 

# init pygame
pygame.init()

# defining colors
purple = (138, 43, 226) # color of snake
black = (0, 0, 0) # color of background
red = (255, 0, 0) # game over color
green = (69, 139, 116) # food color
white = (255, 255, 255) # super food color 

width, height = 700, 600

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ultimate Snake Game by Woyhi Tahsin and Mahbubul Khan")

clock = pygame.time.Clock()

snake_size = 10

# game over font
message_font = pygame.font.SysFont('impact', 30)
# scores font
score_font = pygame.font.SysFont('impact', 25)

# functions for updating score and updating snake size and position
def print_score(score):
    text = score_font.render("Score: " + str(score), True, green)
    game_display.blit(text, [0,0])
    
def draw_snake(snake_size, snake_pixel):
    for pixel in snake_pixel:
        pygame.draw.rect(game_display, purple, [pixel[0], pixel[1], snake_size, snake_size])  

# initializing snake speed
snake_speed = 15

# start game function
def run_game():
    game_over = False   # you lost/start over, doesn't close game
    game_close = False  # actually closing off the game

    #starting position
    x = width / 2
    y = height / 2
    
    # starting speed
    x_speed = 0
    y_speed = 0

    # starting length
    snake_pixel =[]
    snake_length = 1
    
    # food size
    food_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0

    # super food size
    super_food_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
    super_food_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0
    super_food_speed = 7
    super_food_timer = 0 


    # super food timer
    super_food_timer = 0
    
    # Ingame movement
    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over! You suck!", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            # restart and quit game 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # shows game over screen
                    if event.key == pygame.K_1:                    
                        game_over = True
                        game_close = False
                    # restarts the game
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # negative snake value bc it travels a negative distance (like on the x-axis)
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                # positive snake value bc it travels a positive distance (on the x-axis)
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
                    
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # updates the position of the snake's head along with the speed as it moves on the x and y axis
        x += x_speed 
        y += y_speed

        # setting the background
        game_display.fill(black)
        pygame.draw.rect(game_display, green, [food_x, food_y, snake_size, snake_size])
        pygame.draw.rect(game_display, white, [super_food_x, super_food_y, snake_size, snake_size])


        # checking current position to add length 
        snake_pixel.append([x,y])

        # increasing snake length once food is consumed
        if len(snake_pixel) > snake_length:
            del snake_pixel[0]
        
        # if the snake runs into itself, game over
        for pixel in snake_pixel[:-1]:
            if pixel == [x, y]:
                game_close = True
        
        draw_snake(snake_size, snake_pixel)
        print_score(snake_length - 1)
        
        pygame.display.update()

        # increases length by 1 once the food is eaten
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0
            snake_length += 1

        global snake_speed
        if x == super_food_x and y == super_food_y:
            super_food_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
            super_food_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0
            snake_speed /= 2 
            snake_speed = super_food_speed
            super_food_timer = 0

        # increase the super food timer if the snake has eaten the super food
        if super_food_timer > 0:
            super_food_timer += 1 

        # restore the original speed if the super food effect has ended
        if super_food_timer > 30 * snake_speed:
            snake_speed = 15 # the original speed
            super_food_timer = 0
            
        clock.tick(snake_speed)
    pygame.quit()
    quit()
    
if __name__ == '__main__':
    run_game()



