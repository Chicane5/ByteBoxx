'''
Created on 12 Mar 2014

@author: ByteBoxx
'''


import os, sys
 



class MYBatchJobs(object):
    
    cBATCH_TASKS = ['scanassembly',
                    'batchrender',
                    'webglexport']
    
    def __init__(self):
        pass
    
    def __call__(self, value):
        if value == 'test':
            self.test()
    
    def test(self):
        maya.standalone.initialize(name='python')
        cmds.file(new=True, f=True)
        cmds.sphere()
        cmds.file(rename="C:\\Users\\ByteBoxx\\test.ma")
        cmds.file(save=True, f=True)
        
        
if __name__ == "__main__":
    import maya.standalone
    import maya.cmds as cmds
    c = MYBatchJobs()
    c(sys.argv[1])
    
        
            