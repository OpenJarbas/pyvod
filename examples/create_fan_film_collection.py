from pyvod import Collection

MyTV = Collection("FanFilms", db_path="fanfilms.jsondb")

# Judge Dredd
data = {
    "title": "Judge Minty",
    "year": 2013,
    "description": "Judge William Minty has spent his entire adult life "
                   "policing the violent streets of Mega-City One - and now "
                   "he's slowing down. When a lapse of judgement almost ends"
                   " his life, he knows that it's time to quit. He can"
                   " choose to teach in the Academy, or he can leave the city "
                   "and walk alone out into the anarchy of the Cursed Earth,"
                   " taking law to the lawless.",
    "stream": "https://youtu.be/aavS_XUITXU",
    "tags": ["Fan Made", "Fan Film", "Judge Dredd"],
    "logo": "https://m.media-amazon.com/images/M/MV5BMjMxMDU2MjExOV5BMl5BanBnXkFtZTcwNDgyMjA1OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "identifier": "JUDGE_MINTY",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# Star Wars
data = {
    "title": "Hoshino - Star Wars ",
    "year": 2016,
    "description": "The tale of blind Jedi Master Ko Hoshino and her journey to becoming one with the Force.",
    "stream": "https://www.youtube.com/watch?v=G7-n36MBs1A",
    "tags": ["Fan Made", "Fan Film", "Star Wars"],
    "logo": "",
    "identifier": "STAR_WARS_HOSHINO",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "TIE Fighter Star Wars Anime",
    "year": 2017,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=E9GRYa_3gno",
    "tags": ["Fan Made", "Fan Film", "Star Wars", "Short Film", "Animated"],
    "logo": "",
    "identifier": "STAR_WARS_TIE_FIGHTER",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "DARTH MAUL: Apprentice",
    "year": 2016,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=Djo_91jN3Pk",
    "tags": ["Fan Made", "Fan Film", "Star Wars", "Short Film"],
    "logo": "",
    "identifier": "STAR_WARS_DARTH_MAUL",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Wars Exile",
    "year": 2016,
    "description": "Jedi around the galaxy are being viciously hunted and killed by the evil Galactic Empire. Aware of the imminent danger, Jedi Master Boemana Tora and her Padawan Makal Lori, flee to the outer rim systems close to the planet of Lothal.",
    "stream": "https://www.youtube.com/watch?v=v-6ae6tMHb0",
    "tags": ["Fan Made", "Fan Film", "Star Wars", "Short Film"],
    "logo": "",
    "identifier": "STAR_WARS_EXILE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "TK-436: A Stormtrooper Story",
    "year": 2016,
    "description": "TK-436: A Stormtrooper Story, the gritty tale of a loyal Imperial Stormtrooper who is forced to confront his past in the heat of an epic battle. Directors Samtubia & Samgoma Edwards imagined it from a perspective that is seldom explored within the Star Wars universe.",
    "stream": "https://www.youtube.com/watch?v=2GdEXQ6Ulw8",
    "tags": ["Fan Made", "Fan Film", "Star Wars"],
    "logo": "",
    "identifier": "STAR_WARS_TK436",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Wars The Lesser Evil",
    "year": 2015,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=vgaeH6hAICU",
    "tags": ["Fan Made", "Fan Film", "Star Wars"],
    "logo": "",
    "identifier": "STAR_WARS_THE_LESSER_EVIL",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "VADER EPISODE 1: SHARDS OF THE PAST",
    "year": 2018,
    "description": "For eight months, the mysterious Darth Vader has enforced the Emperor's commands. Fighting between the loss of Padme, and the new cursed life he now leads, Vader must do what must be done when a surviving Jedi Master from Order 66 has lured him to the home planet of his late Wife's tomb...",
    "stream": "https://www.youtube.com/watch?v=Ey68aMOV9gc",
    "tags": ["Fan Made", "Fan Film", "Star Wars"],
    "logo": "",
    "identifier": "VADER",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# Star Trek
data = {
    "title": "Star Trek: Deception",
    "year": 2013,
    "description": "two Starfleet officers aboard a Danube Class Runabout, transporting a Klingon prisoner to a detention centre, only to be ambushed by a Klingon Bird of Prey that had been lying in wait.",
    "stream": "https://youtu.be/ALGLRd5RyA4",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "",
    "identifier": "STAR_TREK_DECEPTION",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)


data = {
    "title": "Star Trek: Deception 2",
    "year": 2018,
    "description": "After attaching a tracking device to their Klingon prisoner and setting up an elaborate deception to allow to him to escape, the crew of the USS Longshanks, a Federation Excelsior class starship, are led straight to the main staging point for Klingon raiding attacks that have been plaguing the system recently. With the mission to find the Klingons responsible and, if necessary, eliminate them...",
    "stream": "https://youtu.be/jZQqzMC2HXs",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "",
    "identifier": "STAR_TREK_DECEPTION2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)


data = {
    "title": "Star Trek TNG: A Tale of Two Cities",
    "year": 2013,
    "description": "Starring Giles Ashton (of Star Trek: Intrepid fame), this special edition fan film was originally made as an XXX parody. All porn scenes have been removed and new opening credits have been added to create a proper new TNG episode!",
    "stream": "https://youtu.be/NzDIACP8nf8",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "",
    "identifier": "STAR_TREK_2CITIES",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Last Survivor",
    "year": 2018,
    "description": "An away team must investigate a destroyed ship, a missing crew, and the mysterious Aliens at the center of it all in a place where time, space, and thought converge. The final movie in a very unlikely trilogy that began with Star Trek: Survivor (2010)",
    "stream": "https://youtu.be/hfCLuYuUhDk",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "",
    "identifier": "STAR_TREK_LAST_SURVIVOR",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Survivors: A Star Trek Fan Production",
    "year": 2017,
    "description": "After an attack leaves their ship destroyed, a Captain with a dark secret and his familiar Vulcan officer take their chances on the planet below as hostile aliens hunt them down. ",
    "stream": "https://youtu.be/hSS0W99RVxc",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "",
    "identifier": "STAR_TREK_SURVIVORS",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Survivor",
    "year": 2010,
    "description": "A battle with the Romulans leaves a Commander stranded on a desolate planet where he may not be alone...This is an original Star Trek fan film made for the fun of it with a literal zero budget, making use of spectacular locations at Vasquez Rocks and Mojave Desert. We wanted it to be grittier than previous Star Trek fan projects with a focus on how someone would actually survive on a completely inhospitable planet and to explore the dark side of Vulcan logic.",
    "stream": "https://youtu.be/v60Uh3ugqv4",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "",
    "identifier": "STAR_TREK_SURVIVOR",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek Renegades",
    "year": 2007,
    "description": "",
    "stream": "https://youtu.be/eE2Wgop9VLM",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "http://renegades.show/home/media/NewLogoWithSeries2.png",
    "identifier": "STAR_TREK_RENEGADES",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

MyTV.add_movie(data)

data = {
    "title": "Star Trek: Of Gods and Men",
    "year": 2007,
    "description": "It is the year 2306. Thirteen years have passed since Captain James T. Kirk was swept away by the Nexus, after saving the crew of the USS Enterprise-B. The remaining crew members of the original USS Enterprise have gone their separate ways. Captain Nyota Uhura and Captain Pavel Chekov, along with Captain John Harriman of the Enterprise-B, come together for a special dedication in honor of Kirk's Enterprise. Their reunion is cut short when they receive a distress call from a mysterious planet, that presses the three friends to embark on a mission that will change their lives forever.",
    "stream": "https://www.youtube.com/watch?v=kFqAME7dx58",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "",
    "identifier": "STAR_TREK_OF_GODS_AND_MEN",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek: Prelude to Axanar",
    "year": 2014,
    "description": "Various retired leaders discuss their experiences of the Four Years War, a war between the Federation and the Klingons, and the build up to a battle at Axanar that caused a major turning point in the war. ",
    "stream": "https://www.youtube.com/watch?v=1W1_8IV8uhA",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "",
    "identifier": "STAR_TREK_AXANAR",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek: Horizon",
    "year": 2016,
    "description": "The Coalition of Planets, a young alliance of worlds led by Earth, is at war with the Romulan Empire. Desperate for a chance to gain the upper hand in the war, the Coalition forms an alliance with T'mar, a Romulan deserter, in the hopes that she can provide valuable intelligence on her former masters.",
    "stream": "https://www.youtube.com/watch?v=l94v4YOqxOc",
    "tags": ["Fan Made", "Fan Film", "Star Trek"],
    "logo": "",
    "identifier": "STAR_TREK_HORIZON",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Star Trek: Phoenix  Cloak & Dagger",
    "year": 2010,
    "description": "After their diplomatic envoy crashes on the remote planet of Katrassii Prime, Captain Avari and the crew of the U.S.S. Phoenix embark on a dangerous mission to rescue them. Upon arrival in the Neutral Zone, the rescue team faces a labyrinth of mysteries while their true enemy lurks in the shadows. The crew of the Phoenix will sail into the unknown as the architect of their destruction leads them back to the beginning of their maiden voyage.",
    "stream": "https://youtu.be/YWAGSwEqkxI",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STAR_TREK_PHOENIX",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Starship Republic  Serpent of Yesterday",
    "year": 2017,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=X1gvy_kewM4",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Star Trek"],
    "logo": "",
    "identifier": "STARSHIP_REPUBLIC",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# Lord of the rings
data = {
    "title": "Halifirien",
    "year": 2009,
    "description": " A Lord of the Rings fan film set during the War of the ring in the third age. Follows the story of the beacon wardens on the Halifirien as they defend the mountain from marauding orc bands. ",
    "stream": "https://youtu.be/coRcO9dh7I8",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Lord of the Rings"],
    "logo": "https://m.media-amazon.com/images/M/MV5BY2ZlN2MyYmUtNDM4Zi00NWJiLTgzYWUtMzlkYWI0ODExOGI4XkEyXkFqcGdeQXVyMzYzNzc1NjY@._V1_.jpg",
    "identifier": "LOTR_HALIFIRIEN",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "The Ranger",
    "year": 2017,
    "description": "",
    "stream": "https://youtu.be/qIr4egz9kVI",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Lord of the Rings"],
    "logo": "",
    "identifier": "LOTR_RANGER",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Beren & Lùthien",
    "year": 2013,
    "description": "Court métrage fan film tiré de l'histoire de Beren & Lùthien du Silmarillion de J.R.R.Tolkien.",
    "stream": "https://youtu.be/DxTQuqvfhZM",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Lord of the Rings"],
    "logo": "",
    "identifier": "BEREN_LUTHIEN",
    "collection": ["FanFilms"],
    "lang": "fr"
}
MyTV.add_movie(data)

data = {
    "title": "In the Forest of Tom Bombadil",
    "year": 2013,
    "description": "After the four hobbits; Merry, Pippin, Frodo and Sam leave the Shire for Bree, they encounter some trouble with a Willow Tree, only to be rescued by the mysterious yet whimsical character, Tom Bombadil. As the hobbits linger in Bombadil's hollow, danger lurks outside the Old Forest, and Frodo begins to question secrets the One Ring may hold. When morning dawns again the hobbits must face an important question; Who is Tom Bombadil?",
    "stream": "https://youtu.be/i95mdzDuTvc",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Lord of the Rings"],
    "logo": "",
    "identifier": "IN_THE_FOREST_OF_TOM_BOMBADIL",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "The Hunt For Gollum",
    "year": 2009,
    "description": "The acclaimed fan-produced prequel film based on Appendices in The Lord of the Rings and dramatising Aragorn & Gandalf's search for Gollum. The Hunt for Gollum is a non-profit, serious homage to the writing of J.R.R Tolkien and the films of Peter Jackson. Directed by British filmmaker Chris Bouchard, shot on location in England and Wales. Produced by a small army of Tolkien fans and independent filmmakers.",
    "stream": "https://www.youtube.com/watch?v=uZWuxEwqYzM",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Lord of the Rings"],
    "logo": "https://upload.wikimedia.org/wikipedia/en/a/a7/Huntforgollumposter1.jpg",
    "identifier": "THE_HUNT_FOR_GOLLUM",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Born of Hope",
    "year": 2009,
    "description": "Born of Hope: The Ring of Barahir is a 2009 fantasy-adventure fan film directed by Kate Madison and written by Paula DiSante (as Alex K. Aldridge) based on the appendices of J. R. R. Tolkien's The Lord of the Rings. The film centres on the communities affected by Sauron's war[2]; the Dúnedain bloodline; and the story of Arathorn II and his relationship with Gilraen as they would be the parents of Aragorn, who became a key leader against Sauron.",
    "stream": "https://www.youtube.com/watch?v=qINwCRM8acM",
    "tags": ["Fan Made", "Fan Film", "Lord of the Rings"],
    "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/9/90/Poster_boh_ring.jpg/220px-Poster_boh_ring.jpg",
    "identifier": "BORN_OF_HOPE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# AMDS films
data = {
    "title": "THE FIGHT OF THE UNIVERSE",
    "year": 2009,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=8LJD0RZzBjQ",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Mashup", "Matrix"],
    "identifier": "THE_FIGHT_OF_THE_UNIVERSE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "THE FIGHT OF THE UNIVERSE 2",
    "year": 2009,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=cS8onUX6bc0",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Mashup", "Robocop",
             "Terminator", "Matrix", "Star wars"],
    "identifier": "THE_FIGHT_OF_THE_UNIVERSE_2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "ARNOLD SCHWARZENEGGER VS SYLVESTER STALLONE",
    "year": 2015,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=fz0pYhAy36o",
    "tags": ["Fan Made", "Fan Film", "Short Film", "Mashup"],
    "identifier": "ARNOLD_SCHWARZENEGGER_VS_SYLVESTER_STALLONE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "STAR WARS  BATTLE OF THE DARK SIDE",
    "year": 2017,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=4pgdeHI0GvY",
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Star Wars",
             "Mashup"],
    "identifier": "ALIEN_STAR_WARS",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)


data = {
    "title": "RISE OF THE BOOGEYMEN  SLASHER MASHUP",
    "year": 2006,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=uBH4VDX6xq4",
    "tags": ["Fan Made", "Fan Film", "Friday the 13th", "Horror", "Short Film",
             "Mashup"],
    "identifier": "RISE_OF_THE_BOOGEYMEN_SLASHER_MASHUP",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# Batman
data = {
    "title": "BATMAN DEAD END",
    "year": 2003,
    "description": "Batman: Dead End is a fan film written and directed by Sandy Collora that premiered July 19, 2003 at the San Diego Comic-Con, and on the internet shortly thereafter. The film crosses over the DC Comics superhero Batman with the Alien and Predator science fiction film franchises. ",
    "mirrors": [
        "https://www.youtube.com/watch?v=3j7d3lIAkes",
        "https://www.youtube.com/watch?v=5XjIH8Y5wWI",
        "https://www.youtube.com/watch?v=RbS9p_Ci_lw",
        "https://www.youtube.com/watch?v=cKxL2GnGFrw"
    ],
    "stream": "https://www.youtube.com/watch?v=pGO6gZJbTwE",
    "tags": ["Fan Made", "Fan Film", "Predator", "Short Film", "Batman"],
    "logo": "https://www.avpgalaxy.net/wordpress/wp-content/uploads/2006/12/Batman_DeadEnd.jpg",
    "identifier": "BATMAN_DEAD_END",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# Alien
data = {
    "title": "Aliens Unleashed",
    "year": 2020,
    "description": "Aliens Unleashed Volume 1: Set 20 years after Aliens, after Hadley's Hope, Ripley has vanished with no sign of her, Newt has grown up and got a job on a new colony thanks to Hicks, who is retired from the Marines. The Aliens have not been seen in years, but the company, Weyland-Yutani has dug up the Derelict ship from Alien, which was buried by the Hadley's Hope explosion, and they brought the Aliens to the same planet Newt and Hicks are now living. The Aliens have escaped and taken over the colony, Newt must take charge and lead the colonists to safety or they will suffer the same fate as Hadley's Hope.",
    "stream": "https://www.youtube.com/watch?v=i3Z6FURkhaM",
    "tags": ["Fan Made", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIENS_UNLEASHED",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Aliens Apocalypse",
    "year": 2020,
    "description": "Aliens Apocalypse Volume 2: Months after Part 1, Newt is back on Earth and she and her friends have been blacklisted by the company and are just trying to get by. Little do they know, Wey-Yu has been breeding Aliens in secret, and with animals creating Alien crossbreeds (based on the Kenner toys of course). The Aliens have gotten lose and for the past few months have been lurking and breeding underground. Now they're time has come and they have conquered the planet like a zombie apocalypse. Newt and her friends are trying to survive, when they find a rescue team who taking them somewhere safe, but they must avoid Aliens and Wey-Yu's Alien crossbreeds.",
    "stream": "https://www.youtube.com/watch?v=2nVUU8EkgGw",
    "tags": ["Fan Made", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIENS_APOCALYPSE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Aliens Vengeance",
    "year": 2020,
    "description": "Aliens Vengeance Volume 3: After escaping Earth in Part 2, Newt and her friends have awakened on a Wey-Yu space station and find it crawling with Aliens. But that's not all they find, Ripley has returned and joined their fight for survival. Our heroes and the survivors must escape the space station and finish the Aliens and Wey-Yu once and for all. This is their final stand, and not all of them will survive it.",
    "stream": "https://www.youtube.com/watch?v=vTccDWNjnLk",
    "tags": ["Fan Made", "Alien", "Short Film", "Animated"],
    "logo": "",
    "identifier": "ALIENS_VENGEANCE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: The Hybrid",
    "year": 2017,
    "description": "The crew of the Harbinger, a freighter spaceship "
                   "intercepted a distress transmission from the remote planet of Origin-6 The signal came from a young woman called Eve. Eve has offered a reward to gather and information on the mysterious disappearance of the crew of the Covenant. The crew of the Harbinger will discover some rewards have a price.",
    "stream": "https://youtu.be/zm0RUf6kuy0",
    "tags": ["Fan Made", "Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_HYBRID",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Isolation",
    "year": 2015,
    "description": "",
    "stream": "https://youtu.be/y9NP5Q3lq8k",
    "tags": ["Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_ISOLATION",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Containment",
    "year": 2019,
    "description": "Four survivors find themselves stranded aboard a small escape pod in deep space. Trying to piece together the details around the outbreak that led to their ship’s destruction, they find themselves unsure to trust whether or not one of them might be infected.",
    "stream": "https://www.youtube.com/watch?v=oputwvJRPz0",
    "tags": ["Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_CONTAINMENT",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Specimen",
    "year": 2019,
    "description": "It’s the night shift in a colony greenhouse, and Julie, a botanist, does her best to contain suspicious soil samples that have triggered her sensitive lab dog. Despite her best efforts the lab unexpectedly goes into full shutdown and she is trapped inside. Little does she know, an alien specimen has escaped the mysterious cargo, and a game of cat and mouse ensues as the creature searches for a host.",
    "stream": "https://youtu.be/dYAHOZ_91A0",
    "tags": ["Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_SPECIMEN",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Night Shift",
    "year": 2019,
    "description": "When a missing space trucker is discovered hungover and disoriented, his co-worker suggests a nightcap as a remedy. Near closing time, they are reluctantly allowed inside the colony supply depot where the trucker’s condition worsens, leaving a young supply worker alone to take matters into her own hands.",
    "stream": "https://youtu.be/lZnDnK3YLsI",
    "tags": ["Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_NIGHTSHIFT",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Ore",
    "year": 2019,
    "description": "As a hard-working miner of a planet mining colony, Lorraine longs to make a better life for her daughter and grandchildren. When her shift uncovers the death of a fellow miner under mysterious circumstances, Lorraine is forced to choose between escape or defying management orders and facing her fears to fight for the safety of her family.",
    "stream": "https://youtu.be/BUMsMaVhnQs?list=PLdZugR0wc7bM3KbeVySz4Xv2QuFKQFGXD",
    "tags": ["Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_ORE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Harvest",
    "year": 2019,
    "description": "The surviving crew of a damaged deep-space harvester have minutes to reach the emergency evacuation shuttle. A motion sensor is their only navigation tool leading them to safety while a creature in the shadows terrorizes the crew. However, the greatest threat might have been hiding in plain sight all along.  ",
    "stream": "https://youtu.be/Q0tIu7zvQcw",
    "tags": ["Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_HARVEST",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Alone",
    "year": 2019,
    "description": "Hope, an abandoned crew member aboard the derelict chemical hauler Otranto, has spent a year trying to keep her ship and herself alive as both slowly fall apart. After discovering hidden cargo, she risks it all to power up the broken ship in search of human life.",
    "stream": "https://youtu.be/ApNPbQxMFtk",
    "tags": ["Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_ALONE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien 5",
    "year": 1998,
    "description": '“ALIEN 5 was our first action-figure-movie, made in 1998 with just a camcorder and lots of home-made special effects! Honestly, it’s kinda primitive compared to our later work, but it’s still fun!”',
    "stream": "https://youtu.be/dFQcEHLCqL8",
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Toy"],
    "logo": "https://www.avpgalaxy.net/images/films/fanfilms/alien507.jpg",
    "identifier": "ALIEN5",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien 5²",
    "year": 2004,
    "description": "The sequel to Probot Productions’ ALIEN 5. Made with action figures and innovative special effects. This time, Ripley’s worst fears have come true and the Aliens have gotten loose on Earth!",
    "stream": "https://youtu.be/Evt82UqJk5s",
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "Toy"],
    "logo": "https://www.avpgalaxy.net/images/films/fanfilms/alien5squared07.jpg",
    "identifier": "ALIEN5_2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Aliens: Epilogue",
    "year": 2012,
    "description": "The events in Aliens: Epilogue take place between Aliens and Alien 3 and it appears Weyland-Yutani have been experimenting with some Alien Eggs at a bio-weapons facility. A rogue team infiltrates the facility and causes the Xenomorphs to escape. A team of Colonial Marines is dispatched to investigate the site.",
    "stream":
        "https://www.avpgalaxy.net/files/other/fanfilm_aliensepilogue.mp4",
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIENS_EPILOGUE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "LV-426",
    "year": 2014,
    "description": 'The fan film is loosely based around James Cameron’s Aliens and is about an adult Newt returning to LV-426 10 years after the events in Aliens. She finds a damaged Bishop android and asks him what happened. The short film is from Brazilian filmmaker Márcio Napoli and it’s in Portuguese with English subtitles.',
    "stream": "https://youtu.be/aliscTnlsvg",
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_LV426",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Special Order",
    "year": 2017,
    "description": '“Bring back life form. Priority One. All other priorities rescinded.”',
    "stream": "https://youtu.be/QAwvGWVkZcs",
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film"],
    "logo": "https://www.avpgalaxy.net/wordpress/wp-content/uploads/2017/12/special-01.jpg",
    "identifier": "ALIEN_SPECIAL_ORDER",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: The Adora Files",
    "year": 2015,
    "description": "Tyran is the leading company of an alliance called The Union which also includes Seegson as a partner, so Seegson and Tyran are working close together to defeat Weyland-Yutani. The ship on which all hell is breaking lose is called the U.S.S. Adora — a Union space ship that belongs to Tyran Industries — where the crew is fighting/losing against some aliens — but where the aliens are from is a secret right now.",
    "stream": "https://www.youtube.com/watch?v=jT7vI8MBCxQ",
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film"],
    "logo": "https://www.avpgalaxy.net/wordpress/wp-content/uploads/2015/04/alien-adora-file-poster.png",
    "identifier": "ALIEN_ADORA_FILES",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Colonial Marines: Elite Force",
    "year": 2003,
    "description": "The Crew of the USS Aurian have been called upon to investigate the sudden loss of contact on LV429. A secret Medical Research and Developement Facility deep in the Beta Fora system. Details are sketchy at best. However, if the crew have been called, then something is seriously wrong on the planet.",
    "stream": "https://vimeo.com/16435805",
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "CGI", "Animated"],
    "logo": "https://www.avpgalaxy.net/images/films/fanfilms/eliteforce/eliteforce01.jpg",
    "identifier": "ALIENS_ELITE_FORCE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: INFINITY",
    "year": 2015,
    "description": "",
    "stream": "https://youtu.be/heEWPLCaTOc",
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film", "CGI", "Animated"],
    "logo": "",
    "identifier": "ALIENS_INFINITY",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: CONTINUUM",
    "year": 2017,
    "description": "",
    "stream": "https://youtu.be/KLdWNaSFjYo",
    "tags": ["Fan Made", "Fan Film", "Alien", "CGI", "Animated"],
    "logo": "",
    "identifier": "ALIENS_CONTINUUM",
    "collection": ["FanFilms"]
}
# TODO its not about alien, maybe put it in another collection
# MyTV.add_movie(data)

data = {
    "title": "Alien: The Last Survivor",
    "year": 2013,
    "description": "Ridley Scott's Alien remade: In 2012 we produced this "
                   "shortfilm for the International Shortfilm Festival Hamburg. The task was to do a 3-minute remake of another film. We decided to stick to the scariest, darkest and - in my opinion - best sci-fi-movie ever made: ALIEN by Ridley Scott. And so we remade the last scene of the film, in which Ripley seems to be safe from the xenomorph, but suddenly finds herself face to face with the ALIEN. ",
    "stream": "https://youtu.be/a2emA8OusWo",
    "tags": ["Fan Made", "Fan Film", "Alien"],
    "logo": "",
    "identifier": "ALIEN_LAST_SURVIVOR",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: The Message",
    "year": 2020,
    "description": "",
    "stream": "https://youtu.be/NLmsaJzo-zs",
    "tags": ["Fan Made", "Fan Film", "Alien", "CGI", "Animated"],
    "logo": "",
    "identifier": "ALIEN_MESSAGE",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: SUPREMACY",
    "year": 2017,
    "description": "",
    "stream": "https://youtu.be/zpAD0kI4fm8",
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_SUPREMACY",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Alien: Infestation",
    "year": 2016,
    "description": "",
    "streams": [
        "https://youtu.be/kAEOBDrYuiE",
        "https://youtu.be/kGTFsfu0w-o"
    ],
    "tags": ["Fan Made", "Fan Film", "Alien", "Short Film"],
    "logo": "",
    "identifier": "ALIEN_INFESTATION",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# Alien vs Predator
data = {
    "title": "Aliens VS Predator S E E D",
    "year": 2006,
    "description": "In 1947, Roswell New Mexico was the scene of what most believe to be a UFO crash zone, but this site like many others were quickly covered up and shrouded in secrecy by an unknown non-government organization. Many years later, the massive and powerful Yutani Corporation is investing billions in new space program development and the organization of a highly trained Special Ops team to protect their secret interests. Rumors surrounding their mysterious investments speak of the ultimate weapon that would allow the military to dominate any opposition.",
    "stream": "https://youtu.be/kQlS7Yaf5dA",
    "tags": ["Fan Made", "Fan Film", "Predator", "Alien", "Alien vs Predator"],
    "logo": "https://www.avpgalaxy.net/wordpress/wp-content/uploads/2006/12/seed_poster_1.jpg.w560h700.jpg",
    "identifier": "AVP_SEED",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "AVP Redemption",
    "year": 2010,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=nAu8gD1j5tk&t=741s",
    "tags": ["Fan Made", "Fan Film", "Predator", "Alien",
             "Alien vs Predator", "Short Film"],
    "logo": "https://www.avpgalaxy.net/wordpress/wp-content/uploads/2008/03/normal_avpr_poster1.jpg",
    "identifier": "AVP_REDEMPTION",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

# Predator
data = {
    "title": "zatoichi vs predator",
    "year": 2017,
    "description": "This fan-made samurai short film, appropriately titled ZVP: Zatoichi vs Predator, clashes together the samurai and sci-fi genre. The short intends to stand as the nexus for 50th and 20th anniversaries of the death of Zatoichi creator and actor Kan Shimozawa and Shintaro Katsu, respectively, and the 30th anniversary of the The Predator movie.",
    "stream": "https://youtu.be/NsbVTPftcgs",
    "tags": ["Samurai", "Ninja", "Predator", "Short Film"],
    "logo": "https://geekculture.co/wp-content/uploads/2018/01/This-Zatoichi-vs-Predator-Fan-Movie-Should-Be-An-Actual-Film-5-886x500.jpg",
    "identifier": "ZVP",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "PREDATOR: The Prey and the Hunt",
    "year": 2017,
    "description": "In the federal laboratories facilities artifacts from an archaeological site are stolen by Sp. Sheppard (Marcelo Naves) head of security. The director of the laboratory Dra Heather (Lilian Morais) and the Ten. J. Whitaker (W Jr.) spot the theft and try to stop it. The real possessor of the pieces, Hunter, appears the same night to retrieve his objects. The hunt is on.",
    "stream": "https://youtu.be/scOJDthHj_c",
    "tags": ["Fan Made", "Fan Film", "Predator"],
    "logo": "",
    "identifier": "PREDATOR_THE_PREY_AND_THE_HUNT",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "PREDATOR: The Harvest",
    "year": 2004,
    "description": "Heading to a cabin for a nice weekend getaway, two young couples find themselves stranded on a country road with no help in sight. As the couples decide to go for help their nice weekend getaway takes a turn for the worse. Now they must fight their own fears and come together in a hopeless struggle against a deadly nightmare (a Bad-Blood Predator), hell-bent on stockpiling as many victims as it can on the start of it’s grizzly, ritual harvest.",
    "stream": "https://www.avpgalaxy.net/files/other/fanfilm_the_harvest.mp4",
    "tags": ["Fan Made", "Fan Film", "Predator", "Short Film"],
    "logo": "https://www.avpgalaxy.net/images/films/fanfilms/predatorharvest/harvest01.jpg",
    "identifier": "PREDATOR_HARVEST",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Wolverine vs. Predator",
    "year": 2013,
    "description": "Wolverine vs. Predator isn’t strictly a fan film but was made for the Super Power Beat Down web series which pits movie/comic characters against each other",
    "stream": "https://youtu.be/s3wDj7bYve0",
    "tags": ["Wolverine", "Predator", "Short Film"],
    "logo": "https://www.avpgalaxy.net/wordpress/wp-content/uploads/2015/05/wolverine1.jpg",
    "identifier": "WOLVERINE_VS_PREDATOR",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Predator: Celtic Days",
    "year": 2018,
    "description": "XVIII c. Ireland. Father is searching for his son, who run away from home.  During his journey he's finding out more then he anticipated and of course he's faced with our good old friend „Creachadóir“(that's Predator in gaelic). Is it the same one that will give Lieutenant Mike Harrigan (Danny Glover) the pistol? You just have to watch this movie.",
    "stream": "https://youtu.be/jxi_RX9TK1M",
    "tags": ["Fan Made", "Fan Film", "Predator", "Short Film"],
    "logo": "",
    "identifier": "PREDATOR_CELTIC",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "THE CREATURE FROM THE BIG MOUNTAIN",
    "year": 2018,
    "description": "During the WW2, a father and his daughter are pursued by a group of German Soldiers. They sink into the nearly forest, but very fast the group of soldiers sent to get them back are confronted to a creature which decimate them one by one...",
    "stream": "https://www.youtube.com/watch?v=dFbGV9UNSPw",
    "tags": ["Fan Made", "Fan Film", "Predator", "Short Film"],
    "logo": "",
    "identifier": "THE_CREATURE_FROM_THE_BIG_MOUNTAIN",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "THE CREATURE FROM THE BIG MOUNTAIN (NEW VERSION)",
    "year": 2019,
    "description": "During the WW2, a father and his daughter are pursued by a group of German Soldiers. They sink into the nearly forest, but very fast the group of soldiers sent to get them back are confronted to a creature which decimate them one by one...",
    "stream": "https://www.youtube.com/watch?v=iqdsOwQxl_M",
    "tags": ["Fan Made", "Fan Film", "Predator", "Short Film"],
    "logo": "",
    "identifier": "THE_CREATURE_FROM_THE_BIG_MOUNTAIN_2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "PREDATOR: DARK AGES",
    "year": 2015,
    "description": "Set during the Crusades, the faith & fighting skills of a group of Templar Knights is put to the test when they encounter the Predator. Their battle is the thing Myths and Legends are born from.",
    "stream": "https://www.youtube.com/watch?v=YRD8jAk274I",
    "tags": ["Fan Made", "Fan Film", "Predator", "Short Film"],
    "logo": "",
    "identifier": "PREDATOR_DARK_AGES",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "WARRIOR : PREDATOR",
    "year": 2019,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=YZBh2BW9CMs",
    "tags": ["Fan Made", "Fan Film", "Predator", "Short Film"],
    "logo": "",
    "identifier": "WARRIOR_PREDATOR",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "PREDATOR: Final Stand",
    "year": 2015,
    "description": "When two aircraft mysteriously go missing, a team is deployed to find them only to discover that they are being hunted by something they've never encountered before.",
    "stream": "https://www.youtube.com/watch?v=gVAMtYwQUZg",
    "tags": ["Fan Made", "Fan Film", "Predator", "Short Film"],
    "logo": "",
    "identifier": "PREDATOR_FINAL_STAND",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "PREDATOR: 2019",
    "year": 2019,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=R4yIYlObBKs",
    "tags": ["Fan Made", "Fan Film", "Predator", "Short Film"],
    "logo": "",
    "identifier": "PREDATOR_SHORT_2019",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

data = {
    "title": "Predator in WW2",
    "year": 2013,
    "description": "",
    "stream": "https://www.youtube.com/watch?v=dFbGV9UNSPw",
    "tags": ["Fan Made", "Fan Film", "Predator", "Short Film"],
    "logo": "",
    "identifier": "PREDATOR_WW2",
    "collection": ["FanFilms"]
}
MyTV.add_movie(data)

MyTV.dump_m3u8("FanFilmsVOD.m3u8")