'''
Created on 11 Mar 2014

@author: ByteBoxx
'''

class PSBatchJobs(object):
    '''
    cunting photoscan wont accept command line py scripts so we have to
    generate them dynamically at runtime you Russian bastards
    '''
    cSINGLE_SPACE = '    '
    cDOUBLE_SPACE = cSINGLE_SPACE+cSINGLE_SPACE 
    
    def __init__(self):
        pass
    
 
    def align(self, label, photodir, accuracy):
        with open("C:\\Users\\ByteBoxx\\Desktop\\AlignMe.py", 'w') as fh:
            fh.write("####AUTO GENERATED PHOTOSCAN SCRIPT...POWERED BY BYTEBOXX LTD###\n\n\n")
            fh.write("import PhotoScan\n")
            fh.write("import os\n\n")
            fh.write("app = PhotoScan.Application()\n")
            fh.write("doc = PhotoScan.Document()\n")
            
            fh.write("chunk = PhotoScan.Chunk()\n")
            fh.write("chunk.label = '"+label+"'\n")
            fh.write("doc.chunks.add(chunk)\n")
            fh.write("photos_list = os.listdir('"+photodir+"')\n")
            
            fh.write("for photo_name in photos_list:\n")
            fh.write(self.cSINGLE_SPACE+"chunk.photos.add(os.path.join('"+photodir+"', photo_name))\n")
            
            fh.write("chunk.matchPhotos(accuracy='"+accuracy+"', preselection='disabled', filter_mask=False)\n")
            fh.write("chunk.alignPhotos()\n")
            
            #fh.write("doc.save('C:\\Users\\ByteBoxx\\Desktop\\align_celery.psz')\n")
            #fh.write("app.quit()")
            
            
            fh.close()
            
if __name__ == "__main__":
    psb = PSBatchJobs()
    psb.align('twat', "C:\\sometwatdir\\init", "low")
