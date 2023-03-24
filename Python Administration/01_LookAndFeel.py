import arcgis
from Settings import PortalUrl,ProfileName,DataFolder
import datetime
import os

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

ux = gis.admin.ux

# CHANGE HOMEPAGE TITLE
newTitle = "DevTeam Server [Esri GISTech 2023]"
ux.homepage_settings.set_title(newTitle)
print(f"Home page title updated to {newTitle}")

# CHANGE HOMEPAGE BACKGROUND
ux.homepage_settings.set_background(r"D:\Data\background.jpg")
print(f"Home page background updated")


# CHANGE PORTAL TITLE
# sign in to dashboard using incognito: https://devteam.esri.nl/portal/apps/dashboards/home

editDatTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
gis.admin.ux.name = f"Our Fabulous portal {editDatTime}"

# sign in to dashboard using incognito: https://devteam.esri.nl/portal/apps/dashboards/home