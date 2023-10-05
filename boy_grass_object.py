import os
import random
from pico2d import *
os.chdir(os.path.dirname(__file__))
# Game object class here
class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x,self.y=random.randint(100,700),90
        self.frame=random.randint(0,8)
        self.image=load_image('run_animation.png')

    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5
    
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

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
def reset_world():
    global running
    global grass
    global team

    running =True
    grass=Grass()
    team=[Boy()for i in range(10)] 
    

def update_world():
    grass.update()
    for boy in team:
        boy.update()


def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

# game main loop code
reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
