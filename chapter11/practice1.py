""" Regular Expressions"""

import re
from pathlib import Path

#print(dir(re))
#print(repr(dir(re)))

helloWorld = "Hello World"
filePath = Path(r"learningDocs/funcMethods.txt")
filePath.parent.mkdir(parents=True,exist_ok=True)

print(re.search("Hello",helloWorld))
print(helloWorld.find("Hello"))
# When is find and regular expressions used ?
# and search is under regular expressions 
reDir = ((dir(re)))

with open(filePath,mode="w",encoding="utf-8") as f:
    for item in reDir:
        f.write(f"{item}\n")

