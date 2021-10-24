from pathlib import Path

import orjson

TEST_CONTAINER_SRC_DIR_PATH = Path("/code/tests/functional/testdata/")

with open(TEST_CONTAINER_SRC_DIR_PATH / "films_list.json", encoding="utf-8") as file:
    LIST_FILMS_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "film_details.json", encoding="utf-8") as file:
    FILM_DETAILS_ES_RESPONSE = orjson.loads(file.read())

EXPECTED_LIST_FILMS_RESPONSE = [
    {
        "id": "a801e84c-316a-4c0c-a5a5-cc024234b2cb",
        "rating": 6.5,
        "title": "Kre-O Star Trek",
        "description": "A stop-motion animated story about 'Star Trek' featuring Kre-O toy blocks.",
        "genres": [
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
            {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
        ],
        "directors": [],
        "actors": [],
        "writers": [],
        "actors_names": [],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "a88cbbeb-b998-4ca6-aeff-501463dcdaa0",
        "rating": 9,
        "title": "Cory in the House: All Star Edition",
        "description": "",
        "genres": [
            {"id": "55c723c1-6d90-4a04-a44b-e9792040251a", "name": "Family"},
            {"id": "9c91a5b2-eb70-4889-8581-ebe427370edd", "name": "Musical"},
        ],
        "directors": [],
        "actors": [
            {"id": "1db6d260-e8dd-46e9-b610-6609dcf04231", "name": "Jason Dolley"},
            {"id": "7ae6bfd2-3fab-4b8a-9e08-f2c901bf1869", "name": "Lisa Arch"},
            {"id": "99cb58d0-4b03-46ce-b581-d9d9887a97c2", "name": "Lori Alan"},
            {"id": "9cefe2b3-cf3c-4c3f-be22-554604cd6146", "name": "John D'Aquino"},
        ],
        "writers": [],
        "actors_names": ["Jason Dolley", "John D'Aquino", "Lisa Arch", "Lori Alan"],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "a8f6bd5b-036a-4d79-b952-3c7b5aa3ea83",
        "rating": 7.4,
        "title": "Star Wars: Hoshino",
        "description": "The tale of blind Jedi Master Ko Hoshino and her path to becoming one with the force.",
        "genres": [
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
            {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
            {"id": "b92ef010-5e4c-4fd0-99d6-41b6456272cd", "name": "Fantasy"},
        ],
        "directors": [
            {"id": "627e1bee-5589-421e-bcaa-d20c25557117", "name": "Stephen Vitale"}
        ],
        "actors": [
            {"id": "54da121d-5c9a-4852-815c-5b9b646d2fb1", "name": "Eric Carrasco"},
            {"id": "b167d72b-64da-4550-a170-52f17a3e5b9b", "name": "Anna Akana"},
            {"id": "e83bc9cf-206b-4e4c-aa8e-0e6c9a681fc4", "name": "Tim McKernan"},
            {"id": "f27d0d48-5895-46f1-8eae-4405152be83f", "name": "Patrick Sullivan"},
        ],
        "writers": [
            {"id": "54da121d-5c9a-4852-815c-5b9b646d2fb1", "name": "Eric Carrasco"},
            {"id": "a5a8f573-3cee-4ccc-8a2b-91cb9f55250a", "name": "George Lucas"},
        ],
        "actors_names": [
            "Anna Akana",
            "Eric Carrasco",
            "Patrick Sullivan",
            "Tim McKernan",
        ],
        "writers_names": ["Eric Carrasco", "George Lucas"],
        "directors_names": ["Stephen Vitale"],
    },
    {
        "id": "a99bbda2-d244-4b38-b32c-761248fb0bf2",
        "rating": 6,
        "title": "Star Trek: Starships",
        "description": "A look at the re-design of the starship Enterprise.",
        "genres": [
            {"id": "6d141ad2-d407-4252-bda4-95590aaf062a", "name": "Documentary"},
            {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
        ],
        "directors": [],
        "actors": [
            {"id": "959d148c-022b-427f-a68b-bbe58674fe65", "name": "Eric Bana"},
            {"id": "967a13ac-a6e5-4f0d-8f66-e8fc55827d83", "name": "Bruce Greenwood"},
            {"id": "a1758395-9578-41af-88b8-3f9456e6d938", "name": "J.J. Abrams"},
            {"id": "f89a9bad-5bd3-446d-bbdf-e1fd0d217e5d", "name": "John Cho"},
        ],
        "writers": [
            {"id": "6d1b08e4-62a0-43c7-9e6e-640f876649ce", "name": "M. David Melvin"}
        ],
        "actors_names": ["Bruce Greenwood", "Eric Bana", "J.J. Abrams", "John Cho"],
        "writers_names": ["M. David Melvin"],
        "directors_names": [],
    },
    {
        "id": "a99d6476-4b05-467d-a612-b7ebbec900dc",
        "rating": 5.9,
        "title": "The Muppets All-Star Comedy Gala",
        "description": "",
        "genres": [{"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"}],
        "directors": [],
        "actors": [
            {"id": "2af5ed7b-138c-4bfb-931f-c376e5be73f4", "name": "Eric Jacobson"},
            {"id": "8776732e-91a2-4066-a871-614bbac57b12", "name": "David Rudman"},
            {"id": "9e013e0a-dc00-4d61-8ca3-788649f7e015", "name": "Dave Goelz"},
            {"id": "d2723114-44d3-45af-9b87-8b39553904b5", "name": "Steve Whitmire"},
        ],
        "writers": [
            {"id": "be814de6-7f17-4b7c-8130-a23977e335cd", "name": "Mark Critch"},
            {"id": "f37054a9-8ede-44ac-b9ca-871c7cf7193f", "name": "Dean Jenkinson"},
            {"id": "f58b9c52-3029-47a6-9dfb-02fa9c6238f0", "name": "Tim McAuliffe"},
        ],
        "actors_names": [
            "Dave Goelz",
            "David Rudman",
            "Eric Jacobson",
            "Steve Whitmire",
        ],
        "writers_names": ["Dean Jenkinson", "Mark Critch", "Tim McAuliffe"],
        "directors_names": [],
    },
    {
        "id": "a9b57067-b910-47b8-bb83-3169429c84e1",
        "rating": 7.5,
        "title": "All Star Comedy Jam",
        "description": "The Original King of Comedy and Shaquille O'Neal presents this Stand-Up Special with some of the industry's most talented and sought after comedians.",
        "genres": [
            {"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"},
            {"id": "6d141ad2-d407-4252-bda4-95590aaf062a", "name": "Documentary"},
        ],
        "directors": [
            {"id": "f09c267a-1a38-46c2-8b1a-35721b96ec34", "name": "Leslie Small"}
        ],
        "actors": [
            {"id": "22dbe9c3-cb14-4a1e-b6a9-47f9b76867c8", "name": "Tommy Davidson"},
            {
                "id": "272b3940-e37e-492a-9530-81848ed3a863",
                "name": "Cedric the Entertainer",
            },
            {"id": "474a88b6-110e-4a49-91b7-66839b9ebeaf", "name": "Kevin Hart"},
            {"id": "edc4f8f2-32a0-409d-9de2-4c34cbf1ae7d", "name": "DeRay Davis"},
        ],
        "writers": [],
        "actors_names": [
            "Cedric the Entertainer",
            "DeRay Davis",
            "Kevin Hart",
            "Tommy Davidson",
        ],
        "writers_names": [],
        "directors_names": ["Leslie Small"],
    },
    {
        "id": "a9bbc1d8-bb8a-41d2-b61a-d8ddc9b31ede",
        "rating": 1.8,
        "title": "Amy Winehouse: Fallen Star",
        "description": "A biography on the life of Amy Winehouse.",
        "genres": [{"id": "ca124c76-9760-4406-bfa0-409b1e38d200", "name": "Biography"}],
        "directors": [
            {"id": "bcacce93-0190-47b9-8350-68a463ac99f8", "name": "Jason Boritz"}
        ],
        "actors": [
            {"id": "0f8c8862-70bd-4651-80a8-882a8ba2ca04", "name": "Julia Eringer"},
            {"id": "18faf5f6-2fc1-4f72-b47e-5e6bb31b2209", "name": "Josh Mann"},
            {"id": "45605628-64c2-4a57-a1ff-ec9e3158f1da", "name": "Alain Azoulay"},
            {"id": "712cad1d-96a7-45f0-986f-c80c030c6536", "name": "Sarah Rochelle"},
        ],
        "writers": [
            {"id": "7d2a54c4-7817-4ae0-807f-1c9256c93d92", "name": "Rose Berkman"}
        ],
        "actors_names": [
            "Alain Azoulay",
            "Josh Mann",
            "Julia Eringer",
            "Sarah Rochelle",
        ],
        "writers_names": ["Rose Berkman"],
        "directors_names": ["Jason Boritz"],
    },
    {
        "id": "a9d52337-3249-49ae-92b8-65ee9ebaf359",
        "rating": 8,
        "title": "Star Wars Rebels",
        "description": "An animated TV series set between the events of Episode III and IV, Star Wars Rebels takes place in a time where the Empire is securing its grip on the galaxy and hunting down the last of the Jedi Knights as a fledgling rebellion against the Empire is taking shape.",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "55c723c1-6d90-4a04-a44b-e9792040251a", "name": "Family"},
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
            {"id": "b92ef010-5e4c-4fd0-99d6-41b6456272cd", "name": "Fantasy"},
            {"id": "ca88141b-a6b4-450d-bbc3-efa940e4953f", "name": "Mystery"},
        ],
        "directors": [],
        "actors": [
            {"id": "11819966-b9d1-494d-bafa-9033ddbe3ab4", "name": "Taylor Gray"},
            {"id": "32f131ef-cd32-4659-a037-bcff3f12ac0c", "name": "Dave Filoni"},
            {
                "id": "57a4f809-225e-4a8a-a867-0537a085d6c4",
                "name": "Freddie Prinze Jr.",
            },
            {"id": "8026ef16-24cf-43a3-be5b-20609a5265ba", "name": "Vanessa Marshall"},
        ],
        "writers": [
            {"id": "32f131ef-cd32-4659-a037-bcff3f12ac0c", "name": "Dave Filoni"},
            {"id": "6ba834a0-1039-4b5c-ab78-d5f1f18a4e7d", "name": "Carrie Beck"},
            {"id": "a6d0f7e6-450c-4a16-8b9f-1a6d9a1ce837", "name": "Simon Kinberg"},
        ],
        "actors_names": [
            "Dave Filoni",
            "Freddie Prinze Jr.",
            "Taylor Gray",
            "Vanessa Marshall",
        ],
        "writers_names": ["Carrie Beck", "Dave Filoni", "Simon Kinberg"],
        "directors_names": [],
    },
    {
        "id": "a9ee0b3f-ec56-4107-9b6d-0458dfa3f415",
        "rating": 7,
        "title": "Star Trek: Short Treks",
        "description": "A series of stand-alone short films featuring characters and storylines from Star Trek: Discovery (2017).",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
            {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
        ],
        "directors": [],
        "actors": [
            {"id": "165f52f9-48bf-47b8-b14e-0b81079d1ba9", "name": "Ethan Peck"},
            {"id": "1d565221-1e6d-4bb1-b82a-b8d70d258c88", "name": "Rebecca Romijn"},
            {"id": "87a32a48-fdaa-4b6d-bd0d-ee4edfaec18d", "name": "Anson Mount"},
            {"id": "cd3765d7-a725-47a6-b602-02da78259f4b", "name": "Jenette Goldstein"},
        ],
        "writers": [
            {"id": "772faacb-5d57-4e72-b44f-01fde7f08c1a", "name": "Akiva Goldsman"},
            {"id": "82b7dffe-6254-4598-b6ef-5be747193946", "name": "Alex Kurtzman"},
            {"id": "8a9cb7b2-dd61-4f7f-94ec-61aac18ed5d9", "name": "Kirsten Beyer"},
            {"id": "b670fa3e-9f7b-4786-a00c-09d95f1e7b5c", "name": "Bryan Fuller"},
            {"id": "c5affe3b-e9f2-4fdb-a5ee-018dd751d3f4", "name": "Michael Chabon"},
        ],
        "actors_names": [
            "Anson Mount",
            "Ethan Peck",
            "Jenette Goldstein",
            "Rebecca Romijn",
        ],
        "writers_names": [
            "Akiva Goldsman",
            "Alex Kurtzman",
            "Bryan Fuller",
            "Kirsten Beyer",
            "Michael Chabon",
        ],
        "directors_names": [],
    },
    {
        "id": "aa00b2ae-86b4-43e9-9032-f0ea4c12697a",
        "rating": 7.2,
        "title": "The Stories: The Making of 'Rogue One: A Star Wars Story'",
        "description": "Divided 10 segments: A Rogue Idea: A recount of John Knoll's idea and pitch for the film, looking at the early days of production, hiring Gareth Edwards to direct, Edwards' love for the series, and building a collection of characters. Jyn: The Rebel: A closer look at the film's main protagonist: personality, character history and what separates her from other protagonists from the Star Wars universe, physical preparations for the shoot, and more. Cassian: The Spy: Much the same as the previous supplement in terms of introducing the character and his history, the qualities the character brings to the story, and casting Diego Luna. K-2SO: The Droid: A look at the robotic character: his \"anti C-3PO personality,\" character design, Alan Tudyk's motion capture performance, and the humor the actor brought to the set. Baze and Chirrut: Guardians of the Whills: The actors discuss landing and accepting the roles, the characters' camaraderie, individual character details, faith and the force in the movie and the Star Wars universe, and the actors' physical performances. Bodhi and Saw: The Pilot and The Revolutionary: The piece begins with Riz Ahmed's auditions and crafting the character, the character's fate, and making key sequences. It moves on to examine Forest Whitaker's character and his history in the Star Wars universe, character definition and history, Whitaker's preparations for the role, and more. The Empire: A run through of key Imperial characters, including Galen Erso, Orson Krennic, Grand Moff Tarkin, and Darth Vader and the qualities (and in Vader's case, the presence) their actors brought to their roles. Visions of Hope: The Look of Rogue One: Designing a world that's true and familiar to the Star Wars universe but still unique to the film. It explores set construction, small design changes, and the black stormtroopers. The Princess and The Governor: Digitally recreating two important characters. Epilogue: The Story Continues (1080p, 4:15): Images from the film's premiere juxtaposed against fans talking up the film and the franchise. The piece ends with a selection of clips from the film.",
        "genres": [
            {"id": "6d141ad2-d407-4252-bda4-95590aaf062a", "name": "Documentary"}
        ],
        "directors": [
            {
                "id": "92a9f4f9-254f-41ff-b53e-b0b4c1a165a2",
                "name": "Ian Bucknole(co-director)",
            },
            {"id": "a0749409-274e-46b4-9419-7d150de71957", "name": "Glen Milner"},
        ],
        "actors": [
            {"id": "5bd4381f-5763-474f-baa0-f7f62a0819f9", "name": "John Knoll"},
            {"id": "5dd7d75e-2b21-4391-893e-f96da598ee37", "name": "Kiri Hart"},
            {"id": "b8dfac63-90a0-4eda-ae13-a25cbd46af82", "name": "Doug Chiang"},
            {"id": "e9f382c9-77ee-48d9-b402-089d283b2428", "name": "Kathleen Kennedy"},
        ],
        "writers": [],
        "actors_names": ["Doug Chiang", "John Knoll", "Kathleen Kennedy", "Kiri Hart"],
        "writers_names": [],
        "directors_names": ["Glen Milner", "Ian Bucknole(co-director)"],
    },
    {
        "id": "aa5aea7a-cd65-4aec-963f-98375b370717",
        "rating": 8.1,
        "title": "The Young Person's Guide to Becoming a Rock Star",
        "description": "An up-and-coming Glasgow based rock band are faced the harsh realities of the music industry on their journey to becoming the next big thing.",
        "genres": [{"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"}],
        "directors": [],
        "actors": [
            {"id": "4b3dcdbf-22f1-4bb3-b912-25cebef857df", "name": "Keith Allen"},
            {"id": "4db91bc9-a3f0-449d-8afd-94fda9641da8", "name": "Gerard Butler"},
            {"id": "d468ef8b-61bb-4959-93e6-f5f3f338b6eb", "name": "Ciarán McMenamin"},
            {"id": "f219c59c-fcb2-4aab-b40e-9d28cf969a63", "name": "Simone Lahbib"},
        ],
        "writers": [],
        "actors_names": [
            "Ciarán McMenamin",
            "Gerard Butler",
            "Keith Allen",
            "Simone Lahbib",
        ],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "aa78103d-9ef7-4668-aefa-aeadafc2613b",
        "rating": 6.1,
        "title": "Billion Star Hotel",
        "description": "Every day, we're faced with the following exercise: to give the world around us a certain cue. To smile, to take everything as a joke, to laugh out loud, or to allow ourselves to be overwhelmed by reality. To be painfully aware of the distance between us and our dreams, of the obstacles, and the fact that we are alone all the time. Some choose to escape, to build their own world, with it's own rules, with the memories of fairy tales and dreams that really come to be. A world where three friends are brought together by the same destination. Or maybe, it all comes down to daydreaming. And feeling the empty spaces with music. It all depends on how you choose to see things. In black, in white, or in sync with the beat. Billion Star Hotel, for each viewer, a different story.",
        "genres": [{"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"}],
        "directors": [
            {"id": "d5f561a9-f317-43c2-b08e-23ad01336239", "name": "Alecs Nastoiu"}
        ],
        "actors": [
            {"id": "5f516028-4a22-4357-9ddf-72d3f07a2d06", "name": "Nicu Mihoc"},
            {"id": "8ca506fe-593c-4abc-bd0e-f995441e0c4c", "name": "Rudy Moca"},
            {"id": "b2fd2bbf-c962-46aa-9bf2-f04b9d7a9cd9", "name": "Theo Marton"},
            {"id": "f57aab36-9115-47c5-8eba-2e5114c32f47", "name": "Dan Radulescu"},
        ],
        "writers": [
            {"id": "5438c6dd-8754-483f-99d8-51e4e7973cde", "name": "Alexandra Pater"},
            {"id": "d5f561a9-f317-43c2-b08e-23ad01336239", "name": "Alecs Nastoiu"},
        ],
        "actors_names": ["Dan Radulescu", "Nicu Mihoc", "Rudy Moca", "Theo Marton"],
        "writers_names": ["Alecs Nastoiu", "Alexandra Pater"],
        "directors_names": ["Alecs Nastoiu"],
    },
    {
        "id": "aa7ed707-ef80-43af-9f7f-c4a9f8af9436",
        "rating": 8.3,
        "title": "Michael Stahl-David: Behind the Star",
        "description": "Michael Stahl-David, star of the film Cloverfield, may have smashed box office records but that has not changed him. He's still the down-to-earth normal guy he always was.",
        "genres": [{"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"}],
        "directors": [],
        "actors": [
            {"id": "09d67d34-44d6-42cc-a472-d8d67868f844", "name": "Chris Chalk"},
            {"id": "15de37f5-1317-4f7b-aa6e-fb9b089151af", "name": "Devin Sanchez"},
            {"id": "86986bdb-88e4-4f95-930e-eaccefd016da", "name": "Jeremy Beiler"},
            {
                "id": "d4e3b41e-7761-433a-a5ea-d8bda9eab1a5",
                "name": "Michael Stahl-David",
            },
        ],
        "writers": [],
        "actors_names": [
            "Chris Chalk",
            "Devin Sanchez",
            "Jeremy Beiler",
            "Michael Stahl-David",
        ],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "aa90ffe4-6fc2-4cb9-b984-0cd169aedcd9",
        "rating": 7.2,
        "title": "Lego Star Wars: The Padawan Menace",
        "description": "Ian,a young boy,Commander Cody and Yoda must go to rescue the secret battle plans.However,when substitute teacher C-3PO and a class of padawans go too,things become more complicated....",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"},
            {"id": "55c723c1-6d90-4a04-a44b-e9792040251a", "name": "Family"},
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
            {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
            {"id": "b92ef010-5e4c-4fd0-99d6-41b6456272cd", "name": "Fantasy"},
        ],
        "directors": [
            {"id": "b721075f-2ef0-4774-b362-9c110ee5d437", "name": "David Scott"}
        ],
        "actors": [
            {"id": "5237aac5-f652-4aa5-9061-55bb007cd7be", "name": "Tom Kane"},
            {"id": "6f685ee1-95cb-46e8-8e88-48f61c7b58ce", "name": "Phil LaMarr"},
            {"id": "86f1f44b-39f5-41a6-8b3b-af5a9ed09858", "name": "Anthony Daniels"},
            {"id": "e94a4fc6-af54-41c3-86cb-5cd9ef015f9b", "name": "Nika Futterman"},
        ],
        "writers": [
            {
                "id": "4ca937e0-34f6-4d56-8674-365be5a26a63",
                "name": "Jens Nygaard Knudsen",
            },
            {
                "id": "59711626-c533-4ef7-80c9-74df1ee983e0",
                "name": "Godtfred Kirk Christiansen",
            },
            {"id": "83b8d23a-2c8b-4c98-b6d4-6e2d2deba0b1", "name": "Michael Price"},
            {
                "id": "cdd472c9-bf4a-48c5-aa3a-099ec0089af2",
                "name": "Ole Kirk Christiansen",
            },
        ],
        "actors_names": [
            "Anthony Daniels",
            "Nika Futterman",
            "Phil LaMarr",
            "Tom Kane",
        ],
        "writers_names": [
            "Godtfred Kirk Christiansen",
            "Jens Nygaard Knudsen",
            "Michael Price",
            "Ole Kirk Christiansen",
        ],
        "directors_names": ["David Scott"],
    },
    {
        "id": "ab1643e7-08b9-43dc-8265-ffaba9635a4d",
        "rating": 7.8,
        "title": "Star Trek: Shattered Universe",
        "description": "The U.S.S. Excelsior, under the command of Captain Sulu is transported to the hostile Mirror Universe where Starfleet and the Federation are the bad guys, and its up to you to find a way to get the Excelsior back to the normal universe, fighting hostile Federation ships, including the I.S.S. Enterprise along the way.",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
        ],
        "directors": [
            {"id": "6a7fe72e-6f29-462b-a32a-f328276274c8", "name": "Henrik Markarian"},
            {"id": "d9760bd9-2ffc-44ae-b551-2c12146bc35b", "name": "Andrew Iverson"},
        ],
        "actors": [
            {"id": "a4fc2b18-b89b-47f5-8d11-8b26e26fcdb9", "name": "George Takei"},
            {"id": "c2c1ef6b-2267-4a85-9861-1186019f591b", "name": "Matthew Mercer"},
            {"id": "c540c6d9-e110-4fec-a733-b90a18f3158a", "name": "Doug Stone"},
            {"id": "d9162823-9df0-4b03-bbab-272601eba66c", "name": "Walter Koenig"},
        ],
        "writers": [
            {"id": "d9760bd9-2ffc-44ae-b551-2c12146bc35b", "name": "Andrew Iverson"}
        ],
        "actors_names": [
            "Doug Stone",
            "George Takei",
            "Matthew Mercer",
            "Walter Koenig",
        ],
        "writers_names": ["Andrew Iverson"],
        "directors_names": ["Andrew Iverson", "Henrik Markarian"],
    },
    {
        "id": "ab2ec7a9-3cfc-448a-915c-9a0584dfc297",
        "rating": 5.2,
        "title": "Star Runner",
        "description": "Get ready for the ultimate martial arts competition, where anything goes and lives are bought and sold. Tank is the celebrated Champion Star Runner and is deemed invincible among the martial arts community. When the headstrong Bond becomes determined to take on the undefeated fighter, he knows he must be in the best fighting condition. Training under a renowned martial arts expert, Bond learns to supplement his Thai Kickboxing skills with various styles of Chinese kun-fu, creating a powerful hybrid fighting style. With his new skills, Bond prepares to take on Tank and the fight of his life.",
        "genres": [
            {"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"},
            {"id": "237fd1e4-c98e-454e-aa13-8a13fb7547b5", "name": "Romance"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
        ],
        "directors": [
            {"id": "e74122b2-a541-449b-a75a-f261a4dd06fe", "name": "Daniel Lee"}
        ],
        "actors": [
            {"id": "3163b0c4-be1b-4ca0-8192-af6adb40928e", "name": "Vanness Wu"},
            {"id": "379f532d-c38f-4887-8d7a-cc2871c4b111", "name": "Hyun-joo Kim"},
            {"id": "6c26fa66-e385-4065-a6d2-7aa30128e00b", "name": "Andy On"},
            {"id": "a5a4cdf0-dd5e-4578-8177-b5389c803396", "name": "Shaun Tam"},
        ],
        "writers": [
            {"id": "4e1f85b9-750d-425c-a317-27369a195a49", "name": "Yin Han Chow"},
            {"id": "8b58b717-e469-4f61-92bc-8fe6302e7abd", "name": "Abe Kwong"},
            {"id": "e74122b2-a541-449b-a75a-f261a4dd06fe", "name": "Daniel Lee"},
        ],
        "actors_names": ["Andy On", "Hyun-joo Kim", "Shaun Tam", "Vanness Wu"],
        "writers_names": ["Abe Kwong", "Daniel Lee", "Yin Han Chow"],
        "directors_names": ["Daniel Lee"],
    },
    {
        "id": "ab6aa3c1-fa9b-4959-8b19-1daae731b84b",
        "rating": 6.5,
        "title": "Star Power: The Creation of United Artists",
        "description": "Roddy McDowall narrates this retrospective of the careers of film pioneers D. W. Griffith, Mary Pickford, Douglas Fairbanks, and Charlie Chaplin, culminating in the formation of United Artists. Douglas Fairbanks, Jr., and Marc Wanamaker add insight to the film clips and archival footage.",
        "genres": [
            {"id": "6d141ad2-d407-4252-bda4-95590aaf062a", "name": "Documentary"},
            {"id": "ca124c76-9760-4406-bfa0-409b1e38d200", "name": "Biography"},
        ],
        "directors": [
            {"id": "b8fec55d-25df-477b-adee-44916fcfb0ff", "name": "Hugh Munro Neely"}
        ],
        "actors": [
            {
                "id": "2c4e04f9-8a48-493a-b594-f832788f7aa2",
                "name": "Christopher Sanders",
            },
            {"id": "77d6381f-2fa9-4fc3-98ef-071fc7615e1f", "name": "Marc Wanamaker"},
            {"id": "837509a4-03cf-4776-b644-d4aa3d22be33", "name": "Joy Noe"},
            {"id": "e37e73d9-817d-4851-8d7b-6ac74d46842b", "name": "Roddy McDowall"},
        ],
        "writers": [
            {"id": "b8fec55d-25df-477b-adee-44916fcfb0ff", "name": "Hugh Munro Neely"},
            {"id": "ccfb13a8-3fb0-4223-8924-93838018a625", "name": "John J. Flynn"},
        ],
        "actors_names": [
            "Christopher Sanders",
            "Joy Noe",
            "Marc Wanamaker",
            "Roddy McDowall",
        ],
        "writers_names": ["Hugh Munro Neely", "John J. Flynn"],
        "directors_names": ["Hugh Munro Neely"],
    },
    {
        "id": "ac120a7e-da82-4383-a724-41cfd811e37d",
        "rating": 7.2,
        "title": "Star Wars: Jedi Starfighter",
        "description": "",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
        ],
        "directors": [
            {"id": "37c05f38-90d7-4817-9341-5799f6b19ec0", "name": "Daron Stinnett"}
        ],
        "actors": [
            {"id": "0dfb6ccf-137a-4bd5-8365-c9473bd0876b", "name": "Masasa Moyo"},
            {"id": "7f50cec9-1b7c-44c9-9afd-6314182d396d", "name": "Roger Jackson"},
            {"id": "c23936f1-2695-4c16-bbdc-45211ef2a4a7", "name": "Jeff Bennett"},
            {"id": "d0fa5635-8e94-4817-9079-28f049bd855f", "name": "Sterling James"},
        ],
        "writers": [
            {"id": "e73f46a4-cf53-4b12-b5da-52503b6319f7", "name": "Haden Blackman"}
        ],
        "actors_names": [
            "Jeff Bennett",
            "Masasa Moyo",
            "Roger Jackson",
            "Sterling James",
        ],
        "writers_names": ["Haden Blackman"],
        "directors_names": ["Daron Stinnett"],
    },
    {
        "id": "ac29ce6b-b33b-4733-bbb0-e96ddb33afcb",
        "rating": 6.9,
        "title": "Star Wars: Generations",
        "description": "A young boy and his Grandfather use their imagination to take us back to a galaxy far, far away.",
        "genres": [
            {"id": "55c723c1-6d90-4a04-a44b-e9792040251a", "name": "Family"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
            {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
        ],
        "directors": [
            {"id": "0453bbbf-3816-4974-8da8-2f1572522151", "name": "Don Bitters III"}
        ],
        "actors": [
            {"id": "0ca7ed61-f908-43f4-b5b4-b2cab86c9a76", "name": "Jason Tobias"},
            {"id": "290537de-eb07-42f1-bd9b-e291434afe7b", "name": "Jack E. Curenton"},
            {"id": "70bbe599-05cb-4fe3-a19c-d53f22c14671", "name": "Jentzen Ramirez"},
        ],
        "writers": [
            {"id": "0453bbbf-3816-4974-8da8-2f1572522151", "name": "Don Bitters III"},
            {"id": "0ca7ed61-f908-43f4-b5b4-b2cab86c9a76", "name": "Jason Tobias"},
            {"id": "d1807505-f905-4e97-969f-0d53c1122828", "name": "Todd Blood"},
        ],
        "actors_names": ["Jack E. Curenton", "Jason Tobias", "Jentzen Ramirez"],
        "writers_names": ["Don Bitters III", "Jason Tobias", "Todd Blood"],
        "directors_names": ["Don Bitters III"],
    },
    {
        "id": "ac2cb378-29f1-4773-b3ba-28a8bd276b85",
        "rating": 7,
        "title": "One Night One Star: Usher Live",
        "description": "",
        "genres": [{"id": "56b541ab-4d66-4021-8708-397762bff2d4", "name": "Music"}],
        "directors": [
            {"id": "357608e0-6ec3-4b93-bbe4-496197651fa1", "name": "Hamish Hamilton"}
        ],
        "actors": [
            {"id": "07f89ba0-67b1-4128-9a7f-5aeee1787416", "name": "Usher Raymond"}
        ],
        "writers": [
            {"id": "07f89ba0-67b1-4128-9a7f-5aeee1787416", "name": "Usher Raymond"}
        ],
        "actors_names": ["Usher Raymond"],
        "writers_names": ["Usher Raymond"],
        "directors_names": ["Hamish Hamilton"],
    },
    {
        "id": "ac58403b-7070-4dcc-8e53-fa2d2d2284ab",
        "rating": 7,
        "title": "Video Killed the Radio Star",
        "description": "Featuring interviews with iconic bands and artists, such as Guns 'n' Roses, Fleetwood Mac, Metallica, A-Ha, Bon Jovi and Bryan Adams.",
        "genres": [
            {"id": "56b541ab-4d66-4021-8708-397762bff2d4", "name": "Music"},
            {"id": "6d141ad2-d407-4252-bda4-95590aaf062a", "name": "Documentary"},
        ],
        "directors": [],
        "actors": [
            {"id": "589a55c7-d9b0-4f3f-862f-4f547f6218e8", "name": "David Mallet"},
            {"id": "ab77efeb-dc56-4452-bdd9-43d782e223f1", "name": "Robert Elms"},
        ],
        "writers": [],
        "actors_names": ["David Mallet", "Robert Elms"],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "acaa9ff8-b261-4ff4-b194-a99fd7669542",
        "rating": 7.9,
        "title": "Outlaw Star",
        "description": "Gene Starwind dreams of a life as an Outlaw, and fate smiles on him as he seems to suddenly wind up with a great job. But things go awry, and he finds himself the new owner of the fastest, most technologically advanced space ship in the galaxy. Unfortunately, it's stolen and the owners want it back Along with his partner Jim and the lovely Melfina, Gene must fight his way across the galaxy battling pirates, aliens and assassins as he attempts to discover the secrets of the Outlaw star.",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "526769d7-df18-4661-9aa6-49ed24e9dfd8", "name": "Thriller"},
            {"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"},
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
        ],
        "directors": [],
        "actors": [
            {
                "id": "05a0b8e6-18c7-4195-9093-18c11e8faf0a",
                "name": "Emilie de Azevedo Brown",
            },
            {"id": "225c130b-33cf-4bdf-bfb2-51f369fe8f5c", "name": "Bridget Hoffman"},
            {"id": "35ad0356-4590-4d55-a599-03a5696e037e", "name": "Bob Buchholz"},
            {"id": "9dd92f6b-57af-46a5-8cb7-7673a61e70be", "name": "Ayako Kawasumi"},
        ],
        "writers": [
            {"id": "1489cc75-3380-4f72-8557-04baddc9351d", "name": "Hajime Yatate"}
        ],
        "actors_names": [
            "Ayako Kawasumi",
            "Bob Buchholz",
            "Bridget Hoffman",
            "Emilie de Azevedo Brown",
        ],
        "writers_names": ["Hajime Yatate"],
        "directors_names": [],
    },
    {
        "id": "acded899-2fc1-43af-b681-7630381fbd73",
        "rating": 6.7,
        "title": "A Star and Two Coffees",
        "description": "Carlos, a young architect in crisis with his partner, arrives in a small town in the north of Argentina to build a complex of cabins. There he meets Estela, a thirteen-year-old girl, but he...",
        "genres": [
            {"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"},
            {"id": "237fd1e4-c98e-454e-aa13-8a13fb7547b5", "name": "Romance"},
        ],
        "directors": [
            {"id": "1e1e384b-fbd9-4acb-a1d8-8ce2e2252d28", "name": "Alberto Lecchi"}
        ],
        "actors": [
            {
                "id": "5c644c4b-95e3-44bd-9ece-e632376419a0",
                "name": "Gabriela Bertolone",
            },
            {"id": "805f92c4-395b-4696-b4bc-70341dda5b76", "name": "Rubén Fleitas"},
            {
                "id": "86ee2554-923b-40f1-9b02-bf66fb2c5686",
                "name": "Gerardo Albarracín",
            },
            {"id": "eb68fdf1-8b04-4855-9523-dd6d6e228a5a", "name": "Silvia Gallegos"},
        ],
        "writers": [
            {"id": "1e1e384b-fbd9-4acb-a1d8-8ce2e2252d28", "name": "Alberto Lecchi"},
            {
                "id": "52a1e34e-9670-4d21-9d08-85c5320e7838",
                "name": "Daniel García Molt",
            },
        ],
        "actors_names": [
            "Gabriela Bertolone",
            "Gerardo Albarracín",
            "Rubén Fleitas",
            "Silvia Gallegos",
        ],
        "writers_names": ["Alberto Lecchi", "Daniel García Molt"],
        "directors_names": ["Alberto Lecchi"],
    },
    {
        "id": "ace46a3c-da44-474f-9c20-5dafc22cf0d6",
        "rating": 7.2,
        "title": "Star Wars: Aeon",
        "description": "Sith Lord Darth Tenebris is sent to retrieve a crystal to power a new superweapon, but encounters a Jedi Knight who intends to stop him and a third character who surprises both of them.",
        "genres": [
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
            {"id": "b92ef010-5e4c-4fd0-99d6-41b6456272cd", "name": "Fantasy"},
        ],
        "directors": [
            {"id": "ba99932d-4481-449d-a222-b4591636b736", "name": "Saygi Uygur"}
        ],
        "actors": [
            {"id": "8c2f0f87-5537-4540-8296-1be8cb4516b0", "name": "Orçun Atay"},
            {"id": "a3dc299e-7a97-4834-9245-b248aaec06f2", "name": "Burak Yavuz"},
            {"id": "ba99932d-4481-449d-a222-b4591636b736", "name": "Saygi Uygur"},
            {"id": "d420ab97-9ab8-4fe8-a466-bb09467a10d0", "name": "Güney Inal"},
        ],
        "writers": [
            {"id": "a3dc299e-7a97-4834-9245-b248aaec06f2", "name": "Burak Yavuz"},
            {"id": "ba99932d-4481-449d-a222-b4591636b736", "name": "Saygi Uygur"},
        ],
        "actors_names": ["Burak Yavuz", "Güney Inal", "Orçun Atay", "Saygi Uygur"],
        "writers_names": ["Burak Yavuz", "Saygi Uygur"],
        "directors_names": ["Saygi Uygur"],
    },
    {
        "id": "ace652ed-62dc-4c5a-a96d-4f4c9361ae56",
        "rating": 7.9,
        "title": "Star Portraits with Rolf Harris",
        "description": "A group of three portrait artists, both amateur and professional, are assigned the task of painting a celebrity from life using their preferred style. The star then decides which portrait to take home with them.",
        "genres": [
            {"id": "6d141ad2-d407-4252-bda4-95590aaf062a", "name": "Documentary"}
        ],
        "directors": [],
        "actors": [
            {"id": "d10dbf04-ac41-48eb-a412-b07578fc9605", "name": "Rolf Harris"}
        ],
        "writers": [],
        "actors_names": ["Rolf Harris"],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "adc67ce9-a096-46e7-bc70-247266a058b7",
        "rating": 7.9,
        "title": "The Poker Star",
        "description": "Eleven people from all over Australia come together to live in a Penthouse apartment in Melbourne to compete in challenges. These challenges, based on the fundamental skills of poker, but take place off the table. Can the contestants Bluff their way through a job interview, have the Focus to escape from a tank full of sharks, possess the charisma to respond to live questions from the press while maintaining composure?",
        "genres": [
            {"id": "e508c1c8-24c0-4136-80b4-340c4befb190", "name": "Reality-TV"}
        ],
        "directors": [],
        "actors": [
            {"id": "8ba1658c-a9a3-4d08-b67a-9695dc79028d", "name": "Joe Hachem"},
            {"id": "8ef0d895-5cac-4d21-b67d-ea09f686f1f8", "name": "Amanda"},
            {"id": "e7bd386e-455c-4878-ad9e-94c7122d966b", "name": "Ben"},
            {"id": "f8ca9620-7d52-4c9b-8514-85fc5a73fca3", "name": "Lee Dr. Nelson"},
        ],
        "writers": [],
        "actors_names": ["Amanda", "Ben", "Joe Hachem", "Lee Dr. Nelson"],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "ae41e972-bff3-449c-afa1-8d722fa46a52",
        "rating": 5,
        "title": "Star Wars: A Galaxy in Darkness",
        "description": "",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
        ],
        "directors": [
            {"id": "5890809a-0dec-49da-a4f2-f78fc59546e4", "name": "Damien Valentine"}
        ],
        "actors": [
            {"id": "289af333-1bc3-4efd-9689-df036ad04b84", "name": "Lani Minella"},
            {"id": "5890809a-0dec-49da-a4f2-f78fc59546e4", "name": "Damien Valentine"},
            {"id": "c73206cd-f427-4e9d-87f4-a3393b5ae8cc", "name": "Azure"},
            {"id": "e909431e-2194-4eca-8d8d-c142ff5d956a", "name": "Elizabeth Cameron"},
        ],
        "writers": [
            {"id": "5890809a-0dec-49da-a4f2-f78fc59546e4", "name": "Damien Valentine"}
        ],
        "actors_names": [
            "Azure",
            "Damien Valentine",
            "Elizabeth Cameron",
            "Lani Minella",
        ],
        "writers_names": ["Damien Valentine"],
        "directors_names": ["Damien Valentine"],
    },
    {
        "id": "ae890b4e-6716-4077-8f07-a7a77d9b5543",
        "rating": 8.1,
        "title": "The Shining Star of Losers Everywhere",
        "description": "Haru Urara, a Japanese racehorse, became a national icon after enduring a losing streak of epic proportions.",
        "genres": [
            {"id": "2f89e116-4827-4ff4-853c-b6e058f71e31", "name": "Sport"},
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
            {"id": "6d141ad2-d407-4252-bda4-95590aaf062a", "name": "Documentary"},
            {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
            {"id": "ca124c76-9760-4406-bfa0-409b1e38d200", "name": "Biography"},
        ],
        "directors": [
            {"id": "a534611d-6873-45c1-8dd4-fa253e9e0652", "name": "Mickey Duzyj"}
        ],
        "actors": [],
        "writers": [
            {"id": "a534611d-6873-45c1-8dd4-fa253e9e0652", "name": "Mickey Duzyj"}
        ],
        "actors_names": [],
        "writers_names": ["Mickey Duzyj"],
        "directors_names": ["Mickey Duzyj"],
    },
    {
        "id": "aebbf032-d948-459f-a142-7a0e11a0c9ed",
        "rating": 5.9,
        "title": "Star Wreck 2pi: Full Twist, Now!",
        "description": "The world was been conquered by Emperor James B. Pirk with the help of the russian. Now everybody must speak finnish and a huge space fleet is built...",
        "genres": [
            {"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
        ],
        "directors": [
            {"id": "45bcd3da-b106-4fae-9ea4-27dd99590b32", "name": "Fabienne Gschwind"}
        ],
        "actors": [
            {"id": "4e12a686-1aff-40da-9ae5-7168ca72adb1", "name": "Stig Bremseth"},
            {"id": "ea0ec0e0-f51a-486c-8f60-c52a034f1bb3", "name": "Antti Hukkanen"},
            {"id": "eb990bd5-ee1a-4590-8fa6-77a514a73f8e", "name": "Cédric Gerold"},
            {
                "id": "f91b113c-542b-462e-9349-1508d71d6f17",
                "name": "Stig Magnus Gjerald",
            },
        ],
        "writers": [
            {"id": "45bcd3da-b106-4fae-9ea4-27dd99590b32", "name": "Fabienne Gschwind"}
        ],
        "actors_names": [
            "Antti Hukkanen",
            "Cédric Gerold",
            "Stig Bremseth",
            "Stig Magnus Gjerald",
        ],
        "writers_names": ["Fabienne Gschwind"],
        "directors_names": ["Fabienne Gschwind"],
    },
    {
        "id": "af749d09-d3cb-40f6-a01c-c49f13df35ee",
        "rating": 7.8,
        "title": "WWF All-Star Wrestling",
        "description": "",
        "genres": [{"id": "2f89e116-4827-4ff4-853c-b6e058f71e31", "name": "Sport"}],
        "directors": [],
        "actors": [
            {"id": "0ce1ce6c-adb6-4bdd-9579-9f7f96fd3450", "name": "Merced Solis"},
            {"id": "68bfa031-9067-4ff2-b3ac-718207fbb112", "name": "Vince McMahon"},
            {"id": "92501a55-cef3-47bb-80cf-a12897bc75ef", "name": "Jimmy Hart"},
            {"id": "da5600e9-263d-407b-a446-e2b97c24cdd6", "name": "Don Muraco"},
        ],
        "writers": [],
        "actors_names": ["Don Muraco", "Jimmy Hart", "Merced Solis", "Vince McMahon"],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "b0752ea4-76fe-4a00-986d-71fb34f908cd",
        "rating": 7.4,
        "title": "The Blue Star Hotel",
        "description": "Zuzanka (Natasa Gollová) can finally stop toiling away at washing dishes at hotel Mercur after a distant aunt has bequeathed her her own hotel - Blue Star. She proudly marches over to the luxury hotel in the center of town and immediately begins to change the personnel. Because this involves the facilities belonging to a joint-stock company, which no one can inherit, she is considered insane. It comes out that her inheritance is in reality a small, shabby little hotel of the same name in the IV town district. The personnel are three unemployed youths who in this way work off the money they owe for rent. The first guest is wealthy Vladimír Rychta Rohan (Oldrich Nový), whose parents spent their honeymoon in this very hotel. He wants to celebrate his wedding there, with which his fiancée Milada (Adina Mandlová), who is waiting for him at the luxurious Blue Star, does not concur.",
        "genres": [{"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"}],
        "directors": [
            {"id": "9bce39fb-4614-4b76-a588-5300da89ecaa", "name": "Martin Fric"}
        ],
        "actors": [
            {"id": "326d3397-5b1b-4f7b-9ffd-8d5b87049249", "name": "Oldrich Nový"},
            {"id": "631490c0-a64c-4fc6-94ac-6e7a9a23e0da", "name": "Adina Mandlová"},
            {"id": "a219f8e0-b0c8-4acc-8cf7-dcbd16d9e7aa", "name": "Ella Nollová"},
            {"id": "a336172e-1d9f-4607-9f11-8c58e26267ea", "name": "Natasa Gollová"},
        ],
        "writers": [
            {"id": "3b6facb9-11ff-4970-bb82-3aa1a5c68f66", "name": "Marie Svobodová"},
            {"id": "76217a1e-8304-42cf-82ea-38173454f989", "name": "Václav Wasserman"},
            {"id": "9bce39fb-4614-4b76-a588-5300da89ecaa", "name": "Martin Fric"},
        ],
        "actors_names": [
            "Adina Mandlová",
            "Ella Nollová",
            "Natasa Gollová",
            "Oldrich Nový",
        ],
        "writers_names": ["Marie Svobodová", "Martin Fric", "Václav Wasserman"],
        "directors_names": ["Martin Fric"],
    },
    {
        "id": "b13516e1-10bf-4f22-a5f4-e3ccf7e67097",
        "rating": 5.8,
        "title": "5 Star Day",
        "description": "Four People. One Horoscope. Infinite Possibilities. Jake Gibson's (Cam Gigandet) horoscope forecasts a perfect FIVE STAR DAY the morning of his birthday, but what's foretold as a flawless day unfolds to be far less than stellar. Jake's world turns upside down when all that could go wrong ... does. Determined that Astrology has no legitimacy, Jake embarks on a journey to test the theory of Astrology by finding the three people born the same time and place as himself - Sarah Reynolds (Jena Malone), Yvette Montgomery (Brooklyn Sudano) and Wesley Henderson (Max Hartman). The journey quickly uproots Jake from the small college town of Berkeley, California, to downtown Chicago where he sets out to find and interview Sarah, Yvette and Wesley to see if their birthdays proved to be as deplorable as his own. Jake's pursuit in finding his three Astrological matches (or Zodiac twins) will not only test his convictions, but validate how life's unexpected twists of fate can deliver much more than the anticipated. The unforeseen takes Jake from the Windy City, to the boardwalk of New Jersey's Atlantic City, to the bustling streets of New York. What Jake learns along the way is an important lesson about life, love, fate and destiny that will unexpectedly change his life forever.",
        "genres": [
            {"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"},
            {"id": "237fd1e4-c98e-454e-aa13-8a13fb7547b5", "name": "Romance"},
        ],
        "directors": [
            {"id": "9d39e6a1-0b39-4c73-af49-3656470a4880", "name": "Danny Buday"}
        ],
        "actors": [
            {"id": "17bf5adc-1fcd-48e6-943d-9a2c198781d4", "name": "Cam Gigandet"},
            {"id": "3d5c4cd7-7772-4099-a6c3-c1aa06de02fc", "name": "Guy Herbert"},
            {"id": "5509f1e0-d985-4d33-8393-502d95a355fe", "name": "Derek Shipp"},
            {"id": "cfb997e7-9b3b-46c6-ad9d-95056b84c7fd", "name": "Will Yun Lee"},
        ],
        "writers": [
            {"id": "9d39e6a1-0b39-4c73-af49-3656470a4880", "name": "Danny Buday"}
        ],
        "actors_names": ["Cam Gigandet", "Derek Shipp", "Guy Herbert", "Will Yun Lee"],
        "writers_names": ["Danny Buday"],
        "directors_names": ["Danny Buday"],
    },
    {
        "id": "b1384a92-f7fe-476b-b90b-6cec2b7a0dce",
        "rating": 8.6,
        "title": "Star Trek: The Next Generation",
        "description": "Set in the 24th century and decades after the adventures of the original crew of the starship Enterprise, this new series is the long-awaited successor to the original Star Trek (1966). Under the command of Captain Jean-Luc Picard, the all new Enterprise NCC 1701-D travels out to distant planets to seek out new life and to boldly go where no one has gone before.",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
            {"id": "ca88141b-a6b4-450d-bbc3-efa940e4953f", "name": "Mystery"},
        ],
        "directors": [],
        "actors": [
            {"id": "035c4793-4864-45b8-8d4f-b86b454c60b0", "name": "Marina Sirtis"},
            {"id": "57a471b1-09dc-48fd-ba8a-1211015a0110", "name": "Patrick Stewart"},
            {"id": "5bddea2c-8609-499a-a444-77e0142743c0", "name": "Jonathan Frakes"},
            {"id": "fc9f27d2-aaee-46e6-b263-40ec8d2dd355", "name": "LeVar Burton"},
        ],
        "writers": [
            {"id": "6960e2ca-889f-41f5-b728-1e7313e54d6c", "name": "Gene Roddenberry"}
        ],
        "actors_names": [
            "Jonathan Frakes",
            "LeVar Burton",
            "Marina Sirtis",
            "Patrick Stewart",
        ],
        "writers_names": ["Gene Roddenberry"],
        "directors_names": [],
    },
    {
        "id": "b164fef5-0867-46d8-b635-737e1721f6bf",
        "rating": 6.7,
        "title": "Tar with a Star",
        "description": "",
        "genres": [
            {"id": "0b105f87-e0a5-45dc-8ce7-f8632088f390", "name": "Western"},
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
            {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
        ],
        "directors": [
            {"id": "3138e609-870f-4764-9a57-97d39feef7a8", "name": "Bill Tytla"},
            {"id": "96f18d84-55e0-4718-b87f-4a9e63544d76", "name": "George Germanetti"},
        ],
        "actors": [
            {"id": "2e01e457-f993-4bfe-87c3-de2ef8626cc7", "name": "Mae Questel"},
            {"id": "448b9382-f235-478b-a013-d127f421ea4a", "name": "Jackson Beck"},
            {"id": "89d4622f-5dde-4257-9401-36e3052de105", "name": "Jack Mercer"},
        ],
        "writers": [
            {"id": "89d4622f-5dde-4257-9401-36e3052de105", "name": "Jack Mercer"},
            {"id": "cb7d11c1-9041-4bf5-84b2-728847bbf035", "name": "Carl Meyer"},
        ],
        "actors_names": ["Jack Mercer", "Jackson Beck", "Mae Questel"],
        "writers_names": ["Carl Meyer", "Jack Mercer"],
        "directors_names": ["Bill Tytla", "George Germanetti"],
    },
    {
        "id": "b16d59f7-a386-467b-bea3-35e7ffbba902",
        "rating": 8.8,
        "title": "Star Tech",
        "description": "Star Tech is weekly TV talk show featuring most interesting geeks, techies, bloggers, startup founders, CEOs and others who thrive on the business of new technologies. Show is hosted by the leading regional tech editor, Dragan Petric.",
        "genres": [
            {"id": "31cabbb5-6389-45c6-9b48-f7f173f6c40f", "name": "Talk-Show"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
        ],
        "directors": [],
        "actors": [
            {"id": "099a5001-992b-47eb-951a-7b9b73edb3cf", "name": "Dragan Petric"}
        ],
        "writers": [],
        "actors_names": ["Dragan Petric"],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "b1a2aae8-5c9e-4583-b89e-883c0d0c969a",
        "rating": 8.5,
        "title": "Star Trek: Elite Force II",
        "description": "After the long return journey of the USS Voyager to the Federation, the elite Hazard Team finds themselves declared redundant and disbanded. You play Lt. Munro, the leader of the team who is relegated to being an instructor at Starfleet Academy. After years at the unexciting post, your fortunes change dramatically when Capt. Picard himself has the team reassembled and assigned to the Enterprise. The good captain's wisdom could not have been better placed as the Enterprise is sent to investigate the loss of contact with the USS Dallas. Leading your Hazard Team, you find yourself at the front line when you discover a formidable new enemy who represents a terrible threat to the galaxy and it will require all your courage and cunning to stop it.",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
        ],
        "directors": [],
        "actors": [
            {"id": "3574a052-0d45-41be-8837-648ba5786af7", "name": "Tim Russ"},
            {"id": "57a471b1-09dc-48fd-ba8a-1211015a0110", "name": "Patrick Stewart"},
            {"id": "9a52a5f3-e2df-49b7-ba7c-006f2f50f67b", "name": "Rino Romano"},
            {"id": "d1507689-c396-4603-89ed-825022d64296", "name": "Dwight Schultz"},
        ],
        "writers": [
            {"id": "998acbe6-dd4b-4f93-9996-0efac51d5b95", "name": "Daniel Greenberg"}
        ],
        "actors_names": [
            "Dwight Schultz",
            "Patrick Stewart",
            "Rino Romano",
            "Tim Russ",
        ],
        "writers_names": ["Daniel Greenberg"],
        "directors_names": [],
    },
    {
        "id": "b1f1e8a6-e310-47d9-a93c-6a7b192bac0e",
        "rating": 7.1,
        "title": "Star Trek Beyond",
        "description": "After stopping off at Starbase Yorktown, a remote outpost on the fringes of Federation space, the USS Enterprise, halfway into their five-year mission, is destroyed by an unstoppable wave of unknown aliens. With the crew stranded on an unknown planet and with no apparent means of rescue, they find themselves fighting against a ruthless enemy with a well-earned hatred of the Federation and everything it stands for. Only a rebellious alien warrior can help them reunite and leave the planet to stop this deadly menace from beginning a possible galactic war.",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "526769d7-df18-4661-9aa6-49ed24e9dfd8", "name": "Thriller"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
        ],
        "directors": [
            {"id": "8856053e-8a4f-42e1-bb27-6ab8fd664518", "name": "Justin Lin"}
        ],
        "actors": [
            {"id": "4a416628-4a36-431c-9121-513674dae840", "name": "Zoe Saldana"},
            {"id": "8a34f121-7ce6-4021-b467-abec993fc6cd", "name": "Zachary Quinto"},
            {"id": "9f38323f-5912-40d2-a90c-b56899746f2a", "name": "Chris Pine"},
            {"id": "afa7c253-6702-47d7-a451-cf2bc9350310", "name": "Karl Urban"},
        ],
        "writers": [
            {"id": "2cf03687-ebc3-47dc-a99f-602f6cc55f7a", "name": "Simon Pegg"},
            {"id": "6960e2ca-889f-41f5-b728-1e7313e54d6c", "name": "Gene Roddenberry"},
            {"id": "698522c6-f8e9-403a-8922-9d320dec5753", "name": "Doug Jung"},
        ],
        "actors_names": ["Chris Pine", "Karl Urban", "Zachary Quinto", "Zoe Saldana"],
        "writers_names": ["Doug Jung", "Gene Roddenberry", "Simon Pegg"],
        "directors_names": ["Justin Lin"],
    },
    {
        "id": "b2540995-0f91-4db1-99ed-dd7bcb3976d9",
        "rating": 6,
        "title": "Catch a Falling Star",
        "description": "Sydney Clarke is a spoiled famous actress who is shooting a film when she suddenly gets angry and storms off. She wakes up in the middle of nowhere and gets a ride to a small New England town. There she meets and develops a friendship with Joyce, a waitress at a bowling alley. There she meets Ben, a steel mill owner, and later when she goes to get a job in that small town, she meets Ben again. Sydney becomes a nurse at the mill. All the men adore her. There they have many great times together, and Sydney realizes how important real friends are and that small towns are better than big name Hollywood.",
        "genres": [
            {"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"},
            {"id": "237fd1e4-c98e-454e-aa13-8a13fb7547b5", "name": "Romance"},
            {"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"},
        ],
        "directors": [
            {"id": "c677c254-215c-4acf-bfdf-e8d24b4c0085", "name": "Bob Clark"}
        ],
        "actors": [
            {"id": "0092a672-4ed5-4838-a6fc-6abf300f6939", "name": "Andrew Jackson"},
            {"id": "2350b175-b8b1-46f4-9ca7-cc311dbe15dc", "name": "Rebecca Jenkins"},
            {"id": "3fa268fe-87a2-4e98-a76b-f54aa5829ab4", "name": "Sela Ward"},
            {"id": "bd3549cb-70b0-4577-ac51-3280341a59c5", "name": "Jane Curtin"},
        ],
        "writers": [
            {"id": "5672aa6d-4377-451d-9cd5-45ca6ed5e9fa", "name": "Paul Eric Myers"},
            {"id": "9f13a031-cea4-4db2-bf28-1989d56e5be4", "name": "Jonathan Prince"},
            {"id": "b1b97172-c704-45c3-b1bf-5a3e2bec86fa", "name": "Josh Goldstein"},
        ],
        "actors_names": [
            "Andrew Jackson",
            "Jane Curtin",
            "Rebecca Jenkins",
            "Sela Ward",
        ],
        "writers_names": ["Jonathan Prince", "Josh Goldstein", "Paul Eric Myers"],
        "directors_names": ["Bob Clark"],
    },
    {
        "id": "b2ddce38-9689-4a33-8dd6-7efd2411ed2d",
        "rating": 5.6,
        "title": "Star of India",
        "description": "Squire Pierre St. Laurent returns from wars in India to 17th-century provincial France to find his estate confiscated by governor Narbonne, for back taxes, and resold to Katrina, a Dutch Countess. Katrina offers to return Pierre's property if he will help her get possession of the 'Star of India,' a fabulous sapphire, held at the moment by Narbonne. The Dutch government wants it returned to its Indian worshipers, in order to keep peace. Pierre is a guest at Narbonne's château during a visit from King Louis IV, who wants to acquire the sapphire for his new court-favorite, Mme. de Montespan. Pierre discovers that the \"Star\" is hidden in the hilt of Narbonne's sword, He challenges Narbonne to a duel, gains possession of Narbonne's sword, extracts the jewel and escapes the castle with Narbonne's men in pursuit. Katrina is on a Dutch ship in the harbor and is soon joined by Pierre and his pursuers.",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "237fd1e4-c98e-454e-aa13-8a13fb7547b5", "name": "Romance"},
        ],
        "directors": [
            {"id": "05572526-d39e-483f-b548-92ebda7702eb", "name": "Arthur Lubin"}
        ],
        "actors": [
            {"id": "4b007bdf-b309-4022-bf2b-d54bdcc6c1f3", "name": "Herbert Lom"},
            {"id": "81803c31-d0d8-4b15-99af-2ec3cc85f09c", "name": "Cornel Wilde"},
            {"id": "8d93102f-c5ca-433a-85d7-9cf17b3abc09", "name": "Jean Wallace"},
            {"id": "f6b045e4-b3aa-46d8-8201-9608ceab48ff", "name": "Leslie Linder"},
        ],
        "writers": [
            {"id": "2ee36223-58b5-4962-9649-44e1014ec726", "name": "Denis Freeman"},
            {"id": "5af88064-d4a6-419d-b78d-881a6e8098b2", "name": "Herbert Dalmas"},
        ],
        "actors_names": [
            "Cornel Wilde",
            "Herbert Lom",
            "Jean Wallace",
            "Leslie Linder",
        ],
        "writers_names": ["Denis Freeman", "Herbert Dalmas"],
        "directors_names": ["Arthur Lubin"],
    },
    {
        "id": "b2faef9b-ad43-455c-9ea5-9d5977c84b73",
        "rating": 8.6,
        "title": "Next Big Star",
        "description": "",
        "genres": [{"id": "55c723c1-6d90-4a04-a44b-e9792040251a", "name": "Family"}],
        "directors": [],
        "actors": [
            {"id": "281d83f0-461b-49d7-ac78-2c104ea1298f", "name": "Malese Jow"},
            {"id": "bfd40cbe-a628-4e62-9681-c78cbfa09168", "name": "Joseph Neibich"},
            {"id": "c6842b76-4f75-4933-931c-8d5fc2469375", "name": "Ed McMahon"},
        ],
        "writers": [],
        "actors_names": ["Ed McMahon", "Joseph Neibich", "Malese Jow"],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "b31be683-6382-46c8-8b00-9c1d43fba763",
        "rating": 5.8,
        "title": "The Lone Star Trail",
        "description": "Rancher Blaze Barker returns to Dead Falls after being framed by land-grabbers and spending two years in jail. Paroled, he can't wear a gun, but is aided by Marshal Fargo Steele. The gang ...",
        "genres": [
            {"id": "237fd1e4-c98e-454e-aa13-8a13fb7547b5", "name": "Romance"},
            {"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"},
            {"id": "56b541ab-4d66-4021-8708-397762bff2d4", "name": "Music"},
        ],
        "directors": [
            {"id": "fefaa0b7-ea97-4231-95e5-c4358d1bfe92", "name": "Ray Taylor"}
        ],
        "actors": [
            {"id": "6a5dac2a-086b-4580-a7fa-51f913c6effc", "name": "Johnny Mack Brown"},
            {"id": "966b8fe2-4ea1-44f5-b0c1-164076e3b21f", "name": "Fuzzy Knight"},
            {"id": "c2adf3ee-699e-4f51-a932-f78f0504ab82", "name": "Tex Ritter"},
            {"id": "d93f17a9-2e6e-45b8-a512-f2ea8b1a8665", "name": "Jennifer Holt"},
        ],
        "writers": [
            {"id": "81a0210b-ea5c-497c-9e95-25f0e19b7552", "name": "Victor Halperin"},
            {"id": "b944f021-dffc-49f7-8cb9-8f9ae8b5780d", "name": "Oliver Drake"},
        ],
        "actors_names": [
            "Fuzzy Knight",
            "Jennifer Holt",
            "Johnny Mack Brown",
            "Tex Ritter",
        ],
        "writers_names": ["Oliver Drake", "Victor Halperin"],
        "directors_names": ["Ray Taylor"],
    },
    {
        "id": "b3d223c7-18e0-428e-aed8-257c43e95992",
        "rating": 5.8,
        "title": "Star Reporter",
        "description": "John Randolph (Warren Hull), an idealistic young newspaper owner who uses his paper as an instrument for the public good, uses a campaign against crime to successfully run grafting politicians out of town. District Attorney William Burnette (Wallis Clark), father of Barbara Burnette (Marsha Hunt) who John loves, learns that John's father (unknown to John) is a criminal they are seeking. He refuses to prosecute him and John, not knowing the real reason, turns against Burnette and tries to run him out of office.",
        "genres": [
            {"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"},
            {"id": "237fd1e4-c98e-454e-aa13-8a13fb7547b5", "name": "Romance"},
            {"id": "63c24835-34d3-4279-8d81-3c5f4ddb0cdc", "name": "Crime"},
        ],
        "directors": [
            {"id": "32f20eed-ac12-416a-a7fc-bdd6728b47e3", "name": "Howard Bretherton"}
        ],
        "actors": [
            {"id": "5b78619f-f4c1-47bc-8e76-5fea0e0357d8", "name": "Marsha Hunt"},
            {"id": "d0fbe351-8477-48b3-bd64-24f4676ac637", "name": "Clay Clement"},
            {"id": "dfefcaae-ed71-4b65-ab63-9fc1bfba1566", "name": "Wallis Clark"},
            {"id": "e117dc0a-3bd2-491f-b5fe-9e96fab95e5a", "name": "Warren Hull"},
        ],
        "writers": [
            {"id": "8264aa96-c73e-478a-b81b-eb2a7f85ec46", "name": "John T. Neville"}
        ],
        "actors_names": ["Clay Clement", "Marsha Hunt", "Wallis Clark", "Warren Hull"],
        "writers_names": ["John T. Neville"],
        "directors_names": ["Howard Bretherton"],
    },
    {
        "id": "b3fcaf6d-6a31-44fb-95ee-6a8993bf9c02",
        "rating": 8.5,
        "title": "Phantasy Star Online",
        "description": "",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
        ],
        "directors": [
            {"id": "dc27e6db-cfd0-4e17-a802-eeca0a587b6b", "name": "Takao Miyoshi"}
        ],
        "actors": [],
        "writers": [
            {"id": "776de0e1-aa41-4bd4-aa63-f4a4ac832f0b", "name": "Daisuke Mori"},
            {"id": "82b37126-e13d-4200-bad9-9d32a19d9eda", "name": "Akinori Nishiyama"},
            {"id": "84b79bc9-4ca6-4b45-8eab-a016a5868a2d", "name": "Rieko Kodama"},
            {"id": "89faaa39-e854-45c1-b5f5-bc2d490028b5", "name": "Atsushi Kanno"},
            {"id": "b52124ec-35fb-4548-80c5-dff0116853ba", "name": "Hidenobu Hasebe"},
        ],
        "actors_names": [],
        "writers_names": [
            "Akinori Nishiyama",
            "Atsushi Kanno",
            "Daisuke Mori",
            "Hidenobu Hasebe",
            "Rieko Kodama",
        ],
        "directors_names": ["Takao Miyoshi"],
    },
    {
        "id": "b43d3ea2-e1aa-4086-b6c5-9db3f180a0cc",
        "rating": 5.9,
        "title": "King Star King",
        "description": 'King Star King is an intergalactic warrior who fights various evil foes throughout the Gigantiverse. Always buy his side are his team of "strange heroes" which includes Hank Waffles, Pooza the Wizard, and Gurbles the flying robot bear.',
        "genres": [
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"},
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
        ],
        "directors": [],
        "actors": [
            {
                "id": "180df8a0-cd59-4ed8-9346-b109acb1ac69",
                "name": "Robin Atkin Downes",
            },
            {"id": "215e5ef5-6f07-423e-acc6-ac547339be3c", "name": "Tommy Blacha"},
            {"id": "7be89ff1-9e6b-4f4b-9009-c046c5758ac7", "name": "J.J. Villard"},
            {"id": "892a0b35-8d92-40e6-aafc-cf4709d9058e", "name": "Rachel Butera"},
        ],
        "writers": [],
        "actors_names": [
            "J.J. Villard",
            "Rachel Butera",
            "Robin Atkin Downes",
            "Tommy Blacha",
        ],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "b4f69a95-47ae-41f3-b745-4c2baad6abf6",
        "rating": 5.9,
        "title": "Laura's Star and the Mysterious Dragon Nian",
        "description": "",
        "genres": [
            {"id": "55c723c1-6d90-4a04-a44b-e9792040251a", "name": "Family"},
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
        ],
        "directors": [
            {"id": "e3974f7f-90d8-4139-9fdf-d744e2428747", "name": "Piet De Rycker"},
            {"id": "e892c62b-f7f3-4ca9-b4e0-5d2061494a33", "name": "Thilo Rothkirch"},
        ],
        "actors": [
            {"id": "4b00a3a2-bbdc-400e-880b-b4b319b74844", "name": "Sandro Iannotta"},
            {"id": "775d9b14-514e-4cc8-8e8a-9fde3fa03b42", "name": "Mariann Schneider"},
            {"id": "8e34840c-b526-4854-aef6-7e2b61db5b3c", "name": "Annabel Wolf"},
            {"id": "d8fcba86-50f4-4920-baa0-7de25716374f", "name": "Dirk Bach"},
        ],
        "writers": [
            {"id": "1aec9f46-d440-4346-89f9-e3b936b1e811", "name": "Rolf Giesen"},
            {"id": "8b220f7b-0759-496c-9514-3f1f01303585", "name": "Klaus Baumgart"},
            {"id": "e3974f7f-90d8-4139-9fdf-d744e2428747", "name": "Piet De Rycker"},
            {"id": "e892c62b-f7f3-4ca9-b4e0-5d2061494a33", "name": "Thilo Rothkirch"},
        ],
        "actors_names": [
            "Annabel Wolf",
            "Dirk Bach",
            "Mariann Schneider",
            "Sandro Iannotta",
        ],
        "writers_names": [
            "Klaus Baumgart",
            "Piet De Rycker",
            "Rolf Giesen",
            "Thilo Rothkirch",
        ],
        "directors_names": ["Piet De Rycker", "Thilo Rothkirch"],
    },
    {
        "id": "b503ced6-fff1-493a-ad41-73449b55ffee",
        "rating": 8.2,
        "title": "Star Wars: The Clone Wars",
        "description": "Jedi Knights lead the Grand Army of the Republic against the droid army of the Separatists.",
        "genres": [
            {"id": "120a21cf-9097-479e-904a-13dd7198c1dd", "name": "Adventure"},
            {"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"},
            {"id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff", "name": "Action"},
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
            {"id": "6c162475-c7ed-4461-9184-001ef3d9f26e", "name": "Sci-Fi"},
            {"id": "b92ef010-5e4c-4fd0-99d6-41b6456272cd", "name": "Fantasy"},
        ],
        "directors": [],
        "actors": [
            {"id": "5237aac5-f652-4aa5-9061-55bb007cd7be", "name": "Tom Kane"},
            {
                "id": "8746ff78-577b-4bef-a7f7-1db05a102def",
                "name": "James Arnold Taylor",
            },
            {"id": "976fdf00-4f46-429b-af5b-2ddf2ff1b7c5", "name": "Matt Lanter"},
            {"id": "a3468637-c3c3-442c-892e-1625385c49c6", "name": "Dee Bradley Baker"},
        ],
        "writers": [
            {"id": "a5a8f573-3cee-4ccc-8a2b-91cb9f55250a", "name": "George Lucas"}
        ],
        "actors_names": [
            "Dee Bradley Baker",
            "James Arnold Taylor",
            "Matt Lanter",
            "Tom Kane",
        ],
        "writers_names": ["George Lucas"],
        "directors_names": [],
    },
    {
        "id": "b5363f75-138f-4133-b61c-62cf035b4466",
        "rating": 3.8,
        "title": "Shaquille O'neal All-star Comedy Jam: Live from Sin City",
        "description": 'Shaquille O\'Neal presents host Lavell Crawford ("Breaking Bad," Mike and Dave Need Wedding Dates, and American Ultra) with special guests K-Dubb, Cocoa Brown, Donnell Rawlings, and ...',
        "genres": [{"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"}],
        "directors": [
            {"id": "f09c267a-1a38-46c2-8b1a-35721b96ec34", "name": "Leslie Small"}
        ],
        "actors": [
            {"id": "59cf475f-a5de-4707-b704-db8562376549", "name": "Earthquake"},
            {"id": "7f13f7d5-a466-4e99-a961-e6132d1393be", "name": "Donnell Rawlings"},
            {"id": "e92ee037-ace9-4521-9fb8-93d962be4ad8", "name": "Lavell Crawford"},
            {"id": "eb78adbd-6fbe-4f04-9b0e-9dddd07c028c", "name": "Cocoa Brown"},
        ],
        "writers": [],
        "actors_names": [
            "Cocoa Brown",
            "Donnell Rawlings",
            "Earthquake",
            "Lavell Crawford",
        ],
        "writers_names": [],
        "directors_names": ["Leslie Small"],
    },
    {
        "id": "b557615d-adfd-44ed-9312-2a40691eb60f",
        "rating": 7.1,
        "title": "The Untitled Star Wars Mockumentary",
        "description": "",
        "genres": [{"id": "5373d043-3f41-4ea8-9947-4b746c601bbd", "name": "Comedy"}],
        "directors": [
            {"id": "6e13d7e9-e5ff-416a-b73b-8e96fe9c1d01", "name": "Damon Packard"}
        ],
        "actors": [
            {"id": "49988f04-6d06-4497-a652-d0d9c0d711ae", "name": "Daryl Haney"},
            {"id": "4ab27dfc-213f-4c82-afdf-24ecf199d98a", "name": "Tony Curtis"},
            {"id": "6e13d7e9-e5ff-416a-b73b-8e96fe9c1d01", "name": "Damon Packard"},
            {"id": "87750e5b-bd9b-48c5-8ac6-5963c0aa25e7", "name": "Shawn Yanez"},
        ],
        "writers": [],
        "actors_names": ["Damon Packard", "Daryl Haney", "Shawn Yanez", "Tony Curtis"],
        "writers_names": [],
        "directors_names": ["Damon Packard"],
    },
    {
        "id": "b56e8825-7551-4117-b05b-0b7b0bd4829b",
        "rating": 4.2,
        "title": "Rising Star",
        "description": "For the first time, a musical talent show, in which the viewers vote through the application during the song.",
        "genres": [
            {"id": "56b541ab-4d66-4021-8708-397762bff2d4", "name": "Music"},
            {"id": "e508c1c8-24c0-4136-80b4-340c4befb190", "name": "Reality-TV"},
        ],
        "directors": [],
        "actors": [
            {"id": "6385ea57-8f4d-4366-ba5b-c917a75c4d07", "name": "Rani Rahav"},
            {"id": "81fa75fa-0845-440e-998d-1729fa61300b", "name": "Assi Azar"},
            {"id": "84c551fb-4f75-4445-81ff-b8b5dcce9b03", "name": "Zvika Hadar"},
            {"id": "df199312-275e-4d1e-83cb-8f96bc5d64fb", "name": "Rita"},
        ],
        "writers": [],
        "actors_names": ["Assi Azar", "Rani Rahav", "Rita", "Zvika Hadar"],
        "writers_names": [],
        "directors_names": [],
    },
    {
        "id": "b5709473-9df9-4c67-b1d5-7e1980e5ba2e",
        "rating": 5.9,
        "title": "Star Wars Episode V 1/2: The Han Solo Affair",
        "description": 'Lego stop motion short that takes place in the 3 minutes after Han Solo is frozen in carbonite. A comical game of "keep away" begins.',
        "genres": [
            {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
            {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
        ],
        "directors": [
            {"id": "452e9c9c-800a-4493-a106-d0c3bde03b46", "name": "Tim Drage"},
            {"id": "c55814e3-22f5-4eac-8c95-1efbdc114b71", "name": "Tony Mines"},
        ],
        "actors": [],
        "writers": [
            {"id": "452e9c9c-800a-4493-a106-d0c3bde03b46", "name": "Tim Drage"},
            {"id": "c55814e3-22f5-4eac-8c95-1efbdc114b71", "name": "Tony Mines"},
        ],
        "actors_names": [],
        "writers_names": ["Tim Drage", "Tony Mines"],
        "directors_names": ["Tim Drage", "Tony Mines"],
    },
]

EXPECTED_FILM_DETAILS_RESPONSE = {
    "id": "a801e84c-316a-4c0c-a5a5-cc024234b2cb",
    "rating": 6.5,
    "title": "Kre-O Star Trek",
    "description": "A stop-motion animated story about 'Star Trek' featuring Kre-O toy blocks.",
    "genres": [
        {"id": "6a0a479b-cfec-41ac-b520-41b2b007b611", "name": "Animation"},
        {"id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395", "name": "Short"},
    ],
    "directors": [],
    "actors": [],
    "writers": [],
    "actors_names": [],
    "writers_names": [],
    "directors_names": [],
}