# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:52:42 2021

@author: mblue
"""

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.visible = False

Entity(
    parent=scene,
    model='sphere',
    texture = load_texture('C:Users/mblue/hamo/horizon.jpg'),
    scale =500,
    double_sided=True    
)

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='brick'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1.0)),
            scale=1.0
            )

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))
        
player = FirstPersonController()

app.run()