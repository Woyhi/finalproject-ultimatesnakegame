ULTIMATE SNAKE GAME by Woyhi Tahsin and Mahbubul Khan

The purpose of this project is to create a fun new twist to a classic game and explore python pygame capabilities 

Key functions in this project include: 
    'print_score' = which updates the score by changing the text of the score at the corner
    'draw_snake' = updates teh snake size and its position as it consumes food
    'def run_game' = this is the lengthiest function and the most important for in game movement and game display 
        more in detail: 
        gives initial position 
        gives initial speed
        gives intil length
        food size 
        super food size
        initializes super food timer 
        enables in game movement using keys (up, down, left, right)
        also enables quit and restart (key 1, key 2)
        closes game if the snake goes out the boundary 
        updates movement
        setting the background to display the snake, food, and super food
        game over screen if the snake eats itself
        global function includes snake speed throughout the function
        adding length
        adding super food effect which should change the snake speed for a certain time

We were able to get a working, functioning snake game going, but we were unable to fix the issue regarding our super food. The effect works by slowing the snake down, which it does, but it stays on that speed throughout the game. We wanted it to revert back to the original speed after 30 seconds. We were also having issues with the spawning, we wanted the super food to spawn every minute but it spawns right after it is eaten. 

