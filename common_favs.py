try:
    from . import favorites
except ImportError:
    import favorites

from collections import defaultdict
import pandas as pd

def run(favs = None, verbose = False):
    if favs is None:
        favs = favorites.favorites()
    users = defaultdict(lambda:0)
    for i,f in enumerate(favs):
        fans = favorites._exhaustive(f.getFavorites)
        n = len(favs)
        if verbose == True:
            print("Trying {} of {}".format(i, n))
        for fan in fans:
            users[fan.username] += 1
    return users

def to_pd(in_dict):
    index = list(in_dict.keys())
    values = [in_dict[i] for i in index]
    return pd.Series(values, index = index)