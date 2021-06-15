import json

import requests

tag = input("TAG: ")

# get all the images with the given tag
r = requests.get(
    f"https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tag}&json=1"
).json()

# print only the file url
for elem in r:
    print(elem["file_url"])
