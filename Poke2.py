#Poke the Dots Version 2

# This is  a grphicall game where two dots move around 
#the screen ,bouncing off the edges

from uagame import Window
from pygame import QUIT,Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

# User-defined functions

def main():
  window = create_window()
  game = create_game(window)
  play_game(game)
  window.close()
  
  #close window()
  
def create_window():
  # Create a window for the game, open it, and return it.
  
    window  = Window('Poke the Dots',500,400)
    window.set_bg_color('black')
    return window

def create_dot(color,radius,center,velocity):
  dot = Dot()
  dot.color= color
  dot.radius= radius
  dot.center= center
  dot.velocity= velocity
  
  return dot
  
  
def create_game(window):
  # Create a Game object for Poke the Dots
  game = Game()
  game.window = window
  game.clock = Clock()
  game.close_selected = False
  game.small_dot = create_dot('red',30,[50,75],[1,2])
  game.big_dot = create_dot('blue',40,[200,100],[2,1])
  
  return game
  
  
def play_game(game):
  
  
  while not game.close_selected:
    handle_events(game)
    draw_game(game)
    update_game(game)
    
def handle_events(game):
  # Handle the current game events. Return True if the player
  # clicked the close icon and False otherwise.  
  event_list =  get_events()
  for event in event_list:
    if event.type == QUIT:
      game.close_selected = True
  

def draw_game(game): 
  window =game.window
  window.clear()
  big_dot=game.big_dot
  small_dot =game.small_dot

  draw_dot(window,big_dot.color,big_dot.center,big_dot.radius)
  # draw small =dot
  draw_dot(window,small_dot.color,small_dot.center,small_dot.radius)
  
  window.update()

def update_game(game):

  frame_rate = 90
  window = game.window
  big_dot=game.big_dot
  small_dot =game.small_dot  
  clock = game.clock
  #move big dot
  move_dot(window,big_dot.center,big_dot.radius,big_dot.velocity)
  #move small dot
  move_dot(window,small_dot.center,small_dot.radius,small_dot.velocity)  
  # control frame rate
  
  clock.tick(frame_rate)

def draw_dot (window,color_string,center,radius):
  # Draw the dot on the window.
     # - window is the Window to draw in
     # - color_string is the str color of the dot
     # - center is the list of x int and y int coordinates of the
     # center of the dot    
     # - radius is the int radius of the dot
  surface =  window.get_surface()
  color =  Color(color_string)
  draw_circle(surface,color,center,radius)

def move_dot(window,center,radius,velocity):
      # Change the location and the velocity of the dot so it
      # remains on the surface by bouncing from its edges.
      # - window is the Window to move in
      # - center is the list of x int and y int coordinates
      # of the center of the dot    
      # - radius is the int radius of the dot
      # - velocity is the list of horizontal int and vertical
      # int speeds of the dot
  
  size =(window.get_width(),window.get_height())
  for index in range(0,2):
    # update center at index
    center[index] = center[index] + velocity[index]
    if (center[index] + radius >= size[index]) or (center[index] <= (radius)) :
      velocity[index] = -velocity[index]


class Game:
  # an object in this class represents a complete game
  # - window
  
  # - frame_rate
  # - close_selected
  # - clock
  # - smaill_dot
  # - big_dot
  pass
class Dot :
  # an object in this class represent a complete dot with
  # color
  # radius
  # center 
  # velocity
  
  pass


main()
