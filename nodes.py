import xmltodict
import json

file = open("./dump.json", "r")
file_json = file.read()
file.close()

nodes = json.loads(file_json)["osm"]["node"]

tagKey = 'tag'
keyKey = '@k'
keyKeyBuildingValue = 'building'
valueKey = '@v'
residentialValue = 'residential'

buildings = []

for item in nodes:
  if tagKey in item.keys():
    # print("HAVE")
    for tagItem in item[tagKey]:
      if type(tagItem) is dict:
        if tagItem[keyKey] == keyKeyBuildingValue and tagItem[valueKey] == residentialValue:
          buildings.append(item)

      # if tagItem[keyKey] == keyKeyBuildingValue:
        # print(tagItem[valueKey])
  else:
    # print("NOT HAVE")
    pass
  
# print(osm_dict["osm"]["node"])



export_file = open("./buildings.json", "w")

export_file.write(json.dumps(buildings, sort_keys=True, indent=4))


