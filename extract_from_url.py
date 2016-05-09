import arcpy
import os
import urllib
import zipfile

arcpy.CheckOutExtension("3D")

mxdFile = r"P:\2371 WDCEP\3_Data\forGoogleEarth\DC_OpenData_Layers\blank.mxd"
WDCEP = r"P:\2371 WDCEP\3_Data\forGoogleEarth\DC_OpenData_Layers\WDCEP.mxd"
WebMap_MXD = r"P:\2371 WDCEP\4_Maps\AGOL_WebMap.mxd"
mxdoutputs = r"P:\2371 WDCEP\3_Data\forGoogleEarth\DC_OpenData_Layers\outputmxds"
arcpy.env.overwriteOutput = True
zipDirectory = r"P:\2371 WDCEP\3_Data\forGoogleEarth\DC_OpenData_Layers\data"
layerFileDirectory = r"P:\2371 WDCEP\3_Data\forGoogleEarth\DC_OpenData_Layers\LayerFiles"
arcpy.env.workspace = zipDirectory


config = [
	{
		"zip": "Metro_Stations_Regional.zip",
		"name": "Metro_Stations_Regional.shp",
		"url":"http://opendata.dc.gov/datasets/e3896b58a4e741d48ddcda03dae9d21b_51.zip",
		"layerfile": "Metro_Stations_Regional.lyr"
	},{
		"zip": "Metro_Bus_Stops.zip",
		"name": "Metro_Bus_Stops.shp",
		"url":"http://opendata.dc.gov/datasets/e85b5321a5a84ff9af56fd614dab81b3_53.zip",
		"layerfile": "Metro_Bus_Stops.lyr"
	},{
		"zip":"Basic_Business_License__2015.zip",
		"name":"Basic_Business_License__2015.shp",
		"url":"http://opendata.dc.gov/datasets/4c4d6b4defdf4561b737a594b6f2b0dd_23.zip",
		"layerfile": "Basic_Business_License__2015.lyr"
	},{
		"zip": "Building_Permits__2015.zip",
		"name": "Building_Permits__2015.shp",
		"url":"http://opendata.dc.gov/datasets/981c105beef74af38cc4090992661264_25.zip",
		"layerfile": "Building_Permits__2015.lyr"
	},{
		"zip": "Commercial_CAMA.zip",
		"name": "Commercial_CAMA.shp",
		"url":"http://opendata.dc.gov/datasets/e53572ef8f124631b965709da8200167_23.zip",
		"layerfile": "Commercial_CAMA.lyr"
	},{
		"zip": "Universities_and_Colleges.zip",
		"name": "Universities_and_Colleges.shp",
		"url":"http://opendata.dc.gov/datasets/1a714ebe2aae41b6a5c2dd96fb613733_12.zip",
		"layerfile": "Universities_and_Colleges.lyr"
	},{
		"zip": "Places_of_Worship.zip",
		"name": "Places_of_Worship.shp",
		"url":"http://opendata.dc.gov/datasets/b134de8f8eaa49499715a38ba97673c8_5.zip",
		"layerfile": "Places_of_Worship.lyr"
	},{
		"zip": "Pharmacy_Locations.zip",
		"name": "Pharmacy_Locations.shp",
		"url":"http://opendata.dc.gov/datasets/2335ba275c3f4320a3113f13181eab56_9.zip",
		"layerfile": "Pharmacy_Locations.lyr"
	},{
		"zip": "Grocery_Store_Locations.zip",
		"name": "Grocery_Store_Locations.shp",
		"url":"http://opendata.dc.gov/datasets/1d7c9d0e3aac49c1aa88d377a3bae430_4.zip",
		"layerfile": "Grocery_Store_Locations.lyr"
	},{
		"zip": "Gas_Stations.zip",
		"name": "Gas_Stations.shp",
		"url":"http://opendata.dc.gov/datasets/d5f6fbd97d244e1c9dbc42f6440ca09b_3.zip",
		"layerfile": "Gas_Stations.lyr"
	},{
		"zip": "Hotel_Locations.zip",
		"name": "Hotel_Locations.shp",
		"url":"http://opendata.dc.gov/datasets/825652c143e447cda4d3b67bc60150a0_7.zip",
		"layerfile": "Hotel_Locations.lyr"
	},{
		"zip": "Liquor_License_Locations.zip",
		"name": "Liquor_License_Locations.shp",
		"url":"http://opendata.dc.gov/datasets/cabe9dcef0b344518c7fae1a3def7de1_5.zip",
		"layerfile": "Liquor_License_Locations.lyr"
	},{
		"zip": "Public_Schools.zip",
		"name": "Public_Schools.shp",
		"url":"http://opendata.dc.gov/datasets/4ac321b2d409438ebd76a6569ad94034_5.zip",
		"layerfile": "Public_Schools.lyr"
	},{
		"zip": "Charter_Schools.zip",
		"name": "Charter_Schools.shp",
		"url":"http://opendata.dc.gov/datasets/a3832935b1d644e48c887e6ec5a65fcd_1.zip",
		"layerfile": "Charter_Schools.lyr"
	},{
		"zip": "Independent_Schools.zip",
		"name": "Independent_Schools.shp",
		"url":"http://opendata.dc.gov/datasets/8986ebe04f554892aa76b95b284c4942_3.zip",
		"layerfile": "Independent_Schools.lyr"
	},{
		"zip": "Metro_Lines_Regional.zip",
		"name": "Metro_Lines_Regional.shp",
		"url":"http://opendata.dc.gov/datasets/ead6291a71874bf8ba332d135036fbda_58.zip",
		"layerfile": "Metro_Lines_Regional.lyr"
	},{
		"zip": "DC_Main_Street_Corridors.zip",
		"name": "DC_Main_Street_Corridors.shp",
		"url":"http://opendata.dc.gov/datasets/8e602ef5080e4343913702452ddf71d4_16.zip",
		"layerfile": "DC_Main_Street_Corridors.lyr"
	},{
		"zip": "Supermarket_Tax_Credit_Zone.zip",
		"name": "Supermarket_Tax_Credit_Zone.shp",
		"url":"http://opendata.dc.gov/datasets/1c5d4b467eaa4301b976547c65cd7d06_24.zip",
		"layerfile": "Supermarket_Tax_Credit_Zone.lyr"
	},{
		"zip": "Ward__2012.zip",
		"name": "Ward__2012.shp",
		"url":"http://opendata.dc.gov/datasets/0ef47379cbae44e88267c01eaec2ff6e_31.zip",
		"layerfile": "Ward__2012.lyr"
	},{
		"zip": "Tax_Increment_Financing_TIF_areas.zip",
		"name": "Tax_Increment_Financing_TIF_areas.shp",
		"url":"http://opendata.dc.gov/datasets/f60a6d54bf2e4e12a779fd0ba3a68e7e_26.zip",
		"layerfile": "Tax_Increment_Financing_TIF_areas.lyr"
	},{
		"zip": "Great_Streets_Corridors.zip",
		"name": "Great_Streets_Corridors.shp",
		"url":"http://opendata.dc.gov/datasets/2ccac3f2585f487c9d14919d02d66740_13.zip",
		"layerfile": "Great_Streets_Corridors.lyr"
	},{
		"zip": "Business_Improvement_Districts.zip",
		"name": "Business_Improvement_Districts.shp",
		"url":"http://opendata.dc.gov/datasets/20ec5862d8f14bcbb9bf14f79c311406_15.zip",
		"layerfile": "Business_Improvement_Districts.lyr"
	},{
		"zip": "Square_Boundaries.zip",
		"name": "Square_Boundaries.shp",
		"url":"http://opendata.dc.gov/datasets/84ab8b676a384c339062b53dca3bdfa2_41.zip",
		"layerfile": "Square_Boundaries.lyr"
	},{
		"zip": "HUB_Zones_Historically_Underutilized_Business_Zones.zip",
		"name": "HUB_Zones_Historically_Underutilized_Business_Zones.shp",
		"url":"http://opendata.dc.gov/datasets/3060b61b0f9c444dbbd873bfae5ffa16_21.zip",
		"layerfile": "HUB_Zones_Historically_Underutilized_Business_Zones.lyr"
	},{
		"zip": "Enterprise_and_Empowerment_Zones.zip",
		"name": "Enterprise_and_Empowerment_Zones.shp",
		"url":"http://opendata.dc.gov/datasets/27221bef23ed4f5aa6e8e51d51edede9_19.zip",
		"layerfile": "Enterprise_and_Empowerment_Zones.lyr"
	},{
		"zip": "Building_Footprints.zip",
		"name": "Building_Footprints.shp",
		"url":"http://opendata.dc.gov/datasets/a657b34942564aa8b06f293cb0934cbd_1.zip",
		"layerfile": "Building_Footprints.lyr"
	},{
		"zip": "Waterbodies.zip",
		"name": "Waterbodies.shp",
		"url":"http://opendata.dc.gov/datasets/db65ff0038ed4270acb1435d931201cf_24.zip",
		"layerfile": "Waterbodies.lyr"
	},{
		"zip": "Owner_Polygons_Common_Ownership_Layer.zip",
		"name": "Owner_Polygons_Common_Ownership_Layer.shp",
		"url":"http://opendata.dc.gov/datasets/1f6708b1f3774306bef2fa81e612a725_40.zip",
		"layerfile": "Owner_Polygons_Common_Ownership_Layer.lyr"
	},{
		"zip": "District_Land_Approximate.zip",
		"name": "District_Land_RPTA_Ownership.shp",
		"url":"http://opendata.dc.gov/datasets/7c45f7875cc84cad9dc2375c21858f95_49.zip",
		"layerfile": "District_Land_RPTA_Ownership.lyr"
	},{
		"zip": "Federal_Land_Approximate.zip",
		"name": "Federal_Land_RPTA_Ownership.shp",
		"url":"http://opendata.dc.gov/datasets/975f8d7ad6a1447dabf28c8bfdeff5f4_50.zip",
		"layerfile": "Federal_Land_RPTA_Ownership.lyr"
	},{
		"zip": "Zoning.zip",
		"name": "Zoning.shp",
		"url":"http://opendata.dc.gov/datasets/7e36b5f8c97f440ab45e31dc58ea9471_12.zip",
		"layerfile": "Zoning.lyr"
	},{
		"zip": "Land_Use__Existing.zip",
		"name": "Land_Use__Existing.shp",
		"url":"http://opendata.dc.gov/datasets/245179183eee41e08852ff9d5dbd3bcb_4.zip",
		"layerfile": "Land_Use__Existing.lyr"
	},{
		"zip": "DC_Boundary.zip",
		"name": "DC_Boundary.shp",
		"url":"http://opendata.dc.gov/datasets/7241f6d500b44288ad983f0942b39663_10.zip",
		"layerfile": "DC_Boundary.lyr"
	}

]

