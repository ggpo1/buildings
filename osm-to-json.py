import xmltodict
import json

file = open("./map.osm", "r")
file_xml_str = file.read()

file.close()

export_file = open("./dump.json", "w")
export_file.write(json.dumps(xmltodict.parse(file_xml_str)))
