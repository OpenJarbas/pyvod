from pyvod import Collection

MyTV = Collection("FanSeries", db_path="FanSeries.jsondb")

data = {
    "title": "NEO WAITS FOR THE GHOST TRAIN",
    "year": 2008,
    "description": "",
    "season": 1,
    "episode": 1,
    "episode_title": "Episode 1",
    "stream": "https://www.youtube.com/watch?v=pxRAFtC1s98E",
    "tags": ["Fan Made", "Fan Film", "Matrix", "Short Film"],
    "identifier": "NEO_WAITS_FOR_THE_GHOST_TRAIN",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "NEO WAITS FOR THE GHOST TRAIN",
    "year": 2008,
    "season": 1,
    "episode": 2,
    "episode_title": "Episode 2",
    "description": "",
    "stream": "https://www.youtube.com/watch?v=1tCw45_A53I",
    "tags": ["Fan Made", "Fan Film", "Matrix", "Short Film"],
    "identifier": "NEO_WAITS_FOR_THE_GHOST_TRAIN_2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "NEO WAITS FOR THE GHOST TRAIN",
    "year": 2008,
    "season": 1,
    "episode": 3,
    "episode_title": "Episode 3",
    "description": "",
    "stream": "https://www.youtube.com/watch?v=zXETAXXv7xE",
    "tags": ["Fan Made", "Fan Film", "Matrix", "Short Film"],
    "identifier": "NEO_WAITS_FOR_THE_GHOST_TRAIN_3",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# Robocop
data = {
    "title": "TERMINATOR VS ROBOCOP",
    "year": 2006,
    "season": 1,
    "episode": 1,
    "episode_title": "Episode 1",

    "logo": "https://p1.storage.canalblog.com/15/41/454385/25220372_p.jpg",
    "description": "",
    "stream": "https://www.youtube.com/watch?v=Az8cOVAEwmM",
    "tags": ["Fan Made", "Fan Film", "Robocop", "Terminator", "Short Film",
             "Mashup"],
    "identifier": "TERMINATOR_VS_ROBOCOP",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "TERMINATOR VS ROBOCOP",
    "year": 2008,
    "season": 1,
    "episode": 2,
    "episode_title": "Episode 2",

    "logo": "https://p4.storage.canalblog.com/40/68/454385/25220402_p.jpg",
    "description": "",
    "stream": "https://www.youtube.com/watch?v=Ca-cs0U0aVc",
    "tags": ["Fan Made", "Fan Film", "Robocop", "Terminator", "Short Film",
             "Mashup"],
    "identifier": "TERMINATOR_VS_ROBOCOP2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "TERMINATOR VS ROBOCOP",
    "season": 1,
    "episode": 3,
    "episode_title": "Episode 3",
    "year": 2010,
    "logo": "https://p7.storage.canalblog.com/77/66/454385/25221288_p.jpg",
    "description": "",
    "stream": "https://www.youtube.com/watch?v=ap_u9LcNNhE",
    "tags": ["Fan Made", "Fan Film", "Robocop", "Terminator", "Short Film",
             "Mashup"],
    "identifier": "TERMINATOR_VS_ROBOCOP3",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# Star Trek
# TODO New Voyages https://www.youtube.com/playlist?list=PL5h4ur_aSq8NxKIK0TWk6puXu4E1RjT8y
# https://www.imdb.com/title/tt0458122/?ref_=tt_sims_tt

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 1,
    "episode_title": "Pilgrim of Eternity",

    "description": "Apollo returns to wreak havoc on Kirk and the Enterprise in the first episode of the new series.",
    "stream": "https://vimeo.com/66784863",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode1.jpg",
    "identifier": "STAR_TREK_CONTINUES",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 2,
    "episode_title": "Lolani",
    "description": "A survivor from a distressed Tellarite vessel pulls Captain Kirk and his crew into a moral quandary over her sovereignty.",
    "stream": "https://vimeo.com/86215323",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode2.jpg",
    "identifier": "STAR_TREK_CONTINUES2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 3,
    "episode_title": "FAIREST OF THEM ALL",
    "description": "In the Mirror Universe, Spock faces a choice that determines the future of the Terran Empire.",
    "stream": "https://vimeo.com/98076892",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode3.jpg",
    "identifier": "STAR_TREK_CONTINUES3",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 4,
    "episode_title": "THE WHITE IRIS",
    "description": "Captain Kirk finds himself haunted by guilt from his past as the fate of an alien world hangs in the balance.",
    "stream": "https://vimeo.com/54562820",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode4.jpg",
    "identifier": "STAR_TREK_CONTINUES4",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 5,
    "episode_title": "DIVIDED WE STAND",
    "description": "Kirk and McCoy are trapped in time while an alien infestation threatens the Enterprise.",
    "stream": "https://vimeo.com/139692418",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode5.jpg",
    "identifier": "STAR_TREK_CONTINUES5",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 6,
    "episode_title": "COME NOT BETWEEN THE DRAGONS",
    "description": "A troubled creature pierces the Enterprise hull, pitting the crew against a pursuer that threatens to tear them apart.",
    "stream": "https://vimeo.com/165431813",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode6.jpg",
    "identifier": "STAR_TREK_CONTINUES6",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 7,
    "episode_title": "EMBRACING THE WINDS",
    "description": "While the Enterprise is sent on a seemingly routine mission, Kirk is recalled to starbase where he faces an ethical dilemma that challenges the very core of Starfleet Command.",
    "stream": "https://vimeo.com/178685237",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode7.jpg",
    "identifier": "STAR_TREK_CONTINUES7",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 8,
    "episode_title": "STILL TREADS THE SHADOW",
    "description": "The Enterprise discovers a lost starship… with an "
                   "unlikely passenger.",
    "stream": "https://vimeo.com/210024763",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode8.jpg",
    "identifier": "STAR_TREK_CONTINUES8",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 9,
    "episode_title": "WHAT SHIPS ARE FOR",
    "description": "Kirk struggles with aiding a society whose inhabitants view their isolated world in a very unique way.",
    "stream": "https://vimeo.com/226223868",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode9.jpg",
    "identifier": "STAR_TREK_CONTINUES9",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 10,
    "episode_title": "TO BOLDLY GO (PART 1)",
    "description": "To solve the ultimate mystery, the Enterprise must return to where Kirk’s five-year mission began.",
    "stream": "https://vimeo.com/236207052",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode10.jpg",
    "identifier": "STAR_TREK_CONTINUES10",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Continues",
    "year": 2007,
    "season": 1,
    "episode": 11,
    "episode_title": "TO BOLDLY GO (PART 2)",
    "description": "The iconic mission of the U.S.S. Enterprise comes to an "
                   "end, as Kirk and his crew battle the ultimate adversary",
    "stream": "https://vimeo.com/241107969",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "https://www.startrekcontinues.com/images/episode11.jpg",
    "identifier": "STAR_TREK_CONTINUES11",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Starship Farragut: The Animated Episodes",
    "year": 2009,
    "description": "",
    "stream": "https://youtu.be/h5t5plMXBq8",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek", "Animated"],
    "logo": "",
    "identifier": "STARSHIP_FARRAGUT_ANIMATED",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Starship Farragut",
    "year": 2002,
    "description": "",
    "season": 1,
    "episode": 1,
    "episode_title": "The Captaincy",
    "stream": "https://www.youtube.com/playlist?list=PL6pBipS_gyhtZXxCYTWnG6qFa-A72zmTs",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STARSHIP_FARRAGUT",
    "collection": ["FanFilms"]
}
# TODO handle playlists
# MyTV.add_movie(data)


data = {
    "title": "Starship Farragut",
    "year": 2002,
    "season": 1,
    "episode": 2,
    "episode_title": "For Want of a nail",
    "description": "",
    "stream": "https://youtu.be/GDeE01J1jy4",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STARSHIP_FARRAGUT2",
    "collection": ["FanFilms"]
}
# TODO official url, fix date
MyTV.add_movie(data)

data = {
    "title": "Starship Farragut",
    "year": 2002,
    "season": 1,
    "episode": 3,
    "episode_title": "Just passing through",
    "description": "",
    "stream": "https://www.youtube.com/watch?v=YKI26MaRN4E",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STARSHIP_FARRAGUT3",
    "collection": ["FanFilms"]
}
# TODO official url, fix date
MyTV.add_movie(data)

data = {
    "title": "Starship Farragut",
    "year": 2008,
    "season": 1,
    "episode": 4,
    "episode_title": "a rock and a hard place",
    "description": "",
    "streams": ["https://youtu.be/d1f6Jjhxl2Q",
                "https://youtu.be/OyDfxmEjvrM"],
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STARSHIP_FARRAGUT4",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Starship Farragut",
    "year": 2012,
    "season": 1,
    "episode": 5,
    "episode_title": "a rock and a hard place",
    "description": "THE PRICE OF ANYTHING",
    "stream": "https://www.youtube.com/watch?v=jJKQ1FHQc68",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STARSHIP_FARRAGUT5",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Starship Farragut",
    "year": 2014,
    "season": 1,
    "episode": 6,
    "episode_title": "CONSPIRACY OF INNOCENCE",
    "description": "",
    "stream": "https://youtu.be/VInpQHwnrrk",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STARSHIP_FARRAGUT6",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Starship Farragut",
    "year": 2016,
    "season": 1,
    "episode": 7,
    "episode_title": "the crossing",
    "description": "",
    "stream": "https://youtu.be/-ZpVMDJrT20",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STARSHIP_FARRAGUT7",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Starship Exeter",
    "year": 2002,
    "season": 1,
    "episode": 1,
    "episode_title": "The Savage Empire",
    "description": "On a mission of peace, the Starship Exeter is drawn into a battle of political intrigue and espionage. Who will survive? Can even Captain Garrovick's own crew be trusted?",
    "stream": "https://www.youtube.com/watch?v=G2re3s0kQgM",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STARSHIP_EXETER",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Starship Exeter",
    "year": 2014,
    "season": 1,
    "episode": 2,
    "episode_title": "The Tressaurian Intersection",
    "description": "Searching for a starship in distress, the crew of the Starship U.S.S. Exeter finds a destroyed starbase and a deepening mystery. Has an enemy species from Captain Garrovick's past invented the ultimate weapon, or is the truth even stranger and more deadly?",
    "stream": "https://www.youtube.com/watch?v=jkuJG1_2MnU",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STARSHIP_EXETER2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# Alien
data = {
    "title": "Alien: Covenant The Unofficial Animated Series",
    "year": 2017,
    "season": 1,
    "episode": 1,
    "episode_title": "LV-223",
    "description": "",
    "streams": [
        "https://youtu.be/SZesg-dTnJY"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIEN_COVENANT_ANIMATED",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Covenant The Unofficial Animated Series",
    "year": 2017,
    "season": 1,
    "episode": 2,
    "episode_title": "Infection",
    "description": "",
    "streams": [
        "https://youtu.be/IMO514lW0FQ"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIEN_COVENANT_ANIMATED_2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "ALIEN: Analects The Animated Series",
    "year": 2019,
    "season": 1,
    "episode": 1,
    "episode_title": "Episode 1",
    "description": "",
    "streams": [
        "https://youtu.be/S38zKIhUv60"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIEN_ANALECTS",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "ALIEN: Analects The Animated Series",
    "year": 2019,
    "season": 1,
    "episode": 2,
    "episode_title": "Episode 2",
    "description": "",
    "streams": [
        "https://youtu.be/ahuTFdJLRnI"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIEN_ANALECTS2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Awakening Animated",
    "year": 2017,
    "season": 1,
    "episode": 1,
    "episode_title": "The Seeds of Deception and Uprising",
    "description": "",
    "streams": [
        "https://youtu.be/OEJCOCf-lX8"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIEN_AWAKENING",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Awakening Animated",
    "year": 2018,
    "season": 1,
    "episode": 2,
    "episode_title": "Fall of the Old Gods",
    "description": "",
    "streams": [
        "https://youtu.be/mDb7bv03Rc8"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIEN_AWAKENING2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Awakening Animated ",
    "year": 2018,
    "season": 1,
    "episode": 3,
    "episode_title": "Wrath of the Subjugated",
    "description": "",
    "streams": [
        "https://youtu.be/gS7xmp1JguQ"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIEN_AWAKENING3",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Awakening Animated",
    "year": 2018,
    "season": 1,
    "episode": 4,
    "episode_title": "The Trickster and the Fools",
    "description": "",
    "streams": [
        "https://youtu.be/zJBCODCKpp8"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIEN_AWAKENING4",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Awakening Animated",
    "year": 2019,
    "season": 1,
    "episode": 5,
    "episode_title": "Lamb to the Slaughter",
    "description": "",
    "streams": [
        "https://youtu.be/-prvD9RLf-U"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIEN_AWAKENING5",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Awakening Animated",
    "year": 2020,
    "season": 1,
    "episode": 6,
    "episode_title": "Cycle of Inevitable Annihilation",
    "description": "",
    "streams": [
        "https://youtu.be/LmjF6YKe0fk"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIEN_AWAKENING6",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

MyTV.dump_m3u8("FanSeriesVOD.m3u8")
