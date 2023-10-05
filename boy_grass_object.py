import os
from pico2d import *
os.chdir(os.path.dirname(__file__))
# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

# initialization code

# game main loop code

# finalization code

close_canvas()
