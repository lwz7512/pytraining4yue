# !/usr/bin/python

 
# step 1 : file traverse from a Drive or folder
import os


ROOT_DIR = "/Users/wenzhili/python"

# FOLDER_COUNT = 0
FILE_COUNT = 0
SIEZ_AMOUNT = 0

FILE_SIZE_MAX = 0
FILE_NAME_MAX = [(0, '')]*10 # list of file path descending with file size


def addToFileList(size, file):
   global FILE_NAME_MAX
   start_pos = -1
   for index, item in enumerate(FILE_NAME_MAX):
      if size > item[0]:
         start_pos = index
         break
   if start_pos > -1:
      FILE_NAME_MAX[start_pos] = (size, file)


def traverseFolder(folder = ROOT_DIR, callback = None):
   global FILE_COUNT, FILE_SIZE_MAX, SIEZ_AMOUNT

   all_flat_files = []

   for root, _, files in os.walk(folder):
      for name in files:
         # print(os.path.join(root, name))
         file_path = os.path.join(root, name)
         file_size = os.path.getsize(file_path)

         # add each file to list and reorder
         addToFileList(file_size, file_path)
         all_flat_files.append((file_path, file_size))

         if file_size > FILE_SIZE_MAX:
            FILE_SIZE_MAX = file_size
         FILE_COUNT += 1
         SIEZ_AMOUNT += file_size
   # write to a file
   # with open("data/files.txt", "w") as outfile:
   #    for item in all_flat_files:
   #       outfile.write("%s,%d\n" % item)

# step 2 : visualize the process

import urwid


def buildTextBy(str, theme, pile):
   txt = urwid.Text(str, align=urwid.CENTER)
   txt = urwid.AttrMap(txt, theme)
   pile.append(txt)


def exitApp(button, _):
   raise urwid.ExitMainLoop()

def startUpdate(loop, pile):

   traverseFolder() # checking files...

   pile.pop() # clear last title row

   total_size_int = int(SIEZ_AMOUNT/(1024*1024))
   total_size_str = "==== size amount: " + str(total_size_int) + "M"
   buildTextBy(total_size_str, 'blue_theme', pile)
   
   file_count_str = "==== file amount: " + str(FILE_COUNT)
   buildTextBy(file_count_str, 'green_theme', pile)

   max_size_file = "==== max size file is: " + FILE_NAME_MAX[0][1]
   mega_size_int = int(FILE_SIZE_MAX/(1024*1024))
   max_size_file += " : " + str(mega_size_int) + "M"
   buildTextBy(max_size_file, 'red_theme', pile)

   div = urwid.Divider()
   pile.append(div)

   delete_box = urwid.LineBox(urwid.Button(u"DELETE", deleteFile, pile))
   next_box = urwid.LineBox(urwid.Button(u" EXIT ", exitApp, pile))
   
   buttons = [
      urwid.Divider(),
      ('fixed', 12, delete_box), 
      ('fixed', 12, next_box), 
      urwid.Divider(),
   ]
   columns = urwid.Columns(buttons, )
   pile.append(columns)
   pile.focus = len(pile) - 1  # focus on last row


def exit_on_q(key):
    if key in ('esc', 'q', 'Q'):
        raise urwid.ExitMainLoop()

# step 3 : delete the selected large files
def deleteFile(button, pile):
   if len(FILE_NAME_MAX) == 0:
      return
   deleted = FILE_NAME_MAX.pop(0) # remove current one
   # delete file ...
   os.remove(deleted[1])
   # display next file
   if len(FILE_NAME_MAX) > 0:
      mega_size_int = int(FILE_NAME_MAX[0][0]/(1024*1024))
      file_and_size = FILE_NAME_MAX[0][1] + " : " + str(mega_size_int) + "M"
      pile[3].base_widget.set_text(file_and_size)
   else:
      pile[3].base_widget.set_text('')

palette = [
    ('banner_theme', 'light green', 'black'),
    ('red_theme', 'black', 'dark red'),
    ('yellow_theme', 'black', 'yellow'),
    ('blue_theme', 'black', 'dark blue'),
    ('green_theme', 'black', 'dark green'),
    ('bg_theme', '', 'black'),
]

lb = urwid.SimpleListWalker([])
start_txt = "Traversing " + ROOT_DIR + " ..."
txt = urwid.Text(start_txt, align=urwid.CENTER)
txt_row = urwid.AttrMap(txt, 'banner_theme')

lb.extend([
   urwid.Divider(top=4), 
   txt_row
])
fill = urwid.ListBox(lb)
background = urwid.AttrMap(fill, 'bg_theme')
loop = urwid.MainLoop(background, palette, unhandled_input=exit_on_q)
loop.set_alarm_in(1, startUpdate, lb) # start scanning after displaying title
loop.run()

# ...