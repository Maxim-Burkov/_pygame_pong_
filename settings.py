import ctypes
import pygame

# some window settings
user32 = ctypes.windll.user32

WIDTH = user32.GetSystemMetrics(78)
HEIGHT = user32.GetSystemMetrics(79)

FPS = 60

# colors
BLACK = (0 , 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BALL_COLOR = (120, 36, 26)
MAP_COLOR = (123, 128, 199)
LIGHT_COLOR = (186, 114, 114)

# some vars
MOVING = 0


ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 7


BALL_SPEED = 2.5


# defolt users buttons

button_new_left_top = ' '
button_new_left_bottom = ' '
button_new_right_top = ' '
button_new_right_bottom = ' '


with open('buttons.txt', 'r') as f:
    button_left_top = f.readline(3)
    button_left_bottom = f.readline(4)

    button_right_top = f.readline(6)
    button_right_bottom = f.readline(7)



with open ('buttons.txt', 'r') as f:
  old_data = f.read()

new_data1 = old_data.replace(button_left_top, button_new_left_top)
new_data2 = new_data1.replace(button_left_bottom, button_new_left_bottom)
new_data3 = new_data2.replace(button_right_top, button_new_right_top)
new_data4 = new_data3.replace(button_right_bottom, button_new_right_bottom)

with open ('buttons.txt', 'w') as f:
    f.write(new_data4)

f.close()