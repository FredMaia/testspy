from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,45,45)
        )

class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red, #Change the color when the mouse is over
            pressed_color = color.lime #Change the color when it's clicked
        )
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print('button pressed')

def update(): #It will execute periodically
    if held_keys['a']: #If a is pressed, the square will move
        test_square.x -= 4 * time.dt #Multiply per time between different frames and make the game smooth
    if held_keys['d']:
        test_square.x += 4 * time.dt

app = Ursina()

#Entity: base object for anything in ursina - it can be a shape, a button, a sound
test_square = Entity(model = 'quad', color = color.red, scale = (1,4), position = (5,-1)) #Instead of circle, could be "quad", "cube"

#Two ways to create a texture
# sans_texture = load_texture('assets/Sans.png')
# sans = Entity(model = 'quad', texture = sans_texture)

test_cube = Test_button()

app.run()   