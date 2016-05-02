import arcpy
import os

arcpy.env.workspace = r"P:\2371 WDCEP\3_Data\forGoogleEarth\2008"
outDir = r"P:\2371 WDCEP\3_Data\forGoogleEarth\2008\kmz"
arcpy.CheckOutExtension("3D")

def layer_to_kmz():
	for tif in arcpy.ListFiles("*.tif"):
		outlyr = os.path.splitext(tif)[0] + '.lyr'
		print (outlyr)

def tif_to_layer():
	for tif in arcpy.ListFiles("*.tif"):
		# print (tif)
		outkmz = os.path.splitext(tif)[0] + '.kmz'
		outkmzpath = os.path.join(outDir, outkmz)
		print (outkmzpath)

		# arcpy.LayerToKML_conversion(layer="400masssp_rec_08.tif", outkmzpath, layer_output_scale="0", is_composite="false", boundary_box_extent="DEFAULT", image_size="3000", dpi_of_client="300", ignore_zvalue="CLAMPED_TO_GROUND")
		# arcpy.LayerToKML_conversion("400MassAve_08.lyr", outkmzpath, '','','','3000','300')
		#arcpy.LayerToKML_conversion(tif, outkmzpath, '', '', '', 4000, 400)

	arcpy.CheckInExtension("3D")
	print ('layer to kml complete')

def main():
	tif_to_layer()
	# layer_to_kmz()


if __name__ == '__main__':
	main()