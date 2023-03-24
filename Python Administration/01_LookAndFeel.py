import arcgis
from Settings import PortalUrl,ProfileName
import datetime
import os

from pathlib import Path

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

ux = gis.admin.ux

# CHANGE HOMEPAGE TITLE
<<<<<<< HEAD
newTitle = "DevTeam Server [Esri GISTech 2023]"
ux.homepage_settings.set_title(newTitle)
print(f"Home page title updated to {newTitle}")

# CHANGE HOMEPAGE BACKGROUND
ux.homepage_settings.set_background(r"D:\Data\background.jpg")
print(f"Home page background updated")

=======
# homePageJson = gis._con.get(f"https://{gis.properties.portalHostname}/sharing/rest/portals/self/resources/home.page.json?f=json")
# print(homePageJson)

# newTitle = "Dev Summit Berlin 2022"
# homePageJson["header"]["title"] = newTitle

# updateHomePageUrl = f"https://{gis.properties.portalHostname}/sharing/rest/portals/self/addResource"
# updateHomePageParams = {}
# updateHomePageParams["key"] = "home.page.json"
# updateHomePageParams["text"] = homePageJson
# updateHomePageParams["f"] = "json"

# updateHomePageJson = gis._con.post(updateHomePageUrl, params=updateHomePageParams)
# print(f"Home page updated: {updateHomePageJson}")



filename = Path(r'D:\Data\background.jpg')
if filename.exists():
    print(gis.admin.ux.set_background(background_file=filename))
else:
    print("file not exists!")
>>>>>>> 139e4bbfb5f758299efc929ee12ae9d33e329399

# CHANGE PORTAL TITLE
# sign in to dashboard using incognito: https://devteam.esri.nl/portal/apps/dashboards/home

editDatTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
gis.admin.ux.name = f"Our Fabulous portal {editDatTime}"

# sign in to dashboard using incognito: https://devteam.esri.nl/portal/apps/dashboards/home