# install urwid:
# % pip install urwid


## Step 2 : draw some chart in console

import urwid
from datetime import datetime as dt

class SwitchingPadding(urwid.Padding):
    def padding_values(self, size, focus):
        maxcol = size[0]
        width, ignore = self.original_widget.pack(size, focus=focus)
        if maxcol > width:
            self.align = "left"
        else:
            self.align = "right"
        return urwid.Padding.padding_values(self, size, focus)


palette = [
    ('banner', 'black', 'light gray'),
    ('bigtext', 'light green', 'black'),
]

# font = urwid.HalfBlock5x4Font()
font = urwid.Thin6x6Font()
btxt = urwid.BigText("DIGITAL CLOCK", font)
btxt_pd = SwitchingPadding(btxt, 'left', None)
btxt_style = urwid.AttrWrap(btxt_pd, 'bigtext')
btxt_fill = urwid.Filler(btxt_style, 'bottom', None, 7)

exit_txt = urwid.Text('press q to exit...')
exit_fill = urwid.Filler(exit_txt)

pile = urwid.Pile([
      ('fixed', font.height, btxt_fill),
      ('fixed', 1, exit_fill),
    ])

def quit(*args, **kwargs):
        raise urwid.ExitMainLoop()

def handle_key(key):
    if key in ('q', 'Q', 'enter'):
        quit()

def onEachSecond(loop, data):
    now = dt.now()
    current = now.strftime("%H:%M:%S")
    btxt.set_text(current)
    loop.screen.clear()
    loop.set_alarm_in(1, onEachSecond)

loop = urwid.MainLoop(
    pile,
    palette=palette,
    handle_mouse = False,
    unhandled_input = handle_key
)
loop.set_alarm_in(3, onEachSecond)
loop.run()
