from pygame import *
from settings import *
import sys
from keys import *
from sounds import load_sounds

init()
mixer.init()

SCREEN = display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT))
display.set_caption('piano')

pressed = set()
key_rects = create_key_rects(7)
sounds = load_sounds(KEYS)

bg_image = image.load('assets/images/bg.png')
bg_image = transform.scale(bg_image , (WINDOW_WIDTH , WINDOW_HEIGHT))

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
            sys.exit()

        if e.type == KEYDOWN:
            k = key.name(e.key)
            if k in sounds:
                pressed.add(k)
                sounds[k].play()

        if e.type == KEYUP:
            k = key.name(e.key)
            if k in pressed:
                pressed.remove(k)
    SCREEN.blit(bg_image , (0 , 0))
    pressed_numbers = []
    if 'a' in pressed: pressed_numbers.append(0)
    if 's' in pressed: pressed_numbers.append(1)
    if 'd' in pressed: pressed_numbers.append(2)
    if 'f' in pressed: pressed_numbers.append(3)
    if 'g' in pressed: pressed_numbers.append(4)
    if 'h' in pressed: pressed_numbers.append(5)
    if 'j' in pressed: pressed_numbers.append(6)

    draw_keys(SCREEN, key_rects, pressed_numbers)
    display.update()