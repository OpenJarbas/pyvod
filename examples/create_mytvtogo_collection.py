from pyvod import Collection

MyTV = Collection("MyTvToGo", db_path="mytvtogo.jsondb")


data = {
    "title": "The Brain That Wouldn’t Die",
    "year": 1962,
    "description": "A doctor experimenting with transplant techniques keeps his girlfriend’s head alive when she is decapitated in a car crash, then goes hunting for a new body.",
    "stream": "https://cdn.gideo.video/ea310a66-f080-4840-9dce-4ea0b56618ee"
              "/72ab6b8467dd03ed673dedda7ab9eecd8b67baa2/81bdcdb408149096039a196a0c6b6b695b674735/playlist.m3u8",
    "stars": ["Jason Evers", "Virginia Leith", "Anthony La Penna"],
    "Director": "Joseph Green",
    "tags": ["Horror"],
    "logo": "BRAIN.png",
    "identifier": "mytvtogoBRAIN",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "Manos: The Hands of Fate",
    "year": 1966,
    "description": "A family gets lost on the road and stumbles upon a hidden, underground, devil-worshiping cult led by the fearsome Master and his servant Torgo.",
    "stream": "https://cdn.gideo.video/04b67c0a-dd45-4a7c-9a5d-68d9b22f2fc4/958c763d01e84c30a4c7c3ba29d0934e6994f9b6/f163d191599fc16e22d4c2ce89de277da757909d/playlist.m3u8",
    "stars": ["Tom Neyman", "John Reynolds", "Diane Adelson"],
    "Director": "Harold P. Warren",
    "tags": ["Horror"],
    "logo": "MANOS.png",
    "identifier": "mytvtogoMANOS",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "The Boneyard",
    "year": 1991,
    "description": "Children turned into zombies wreak havoc in a coroner’s building with just a burned-out psychic, an experienced cop and two coroners to stop the madness.",
    "stream": "https://cdn.gideo.video/ee5c00c7-092e-4ab6-be67-3189e890cdaf/ac25f31187685fb8fed7687e307c598e04b55dcb/6a16d287934c55de689c1e8e9c33fe6bd2469652/playlist.m3u8",
    "stars": ["Ed Nelson", "Deborah Rose", "Norman Fell"],
    "Director": "James Cummins",
    "tags": ["Horror"],
    "logo": "BONEYARD.png",
    "identifier": "mytvtogoBONEYARD",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "The Return of Dracula",
    "year": 1958,
    "description": "After a vampire leaves his native Balkans, he murders a Czech artist, assumes his identity, and moves in with the dead man’s American cousins.",
    "stream": "https://cdn.gideo.video/b5e9e444-58ae-44b1-9feb-542f95081b58/c4cd699ef2e4bcad766331b6da64353a72522f9f/dc695685543a83ec2a57f153e3abaab13c044e26/playlist.m3u8",
    "stars": ["Francis Lederer", "Norma Eberhardt", "Ray Stricklyn"],
    "Director": "Paul Landres",
    "tags": ["Horror"],
    "logo": "DRACULA.png",
    "identifier": "mytvtogoDRACULA",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "Night of the Living Dead",
    "year": 1968,
    "description": "A ragtag group of Pennsylvanians barricade themselves in an old farmhouse to remain safe from a bloodthirsty, flesh-eating breed of monsters who are ravaging the East Coast of the United States.",
    "stream": "https://cdn.gideo.video/d04847b1-f87f-4475-bd1a-693249f041ad/176df276e1efd0207561ef3b2fb82edb8138b980/7552dbdec4d3fa3c0f2e8f2ccadd755868325056/playlist.m3u8",
    "stars": ["Duane Jones", "Judith O’Dea", "Karl Hardman"],
    "Director": "George A. Romero",
    "tags": ["Horror"],
    "logo": "DEAD.png",
    "identifier": "mytvtogoDEAD",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "My Dear Secretary",
    "year": 1948,
    "description": "A romance novelist appoints a would-be writer as his secretary. Although she is initially dismayed by his work ethic and playboy attitude, they begin to fall in love.",
    "stream": "https://cdn.gideo.video/d4ebc01f-0ccc-4be5-94aa-54a0bbbd979d/4a13f24116828cddbe88118e63fb59cfdb44ee6a/d8f45aa2a0125b07b6b59750c6f612dddb85379f/playlist.m3u8",
    "stars": ["Laraine Day", "Kirk Douglas", "Keenan Wynn"],
    "Director": "Charles Martin",
    "tags": [],
    "logo": "DEARSECRETARY.png",
    "identifier": "mytvtogoDEARSECRETARY",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "Motel Hell",
    "year": 1980,
    "description": "A seemingly friendly farmer and his sister kidnap unsuspecting travellers and bury them alive, using them to create the “special meat” they are famous for.",
    "stream": "https://cdn.gideo.video/490a799d-2db6-4aa9-a315-ca2e390bc459/428901c55639d9a31de7ddb279e43c639f72ad13/85741e1a31a20791a4e70411270118a906924323/playlist.m3u8",
    "stars": ["Rory Calhoun", "Paul Linke", "Nancy Parsons"],
    "director": "Kevin Connor",
    "tags": ["Horror"],
    "logo": "MOTELHELL.png",
    "identifier": "mytvtogoMOTELHELL",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "House On Haunted Hill",
    "year": 1959,
    "description": "A millionaire offers $10,000 to five people who agree to be locked in a large, spooky, rented house overnight with him and his wife.",
    "stream": "https://cdn.gideo.video/490a799d-2db6-4aa9-a315-ca2e390bc459/428901c55639d9a31de7ddb279e43c639f72ad13/85741e1a31a20791a4e70411270118a906924323/playlist.m3u8",
    "stars": ["Vincent Price", "Carol Ohmart", "Richard Long"],
    "director": "William Castle",
    "tags": ["Horror"],
    "logo": "HOUSEHAUNTEDHILL.png",
    "identifier": "mytvtogoHOUSEHAUNTEDHILL",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "The Little Shop of Horrors",
    "year": 1960,
    "description": "A clumsy young man nurtures a plant and discovers that it’s carnivorous, forcing him to kill to feed it.",
    "stream": "https://cdn.gideo.video/3becfe43-4505-43df-bee0-041fa606d755/1e9980266e7b974d21843a6c5877c5d8062c2a79/d4a35f17a69d04adc217091e129294584a19cfb8/playlist.m3u8",
    "stars": ["Jonathan Haze", "Jackie Joseph", "Mel Welles"],
    "director": "Roger Corman",
    "tags": ["Horror"],
    "logo": "SHOPHORRORS.png",
    "identifier": "mytvtogoSHOPHORRORS",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "The Burning",
    "year": 1981,
     "description": "A former summer camp caretaker, horribly burned from a prank gone wrong, lurks around an upstate New York summer camp bent on killing the teenagers responsible for his disfigurement.",
    "stream": "https://cdn.gideo.video/de4223f5-0a0e-428e-8267-b9299d15d048/hls/v1/playlist.m3u8",
    "stars": ["Brian Matthews", "Leah Ayres", "Brian Backer"],
    "Director": "Tony Maylam",
    "tags": ["Horror"],
    "logo": "BURNING.png",
    "identifier": "mytvtogoBURNING",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "The Time Machine",
    "year": 1960,
    "description": "A man’s vision for a utopian society is disillusioned when travelling forward into time reveals a dark and dangerous society.",
    "stream": "https://cdn.gideo.video/0398b05c-50fc-4f18-8765-f1db848dfd28/hls/v1/playlist.m3u8",
    "stars": ["Rod Taylor", "Alan Young", "Yvette Mimieux"],
    "Director": "George Pal",
    "tags": ["Horror", "SciFi"],
    "logo": "TIMEMACHINE.png",
    "identifier": "mytvtogoTIMEMACHINE",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "The Deadly Companions",
    "year": 1961,
    "description": "An ex-army officer accidentally kills a woman’s son and tries to make up for it by escorting the funeral procession through dangerous Indian territory.",
    "stream": "https://cdn.gideo.video/65bcfb6f-0550-475e-be19-c685450e583c/a789dd9f91a3404a967b823513d6de662ba724bf/6b1f99f832c1c7a2ed3addfcd310794021183f70/playlist.m3u8",
    "stars": ["Maureen O’Hara", "Brian Keith", "Steve Cochran"],
    "director": "Sam Peckinpah",
    "tags": ["Westerns"],
    "logo": "THE_DEADLY_COMPANIONS.png",
    "identifier": "mytvtogoTHE_DEADLY_COMPANIONS",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "McLintock!",
    "year": 1963,
    "description": "Wealthy rancher G.W. McLintock uses his power and influence in the territory to keep the peace between farmers, ranchers, land-grabbers, Indians and corrupt government officials.",
    "stream": "https://cdn.gideo.video/0dbd361e-e153-4f0f-b7cc-1ffba8d0ac91/55b478b1ae238fdafb4b4c1f2f9a8fbb3b4f4dc3/f771cdaf630eaafcf36e3e2749d79a4fdead370c/playlist.m3u8",
    "stars": ["John Wayne", "Maureen O’Hara", "Patrick Wayne"],
    "director": "Andrew V. McLaglen",
    "tags": ["Westerns"],
    "logo": "MC_LINTOCK.png",
    "identifier": "mytvtogoMC_LINTOCK",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

data = {
    "title": "Angel and the Badman",
    "year": 1947,
    "description": "Quirt Evans, an all round bad guy, is nursed back to health and sought after by Penelope Worth, a Quaker girl. He eventually finds himself having to choose between his world and the world Penelope lives in.",
    "stream": "https://cdn.gideo.video/c2c1a4fe-9be4-4021-a34c-0f99640e23f1/6aa2465ef767a1d8944d6eea1722a12326598411/62531e04578742e2ef1df6994de5443139bd29db/playlist.m3u8",
    "stars": ["John Wayne", "Gail Russell", "Harry Carey"],
    "director": "James Edward Grant",
    "tags": ["Westerns"],
    "logo": "ANGEL_AND_THE_BADMAN.png",
    "identifier": "mytvtogoANGEL_AND_THE_BADMAN",
    "collection": ["MyTVToGo"]
}
MyTV.add_movie(data)

MyTV.dump_m3u8("mytvtogoVOD.m3u8")


# TODO drama page https://mytvtogo.net/category/vod-movies/vod-movies-drama/
data = {
    "title": "",
    "year": 1961,
    "description": "",
    "stream": "",
    "stars": [""],
    "director": "",
    "tags": ["Drama"],
    "logo": ".png",
    "identifier": "mytvtogo",
    "collection": ["MyTVToGo"]
}
#MyTV.add_movie(data)

