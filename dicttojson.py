from os import listdir
from os.path import isfile, join
import os
import json
import itertools
root = "https://swipeart.s3.eu-west-2.amazonaws.com/pics/"

onlyfiles = [f for f in listdir("D:/gan/pics")
             if isfile(join("D:/gan/pics", f))]
print(len(onlyfiles))


d = {"categories":
     {"all": []}
     }
for i in range(0, len(onlyfiles)):
    dd = {}
    user = {}
    dd["id"] = i
    dd["src"] = f"{root}{onlyfiles[i]}"
    dd["liked"] = False
    user["src"] = f"{root}pfp.jpg"
    user["name"] = "Keito"
    user["job"] = "Graphic Designer"
    dd["user"] = user

    d["categories"]["all"].append(dd)

with open("Test.json", "w") as outfile:
    json.dump(d, outfile, indent=4, sort_keys=True)
