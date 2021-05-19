# NASA image downloader through API: https://api.nasa.gov/
# using requests module
# @2021/05/17

import requests
from datetime import date

the_date = input("Enter date(YYYY-MM-DD): ")
api = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
if the_date == "":
  today = date.today()
  the_date = today.strftime("%Y-%m-%d")

# load json data from api
api = f"{api}&date={the_date}"  # f-string is a string literal
print(f">>> requesting: {api}")
r = requests.get(api)
parsed = r.json()
title = parsed['title']
url = parsed['hdurl']
print(f"{title}: {url}")

# download image from url
img = requests.get(url, stream=True)
ext = url.split(".")[-1]
path = f"image/apod_{the_date}.{ext}"
file = open(path, "wb")
file.write(img.content)
file.close()
print(">>>> image downloaded!")