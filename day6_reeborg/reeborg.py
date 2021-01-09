# You can play/solve this challenge on Reeborg[https://reeborg.ca/]

# Hurdle 1

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
    
# Hurdle 2

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
# Hurdel 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
    
# Hurdel 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
    
# Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
    
# Maze code has some issues, in some case the bot get stuck in infinte loop, i am still trying to fix it, any help is welcome.

    
    
