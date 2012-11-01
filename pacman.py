# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu
 
import pygame
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
yellow   = ( 255, 255,   0)

def pacman(screen, x, y):
    color = yellow
    pygame.draw.rect(screen,color,[x,y,20,20])

# This sets the width and height of each grid location
width=20
height=20
 
# This sets the margin between each cell
margin=5
 
# Create a 2 dimensional array. A two dimesional
# array is simply a list of lists.
grid=[]
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0) # Append a cell

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[255,255]
screen=pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Pacman")
 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
    
# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed=0
y_speed=0
  
# Current position
x_coord=5
y_coord=5


# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
            # User pressed down on a key
         
        if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed=-25
            if event.key == pygame.K_RIGHT:
                x_speed=25
            if event.key == pygame.K_UP:
                y_speed=-25
            if event.key == pygame.K_DOWN:
                y_speed=25
                  
        # User let up on a key
        if event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                x_speed=0
            if event.key == pygame.K_RIGHT:
                x_speed=0
            if event.key == pygame.K_UP:
                y_speed=0
            if event.key == pygame.K_DOWN:
                y_speed=0
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # Move the object according to the speed vector.
    x_coord=x_coord+x_speed
    y_coord=y_coord+y_speed
 
    # Set the screen background
    screen.fill(white)

    pacman(screen,x_coord,y_coord)
 
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = white
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # Limit to 20 frames per second
    clock.tick(10)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
