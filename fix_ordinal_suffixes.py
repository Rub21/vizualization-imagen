import sys
import string
from lxml import etree

def ordinal(n):
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
       return  str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")

filename = sys.argv[1] if (len(sys.argv) > 1) else sys.exit("Invalid file name.\nUse:  python namestolower.py filename")
tree = etree.parse(filename)
names = tree.findall(".//tag[@k='addr:street']")

for name in names:
  addrstreet = name.get("v").title()
  num_bef=''
  num_aft=''
  #print addrstreet
  for i, c in enumerate(addrstreet):
    if c.isdigit():
      start = i
      while i < len(addrstreet) and addrstreet[i].isdigit():
        i += 1
      #print 'Integer %d found at position %d' % (int(addrstreet[start:i]), start)
      num_bef=addrstreet[start:i]
      num_aft=ordinal(int(addrstreet[start:i]))
      #print num_bef
      #print num_aft
      addrstreet=addrstreet.replace(num_bef, num_aft)
      if name.get("v") != addrstreet :
        name.set("v", addrstreet)
        parent = name.getparent()
      break
  print addrstreet 
  
 
xml = "<?xml version='1.0' encoding='UTF-8'?>\n"+etree.tostring(tree, encoding='utf8').replace('"',"'")
new_file = open(filename[:-4]+'_new'+filename[-4:], 'w')
new_file.write(xml)