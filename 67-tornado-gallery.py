# Render a local gallery using tornado template:

# https://www.tornadoweb.org/en/stable/
# https://www.tornadoweb.org/en/stable/guide/templates.html
# 
# modules installation:
# pip3 install tornado Pillow
# 
import tornado.ioloop
import tornado.web

import signal
import sys
import os
from os import listdir
from os.path import isfile, join, exists
from PIL import Image

pictures_dir = '/Users/wenzhili/Pictures'  # change to your local Pictures directory before run !!
valid_image_suffix = ('jpg', 'jpeg', 'png')
image_list = None
temp_dir = '.thumbnails'

def prepareImageListAndFolder():
    temp_dir_exists = exists(temp_dir)
    read_write_mode = 0o755  #  the same permission as current user

    if not temp_dir_exists:
        os.mkdir(temp_dir, read_write_mode)
        os.chmod(temp_dir, read_write_mode)
        print('>>> thumbnails directory created!')

    print('>>> read images from picture directory: {0}'.format(pictures_dir))
    onlyfiles = [f for f in listdir(pictures_dir) if isfile(join(pictures_dir, f))]
    images = [f for f in onlyfiles if f.endswith(valid_image_suffix)]
    return images

def tnails(imageSourceFile, thumbnailFile, size):
   try:
      image = Image.open(imageSourceFile)
      image.thumbnail(size)
      image.save(thumbnailFile)
   except IOError as error:
       print('<<<<<<<<< generate thumbnail error!')
       print(error)

def generateThumbnails(images):
    if any(os.scandir(temp_dir)):
        return print('<<< .thumbnails not empty!')
    for img in images:
        print('>>> generate: {0}'.format(img))
        sourceImgPath = join(pictures_dir, img)
        print('>>> full image path: {0}'.format(sourceImgPath))
        thumbnailPath = join(temp_dir, img)
        tnails(sourceImgPath, thumbnailPath, (120,90))
    print('>>>> thumbnails generation done!')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<a href='/gallery'>Enter My Gallery</a>")

class GalleryHandler(tornado.web.RequestHandler):
    def get(self):
        global image_list
        items = image_list
        self.render("library/tornado_template.html", title="My Gallery", items=items)


async def shutdown():
    print('<<< server stopped!')
    tornado.ioloop.IOLoop.current().stop()
    print('<<< process exited!')
    sys.exit(0) # means a clean exit without any errors / problems

def exit_handler(sig, frame):
    print('>>> to stop tornado server...')
    tornado.ioloop.IOLoop.instance().add_callback_from_signal(shutdown)

if __name__ == "__main__":

    # get all the image name list
    image_list = prepareImageListAndFolder()
    generateThumbnails(image_list)

    # start tornado server
    server_settings = {
        "debug": True,
        "autoreload": True
    }
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/gallery", GalleryHandler),
        (r"/thumbnails/(.*)", tornado.web.StaticFileHandler, {"path": "./.thumbnails"}),
        (r"/image_raw/(.*)", tornado.web.StaticFileHandler, {"path": pictures_dir}),
    ], **server_settings)
    
    application.listen(8888)

    signal.signal(signal.SIGTERM, exit_handler)
    signal.signal(signal.SIGINT,  exit_handler)
    print('>>> tornado server started!')
    tornado.ioloop.IOLoop.current().start()