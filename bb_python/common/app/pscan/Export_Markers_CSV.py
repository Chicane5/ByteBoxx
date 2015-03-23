# exports all markers in activeChunk to csv.
# compatibility: Agisoft PhotoScan Professional 0.9.0
import PhotoScan 
import math 


FILEPATH = 'C:/marker_export.txt'

app = PhotoScan.app
doc = PhotoScan.app.document
chunk = doc.activeChunk
f = open(FILEPATH, 'w')
for item in chunk.markers:
	if item.position == None:
		continue
	v = item.position
	v.size = 4
	v.w = 1
	if not chunk.transform:
		chunk.transform = PhotoScan.Matrix.diag( (1,1,1,1) )
	T = chunk.transform
	v_t = T * v
	v_t.size = 3
	proj = chunk.crs
	v_out = proj.project(v_t)
	f.write(item.label + ',' + str(v_out[0]) + ',' + str(v_out[1]) + ',' + str(v_out[2]) + '\n')
f.close()
	