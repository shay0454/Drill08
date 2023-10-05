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


class Ball:
    def __init__(self):
        self.x,self.y=random.randint(100,700),599
        self.v=random.randint(10,70)
        if(random.randint(0,1)):
            self.image=load_image('ball41x41.png')
            self.radius=20
        else:
            self.image=load_image('ball21x21.png')
            self.radius=10

    def update(self):
        if(self.y-self.v>50+self.radius):
            self.y-=self.v
        else:
            self.y=50+self.radius

    def draw(self):
        self.image.draw(self.x,self.y)
        
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
    global balls
    global world

    running =True
    world=[]

    grass=Grass()
    world.append(grass)

    team=[Boy()for i in range(10)] 
    world+=team

    balls=[Ball()for i in range(20)]
    world+=balls
    

def update_world():
    for obj in world:
        obj.update()


def render_world():
    clear_canvas()
    for obj in world:
        obj.draw()
    update_canvas()

# game main loop code
reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.03)
# finalization code

close_canvas()
