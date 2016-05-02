import arcpy
import os


arcpy.env.workspace = r"C:\Users\cgabris\Projects\EHS_Manual_Process\CSV\Admin1"
csvDir = r"C:\Users\cgabris\Projects\EHS_Manual_Process\CSV\Admin1"
pointsDir = r"C:\Users\cgabris\Projects\EHS_Manual_Process\Points\Admin1"
shapefiles = r"C:\Users\cgabris\Projects\EHS_Manual_Process\Points\Admin1\shapefiles"


for csv in arcpy.ListFiles("*.csv"):
	# print (csv)
	outPoints = os.path.splitext(csv)[0] +'.shp'
	outPointsPath = os.path.join(pointsDir, outPoints)
	# print outPointsPath
	arcpy.MakeXYEventLayer_management(csv, "Field2", "Field3", outPoints, "PROJCS['World_Plate_Carree',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Plate_Carree'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],UNIT['Meter',1.0]];-20037700 -10018900 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision", "")
	arcpy.SaveToLayerFile_management(outPoints, outPointsPath)
	arcpy.FeatureClassToShapefile_conversion(outPoints, shapefiles)

print ('done')