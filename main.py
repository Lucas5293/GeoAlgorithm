from osgeo import ogr
from points import *
import random

def randomCoordinate(xmin, ymin, xmax, ymax):
	return (float("%.5f"%random.uniform(xmin, xmax)), float("%.5f"%random.uniform(ymin, ymax)))

shapefile = "mg_municipios.shp"
#shapefile = "/SHPTeste/lotes.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()

print('''
******************************************
| Generator of 10 points in each geometry|
|                                        |
| By: Lucas Augusto de Souza             |
|     Railson Tales                      |
|                                        |
******************************************
''')

input("--Press Enter to start--")


for feature in layer:
	geom = feature.GetGeometryRef()
	env = geom.GetEnvelope()

	for i in range(10):
		repet = 8 # Max number of attempts
		while (repet>0):
			randomPoint = randomCoordinate(env[0],env[2],env[1],env[3])
			print([randomPoint[0], randomPoint[1]])
			point = ogr.Geometry(ogr.wkbPoint)
			point.AddPoint(randomPoint[0], randomPoint[1])
			if point.Within(geom):
				repet = 0
				addPoint([randomPoint[0],randomPoint[1]])
				print([randomPoint[0],randomPoint[1]])
			repet-=1
	print("Geometry - OK")
commit()
print("All points added")