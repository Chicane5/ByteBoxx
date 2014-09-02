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
    def __init__(self, pIn, pBase, pOut):#units, width, height, resolution, rendercam):
        #self.mUnits = units
        #self.mWidth = width
        #self.mHeight = height
        #self.mResolution = resolution
        #self.mRenderCam = rendercam

        self.mIn = pIn
        self.mBase = pBase
        self.mOut = pOut
        self.mTurnTable = turntable.TurnTable(preset=turntable.BodyScanPreset())
        
        self._main()
        
    def _main(self):
        #self._setAttrs()
        self._importFile()
        
    def _setAttrs(self):
        cmds.setAttr("defaultResolution.imageSizeUnits", self.mUnits)
        cmds.setAttr("defaultResolution.dpi", self.mResolution)
        cmds.setAttr("defaultResolution.w", self.mWidth)
        cmds.setAttr("defaultResolution.h", self.mHeight)
        cmds.setAttr("defaultResolution.pixelAspect", 1)
        cmds.setAttr("defaultResolution.deviceAspectRatio",  0.4)
        cmds.setAttr( "defaultRenderGlobals.imageFormat", 8)

        
    def  _importFile(self):
        if os.path.isfile(self.mBase):
            cmds.file(self.mBase, o=True)
        cmds.loadPlugin("fbxmaya")
        cmds.file(self.mIn, i=True)
        self.render(self.mOut)
    
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
    
    c = BatchRender(sys.argv[1], sys.argv[2], sys.argv[3])
    #c(sys.argv[1])