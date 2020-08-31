from pyvod.collections import MovieTrailers, FeatureFilmsPicfixer, FeatureFilms

query = "grindhouse"

print("Searching Feature Films Picfixer for: ", query, "\n")
for movie, score in FeatureFilmsPicfixer.search(query):
    print(movie.name, score)

print("\nSearching Feature Films for: ", query, "\n")
for movie, score in FeatureFilms.search(query):
    print(movie.name, score)
    print(movie.data["tags"])

query = "Frankenstein"
print("\nSearching Movie Trailers for: ", query, "\n")
for movie, score in MovieTrailers.search(query):
    print(movie.name, score)