from pyvod import Collection
from os.path import dirname, join

db = join(dirname(__file__), "sample_collections", "cinemocracy.jsondb")
out = join(dirname(__file__), "m3u8", "Cinemocracy.m3u8")
# NOTE name must match top level key in .jsondb file
# a jsondb can contain more than 1 collection
cinemocracy = Collection("cinemocracy", db_path=db)

m38str = cinemocracy.m3u8

cinemocracy.dump_m3u8(out)

