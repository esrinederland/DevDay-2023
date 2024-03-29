import arcgis
from Settings import PortalUrl,ProfileName
import os

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 


# ADD ITEM
fileFolder = r"D:\Data"
fileName = "earthquakes.csv"
fileType = "CSV"

filePath = os.path.join(fileFolder, fileName)
title = os.path.splitext(fileName)[0]
itemProperties={'type':fileType,
                'title':title,
                'description':'CSV file with earthquake information',
                'tags':'python, csv, earthquakes, DevDay2023'}

addedItem = gis.content.add(item_properties=itemProperties, data=filePath)
print(f"The item '{fileName}' was added to your portal with itemID: '{addedItem.itemid}'")

# ADD THUMBNAIL 
thumbnailPath = r"D:\Data\EarthQuake_image.png"
updatedItemSucceeded = addedItem.update(thumbnail=thumbnailPath)
print(f"Icon Update result: {updatedItemSucceeded}")


# SHARE WITH GROUP
groupsToShareWith = gis.groups.search(query='tags:DevDay2023')

share = addedItem.share(groups=groupsToShareWith)
if share['results'][0]['success']:
    print(f"The item was successfully shared.")
else:
    print("Something went wrong while sharing the item.")

# CREATE WEBMAP
print("Creating a webmap")
wm = arcgis.mapping.WebMap()  # new web map

wm.basemap = "streets-night-vector"

layer = gis.content.get("96cbbfd990844b78a3150313ea9971d6").layers[0]
wm.add_layer(layer)  # add some layers


# SAVE THE WEBMAP
webmap_item_properties = {'title':'DevDay Created Webmap',
             'snippet':'Map created using Python API',
             'tags':['automation', 'python', "DevDay2023"],
             'extent': {'xmin': -17, 'ymin': 42, 'xmax': 39, 'ymax': 59, 'spatialReference': {'wkid': 4326}}}

print("Saving the webmap")
new_wm_item = wm.save(webmap_item_properties, thumbnail=r'D:\Data\WebMap_Icon.jpg')
print(f"Created item with id: {new_wm_item.id}")


print("Script complete")