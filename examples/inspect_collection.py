from pyvod.collections import SciFiHorror, MyTVToGo

n = MyTVToGo.total_movies  # 14
print("\nMyTVToGo\n")
print("Total Movies:", n)

for ch in MyTVToGo.movies:

    print(ch.name, ch.streams[0])
    """
    the brain that wouldn’t die https://cdn.gideo.video/ea310a66-f080-4840-9dce-4ea0b56618ee/72ab6b8467dd03ed673dedda7ab9eecd8b67baa2/81bdcdb408149096039a196a0c6b6b695b674735/playlist.m3u8
    angel and the badman https://cdn.gideo.video/c2c1a4fe-9be4-4021-a34c-0f99640e23f1/6aa2465ef767a1d8944d6eea1722a12326598411/62531e04578742e2ef1df6994de5443139bd29db/playlist.m3u8
    the deadly companions https://cdn.gideo.video/65bcfb6f-0550-475e-be19-c685450e583c/a789dd9f91a3404a967b823513d6de662ba724bf/6b1f99f832c1c7a2ed3addfcd310794021183f70/playlist.m3u8
    manos: the hands of fate https://cdn.gideo.video/04b67c0a-dd45-4a7c-9a5d-68d9b22f2fc4/958c763d01e84c30a4c7c3ba29d0934e6994f9b6/f163d191599fc16e22d4c2ce89de277da757909d/playlist.m3u8
    motel hell https://cdn.gideo.video/490a799d-2db6-4aa9-a315-ca2e390bc459/428901c55639d9a31de7ddb279e43c639f72ad13/85741e1a31a20791a4e70411270118a906924323/playlist.m3u8
    my dear secretary https://cdn.gideo.video/d4ebc01f-0ccc-4be5-94aa-54a0bbbd979d/4a13f24116828cddbe88118e63fb59cfdb44ee6a/d8f45aa2a0125b07b6b59750c6f612dddb85379f/playlist.m3u8
    the boneyard https://cdn.gideo.video/ee5c00c7-092e-4ab6-be67-3189e890cdaf/ac25f31187685fb8fed7687e307c598e04b55dcb/6a16d287934c55de689c1e8e9c33fe6bd2469652/playlist.m3u8
    house on haunted hill https://cdn.gideo.video/490a799d-2db6-4aa9-a315-ca2e390bc459/428901c55639d9a31de7ddb279e43c639f72ad13/85741e1a31a20791a4e70411270118a906924323/playlist.m3u8
    the return of dracula https://cdn.gideo.video/b5e9e444-58ae-44b1-9feb-542f95081b58/c4cd699ef2e4bcad766331b6da64353a72522f9f/dc695685543a83ec2a57f153e3abaab13c044e26/playlist.m3u8
    mclintock! https://cdn.gideo.video/0dbd361e-e153-4f0f-b7cc-1ffba8d0ac91/55b478b1ae238fdafb4b4c1f2f9a8fbb3b4f4dc3/f771cdaf630eaafcf36e3e2749d79a4fdead370c/playlist.m3u8
    the little shop of horrors https://cdn.gideo.video/3becfe43-4505-43df-bee0-041fa606d755/1e9980266e7b974d21843a6c5877c5d8062c2a79/d4a35f17a69d04adc217091e129294584a19cfb8/playlist.m3u8
    the burning https://cdn.gideo.video/de4223f5-0a0e-428e-8267-b9299d15d048/hls/v1/playlist.m3u8
    night of the living dead https://cdn.gideo.video/d04847b1-f87f-4475-bd1a-693249f041ad/176df276e1efd0207561ef3b2fb82edb8138b980/7552dbdec4d3fa3c0f2e8f2ccadd755868325056/playlist.m3u8
    the time machine https://cdn.gideo.video/0398b05c-50fc-4f18-8765-f1db848dfd28/hls/v1/playlist.m3u8
    """


n = SciFiHorror.total_movies  # 461
print("\nSciFiHorror\n")
print("Total Movies:", n)

for ch in SciFiHorror.movies:
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


