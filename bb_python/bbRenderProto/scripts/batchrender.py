'''
Created on 24 Feb 2014

@author: ByteBoxx
'''
import os
from app.maya import turntable

#===============================================================================
# 
#===============================================================================
class RenderUnits(object):
    pixels = 0
    inches = 1
    
#===============================================================================
# 
#===============================================================================
class BatchRender(object):
    '''
    '''
    def __init__(self, pIn, pOutPath, pBase=None):#units, width, height, resolution, rendercam):
        #self.mUnits = units
        #self.mWidth = width
        #self.mHeight = height
        #self.mResolution = resolution
        #self.mRenderCam = rendercam

        self.mIn = pIn
        self.mOutPath = pOutPath
        self.mBase = pBase
        
        self.mTurnTable = turntable.TurnTable(preset=turntable.BodyScanPreset())
        
        self._main()
        
    def _main(self):
        #self._setAttrs()
        self._importFile()
        self._createTurntable()
        
    def _setAttrs(self):
        cmds.setAttr("defaultResolution.imageSizeUnits", self.mUnits)
        cmds.setAttr("defaultResolution.dpi", self.mResolution)
        cmds.setAttr("defaultResolution.w", self.mWidth)
        cmds.setAttr("defaultResolution.h", self.mHeight)
        cmds.setAttr("defaultResolution.pixelAspect", 1)
        cmds.setAttr("defaultResolution.deviceAspectRatio",  0.4)
        cmds.setAttr( "defaultRenderGlobals.imageFormat", 8)

        
    def  _importFile(self):
        #try and grab a base lighting scene
        if self.mBase != None and os.path.isfile(self.mBase):
            cmds.file(self.mBase, open=True, force=True)
            
        cmds.loadPlugin("fbxmaya")
        cmds.file(self.mIn, i=True)
        lSavePath = r"" + (os.path.join(self.mOutPath, "Test.mb"))
        if not os.path.exists(lSavePath):
            os.makedirs(lSavePath)
        cmds.file(rename=lSavePath)
        cmds.file(s=True)
        
    def _createTurntable():
        #self.mTurnTable.
    
    """
    def render(self, prefix):
        #set prefix and path then render out
        cmds.setAttr ("defaultRenderGlobals.imageFilePrefix", 'test', type="string")
        #cmds.lookThru(self.mTurnTable.mCamera)
        cmds.render()
    """    
        
if __name__ == "__main__":
    import sys
    import maya.standalone
    import maya.cmds as cmds
    import maya.mel as mel
    maya.standalone.initialize(name='python')
    cmds.file(new=True, f=True)
    
    if len(sys.argv) == 3:
        c = BatchRender(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        c = BatchRender(sys.argv[1], sys.argv[2], sys.argv[3])
    #c(sys.argv[1])