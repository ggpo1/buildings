# import xmltodict
import json
import uuid

file = open("./dump.json", "r")
file_json = file.read()
file.close()

nodes = json.loads(file_json)["osm"]["node"]

tagKey = 'tag'
keyKey = '@k'
keyKeyBuildingValue = 'building'
valueKey = '@v'
residentialValue = 'residential'

osm_keys = {
  "id": "@id",
  "lat_key": "@lat",
  "lng_key": "@lon",
}

id_cache = {}

def parse_osm_node_to_viable_model(osm_node):
  if osm_keys["id"] not in osm_node or osm_keys["lat_key"] not in osm_node or osm_keys["lng_key"] not in osm_node: return
  if osm_node[osm_keys["id"]] == None or osm_node[osm_keys["lat_key"]] == None or osm_node[osm_keys["lng_key"]] == None: return

  id = osm_node[osm_keys["id"]]

  if id not in id_cache:
    id_cache[id] = True
  else:
    return

  return {
    "id": int(id),
    "lat": float(osm_node[osm_keys["lat_key"]]),
    "lng": float(osm_node[osm_keys["lng_key"]])
  }

buildings = []

for item in nodes:
  if tagKey in item.keys():
    for tagItem in item[tagKey]:
      if type(tagItem) is dict:
          parsed = parse_osm_node_to_viable_model(item)
          if parsed:
            buildings.append(parsed)

export_file = open("./buildings.json", "w")
export_file.write(json.dumps(buildings, sort_keys=True, indent=4))


