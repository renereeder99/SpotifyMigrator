from __future__ import print_function
import xml.etree.ElementTree as ET

#input the path to your .xml file
path = 'SpotifyMigrator\iTunes Music Library.xml'


def extract_data_from_dict(element):
    data = {}
    key = None
    for child in element:
        if child.tag == 'key': 
            key = child.text
        elif key:
            data[key] = child.text
            key = None
    return data

def mp3_list_to_dictionary(path):
    tree = ET.parse(path)
    root = tree.getroot()

    result_info = []

    for dict_element in root.findall(".//dict/dict"):
        data = extract_data_from_dict(dict_element)
        if 'Name' in data and 'Artist' in data:
            result_info.append({"Name": data.get("Name", ""), "Artist": data.get("Artist", ""), "Album": data.get("Album", ""), "Year": data.get("Year", "")})
    
    return result_info

def mp3_list_to_query(result_info):
    for entry in result_info:
        entry["Name"] = entry["Name"].replace(" ", "%20")
        entry["Artist"] = entry["Artist"].replace(" ", "%20")
        entry["Album"] = entry["Album"].replace(" ", "%20")
    return(result_info)


