from pyvod.collections import SciFiHorror, MyTVToGo

n = SciFiHorror.total_movies  # 461
print("\nSciFiHorror\n")
print("Total Movies:", n)

for ch in SciFiHorror.movies:
    # streams are tested when using ch.streams,
    # this can be slow,
    # streams need to be extracted live for some urls (youtube)
    # use ch.movie_data["streams"] instead for direct access to original urls

    print(ch.name, ch.streams)
    """
    Dead Men Walk [https://archive.org/download/DeadMenWalk/DeadMenWalk.mpeg, https://archive.org/download/DeadMenWalk/DeadMenWalk.ogv]
    Dead People [https://archive.org/download/Dead_People_movie/Dead_People.mpeg, https://archive.org/download/Dead_People_movie/Dead_People.ogv, https://archive.org/download/Dead_People_movie/Dead_People_512kb.mp4]
    Deep Red [https://archive.org/download/DeepRed1975/DeepRed.ogv, https://archive.org/download/DeepRed1975/DeepRed_512kb.mp4]
    Deep Red 256 K Stream [https://archive.org/download/DeepRed256K/DeepReda.ogv, https://archive.org/download/DeepRed256K/DeepReda_512kb.mp4]
    Dementia 13 (1963) [https://archive.org/download/Dementia131963/Dementia-13.ogv, https://archive.org/download/Dementia131963/Dementia-13_512kb.mp4]
    """


n = MyTVToGo.total_movies  # 461
print("\nMyTVToGo\n")
print("Total Movies:", n)

for ch in MyTVToGo.movies:
    # streams are tested when using ch.streams,
    # this can be slow,
    # streams need to be extracted live for some urls (youtube)
    # use ch.movie_data["streams"] instead for direct access to original urls

    print(ch.name, ch.streams)
    """
    Dead Men Walk [https://archive.org/download/DeadMenWalk/DeadMenWalk.mpeg, https://archive.org/download/DeadMenWalk/DeadMenWalk.ogv]
    Dead People [https://archive.org/download/Dead_People_movie/Dead_People.mpeg, https://archive.org/download/Dead_People_movie/Dead_People.ogv, https://archive.org/download/Dead_People_movie/Dead_People_512kb.mp4]
    Deep Red [https://archive.org/download/DeepRed1975/DeepRed.ogv, https://archive.org/download/DeepRed1975/DeepRed_512kb.mp4]
    Deep Red 256 K Stream [https://archive.org/download/DeepRed256K/DeepReda.ogv, https://archive.org/download/DeepRed256K/DeepReda_512kb.mp4]
    Dementia 13 (1963) [https://archive.org/download/Dementia131963/Dementia-13.ogv, https://archive.org/download/Dementia131963/Dementia-13_512kb.mp4]
    """
