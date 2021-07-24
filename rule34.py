import json

import requests
import random

images = []

tag = input("TAG (White to get a random image: ")

# get all the images with the given tag
r = requests.get(
    f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tag}&json=1"
).json()

for elem in r:
    images.append(elem["file_url"])

choice = input("\n[1]   View All the images\n[2]   View a random image\n")

if choice == "1":
    # print only the file url
    for elem in r:
        print(elem["file_url"])
else:
    n = random.randint(1, len(images))
    print(images[n])