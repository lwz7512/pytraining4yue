# pick one of free Cloud Storage services to upload your files:
# https://www.guru99.com/free-cloud-storage.html
# 
# Microsoft OneDrive:
# https://www.microsoft.com/en-ca/microsoft-365/onedrive/online-cloud-storage
# https://developer.microsoft.com/en-us/onedrive
# https://docs.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/app-registration?view=odsp-graph-online
# https://github.com/OneDrive/onedrive-sdk-python
# 
# Google Drive:
# https://www.google.com/intl/en_ca/drive/
# https://developers.google.com/drive
# https://github.com/googleworkspace/python-samples
# https://github.com/googleworkspace/python-samples/tree/master/drive/driveapp
# https://developers.google.com/drive/api/v3/quickstart/python
# 
# Dropbox:
# https://www.dropbox.com/?_hp=c
# https://www.dropbox.com/developers
# https://www.dropbox.com/developers/documentation/python
# https://dropbox-sdk-python.readthedocs.io/en/latest/
# https://github.com/dropbox/dropbox-sdk-python/tree/master/example
# 
# iCloud:
# https://www.icloud.com/

# =============================================================
# to use dropbox:
# 1. create an account
# 2. create a dropbox app
# 3. generate an access token in this app
# 4. install python module dropbox
#  
# install dropbox
# pip install dropbox


import contextlib
import datetime
import os
# import six
# import sys
import time
import unicodedata

import dropbox

token = 'sl.xxxxxxx...'
dbx = dropbox.Dropbox(token)
# account = dbx.users_get_current_account()
# print(account)

# List all of the contents in the user's root directory:
# for entry in dbx.files_list_folder('').entries:
#   print(entry.name)

# Upload a file (and take a wild guess at tomorrow's headline):
# https://dropbox-sdk-python.readthedocs.io/en/latest/api/dropbox.html#dropbox.dropbox_client.Dropbox.files_upload
# story_str = 'Potential headline: Game 5 a nail-biter as Warriors inch out Cavs'
# story_bytes = bytes(story_str, 'utf-8')
# dbx.files_upload(story_bytes, '/story.txt')
# print('>>> story.txt uploaded!')
# Get the metadata for a file (and prove that you called it before the game was over!):
# print(dbx.files_get_metadata('/Cavs vs Warriors/Game 5/story.txt').server_modified)



def upload(dbx, fullname, folder, subfolder, name, overwrite=False):
    """Upload a file.
    Return the request response, or None in case of error.

    :param Dropbox dbx: Dropbox instance.
    :param str fullname: local absolute file path to be uploaded.
    :param str folder: Dropbox root folder, like /
    :param str subfolder: Dropbox sub folder, like Photos
    :param str name: Dropbox file name
    """
    path = '/%s/%s/%s' % (folder, subfolder.replace(os.path.sep, '/'), name)
    while '//' in path:
        path = path.replace('//', '/')
    mode = (dropbox.files.WriteMode.overwrite
            if overwrite
            else dropbox.files.WriteMode.add)
    mtime = os.path.getmtime(fullname)
    with open(fullname, 'rb') as f:
        data = f.read()
    with stopwatch('upload %d bytes' % len(data)):
        try:
            res = dbx.files_upload(
                data, path, mode,
                client_modified=datetime.datetime(*time.gmtime(mtime)[:6]),
                mute=True)
        except dropbox.exceptions.ApiError as err:
            print('*** API error', err)
            return None
    print('uploaded as', res.name.encode('utf8'))
    return res

@contextlib.contextmanager
def stopwatch(message):
    """Context manager to print how long a block of code took."""
    t0 = time.time()
    try:
        yield
    finally:
        t1 = time.time()
        print('Total elapsed time for %s: %.3f' % (message, t1 - t0))

# ======================================================
print('>>> uploading image...')
upload(dbx, '/Users/wenzhili/Pictures/johannes-plenio-2TQwrtZnl08-unsplash.jpg', '/', 'Photos', 'road.jpg')
print('<<< image uploaded!')