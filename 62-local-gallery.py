# TODO: Sharing local pictures through browser
# 
# using library: Pillow, Flask
# 
# https://gist.github.com/phrawzty/62540f146ee5e74ea1ab
# https://github.com/python/cpython/blob/3.9/Lib/http/server.py
# https://www.tutorialspoint.com/python_pillow/python_pillow_creating_thumbnails.htm
# https://pillow.readthedocs.io/en/stable/

# installation:
# pip3 install Pillow Flask

# 0 = No Permission
# 1 = Execute, x
# 2 = Write, w
# 4 = Read, r

# start server:
# 
# export FLASK_APP=62-local-gallery
# export FLASK_ENV=development
# python3 -m flask run

# visit gallery:
# http://localhost:5000/gallery


import os
from os import listdir
from os.path import isfile, join, exists
from PIL import Image
from flask import Flask, send_from_directory


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
        thumbnailPath = join(temp_dir, img)
        tnails(sourceImgPath, thumbnailPath, (120,90))
    print('>>>> thumbnails generation done!')


# prepare Flask server
app = Flask(
    __name__, 
    static_folder=temp_dir, 
    static_url_path='/thumbnails'
)

@app.route("/")
def hello_world():
    return "<p>Welcome to Flask World!</p>"

@app.route("/image/<path:image_name>")
def send_image(image_name):
    return send_from_directory(pictures_dir, image_name)

@app.route("/gallery")
def show_gallery():
    global image_list
    gallery_container = "<div>"
    for image in image_list:
        gallery_container += "<a href='/image/" + image + "' style='padding:10px;' >"
        gallery_container += "  <img src='/thumbnails/" + image + "'/>"
        gallery_container += "</a>"
    gallery_container += "</div>"
    return gallery_container


# get all the image name list
image_list = prepareImageListAndFolder()
generateThumbnails(image_list)