import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Balle:
   def __init__(self, x, y):
       self.x = x
       self.y = y
       self.change_x = 3
       self.change_y = 3
       self.rayon = 20
       self.color = arcade.color.BLUE

   def update(self):
       self.x += self.change_x
       self.y += self.change_y
       if self.x < self.rayon:
           self.change_x *= -1
       elif self.x > SCREEN_WIDTH - self.rayon:
           self.change_x *=-1
       if self.y < self.rayon:
           self.change_y *= -1
       elif self.y > SCREEN_HEIGHT - self.rayon:
           self.change_y *= -1

   def draw(self):
       arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Rectangle:
   def __init__(self, x, y):
       self.x = x
       self.y = y
       self.change_x = 3
       self.change_y = 3
       self.width = 40
       self.height = 60
       self.color = arcade.color.RED
       self.angle = 0.0

   def update(self):
       self.x += self.change_x
       self.y += self.change_y
       if self.x < 0:
           self.change_x *= -1
       elif self.x > SCREEN_WIDTH - self.width:
           self.change_x *= -1
       if self.y < 0:
           self.change_y *= -1
       elif self.y > SCREEN_HEIGHT - self.height:
           self.change_y *= -1

   def draw(self):
       arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

class MyGame(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #4")
       self.balles = []
       self.rectangles = []

   def on_mouse_press(self, x, y, button, modifiers):
       if button == arcade.MOUSE_BUTTON_LEFT:
           self.balles.append(Balle(x, y))
       elif button == arcade.MOUSE_BUTTON_RIGHT:
           self.rectangles.append(Rectangle(x, y))

   def on_draw(self):
       arcade.start_render()
       for balle in self.balles:
           balle.draw()
       for rectangle in self.rectangles:
           rectangle.draw()

   def update(self, delta_time):
       for balle in self.balles:
           balle.update()
       for rectangle in self.rectangles:
           rectangle.update()

my_game = MyGame()
arcade.run()

