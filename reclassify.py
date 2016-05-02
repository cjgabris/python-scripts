import arcpy
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
inRas = r"P:\2375 UNICEF\3_Data\Global Population\world_pop_analysis.gdb\UN_world_u18_2015_Europe_Mask"
outRas = r"C:\Users\cgabris\Documents\ArcGIS\scratch.gdb\reclass"
field = "Value"
arcpy.gp.Reclassify_sa(inRas, field, "0 121 7;121 704 8;704 6193 9", outRas, "DATA")
arcpy.CheckInExtension("Spatial")