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
    pygame.draw.ellipse(screen,color,[x,y,30,30])


# This class represents the bar at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,x,y,width,height, color):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
  
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

# This creates all the walls in room 1
def setupRoomOne():
    # Make the walls. (x_pos, y_pos, width, height)
    wall_list=pygame.sprite.RenderPlain()
     
    # This is a list of walls. Each is in the form [x, y, width, height]
    walls = [ [0,0,6,600],
              [0,0,600,6],
              [0,600,606,6],
              [600,0,6,606],
              [300,0,6,66],
              [60,60,186,6],
              [360,60,186,6],
              [60,120,66,6],
              [60,120,6,126],
              [180,120,246,6],
              [300,120,6,66],
              [480,120,66,6],
              [540,120,6,126],
              [120,180,126,6],
              [120,180,6,126],
              [360,180,126,6],
              [480,180,6,126],
              [180,240,6,126],
              [180,360,246,6],
              [420,240,6,126],
              [240,240,6,66],
              [240,300,126,6],
              [360,240,6,66],
              [0,300,66,6],
              [540,300,66,6],
              [60,360,66,6],
              [60,360,6,186],
              [480,360,66,6],
              [540,360,6,186],
              [120,420,366,6],
              [120,420,6,66],
              [480,420,6,66],
              [186,480,246,6],
              [300,480,6,66],
              [120,540,6,66],
              [120,540,126,6],
              [360,540,126,6],
              [480,540,6,66],
            ]
     
    # Loop through the list. Create the wall, add it to the list
    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],blue)
        wall_list.add(wall)
     
    # return our new list
    return wall_list

current_room = 1
wall_list = setupRoomOne()

# This sets the width and height of each grid location
width=54
height=54
 
# This sets the margin between each cell
margin=6
 
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
size=[606,606]
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
x_coord=18
y_coord=18


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
                x_speed=-60
            if event.key == pygame.K_RIGHT:
                x_speed=60
            if event.key == pygame.K_UP:
                y_speed=-60
            if event.key == pygame.K_DOWN:
                y_speed=60
                  
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
    wall_list = setupRoomOne()
    current_room = 1
            
    # Move the object according to the speed vector.
    x_coord=x_coord+x_speed
    y_coord=y_coord+y_speed
 
    # Set the screen background
    screen.fill(black)

    pacman(screen,x_coord,y_coord)

    wall_list.draw(screen)
    
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = yellow
            pygame.draw.ellipse(screen,color,[((margin+width)*column+margin)+24,((margin+height)*row+margin)+24,6,6])
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # Limit to 20 frames per second
    clock.tick(10)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
