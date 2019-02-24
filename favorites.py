import flickr_api

def _set_keys(keyfile = "default.key"):
    f = open(keyfile, 'r')
    lines = f.read().split("\n")
    flickr_api.set_keys(api_key = lines[0], api_secret = lines[1])
    f.close()
    return flickr_api
    
def _set_auth(authfile = "default.auth"):
    flickr_api.set_auth_handler(authfile)
    return flickr_api
    
def start(keyfile = "default.key", authfile = "default.auth"):
    _set_keys(keyfile)
    _set_auth(authfile)
    return flickr_api