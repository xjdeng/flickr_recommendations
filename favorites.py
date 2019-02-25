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

def _exhaustive(myfunction):
    results = myfunction(per_page = 500)
    new = results
    i = 1
    while len(new) != 0:
        i += 1
        new = myfunction(per_page = 500, page = i)
        results += new
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
    return flickr_api,flickr
