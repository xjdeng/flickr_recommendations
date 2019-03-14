from Easy_Image.detect import EasyImageURL, EasyImageList, NotAnImage
try:
    import favorites
except ImportError:
    from . import favorites
from Easy_Image import gui
import random
import copy, time

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

favorites.start()

def load_list(filename):
    """
Loads a Flickr Image List from file
    """
    f = open(filename, 'r')
    ids = f.read().split("\n")
    fil = FlickrImageList()
    for i in ids:
        fi = FlickrImage(favorites.flickr_api.Photo(id = i))
        fil.append(fi)
    return fil

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
        self.flickrobj.getSizes()
        goahead = False
        while goahead == False:
            try:
                if self._img is None:
                    self.url = self.flickrobj.getSizes()[self.dimension]['source']
                self._img = super(FlickrImage, self).getimg()
                goahead = True
            except KeyError:
                self.dimension = 'Original'
            except Exception as e:
                print(e)
                time.sleep(1)
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
    
    def save(self, filename):
        """
Save a Flickr Image List to file
        """
        ids = [f.flickrobj.id for f in self]
        f = open(filename,'w')
        f.write("\n".join(ids))
        f.close()
