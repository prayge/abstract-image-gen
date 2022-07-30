from os import listdir
from os.path import isfile, join
import os
import json

onlyfiles = [f for f in listdir("D://gan//ABS")
             if isfile(join("D://gan//ABS", f))]
print(len(onlyfiles))


d = {}
for i in range(0, len(onlyfiles)):
    dd = {}
    dd["src"] = onlyfiles[i]
    d[i] = dd

with open("sample.json", "w") as outfile:
    json.dump(d, outfile, indent=4, sort_keys=True)
