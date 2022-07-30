from PIL import Image
from os import listdir
from os.path import isfile, join
import os

if not os.path.exists('train'):
    os.makedirs('train')

onlyfiles = [f for f in listdir("pics") if isfile(join("pics", f))]

for file in onlyfiles:
    img_name = file[:-4]
    print(img_name)

    img = Image.open(f"pics/{img_name}.jpg")
    img = img.resize((img.size[0]//2, img.size[1]//2), Image.ANTIALIAS)
    img.save(f"train/r_{img_name}.jpg")
