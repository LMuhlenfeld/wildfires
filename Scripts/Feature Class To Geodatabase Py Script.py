import arcpy
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.FeatureClassToGeodatabase(
    Input_Features="PFIS.POSTFIRE_DINS;'DINS Postfire Structure Points';'Damaged or Destroyed Structures';'No Visible Damage';'Camp Perimeter'",
    Output_Geodatabase=r"C:\Users\lisam\Desktop\Wildfires\Wildfires Project\Default.gdb"
)
