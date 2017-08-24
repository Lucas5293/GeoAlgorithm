import ogr, os

'''
    By: Lucas Augusto de Souza
    This module, create a shapefile
    and add points by the coordinates
'''

# Input data
fieldName = 'points'
fieldType = ogr.OFTString
fieldValue = 'points'
outSHPfn = 'point.shp'

# Create the output shapefile
shpDriver = ogr.GetDriverByName("ESRI Shapefile")
if os.path.exists(outSHPfn):
	shpDriver.DeleteDataSource(outSHPfn)
outDataSource = shpDriver.CreateDataSource(outSHPfn)
outLayer = outDataSource.CreateLayer(outSHPfn, geom_type=ogr.wkbMultiPoint )
#multipoint geometry
multipoint = ogr.Geometry(ogr.wkbMultiPoint)

# Add a point by coordinates
def addPoint(pointCoord):
    global multipoint
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(pointCoord[0], pointCoord[1])
    multipoint.AddGeometry(point)

# save the geometry in shapefile
def commit():
    # create a field
    idField = ogr.FieldDefn(fieldName, fieldType)
    outLayer.CreateField(idField)

    # Create the feature and set values
    featureDefn = outLayer.GetLayerDefn()
    outFeature = ogr.Feature(featureDefn)
    outFeature.SetGeometry(multipoint)
    outFeature.SetField(fieldName, fieldValue)
    outLayer.CreateFeature(outFeature)
    outFeature = None