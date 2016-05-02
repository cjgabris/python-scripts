import arcpy
import os

arcpy.env.workspace = r"C:\Users\cgabris\Projects\EHS_Manual_Process\lossyear_treecover_25"
outPolyPath = r"C:\Users\cgabris\Projects\EHS_Manual_Process\lossyear_treecover_25\polygon"

for ras in arcpy.ListFiles("*.tif"):
	polyName = os.path.splitext(ras)[0] + ".shp"
	# print (polyName)
	polyPath = os.path.join(outPolyPath, polyName)
	# print (polyPath)
	arcpy.RasterToPolygon_conversion(ras, polyPath, "NO_SIMPLIFY", "Value")

print ('done')
