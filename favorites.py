import flickr_api
import time

def _set_keys(keyfile = "default.key"):
    f = open(keyfile, 'r')
    lines = f.read().split("\n")
    flickr_api.set_keys(api_key = lines[0], api_secret = lines[1])
    f.close()
    return flickr_api
    
def _set_auth(authfile = "default.auth"):
    flickr_api.set_auth_handler(authfile)
    return flickr_api

def _exhaustive(myfunction):
    goahead = False
    while goahead == False:
        try:
            results = myfunction(per_page = 500)
            goahead = True
        except Exception:
            print("Server Error!")
            time.sleep(5)       
    pages = results.info.pages
    for i in range(2, pages+1):
        goahead = False
        while goahead == False:
            try:
                additional = myfunction(per_page = 500, page = i)
                goahead = True
            except Exception as e:
                print("Server Error!: {}".format(e))
                time.sleep(5)
        results += additional
    return results

def favorites(user = None):
    if user is None:
        user = myself()
    return _exhaustive(user.getFavorites)

def myself():
    return flickr_api.test.login()
    
def start(keyfile = "default.key", authfile = "default.auth"):
    _set_keys(keyfile)
    _set_auth(authfile)
    flickr_api.enable_cache()
    return flickr_api

def create_gallery(title, description):
    return flickr_api.Gallery.create(title=title, description=description)

def add_from_favs(favs, iterator, gallery):
    for i in iterator:
        goahead = False
        while goahead == False:
            try:
                gallery.addPhoto(photo_id = favs[i].id)
                goahead = True
            except Exception as e:
                if str(e) == "5 : Failed to add photo":
                    goahead = True
                    print("5 : Failed to add photo")
                else:
                    print("Server Error!: {}".format(e))
                    time.sleep(5)
