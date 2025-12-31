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
# Use findtext to avoid None attribute errors if element missing
print(f"Name: {tree.findtext('name')}")

email_el = tree.find('email')
print(f"email hide?: {email_el.get('hide') if email_el is not None else None}")   #This fixed the former issue of having issues when calling attributes 


# Having issues with line 14 and 15 , trying to call the attributes of the tag 







