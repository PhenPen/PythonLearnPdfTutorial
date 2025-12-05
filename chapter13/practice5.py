

import json

data = """ 
[ {"id" : "001", 
"x" : "2",
"name" : "Chuck"},
{"id" : "009", 
"x" : "7",
"name" : "Brent"}
]"""

info = json.loads(data)
print(info)


for person in info:
    print(f"Name : {person.get("name")}")
    print(f"Id : {person.get("id")}")
    print(f"Attribute : {person.get("x")}")