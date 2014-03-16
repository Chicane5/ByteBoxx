'''
Created on 4 Nov 2013

@author: ByteBoxx
'''
import sys, os

def main_is_frozen():
    return (hasattr(sys, "frozen") or hasattr(sys, "importers"))# old py2exe

   
def get_main_dir():
    if main_is_frozen():
        return os.path.dirname(sys.executable)
    else:
        return None