'''
Created on 24 Feb 2014

@author: ByteBoxx
'''

import maya.cmds as cmds

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
    def __init__(self, units, width, height, resolution, rendercam):
        self.mUnits = units
        self.mWidth = width
        self.mHeight = height
        self.mResolution = resolution
        self.mRenderCam = rendercam
        self._setAttrs()
        
    def _setAttrs(self):
        cmds.setAttr("defaultResolution.imageSizeUnits", self.mUnits)
        cmds.setAttr("defaultResolution.dpi", self.mResolution)
        cmds.setAttr("defaultResolution.w", self.mWidth)
        cmds.setAttr("defaultResolution.h", self.mHeight)
        cmds.setAttr("defaultResolution.pixelAspect", 1)
        cmds.setAttr("defaultResolution.deviceAspectRatio",  0.4)
        cmds.setAttr( "defaultRenderGlobals.imageFormat", 8)

        
    
    def render(self, prefix, path):
        #set prefix and path then render out
        cmds.setAttr ("defaultRenderGlobals.imageFilePrefix", prefix, type="string")
        cmds.lookThru(self.mRenderCam)
        cmds.render()