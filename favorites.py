import flickr_api
from flickr_api.api import flickr

def _set_keys(keyfile = "default.key"):
    f = open(keyfile, 'r')
    lines = f.read().split("\n")
    flickr_api.set_keys(api_key = lines[0], api_secret = lines[1])
    f.close()
    return flickr_api
    
def _set_auth(authfile = "default.auth"):
    flickr_api.set_auth_handler(authfile)
    return flickr_api

def myself():
    return flickr_api.test.login()
    
def start(keyfile = "default.key", authfile = "default.auth"):
    _set_keys(keyfile)
    _set_auth(authfile)
    flickr_api.enable_cache()
    return flickr_api,flickr

def favorites():
    me = myself()
    favs = me.getFavorites(per_page = 500)
    newfavs = favs
    i = 1
    while len(newfavs) != 0:
        i += 1
        newfavs = me.getFavorites(per_page = 500, page = i)
        favs += newfavs
    return favs