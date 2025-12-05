""" Parsing through XML nodes ( I guess this is similar to looping through the tags in a doc )"""


from xml.etree import ElementTree as ET


inp = """ <stuff>
 <users>
 <user x="2">
 <id>001</id>
 <name>Chuck</name>
 </user>
 <user x="7">
 <id>009</id>
 <name>Brent</name>
 </user>
 </users>
 </stuff>"""

tree = ET.fromstring(inp)
users = tree.findall('users/user')
print(f"User count : {len(users)}")

for user in users:
    print(f"Name : {user.findtext('name')}")
    print(f"ID : {user.findtext('id')}")
    print(f"Attribute : {user.get('x')}")
    