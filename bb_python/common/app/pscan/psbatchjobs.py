'''
Created on 11 Mar 2014

@author: ByteBoxx
'''
import getpass
import os

class PSBatchJobs(object):
    '''
    cunting photoscan wont accept command line py scripts so we have to
    generate them dynamically at runtime you Russian bastards
    '''
    cSINGLE_SPACE = '    '
    cDOUBLE_SPACE = cSINGLE_SPACE+cSINGLE_SPACE
    cBAT_DIR = 'C:\\Program Files\\ByteBoxx\\RenderBoxx\\bin'
    #standard tasks for processing a photoscan mesh job
    cBATCH_TASKS = ['automask',
                    'align',
                    'builddensecloud',
                    'geotexbuild',
                    'modelexport']
    
    def __init__(self):
        pass
    
 
    def align(self, label, photodir, accuracy):
        tempfile = os.path.abspath(os.path.join(os.path.dirname(photodir), "align.py"))
        with open(tempfile, 'w') as fh:
            fh.write("####AUTO GENERATED PHOTOSCAN SCRIPT...POWERED BY BYTEBOXX LTD###\n\n\n")
            fh.write("import PhotoScan\n")
            fh.write("import os\n\n")
            fh.write("def main():\n")
            fh.write(self.cSINGLE_SPACE+"app = PhotoScan.Application()\n")
            fh.write(self.cSINGLE_SPACE+"doc = app.document\n")
            
            fh.write(self.cSINGLE_SPACE+"chunk = PhotoScan.Chunk()\n")
            fh.write(self.cSINGLE_SPACE+"chunk.label = '"+label+"'\n")
            fh.write(self.cSINGLE_SPACE+"doc.chunks.add(chunk)\n")
            fh.write(self.cSINGLE_SPACE+"photos_list = os.listdir('"+photodir+"')\n")
            
            fh.write(self.cSINGLE_SPACE+"for photo_name in photos_list:\n")
            fh.write(self.cDOUBLE_SPACE+"chunk.photos.add(os.path.join('"+photodir+"', photo_name))\n")
            
            fh.write(self.cSINGLE_SPACE+"doc.activeChunk.matchPhotos(accuracy='"+accuracy+"', preselection='disabled', filter_mask=False)\n")
            fh.write(self.cSINGLE_SPACE+"doc.activeChunk.alignPhotos()\n")
            
            
            fh.write("PhotoScan.app.addMenuItem('ByteBoxx/Align_"+tempfile+"', main)\n")
            #fh.write("doc.save('C:\\Users\\ByteBoxx\\Desktop\\align_celery.psz')\n")
            #fh.write("app.quit()")
            
            
            fh.close()
        return tempfile
    
    def runInPhotoScan(self, script):
        return '"' + os.path.join(self.cBAT_DIR, 'copyToPSScripts.bat') +'" ' + script
        
        
if __name__ == "__main__":
    psb = PSBatchJobs()
    psb.align('twat', "C:\\sometwatdir\\init", "low")
