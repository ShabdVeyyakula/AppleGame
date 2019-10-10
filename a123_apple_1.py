#   a123_apple_1.py
import turtle as trtl

apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)

apple = trtl.Turtle()

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

draw_apple(apple)

trtl.mainloop()