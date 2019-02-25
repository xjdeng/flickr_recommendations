try:
    from . import favorites
except ImportError:
    import favorites

from collections import defaultdict

def run(favs = None):
    if favs is None:
        favs = favorites.favorites()
    users = defaultdict(lambda:0)
    for f in favs:
        fans = favorites._exhaustive(f.getFavorites)
        for fan in fans:
            users[fan] += 1
    return users