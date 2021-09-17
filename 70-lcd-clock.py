# ========== digital clock ===============
# using pyglet:
# https://pyglet.readthedocs.io/en/latest/

# install:
# pip install pyglet --user

# more examples:
# https://github.com/pyglet/pyglet/tree/master/examples


import pyglet
from pyglet import clock
from datetime import datetime

window = pyglet.window.Window()

pyglet.font.add_file('library/DS-DIGIT.TTF')
ds_digital = pyglet.font.load('DS-Digital')

label = pyglet.text.Label(
  text='DIGITAL CLOCK',
  font_name = 'DS-Digital',
  font_size = 48,
  color = (0, 255, 0, 255),
  x = window.width // 2,
  y = window.height // 2,
  anchor_x = 'center',
  anchor_y = 'center'
)

def callback(delta):
  now = datetime.now()
  current = now.strftime("%H:%M:%S")
  label.text = current

@window.event
def on_draw():
  window.clear()
  label.draw()

clock.schedule_interval(callback, 1)
pyglet.app.run()
