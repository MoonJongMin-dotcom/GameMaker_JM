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

blocks = [
    load_texture('assets/grass.png'), # 0
    load_texture('assets/grass.png'), # 1
    load_texture('assets/stone.png'), # 2
    load_texture('assets/gold.png'),  # 3
    load_texture('assets/lava.png'),  # 4   
]

block_id = 1

def input(key):
    global block_id, hand
    if key.isdigit():
        block_id = int(key)
        if block_id >= len(blocks):
            block_id = len(blocks) - 1
        hand.texture = blocks[block_id]

    if key == 'k':
        def add_item():
            inventory.append(random.choice(('bag', 'bow_arrow', 'gem', 'orb', 'sword')))
        
        for i in range(7):
            add_item()
       
    if key == 'j':
        weapon
         
         
       
#       add_item_button = Button(
#            scale = (.1,.1),
#            x = -.5,
#            color = color.lime.tint(-.25),
#            text = '+',
#            tooltip = Tooltip('Add random item'),
#           on_click = add_item
#           )
  


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = 'assets/sky.jpg',
            scale = 500,
            double_sided=True)

class Hand(Entity):
     def __init__(self):
        super().__init__(
    parent=camera.ui,
    model='assets/block',
    texture=blocks[block_id],
    scale=0.2,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)
        
class Weapon(Entity):
     def __init__(self): 
        super().__init__(
    parent=camera.ui,
    model='sword',
    texture = 'sword',
    scale=0.2,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)
        #블락을 없애고 실행해야한다, 인벤토리 기능하게 만들
        
class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = (.3, .5),
            origin = (-.5, .5), 
            position = ( .4, .4),
            texture='white_cube',
            texture_scale = (5,8),
            color = color.dark_gray
            )
        self.item_parent = Entity(parent=self, scale=(1/5,1/8))    
    
    
    def find_free_spot(self):
        taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]
        for y in range(8):
            for x in range(5):
                if not (x,-y) in taken_spots:
                    return(x,-y)
    
    
    def append(self, item):
        icon = Draggable(
            parent = inventory.item_parent,
            model = 'quad',
            texture = item,
#            color = color.White,
            origin = (-.5,.5),
            color = color.random_color(),
            position = self.find_free_spot(),
            z = -.1
            )
        name = item.replace('_', ' ').title()
        icon.tooltip = Tooltip(name)
        icon.tooltip.background.color = color.color(0,0,0,.8)
       
        
        def drag():
            icon.org_pos = (icon.x, ixon.y)
            icon.z -= .01
                
        def drop():
            icon.x = int(icon.x)
            icon.y = int(icon.y)
            icon.z += .01
            
            '''if outsid, returen to original position'''
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = (icon.org_pos)
                returen
            
            
            '''if the spot is taken, swap positions'''
            for c in self.children:
                if c == icon:
                    continue
                
                if c.x == icon.x and x.y == icon.y:
                    print('swap positions')
                    c.position = icon.org_pos
            
        icon.drop = drop
        icon.drag = drag

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
    ##    punch.play()
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)



class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='brick'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1.0)),
            scale=0.5
            )
        
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'right mouse down':
                destroy(self)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))
        

sky = Sky()
hand = Hand()
player = FirstPersonController()
inventory = Inventory()
weapon = Weapon()


#item = Button(parent=inventory.item_parent, origin=(-.5,.5), color=color.red, position=(0,0))
#item = Button(parent=inventory.item_parent, origin=(-.5,.5), color=color.green, position=(2.0))

app.run()