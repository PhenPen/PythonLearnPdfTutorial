""" Parsing XML documents (In the tutorial, I parsed XML from strings, However you can parse other formats, Just read the docs)"""

import xml.etree.ElementTree as ET

data = """<person>
 <name>Chuck</name>
 <phone type="intl">
 +1 734 303 4456
 </phone>
 <email hide="yes" />
 </person>"""

tree = ET.fromstring(data)
print()
# print(f"Name: {tree.find("name").text}") #This lines have issues 
print(f"Name: {tree.findtext("name")}")
# print(f"email: {tree.find("email").get('hide')}") #This lines have issues 
# print(f"email: {tree.find("email").get}") #This lines have issues 


# Having issues with line 14 and 15 , trying to call the attributes of the tag 







