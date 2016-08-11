############################################################################################################################################################################################
##UCNIRKMF.py
##
##Author: Ryan Davison
##        
##Date: August 9, 2012
##
##Purpose: This script sets a definition query for all features in a map document. Add 
##
##IMPORTANT:This script is meant to be used as a tool inside of an MXD. It is not intended as a stand-alone script.
##
############################################################################################################################################################################################


#Import the os and arcpy modules.
import arcpy, os

query = arcpy.GetParameter(0)

try:
        #Set the workspace environment to be the current map document that the tool
        #is being run in.
        arcpy.env.workspace = "Current"

        #Define mxd as the current map document being worked in.
        mxd = arcpy.mapping.MapDocument("Current")

        #Define df as a list of all data frames in the current map document
        df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

        #Loop through each layer in the data frame and apply
        #the definition query.
        for lyr in arcpy.mapping.ListLayers(mxd,"",df):                
                lyr.definitionQuery = query
finally:
        #Refresh the active map view and the table of contents.
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
