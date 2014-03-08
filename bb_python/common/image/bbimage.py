'''
Created on 6 Mar 2014

@author: ByteBoxx
'''

import os
import pyexiv2
gFFMBC_F2V_CMD = 'ffmbc.exe -y -f image2 -r 24000/1001 -i {0} -force_fps -threads 8 -vcodec dnxhd -f mov -b {1} -r 24000/1001 -timecode {2} -s {3} {4}'

class MetaReadError(Exception):
    pass

#===============================================================================
# 
#===============================================================================
class bbImage(object):
    """
    simple class representing a common image file
    """
    DEFAULT_WIDTH_HD1080 = 1920
    DEFAULT_WIDTH_HD720 = 1280
    DEFAULT_HEIGHT_HD1080 = 1080
    DEFAULT_HEIGHT_HD720 = 720
    TC_EXIF_KEY = 'Exif.Image.DateTime'
    cDTO_EXIF_KEY = 'Exif.Photo.DateTimeOriginal'

    def __init__(self, pImagePath):
        self.imagePath = pImagePath
        self.w = 0
        self.h = 0
        self.startTimecode = ''
        self.hour = ''
        self.minute = ''
        self.second = ''
        self.frame = ''
        self.exifKeys = []

    def __repr__(self):
        return '%s' % self.__class__
    
    def _getExifKey_TimeCode(self):
        return bbImage.TC_EXIF_KEY

    def populateMeta(self, *args):
        """
        by default this method will populate timecode (if present). Any firther *args are
        parsed to test for additional exif values
        """
        meta = self._getAllMeta()
        if not meta:
            raise MetaReadError("Error Reading Image MetaData, has image finished copying?")
        else:
            self.exifKeys = self._getAllMetaKeys(meta)
            for key in self.exifKeys:
                if key == self._getExifKey_TimeCode():
                    tag = meta[self._getExifKey_TimeCode()]
                    self.startTimecode = tag.raw_value
                    self._splitTimecode()
    
            if args:
                for arg in args:
                    try:
                        lTag = meta[arg]
                        self.__dict__[arg.split('.')[1] + '_' + arg.split('.')[2]] = lTag.raw_value
                    except:
                        print 'could not get meta for tag ', arg
        
    def writeMeta(self, pNewValue):
        meta = self._getAllMeta()
        self.exifKeys = self._getAllMetaKeys(meta)
        if self._getExifKey_TimeCode() in self.exifKeys:
            meta.writable = os.access(self.imagePath, os.W_OK)
            meta[self._getExifKey_TimeCode()] = pyexiv2.ExifTag(self._getExifKey_TimeCode(), pNewValue)
            meta.write()

    def _getAllMeta(self):
        """
        gets meta from supplied image and reads
        """
        try:
            metadata = pyexiv2.ImageMetadata(self.imagePath)
            metadata.read()
            return metadata
        except:
            print 'error reading meta data'
            return None

    def prettyPrintMeta(self):
        for k in self.exifKeys:
            print k, '\n'

    def _getAllMetaKeys(self, pMetaObject):
        return pMetaObject.exif_keys

    def _splitTimecode(self):
        splitTCStr = self.startTimecode.split(':')
        self.hour = splitTCStr[0]
        self.minute = splitTCStr[1]
        self.second = splitTCStr[2]
        self.frame = splitTCStr[3]

    def getStartTCStr(self):
        return self.startTimecode

    def getHour(self):
        return self.hour

    def getHourAsInt(self):
        return int(self.hour)

    def getMinute(self):
        return self.minute

    def getMinuteAsInt(self):
        return int(self.minute)

    def getSecond(self):
        return self.second

    def getSecondAsInt(self):
        return int(self.second)

    def getFrame(self):
        return self.frame

    def getFrameAsInt(self):
        return int(self.frame)


#===============================================================================
# 
#===============================================================================
class PhotoScanImage(bbImage):
    """
    PhotoScanImage class - we arent sure of the resolution, so must try and resolve from the meta
    """
    cDATE_TIME_ATTR = 'Photo_DateTimeOriginal'

    def __init__(self, pImagePath):
        super(PhotoScanImage, self).__init__(pImagePath)
        self.populateMeta('Exif.Image.XResolution', 'Exif.Image.YResolution', 'Exif.Image.ResolutionUnit', self.cDTO_EXIF_KEY)
        self.w = self.getSizeFromMeta()[0]
        self.h = self.getSizeFromMeta()[1]
        
    def __cmp__(self, other):
        '''
        compare by original datetime meta from exif header
        '''
        return cmp(self.__dict__.get(self.cDATE_TIME_ATTR), other.__dict__.get(self.cDATE_TIME_ATTR))

    def getSizeFromMeta(self):
        return (self.Image_XResolution, self.Image_YResolution)
    
    def getDateTimeOriginal(self):
        return self.__dict__.get(self.cDATE_TIME_ATTR)


if __name__ == '__main__':
    n = PhotoScanImage('Z:\\AL01_20131010.jpg')
    n1 = PhotoScanImage('Z:\\AL01_20131010.cr2')

    print n1 == n
