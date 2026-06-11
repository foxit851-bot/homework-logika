from pygame import mixer
from effects import draw_key_effect

def load_sounds(keys):
    sounds = {}
    for key , filename in keys.items():
        sounds[key] = mixer.Sound(filename)
    return sounds