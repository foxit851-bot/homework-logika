from pygame import draw
from settings import *

def draw_key_effect(screen , rect , key_index , is_pressed = False):

    correct_rect = rect.copy()

    if not is_pressed:
        base_color = (220 , 220 , 220)
    else:

        correct_rect.y += 8
        correct_rect.height -= 8

        if key_index == 0:
            base_color = "#A8EAE0"
        if key_index == 1:
            base_color = "#848FD6"
        if key_index == 2:
            base_color = "#A8EAE0"
        if key_index == 3:
            base_color = "#848FD6"
        if key_index == 4:
            base_color = "#A8EAE0"
        if key_index == 5:
            base_color = "#848FD6"
        if key_index == 6:
            base_color = "#A8EAE0"
    
    
    border_color = BLACK
    draw.rect(screen , base_color , correct_rect , border_radius = 12)
    draw.rect(screen , border_color , correct_rect , 2 , border_radius = 12)