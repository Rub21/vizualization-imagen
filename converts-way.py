# basically the same thing as require()
# in nodejs
from xml.etree.ElementTree import ElementTree
from sys import argv
from datetime import datetime
import time
import json

tree = ElementTree()

if (len(argv) < 3):
    print "specify an input & output filename. input is osm, output is geojson"
    exit()

tree.parse(argv[1])

geojson = { "type": "FeatureCollection", "features": [] }

nodeidx = {}

print 'mapping nodes'

for n in tree.iterfind('node'):
    nodeidx[n.attrib['id']] = [float(n.attrib['lon']), float(n.attrib['lat'])]

print 'mapping ways'

# okay, so a way is like:
#  <way ... user='minoxfilm' visible='true' version='4' ...>
#    <nd ref='290905840' />
#    ... more nodes
#    <tag k='name' v='San Bonifacio' />
#    ... more tags
#  </way>
for w in tree.iterfind('way'):
    # okay, so there aren't that many tags for ways,
    # so just find them all instead of trying some janky XPath magic
    tags = {}
    for t in w.iterfind('tag'):
        tags[t.attrib['k']] = t.attrib['v']
    way = {
        "type": "Feature",
        "geometry": {
            "type": 'LineString',
            "coordinates": []
        },
        "properties": { }
        }
    for n in w.iterfind('nd'):
        way['geometry']['coordinates'].append(nodeidx[n.attrib['ref']])
        # not all ways have names, and when you try to get one
        # from a way that doesn't, you get a nasty keyerror, so check.
        way['properties']['name'] = tags.get('name', '')
        if tags.has_key('highway'):
            way['properties']['highway'] = tags['highway']
            #way['properties']['highway'] = tags.get('highway')            
            #print w.attrib['user']
            
        # ways always have a user
        way['properties']['user'] = w.attrib['user']
        way['properties']['timestamp'] = time.mktime(datetime.strptime(w.attrib['timestamp'], '%Y-%m-%dT%H:%M:%SZ').utctimetuple())
        way['properties']['version'] = w.attrib['version'];
        #print w.attrib['timestamp']
    geojson['features'].append(way)

print 'saving geojson'

json.dump(geojson, open(argv[2], 'w'))