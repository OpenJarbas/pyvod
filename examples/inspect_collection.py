from pyvod import Collection
from os.path import dirname, join

db = join(dirname(__file__), "sample_collections", "scifi_horror.jsondb")
# NOTE name must match top level key in .jsondb file
# a jsondb can contain more than 1 collection
SciFiHorror = Collection("SciFi_Horror", db_path=db)

n = SciFiHorror.total_entries  # 461
print("\nSciFiHorror\n")
print("Total Movies:", n)

for ch in SciFiHorror.entries:
    # streams are tested when using ch.streams,
    # this can be slow,
    # streams need to be extracted live for some urls (youtube)
    # use ch.movie_data["streams"] instead for direct access to original urls

    print(ch.name, ch.streams[0])
    """
    The Ghost Train https://archive.org/download/TheGhostTrain/TheGhostTrain.ogv
    The Ghoul https://archive.org/download/TheGhoul/TheGhoul_1933.ogv
    THE GIANT OF METROPOLIS (1961) https://archive.org/download/TheGiantOfMetropolis1961/GiantOfMetropolisversionUs.ogv
    The Golem https://archive.org/download/TheGolem_893/TheGolem.ogv
    The Hands of Orlac (1924) https://archive.org/download/TheHandsOfOrlac1924/Orlacs.Hande.1924.Wiene.ogv
    The Incredible Petrified World https://archive.org/download/TheIncrediblePetrifiedWorld/TheIncrediblePetrifiedWorld.mpeg
    Invisible Ghost https://archive.org/download/TheInvisibleGhost/TheInvisibleGhost.mpeg
    The Little Shop Of Horrors - Weirdness Bad movie https://archive.org/download/TheLittleShopOfHorrors-WeirdnessBadMovie/WRMB_mp4_LittleShop.ogv
    The Little Shop of Horrors (1960) https://archive.org/download/TheLittleShopOfHorrors1960/The-Little-Shop-of-Horrors.ogv
    The Little Shop of Horrors (1960) https://archive.org/download/TheLittleShopOfHorrors1960_765/TheLittleShopOfHorrors1960.ogv
    The Lost World https://archive.org/download/TheLostWorld_207/TheLostWorld.ogv
    The Man Who Saved The World (Turkish Star Wars) 1982 https://archive.org/download/TheManWhoSavedTheWorldturkishStarWars1982/TurkishLionmanCompressed-desktop.ogv
    """


