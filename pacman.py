# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu
  
import pygame
  
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
purple = (255,0,255)
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
          
# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
  
    # Set speed vector
    change_x=0
    change_y=0
  
    # Constructor function
    def __init__(self,x,y, filename):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
   
        # Set height, width
        self.image = pygame.image.load(filename).convert()
  
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
      
    # Change the speed of the player
    def changespeed(self,x,y):
        self.change_x+=x
        self.change_y+=y
          
    # Find a new position for the player
    def update(self,walls):
        # Get the old position, in case we need to go back to it
        old_x=self.rect.left
        new_x=old_x+self.change_x
        self.rect.left = new_x
          
        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.left=old_x
  
        old_y=self.rect.top
        new_y=old_y+self.change_y
        self.rect.top = new_y
          
        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.top=old_y
  
 
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
  
score = 0
# Call this function so the Pygame library can initialize itself
pygame.init()
  
# Create an 600x600 sized screen
screen = pygame.display.set_mode([606, 606])
  
# Set the title of the window
pygame.display.set_caption('Pac-man')
  
# Create a surface we can draw on
background = pygame.Surface(screen.get_size())
  
# Used for converting color maps and such
background = background.convert()
  
# Fill the screen with a black background
background.fill(black)
  
# Create the player paddle object
player = Player( 378, 138, "pacman.png" )
movingsprites = pygame.sprite.RenderPlain()
movingsprites.add(player)
  
current_room = 1
wall_list = setupRoomOne()
 
clock = pygame.time.Clock()
  
done = False
  
while done == False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-30,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(30,0)
            if event.key == pygame.K_UP:
                player.changespeed(0,-30)
            if event.key == pygame.K_DOWN:
                player.changespeed(0,30)
                  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(30,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-30,0)
            if event.key == pygame.K_UP:
                player.changespeed(0,30)
            if event.key == pygame.K_DOWN:
                player.changespeed(0,-30)
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
    player.update(wall_list)

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
                  
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(black)
      
    movingsprites.draw(screen)
    wall_list.draw(screen)
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = yellow
            if row == 4 and (column == 4 or column == 5):
                continue
            else:
                pygame.draw.ellipse(screen,color,[(60*column+6)+24,(60*row+6)+24,6,6])
 

    pygame.display.flip()
  
    clock.tick(10)
              
pygame.quit()