#baseURL = "http://services.arcgis.com/EDxZDh4HqQ1a9KvA/arcgis/rest/services/Connexio_Media_Sample_Data/FeatureServer/0/query"
# where = "1=1"
# fields = "*"
# query = "?where={}&outFields={}&returnGeometry=true&f=json".format(where, fields)

#  for shp in config:
#  	fsURL = shp["url"] + query
#  	fs = arcpy.FeatureSet()
#  	print "processing> ", shp["name"]
#  	fs.load(fsURL)
#  	outputFs = os.path.join(directory,shp["name"])
# # 	arcpy.CopyFeatures_management(fs, outputFs)
	
def download_and_extract_zips():
	for obj in config:
		url = obj["url"]
		outputZIP = os.path.join(zipDirectory,obj['zip'])
		# print outputZIP
		# print '>>>>>>>>'
		urllib.urlretrieve(url, outputZIP)
		with zipfile.ZipFile(outputZIP, "r") as z:
			z.extractall(zipDirectory)

def add_layers_to_mxd():
	mxd = arcpy.mapping.MapDocument(mxdFile)
	df = arcpy.mapping.ListDataFrames(mxd)[0]
	for shp in arcpy.ListFiles('*.shp'):
		print shp
		layer = arcpy.mapping.Layer(shp)
		layerfile = [i["layerfile"] for i in config if i["name"] == shp][0]
		print layerfile 
		sym = os.path.join(layerFileDirectory,layerfile)
		arcpy.ApplySymbologyFromLayer_management(layer,sym)
		arcpy.mapping.AddLayer(df,layer,"BOTTOM")
		# for lyr in arcpy.mapping.ListLayers(WDCEP, "*",df):
		# 	lyr.visible = False
		
		#To create a mxd for each layer file use the following two lines and comment out mxd.saveACopy(WDCEP)
		# otm = os.path.join(mxdoutputs,shp.split(".shp")[0])
		# mxd.saveACopy(otm)
	mxd.saveACopy(WDCEP)

def map_to_kml():
	mxd = arcpy.mapping.MapDocument(WebMap_MXD)
	df = arcpy.mapping.ListDataFrames(mxd)[0]
	arcpy.MapToKML_conversion(WebMap_MXD, "Layers", "AGOLmap_to_kml2.kmz","0","NO_COMPOSITE","VECTOR_TO_IMAGE","DEFAULT","1024","96","CLAMPED_TO_GROUND")
	# arcpy.MapToKML_conversion(mxd, df, "WDCEP.kmz", "1", '', '','','','','')

	arcpy.CheckInExtension("3D")
	print 'done'
	


def main():
	download_and_extract_zips()
	add_layers_to_mxd()
	map_to_kml()

if __name__ == '__main__':
	main()




