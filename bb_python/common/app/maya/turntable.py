'''
Created on 23 Feb 2014

@author: ByteBoxx
'''
import maya.cmds as cmds
import maya.mel as mel

#===============================================================================
# 
#===============================================================================
class BodyScanPreset(object):
    tx = 0
    ty = 3.5
    tz = 100
    orthwidth = 3.377
    orientations = {'min135':-135.00, 'min90':-90.00, 'min45':-45.00, 'front':0.00, '45':45.00, '90':90.00, '135':135.00 }
    
    
#===============================================================================
# 
#===============================================================================
class TurnTable(object):
    '''
    classdocs
    '''
    def __init__(self, preset=None):
        '''
        Constructor
        '''
        self.mPreset = preset
        self.mCamera = self._createCam()
        self._setupCamParams()
        
    def _createCam(self):
        #create the turntable camera group it to a null node
        if self.mPreset:
            turn = cmds.camera( p= [self.mPreset.tx, self.mPreset.ty, self.mPreset.tz], o=True,  n="turntablecam")

        else:
            turn = cmds.camera( p= [0,0,0], o=True,  n="turntablecam")
        return turn
    
    
    def _setupCamParams(self):
        cmds.setAttr( self.mCamera[1] + ".nearClipPlane", 0.1) 
        cmds.setAttr ( self.mCamera[1] + ".farClipPlane", 200.0)
        
        cmds.xform( ws=True,  piv=[ 0, 0 ,0])
        cmds.setAttr( self.mCamera[1] + ".filmFit", 1 )
        if self.mPreset:
            cmds.setAttr(self.mCamera[1] + ".orthographicWidth", self.mPreset.orthwidth)
            
    def rotate(self, value):
        cmds.setAttr(self.mCamera[0] + ".ry", value)
        