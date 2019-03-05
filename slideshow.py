from Easy_Image.detect import EasyImageURL, EasyImageList, NotAnImage

from Easy_Image import gui
import random
import copy

def slideshow(favs, rand = True):
    if rand == True:
        favs = copy.copy(favs)
        random.shuffle(favs)
    fl = FlickrImageList(favs)
    gui.slideshow_browser(fl)
    

class FlickrImage(EasyImageURL):
    
    def __init__(self, flickrobj, dimension = "Large"):
        self.dimension = dimension
        self.flickrobj = flickrobj
        self.path = None
        self._img = None
        self.url = None
    
    def getimg(self):
        if self._img is None:
            self.url = self.flickrobj.getSizes()[self.dimension]['source']
        self._img = super(FlickrImage, self).getimg()
        return self._img
    
class FlickrImageList(EasyImageList):   
    def __init__(self, x = []):
        super(FlickrImageList, self).__init__(x)

    def __add__(self, x):
        if isinstance(x, FlickrImageList):
            return FlickrImageList(super(FlickrImageList, self).__add__(x))
    
    def __iadd__(self, x):
        if isinstance(x, FlickrImageList):
            return super(FlickrImageList, self).__iadd__(x)

    def append(self, x):
        if isinstance(x, FlickrImage):
            super(FlickrImageList, self).append(x)
        else:
            try:
                tmp = FlickrImage(x)
                super(FlickrImageList, self).append(tmp)
            except NotAnImage:
                pass

