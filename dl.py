import requests
import pickle
import os

if not os.path.exists('pics'):
    os.makedirs('pics')

with open('links', 'rb') as f:
    links = pickle.load(f)

links = filter(None, links)

for i, link in enumerate(links):
    print(link)
    img_data = requests.get(link).content
    if i <= 9:
        with open(f"pics/00{i}-image.jpg", 'wb') as handler:
            handler.write(img_data)
    elif i <= 99:
        with open(f"pics/0{i}-image.jpg", 'wb') as handler:
            handler.write(img_data)
    else:
        with open(f"pics/{i}-image.jpg", 'wb') as handler:
            handler.write(img_data)

    print(f"saved image {i}")
