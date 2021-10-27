from pathlib import Path

import orjson

TEST_CONTAINER_SRC_DIR_PATH = Path("/code/tests/functional/testdata/")

with open(TEST_CONTAINER_SRC_DIR_PATH / "films_list.json", encoding="utf-8") as file:
    LIST_FILMS_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "film_details.json", encoding="utf-8") as file:
    FILM_DETAILS_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "film_search_list.json", encoding="utf-8") as file:
    LIST_FILMS_SEARCH_ES_RESPONSE = orjson.loads(file.read())

EXPECTED_LIST_SEARCH_FILMS_RESPONSE = [
    {
        "id": "1d2fb7ce-8b65-4c71-87d8-bea2dfc36a75",
        "rating": 8.6,
        "title": "2011 NBA All-Star Game",
        "description": "A documented movie about the 2011 All-star game which was held in Los Angeles, California. The game was held February 20, 2011 and was broadcasted by TNT.",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "555d9dcd-2733-4bb5-b62a-b58d2b43465f",
                "name": "Ray Allen"
            },
            {
                "id": "8a6fb388-e67c-4e29-8580-8d8db578c5fe",
                "name": "Kobe Bryant"
            },
            {
                "id": "b3cfe2e6-859f-4ae9-a6a3-457fd65d95c1",
                "name": "Carmelo Anthony"
            },
            {
                "id": "fd1f5117-8138-4a25-a9c4-5e26450f122e",
                "name": "Chris Bosh"
            }
        ],
        "writers": [],
        "actors_names": [
            "Carmelo Anthony",
            "Chris Bosh",
            "Kobe Bryant",
            "Ray Allen"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "e49c02da-e7ee-4da7-bae4-538a5dc7c0f2",
        "rating": 7.6,
        "title": "1987 NBA All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "05c64f45-d003-4748-b591-91b5b2a61c9c",
                "name": "Charles Barkley"
            },
            {
                "id": "18cc968f-11d0-401e-9740-bfc64080d32e",
                "name": "Larry Bird"
            },
            {
                "id": "4df78934-ac20-431d-8d45-6cebff0c9c6a",
                "name": "Mark Aguirre"
            },
            {
                "id": "7abc1fe0-73e5-4d84-b78a-ed386dca8c64",
                "name": "Kareem Abdul-Jabbar"
            }
        ],
        "writers": [],
        "actors_names": [
            "Charles Barkley",
            "Kareem Abdul-Jabbar",
            "Larry Bird",
            "Mark Aguirre"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "667dbe90-4648-47fc-83a9-ca7c71392a4e",
        "rating": 7.2,
        "title": "2001 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "588d0675-3159-4142-8b1b-5c0a29a909c7",
                "name": "Jeanne Zelasko"
            },
            {
                "id": "7b0c328c-53b0-4cb1-abb3-cca0e5a0b0ec",
                "name": "Joe Buck"
            },
            {
                "id": "b8824198-efb9-4869-972f-e7f3b9e3dd90",
                "name": "Steve Lyons"
            },
            {
                "id": "c144ced4-4740-4863-83da-c091bd58ef11",
                "name": "Tim McCarver"
            }
        ],
        "writers": [],
        "actors_names": [
            "Jeanne Zelasko",
            "Joe Buck",
            "Steve Lyons",
            "Tim McCarver"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "a0bdd4e7-84a0-4ec5-9dae-0d16371dc303",
        "rating": 7,
        "title": "2002 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [
            {
                "id": "1f0fa70c-45da-4037-bc54-eaf0143f80ae",
                "name": "Bill Webb"
            }
        ],
        "actors": [
            {
                "id": "588d0675-3159-4142-8b1b-5c0a29a909c7",
                "name": "Jeanne Zelasko"
            },
            {
                "id": "7b0c328c-53b0-4cb1-abb3-cca0e5a0b0ec",
                "name": "Joe Buck"
            },
            {
                "id": "a66c3dca-8d64-4406-b577-012019850678",
                "name": "Kevin Kennedy"
            },
            {
                "id": "c144ced4-4740-4863-83da-c091bd58ef11",
                "name": "Tim McCarver"
            }
        ],
        "writers": [],
        "actors_names": [
            "Jeanne Zelasko",
            "Joe Buck",
            "Kevin Kennedy",
            "Tim McCarver"
        ],
        "writers_names": [],
        "directors_names": [
            "Bill Webb"
        ]
    },
    {
        "id": "efb73bf5-9b65-453e-a627-3435e0c11904",
        "rating": 7.2,
        "title": "2004 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [
            {
                "id": "1f0fa70c-45da-4037-bc54-eaf0143f80ae",
                "name": "Bill Webb"
            }
        ],
        "actors": [
            {
                "id": "588d0675-3159-4142-8b1b-5c0a29a909c7",
                "name": "Jeanne Zelasko"
            },
            {
                "id": "7b0c328c-53b0-4cb1-abb3-cca0e5a0b0ec",
                "name": "Joe Buck"
            },
            {
                "id": "a66c3dca-8d64-4406-b577-012019850678",
                "name": "Kevin Kennedy"
            },
            {
                "id": "c144ced4-4740-4863-83da-c091bd58ef11",
                "name": "Tim McCarver"
            }
        ],
        "writers": [],
        "actors_names": [
            "Jeanne Zelasko",
            "Joe Buck",
            "Kevin Kennedy",
            "Tim McCarver"
        ],
        "writers_names": [],
        "directors_names": [
            "Bill Webb"
        ]
    },
    {
        "id": "2f2486ba-23b2-46c8-90e7-bf0680f2e482",
        "rating": 6.6,
        "title": "2000 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "1412a101-8ae1-4d21-b44a-23e66c8c71ba",
                "name": "Jim Gray"
            },
            {
                "id": "1d66e258-b327-4b2c-b946-acdcf7436fd4",
                "name": "Joe Morgan"
            },
            {
                "id": "947748ec-e90f-4c8f-bd43-594700d33dbc",
                "name": "Bob Costas"
            },
            {
                "id": "b757060b-dffd-4f9c-956f-ca34fff4a231",
                "name": "Hannah Storm"
            }
        ],
        "writers": [],
        "actors_names": [
            "Bob Costas",
            "Hannah Storm",
            "Jim Gray",
            "Joe Morgan"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "2c009dda-f637-4a7a-a3e2-9419ca0ad6e6",
        "rating": 7.8,
        "title": "2005 MLB All-Star Game",
        "description": "In the annual mid-summer game between the American League and National League, the AL defeats the NL 7-5 to extend their record in the last nine All-Star Games to 8-0-1.",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [
            {
                "id": "1f0fa70c-45da-4037-bc54-eaf0143f80ae",
                "name": "Bill Webb"
            }
        ],
        "actors": [
            {
                "id": "588d0675-3159-4142-8b1b-5c0a29a909c7",
                "name": "Jeanne Zelasko"
            },
            {
                "id": "7b0c328c-53b0-4cb1-abb3-cca0e5a0b0ec",
                "name": "Joe Buck"
            },
            {
                "id": "a66c3dca-8d64-4406-b577-012019850678",
                "name": "Kevin Kennedy"
            },
            {
                "id": "c144ced4-4740-4863-83da-c091bd58ef11",
                "name": "Tim McCarver"
            }
        ],
        "writers": [],
        "actors_names": [
            "Jeanne Zelasko",
            "Joe Buck",
            "Kevin Kennedy",
            "Tim McCarver"
        ],
        "writers_names": [],
        "directors_names": [
            "Bill Webb"
        ]
    },
    {
        "id": "80e23a27-2306-4734-9987-c76d229e8d2a",
        "rating": 7.7,
        "title": "1997 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [
            {
                "id": "1f0fa70c-45da-4037-bc54-eaf0143f80ae",
                "name": "Bill Webb"
            }
        ],
        "actors": [
            {
                "id": "1a484b73-3207-4191-b1f3-23f9da801c81",
                "name": "Chip Caray"
            },
            {
                "id": "520b977a-430f-4e4f-84df-874ed742b1da",
                "name": "Bob Brenly"
            },
            {
                "id": "7b0c328c-53b0-4cb1-abb3-cca0e5a0b0ec",
                "name": "Joe Buck"
            },
            {
                "id": "c144ced4-4740-4863-83da-c091bd58ef11",
                "name": "Tim McCarver"
            }
        ],
        "writers": [],
        "actors_names": [
            "Bob Brenly",
            "Chip Caray",
            "Joe Buck",
            "Tim McCarver"
        ],
        "writers_names": [],
        "directors_names": [
            "Bill Webb"
        ]
    },
    {
        "id": "97bddcae-bf97-4c4f-be11-f0d7e060c230",
        "rating": 6.4,
        "title": "2007 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "3eb7aee7-d4f9-4901-a427-902a02866aed",
                "name": "Ken Rosenthal"
            },
            {
                "id": "7b0c328c-53b0-4cb1-abb3-cca0e5a0b0ec",
                "name": "Joe Buck"
            },
            {
                "id": "c144ced4-4740-4863-83da-c091bd58ef11",
                "name": "Tim McCarver"
            },
            {
                "id": "f84e2365-d9e8-4ba1-8e00-78f4ba510d8a",
                "name": "Jose Mota"
            }
        ],
        "writers": [],
        "actors_names": [
            "Joe Buck",
            "Jose Mota",
            "Ken Rosenthal",
            "Tim McCarver"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "a5ae834a-050e-44ac-9dae-071f41b6fe8f",
        "rating": 7.5,
        "title": "1999 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [
            {
                "id": "1f0fa70c-45da-4037-bc54-eaf0143f80ae",
                "name": "Bill Webb"
            }
        ],
        "actors": [
            {
                "id": "5d06cf88-2846-468f-9438-b352b37f5373",
                "name": "Brad Ausmus"
            },
            {
                "id": "5fd14f68-e7da-485c-b0e2-8c308df998f3",
                "name": "Andy Ashby"
            },
            {
                "id": "a020f921-e16c-4be9-9da4-b4b7e778507a",
                "name": "Jeff Bagwell"
            },
            {
                "id": "b1ec6d73-7a89-4765-8f28-b7890f410e5b",
                "name": "Roberto Alomar"
            }
        ],
        "writers": [],
        "actors_names": [
            "Andy Ashby",
            "Brad Ausmus",
            "Jeff Bagwell",
            "Roberto Alomar"
        ],
        "writers_names": [],
        "directors_names": [
            "Bill Webb"
        ]
    },
    {
        "id": "d2e3536d-07f7-490d-9801-e69253ab518e",
        "rating": 7.6,
        "title": "1998 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "1412a101-8ae1-4d21-b44a-23e66c8c71ba",
                "name": "Jim Gray"
            },
            {
                "id": "1d66e258-b327-4b2c-b946-acdcf7436fd4",
                "name": "Joe Morgan"
            },
            {
                "id": "947748ec-e90f-4c8f-bd43-594700d33dbc",
                "name": "Bob Costas"
            },
            {
                "id": "b757060b-dffd-4f9c-956f-ca34fff4a231",
                "name": "Hannah Storm"
            }
        ],
        "writers": [],
        "actors_names": [
            "Bob Costas",
            "Hannah Storm",
            "Jim Gray",
            "Joe Morgan"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "92f303c3-58f4-41bf-b5db-e00f0e6f70a7",
        "rating": 7.8,
        "title": "2008 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "115e88bc-1f74-4694-a78c-bdaf59cf6e2a",
                "name": "Ernie Banks"
            },
            {
                "id": "76223485-e9d7-4ae6-bfe7-78d88f6af5ea",
                "name": "Bob Apodaca"
            },
            {
                "id": "e19de701-5463-46e7-8f57-d1421e305064",
                "name": "Luis Aparicio"
            },
            {
                "id": "e5fa268b-62ad-4d49-95e1-dbfc8df6124d",
                "name": "Hank Aaron"
            }
        ],
        "writers": [],
        "actors_names": [
            "Bob Apodaca",
            "Ernie Banks",
            "Hank Aaron",
            "Luis Aparicio"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "63401833-6692-4d9a-aaa0-de803a92b64d",
        "rating": 6.9,
        "title": "2003 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "588d0675-3159-4142-8b1b-5c0a29a909c7",
                "name": "Jeanne Zelasko"
            },
            {
                "id": "7b0c328c-53b0-4cb1-abb3-cca0e5a0b0ec",
                "name": "Joe Buck"
            },
            {
                "id": "a66c3dca-8d64-4406-b577-012019850678",
                "name": "Kevin Kennedy"
            },
            {
                "id": "c144ced4-4740-4863-83da-c091bd58ef11",
                "name": "Tim McCarver"
            }
        ],
        "writers": [],
        "actors_names": [
            "Jeanne Zelasko",
            "Joe Buck",
            "Kevin Kennedy",
            "Tim McCarver"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "6ab2d71d-106c-4af8-bbec-822a87f94909",
        "rating": 7.2,
        "title": "2006 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "3eb7aee7-d4f9-4901-a427-902a02866aed",
                "name": "Ken Rosenthal"
            },
            {
                "id": "588d0675-3159-4142-8b1b-5c0a29a909c7",
                "name": "Jeanne Zelasko"
            },
            {
                "id": "7b0c328c-53b0-4cb1-abb3-cca0e5a0b0ec",
                "name": "Joe Buck"
            },
            {
                "id": "c144ced4-4740-4863-83da-c091bd58ef11",
                "name": "Tim McCarver"
            }
        ],
        "writers": [],
        "actors_names": [
            "Jeanne Zelasko",
            "Joe Buck",
            "Ken Rosenthal",
            "Tim McCarver"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "d0e7e53a-8de1-4a21-b869-4ff8fc0e846e",
        "rating": 6.5,
        "title": "1983 MLB All-Star Game",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "45190b38-35c8-4ae4-b94d-42febc145096",
                "name": "Joe Garagiola"
            },
            {
                "id": "947748ec-e90f-4c8f-bd43-594700d33dbc",
                "name": "Bob Costas"
            },
            {
                "id": "b3538c40-d28f-4ba9-9784-34ba952904ab",
                "name": "Vin Scully"
            },
            {
                "id": "d6e4407c-afc7-4e22-b9b7-7fbfb04df455",
                "name": "Joe Altobelli"
            }
        ],
        "writers": [],
        "actors_names": [
            "Bob Costas",
            "Joe Altobelli",
            "Joe Garagiola",
            "Vin Scully"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "c604ca5d-4d07-4412-a7f6-ebb3942232b5",
        "rating": 8.3,
        "title": "Star Wars Celebration 2017",
        "description": "",
        "genres": [
            {
                "id": "6c162475-c7ed-4461-9184-001ef3d9f26e",
                "name": "Sci-Fi"
            },
            {
                "id": "e508c1c8-24c0-4136-80b4-340c4befb190",
                "name": "Reality-TV"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "3c883480-9803-4c77-a0b3-a6c91244e674",
                "name": "Anthony Carboni"
            },
            {
                "id": "4903bbf3-2413-4cc9-9c67-32c55b398445",
                "name": "Andi Gutierrez"
            },
            {
                "id": "86f1f44b-39f5-41a6-8b3b-af5a9ed09858",
                "name": "Anthony Daniels"
            },
            {
                "id": "c5664b88-7286-4b38-9a3c-3f3cc6f72e9e",
                "name": "Warwick Davis"
            }
        ],
        "writers": [],
        "actors_names": [
            "Andi Gutierrez",
            "Anthony Carboni",
            "Anthony Daniels",
            "Warwick Davis"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "3e21bf14-ae47-40f0-b71d-459ec61eb4f8",
        "rating": 6.6,
        "title": "Star Trek: The Game Show",
        "description": "You are stuck in the middle of one of Q's games as he makes you answer trivia about the 20th Century television science fiction phenomenon 'Star Trek'.",
        "genres": [
            {
                "id": "55c723c1-6d90-4a04-a44b-e9792040251a",
                "name": "Family"
            },
            {
                "id": "fb58fd7f-7afd-447f-b833-e51e45e2a778",
                "name": "Game-Show"
            }
        ],
        "directors": [
            {
                "id": "c8f4604d-b730-4b13-8588-92356bc22600",
                "name": "H. Quinn"
            }
        ],
        "actors": [
            {
                "id": "1ce3e209-51b7-40f6-adfd-d4b0305d1bd9",
                "name": "John de Lancie"
            },
            {
                "id": "c540c6d9-e110-4fec-a733-b90a18f3158a",
                "name": "Doug Stone"
            },
            {
                "id": "da271596-f7c8-40d5-8c22-9fb0c9e6dac6",
                "name": "Karen Cornwell"
            },
            {
                "id": "f042db61-c492-4aae-9369-c1bb859dfc3d",
                "name": "T. Buffalo Wagnon"
            }
        ],
        "writers": [
            {
                "id": "61c4071b-6f1e-4897-992f-72f132226f83",
                "name": "Tim Lynch"
            },
            {
                "id": "66ecc6d1-0b9a-4b6c-ad6f-5ad4db4aed57",
                "name": "Jim Wright"
            },
            {
                "id": "94ecddc6-badc-423f-b689-c3bef21ec348",
                "name": "Lisa Hazard"
            },
            {
                "id": "a174c4f1-ff80-4762-bc60-8c11b7da2d38",
                "name": "Chairman Barnes"
            },
            {
                "id": "a444a1a8-a77a-46d0-b0e0-5321bd688238",
                "name": "Alex Rosensweig"
            },
            {
                "id": "c8f4604d-b730-4b13-8588-92356bc22600",
                "name": "H. Quinn"
            },
            {
                "id": "cf709a32-7df1-462d-b1be-2f3dc2496b20",
                "name": "Ahna Wagnon"
            }
        ],
        "actors_names": [
            "Doug Stone",
            "John de Lancie",
            "Karen Cornwell",
            "T. Buffalo Wagnon"
        ],
        "writers_names": [
            "Ahna Wagnon",
            "Alex Rosensweig",
            "Chairman Barnes",
            "H. Quinn",
            "Jim Wright",
            "Lisa Hazard",
            "Tim Lynch"
        ],
        "directors_names": [
            "H. Quinn"
        ]
    },
    {
        "id": "ded3515c-3220-42f4-9ec6-0d04556229e9",
        "rating": 8.1,
        "title": "All-Star Party for Lucille Ball",
        "description": "Variety Clubs International hosted this tribute to Lucille ball. It brought Lucy and her husband, Gary Morton together on their anniversary, to present her with a humanitarian award. Lucy ...",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            }
        ],
        "directors": [
            {
                "id": "cc2b4b6e-c5b7-4b96-8a5b-25b05f682659",
                "name": "Dick McDonough"
            }
        ],
        "actors": [
            {
                "id": "02c9eac3-83a1-453b-83a4-da6f20c3d729",
                "name": "James Caan"
            },
            {
                "id": "4ba3ab95-b70a-4ab7-ad0d-636a4c3c4906",
                "name": "Lucie Arnaz"
            },
            {
                "id": "6f93e82d-56ad-40a1-b3fc-393543de5073",
                "name": "Desi Arnaz Jr."
            },
            {
                "id": "e22f0a9a-cd7c-4937-a44c-648b4a12f193",
                "name": "Lucille Ball"
            }
        ],
        "writers": [
            {
                "id": "c17de384-8c55-46d8-b993-ee24e239d28e",
                "name": "Paul Keyes"
            }
        ],
        "actors_names": [
            "Desi Arnaz Jr.",
            "James Caan",
            "Lucie Arnaz",
            "Lucille Ball"
        ],
        "writers_names": [
            "Paul Keyes"
        ],
        "directors_names": [
            "Dick McDonough"
        ]
    },
    {
        "id": "d569ac4e-4e9f-4dcd-af3b-8267118d4664",
        "rating": 5.8,
        "title": "Shaquille O'Neal Presents: All-Star Comedy Jam - Live from Dallas",
        "description": "Academy Award winner and one of the Original Queens of Comedy, Mo'Nique rules the stage as host of the 3rd installment in Shaquille O'Neal's All Star Comedy Jam concert series. Filmed in front of a live audience during the 2010 NBA All-Star Weekend in Dallas Texas, comedy queen Mo'Nique leads her court with some of the industry's most talented and sought after comedians. No topic is off limits on this night at AEG's Nokia Theatre stage. Seasoned comedians, Paul Mooney, Corey Holcomb, George Willborn and Michael Blackson deliver side busting, non-stop laughs in this energetic and memorable night of comedy.",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            }
        ],
        "directors": [
            {
                "id": "f09c267a-1a38-46c2-8b1a-35721b96ec34",
                "name": "Leslie Small"
            }
        ],
        "actors": [
            {
                "id": "7b2cede0-b37e-4c64-8b7c-5a5ca1c7027d",
                "name": "Paul Mooney"
            },
            {
                "id": "8ce7450e-c296-4fc5-b6e5-6c7e1626b231",
                "name": "Michael Blackson"
            },
            {
                "id": "a9e7d5ad-b790-47d1-9808-322a16459a2a",
                "name": "Mo'Nique"
            },
            {
                "id": "e958b222-4888-4791-b0b5-20d873b6f224",
                "name": "Corey Holcomb"
            }
        ],
        "writers": [],
        "actors_names": [
            "Corey Holcomb",
            "Michael Blackson",
            "Mo'Nique",
            "Paul Mooney"
        ],
        "writers_names": [],
        "directors_names": [
            "Leslie Small"
        ]
    },
    {
        "id": "96bf7310-dbd3-4372-924d-bf920f38276d",
        "rating": 7.5,
        "title": "Disney Channel New Year Star Showdown",
        "description": "Bring in 2010 with Disney channel stars as they compete in game show challenges and we countdown 2009's favorite music videos.",
        "genres": [
            {
                "id": "55c723c1-6d90-4a04-a44b-e9792040251a",
                "name": "Family"
            }
        ],
        "directors": [
            {
                "id": "9221d30e-64dd-4a01-9e42-3d0c22df9a78",
                "name": "Art Spigel"
            }
        ],
        "actors": [
            {
                "id": "313b425b-0138-4e97-b020-903a36fed527",
                "name": "Leo Howard"
            },
            {
                "id": "4d7fc098-b25e-44b2-9710-86ec2ace999e",
                "name": "David Henrie"
            },
            {
                "id": "505bb0ee-86b5-4ed2-832a-d1f3f456cb17",
                "name": "Selena Gomez"
            },
            {
                "id": "afef5d90-0a17-4031-825e-1f7571c35621",
                "name": "Nicole Gale Anderson"
            }
        ],
        "writers": [
            {
                "id": "6863e0ca-65b7-472b-b5bf-9f4ae4100836",
                "name": "Brian Alexander"
            }
        ],
        "actors_names": [
            "David Henrie",
            "Leo Howard",
            "Nicole Gale Anderson",
            "Selena Gomez"
        ],
        "writers_names": [
            "Brian Alexander"
        ],
        "directors_names": [
            "Art Spigel"
        ]
    },
    {
        "id": "daae47e4-cbd0-4ffd-a150-55201b357d5b",
        "rating": 8.2,
        "title": "Lego Star Wars: The Video Game",
        "description": "Play through the star wars prequel trilogy in episodes 1,2,and 3, in lego.",
        "genres": [
            {
                "id": "120a21cf-9097-479e-904a-13dd7198c1dd",
                "name": "Adventure"
            },
            {
                "id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff",
                "name": "Action"
            },
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            }
        ],
        "directors": [
            {
                "id": "b505845f-d7bc-4271-a59d-5dc16a641cac",
                "name": "Jon Burton"
            }
        ],
        "actors": [
            {
                "id": "509c1168-0ced-4704-a3b9-f17b9dc37667",
                "name": "Lindsay Duncan"
            },
            {
                "id": "62df10e8-244d-4c31-b396-564dfbc2f9c5",
                "name": "Hayden Christensen"
            },
            {
                "id": "746b394f-7808-4386-a281-b06504c07b58",
                "name": "Ahmed Best"
            },
            {
                "id": "86f1f44b-39f5-41a6-8b3b-af5a9ed09858",
                "name": "Anthony Daniels"
            }
        ],
        "writers": [
            {
                "id": "a5a8f573-3cee-4ccc-8a2b-91cb9f55250a",
                "name": "George Lucas"
            }
        ],
        "actors_names": [
            "Ahmed Best",
            "Anthony Daniels",
            "Hayden Christensen",
            "Lindsay Duncan"
        ],
        "writers_names": [
            "George Lucas"
        ],
        "directors_names": [
            "Jon Burton"
        ]
    },
    {
        "id": "2c856df1-be00-46ff-b9c7-f9e880d6f4c7",
        "rating": 6.9,
        "title": "Wyclef Jean: All Star Jam at Carnegie Hall",
        "description": "The show is fronted by Wyclef Jean and features guest appearances from a stellar line up of guests including Eric Clapton, Stevie Wonder, Destiny's Child, Macy Gray, Marc Anthony, Charlotte Church, Third World and Mary J Blige",
        "genres": [
            {
                "id": "56b541ab-4d66-4021-8708-397762bff2d4",
                "name": "Music"
            }
        ],
        "directors": [
            {
                "id": "3e4281de-2b49-4e94-a250-c497fc1767f5",
                "name": "Bud Schaetzle"
            }
        ],
        "actors": [
            {
                "id": "07c0d420-1a93-4a26-b0eb-5b8e671f36bc",
                "name": "Marc Anthony"
            },
            {
                "id": "1f7e393e-b862-4a24-99bc-bcd9f4e03980",
                "name": "Eric Clapton"
            },
            {
                "id": "ce080bbf-578b-4049-a29e-bd2965b1c9fa",
                "name": "Mary J. Blige"
            },
            {
                "id": "d86807ce-eed5-4271-98ee-142f82619d2d",
                "name": "Destiny's Child"
            }
        ],
        "writers": [
            {
                "id": "3e4281de-2b49-4e94-a250-c497fc1767f5",
                "name": "Bud Schaetzle"
            }
        ],
        "actors_names": [
            "Destiny's Child",
            "Eric Clapton",
            "Marc Anthony",
            "Mary J. Blige"
        ],
        "writers_names": [
            "Bud Schaetzle"
        ],
        "directors_names": [
            "Bud Schaetzle"
        ]
    },
    {
        "id": "87c64348-61a0-4e6c-99c5-a6bd8b0bcbc3",
        "rating": 8,
        "title": "A Star Named Ayrton Senna",
        "description": "The Official Film of Brazil's greatest Formula One driver, Ayrton Senna, who's sudden death in the 1994 San Marino Grand Prix sent shock waves around the World. It cemented his reputation both within the sport, and his native Brazil, as a legend. The film looks at his life and career using archive footage and featuring revealing interviews with the man, as well as those who knew him well; friends, family and competitors. It also shows how the Ayrton Senna Foundation, set up in his honor, is working to help under privileged and street-bound children in his native Brazil using sport as an incentive to learn.",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            },
            {
                "id": "6d141ad2-d407-4252-bda4-95590aaf062a",
                "name": "Documentary"
            },
            {
                "id": "ca124c76-9760-4406-bfa0-409b1e38d200",
                "name": "Biography"
            }
        ],
        "directors": [
            {
                "id": "6c615482-994c-4f66-8ed3-f931ea615056",
                "name": "Jean Claude Guiter"
            }
        ],
        "actors": [
            {
                "id": "0398c6b9-ef70-4222-969e-d33459c4fde0",
                "name": "Jean Alesi"
            },
            {
                "id": "66c3c3a3-9b4e-42fa-a390-2442f8689985",
                "name": "Juan Manuel Fangio"
            },
            {
                "id": "87229db6-4a52-49f2-a4fb-2249142bd65b",
                "name": "Martin Brundle"
            },
            {
                "id": "9e1ea10f-fbcb-4332-990b-ec1ea8536c2e",
                "name": "Alain Prost"
            }
        ],
        "writers": [],
        "actors_names": [
            "Alain Prost",
            "Jean Alesi",
            "Juan Manuel Fangio",
            "Martin Brundle"
        ],
        "writers_names": [],
        "directors_names": [
            "Jean Claude Guiter"
        ]
    },
    {
        "id": "22cd1a60-c386-462f-b5a3-e421b354226f",
        "rating": 7,
        "title": "All-Star Academy",
        "description": "Together, Alex Guarnaschelli, Bobby Flay, Michael Symon and Curtis Stone make up one of the fiercest foursomes in culinary competitions. In this series, they will battle it out in the kitchen, as mentor versus mentor with teams of shining home cooks.",
        "genres": [
            {
                "id": "e508c1c8-24c0-4136-80b4-340c4befb190",
                "name": "Reality-TV"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "01ea2ac8-69e1-4967-be2b-117b5c409b70",
                "name": "Ted Allen"
            },
            {
                "id": "a7595efe-5c65-42e6-a092-8e8879bd4b67",
                "name": "Curtis Stone"
            },
            {
                "id": "e8c5660b-74ca-4082-b69f-c8c7ffd4d19e",
                "name": "Robert Irvine"
            },
            {
                "id": "eabb5a83-08dc-41a0-9075-b33e9f439f1c",
                "name": "Alex Guarnaschelli"
            }
        ],
        "writers": [],
        "actors_names": [
            "Alex Guarnaschelli",
            "Curtis Stone",
            "Robert Irvine",
            "Ted Allen"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "9c7dc26a-489d-4c08-9bba-6ae9dc8117f1",
        "rating": 7,
        "title": "All-Star Superman",
        "description": "While saving the crew of the first manned mission to the sun, Superman is poisoned by solar radiation. Dying, he decides to fulfill his lifelong dreams, while still saving the Earth from various threats. But when Lex Luthor reveals his latest plot to control the world, Superman must use his remaining strength to stop him.",
        "genres": [
            {
                "id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff",
                "name": "Action"
            },
            {
                "id": "6a0a479b-cfec-41ac-b520-41b2b007b611",
                "name": "Animation"
            },
            {
                "id": "6c162475-c7ed-4461-9184-001ef3d9f26e",
                "name": "Sci-Fi"
            }
        ],
        "directors": [
            {
                "id": "200a8ad1-fe5a-4246-a31c-57902b000613",
                "name": "Sam Liu"
            }
        ],
        "actors": [
            {
                "id": "477c81a7-4caf-4ce3-b354-831169a1a068",
                "name": "James Denton"
            },
            {
                "id": "78e917f3-a80b-4d44-82f4-80712a4160ee",
                "name": "Anthony LaPaglia"
            },
            {
                "id": "c05bfb01-60d1-42c7-b372-62bc0a916abf",
                "name": "Christina Hendricks"
            },
            {
                "id": "eac1449e-09ed-4912-8467-fba3d489c6bb",
                "name": "Edward Asner"
            }
        ],
        "writers": [
            {
                "id": "1f651d3f-b94a-4bc3-9a7d-68d79848124b",
                "name": "Joe Shuster"
            },
            {
                "id": "618ed131-f181-4932-b3cb-e637a87d594e",
                "name": "Jerry Siegel"
            },
            {
                "id": "7754f297-7531-4d31-9ae4-b46100a54982",
                "name": "Grant Morrison"
            },
            {
                "id": "9b401777-277e-40a2-8e69-cf6561b987ed",
                "name": "Frank Quitely"
            },
            {
                "id": "cff61032-be90-44b6-85e2-c0fd6049440c",
                "name": "Dwayne McDuffie"
            }
        ],
        "actors_names": [
            "Anthony LaPaglia",
            "Christina Hendricks",
            "Edward Asner",
            "James Denton"
        ],
        "writers_names": [
            "Dwayne McDuffie",
            "Frank Quitely",
            "Grant Morrison",
            "Jerry Siegel",
            "Joe Shuster"
        ],
        "directors_names": [
            "Sam Liu"
        ]
    },
    {
        "id": "c11df3f1-8b6a-4899-82f1-67a1c326a4b4",
        "rating": 8.2,
        "title": "All Star Revue",
        "description": "This early comedy program started off with a rotating cast of four famous comedians, each of whom would take turns hosting the show. The program format was similar to that of a Vaudeville show or stage revue, with the prestige of the hosts enabling the show to bring in equally well-known talent for individual performances. As more hosts were added to the program's roster, the name was changed to \"All Star Revue\".",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "0d5b894f-25fe-4bb1-b04c-a59fc4f65b95",
                "name": "Jack Roth"
            },
            {
                "id": "4beb6833-9550-423a-a5c1-f3a46f8bc2b8",
                "name": "Eddie Jackson"
            },
            {
                "id": "4fa74dfb-5bbf-439e-bda2-b9c7a2feb199",
                "name": "Jimmy Durante"
            },
            {
                "id": "5f9b5959-31fc-43ba-8ab5-9551c34cd617",
                "name": "Danny Thomas"
            }
        ],
        "writers": [],
        "actors_names": [
            "Danny Thomas",
            "Eddie Jackson",
            "Jack Roth",
            "Jimmy Durante"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "1ca9a4b7-d78d-4cee-b590-c99c063bbd67",
        "rating": 5.8,
        "title": "All-Star Vaudeville",
        "description": "A miniature vaudeville show, complete with a title card introducing each act, is presented. First up is The On-Wah Troupe, an East Asian group of contortionists. Next, Blossom Seeley and Benny Fields sing a duet of the song, \"Why Don't You Practice What You Preach\". Third up, father and son Pat Rooney and Pat Rooney Jr. perform a recitation and dance musing about if they will ever be as clever as their dad. And the last act on the bill is The Runaway Four, a group of comic acrobats.",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            },
            {
                "id": "56b541ab-4d66-4021-8708-397762bff2d4",
                "name": "Music"
            },
            {
                "id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395",
                "name": "Short"
            }
        ],
        "directors": [
            {
                "id": "57b6ba69-8fbd-41d2-9c4f-1e826a81e91b",
                "name": "Roy Mack"
            }
        ],
        "actors": [
            {
                "id": "317e3123-866a-48ad-b284-7ccacbabfd2e",
                "name": "Blossom Seeley"
            },
            {
                "id": "9fe4e4be-4961-4a08-93ad-f4ceb8fd2fd5",
                "name": "Pat Rooney"
            },
            {
                "id": "ce4fa822-0aa7-44ba-9fdd-ac39e76e99f6",
                "name": "Pat Rooney Jr."
            },
            {
                "id": "f0dbc382-b14e-4335-ab48-077acfdea6bd",
                "name": "Benny Fields"
            }
        ],
        "writers": [],
        "actors_names": [
            "Benny Fields",
            "Blossom Seeley",
            "Pat Rooney",
            "Pat Rooney Jr."
        ],
        "writers_names": [],
        "directors_names": [
            "Roy Mack"
        ]
    },
    {
        "id": "73ecd1e6-6326-405a-b51b-69008f383b72",
        "rating": 8.5,
        "title": "Lego Star Wars: The Complete Saga",
        "description": "In Lego Star Wars: The Complete Saga, you can now experience all 6 episodes at once. Containing the same levels and locations. Only with newer features and improvements. Such as more extras to unlock, more vehicles to build, new playable characters, & a better customizing Lego character feature. Now all Lego & Star Wars fans alike can experience this game more than it's successors.",
        "genres": [
            {
                "id": "120a21cf-9097-479e-904a-13dd7198c1dd",
                "name": "Adventure"
            },
            {
                "id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff",
                "name": "Action"
            },
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            }
        ],
        "directors": [
            {
                "id": "b505845f-d7bc-4271-a59d-5dc16a641cac",
                "name": "Jon Burton"
            }
        ],
        "actors": [
            {
                "id": "746b394f-7808-4386-a281-b06504c07b58",
                "name": "Ahmed Best"
            },
            {
                "id": "86f1f44b-39f5-41a6-8b3b-af5a9ed09858",
                "name": "Anthony Daniels"
            },
            {
                "id": "c5664b88-7286-4b38-9a3c-3f3cc6f72e9e",
                "name": "Warwick Davis"
            },
            {
                "id": "e039eedf-4daf-452a-bf92-a0085c68e156",
                "name": "Peter Cushing"
            }
        ],
        "writers": [
            {
                "id": "a5a8f573-3cee-4ccc-8a2b-91cb9f55250a",
                "name": "George Lucas"
            }
        ],
        "actors_names": [
            "Ahmed Best",
            "Anthony Daniels",
            "Peter Cushing",
            "Warwick Davis"
        ],
        "writers_names": [
            "George Lucas"
        ],
        "directors_names": [
            "Jon Burton"
        ]
    },
    {
        "id": "6d6a04d9-3e89-4f66-9256-7799beca0458",
        "rating": 6.2,
        "title": "Shuten Doji: The Star Hand Kid 4 - End Game",
        "description": "Human vs Human. Oni vs Oni. The final battle has begun!",
        "genres": [
            {
                "id": "6a0a479b-cfec-41ac-b520-41b2b007b611",
                "name": "Animation"
            },
            {
                "id": "b92ef010-5e4c-4fd0-99d6-41b6456272cd",
                "name": "Fantasy"
            },
            {
                "id": "f39d7b6d-aef2-40b1-aaf0-cf05e7048011",
                "name": "Horror"
            }
        ],
        "directors": [
            {
                "id": "665a488c-f84b-4317-aabf-529537279f40",
                "name": "Junji Nishimura"
            }
        ],
        "actors": [
            {
                "id": "30410f8f-cb09-4379-bbc3-1195d0890554",
                "name": "Josh Meyer"
            }
        ],
        "writers": [
            {
                "id": "1e49074b-f283-4793-a8ff-8027d67775ed",
                "name": "Gô Nagai"
            }
        ],
        "actors_names": [
            "Josh Meyer"
        ],
        "writers_names": [
            "Gô Nagai"
        ],
        "directors_names": [
            "Junji Nishimura"
        ]
    },
    {
        "id": "af749d09-d3cb-40f6-a01c-c49f13df35ee",
        "rating": 7.8,
        "title": "WWF All-Star Wrestling",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "0ce1ce6c-adb6-4bdd-9579-9f7f96fd3450",
                "name": "Merced Solis"
            },
            {
                "id": "68bfa031-9067-4ff2-b3ac-718207fbb112",
                "name": "Vince McMahon"
            },
            {
                "id": "92501a55-cef3-47bb-80cf-a12897bc75ef",
                "name": "Jimmy Hart"
            },
            {
                "id": "da5600e9-263d-407b-a446-e2b97c24cdd6",
                "name": "Don Muraco"
            }
        ],
        "writers": [],
        "actors_names": [
            "Don Muraco",
            "Jimmy Hart",
            "Merced Solis",
            "Vince McMahon"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "f7b7dc7e-d5cc-4ea2-bd66-7496b6551c61",
        "rating": 7.6,
        "title": "ROH: All Star Extravaganza",
        "description": "",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            },
            {
                "id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff",
                "name": "Action"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "2831abfa-cf84-4b6c-b818-0238445ccde6",
                "name": "Shinjirô Ôtani"
            },
            {
                "id": "4733e8cf-c1d0-42fa-9bdc-62776c194219",
                "name": "Brandon Silvestry"
            },
            {
                "id": "a15708fb-78d0-42bb-b434-cd57d9b7d288",
                "name": "Masato Tanaka"
            },
            {
                "id": "c5e7fc6e-e90f-49e4-8012-6ee29a9be097",
                "name": "Steve Corino"
            }
        ],
        "writers": [],
        "actors_names": [
            "Brandon Silvestry",
            "Masato Tanaka",
            "Shinjirô Ôtani",
            "Steve Corino"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "f09581c8-f364-4673-836e-ef584e8ebcb7",
        "rating": 7.3,
        "title": "Elvis All-Star Tribute",
        "description": "A re-enactment by some of the music industry's biggest stars of Elvis Presley's 1968 NBC comeback special, in tribute to the King.",
        "genres": [
            {
                "id": "56b541ab-4d66-4021-8708-397762bff2d4",
                "name": "Music"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "00e2e97b-3a93-4d44-a31d-9346b1348cc6",
                "name": "Jennifer Lopez"
            },
            {
                "id": "03375539-7607-42b5-944a-0e98fe2128e5",
                "name": "Post Malone"
            },
            {
                "id": "28b406df-ee09-49d4-8cb9-741e96b373bd",
                "name": "Alessia Cara"
            },
            {
                "id": "a429c4d0-399c-4c2e-94d1-46f250717d6a",
                "name": "Ed Sheeran"
            }
        ],
        "writers": [
            {
                "id": "ef478f80-fe53-4bb8-942f-a9dac0cb2cd1",
                "name": "David Wild"
            }
        ],
        "actors_names": [
            "Alessia Cara",
            "Ed Sheeran",
            "Jennifer Lopez",
            "Post Malone"
        ],
        "writers_names": [
            "David Wild"
        ],
        "directors_names": []
    },
    {
        "id": "2b301aa8-7c13-4be7-a552-d80c14af7487",
        "rating": 3.5,
        "title": "The All Star Impressions Show",
        "description": "Famous faces act out sketches impersonating other famous faces, and there is also an singing appearance by pop group JLS as themselves.",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            }
        ],
        "directors": [
            {
                "id": "d74eda1d-bdcc-428c-9458-69646c5a7636",
                "name": "John F.D. Northover"
            }
        ],
        "actors": [
            {
                "id": "31b84bca-0603-4b1d-a273-348f0085aa5f",
                "name": "Stephen Mulhern"
            },
            {
                "id": "68ac2126-f65d-4ab4-bdca-fd4732c68919",
                "name": "Diane Abbott"
            },
            {
                "id": "d0c33b8e-0a8a-45ae-9703-b32262eca1b0",
                "name": "Peter Dickson"
            },
            {
                "id": "de9a54fb-77a2-4fc3-b4ed-e0acb22aaf26",
                "name": "Tony Blackburn"
            }
        ],
        "writers": [
            {
                "id": "00591223-0fd4-4a5f-89f8-0317eff58c1b",
                "name": "Marc Blakewill"
            },
            {
                "id": "00a770fc-8964-41fa-9d3b-f6c958c9dddb",
                "name": "Tony Cooke"
            },
            {
                "id": "0c753724-fece-40cb-9115-abded78a7a2c",
                "name": "Martin Trenaman"
            },
            {
                "id": "3e0fd7d3-115e-4537-81f3-3e912b3cccb8",
                "name": "James Harris"
            },
            {
                "id": "4e4bacb2-a327-4b19-b579-5dfbfa410bd3",
                "name": "Matthew Leys"
            },
            {
                "id": "507e61e8-7d39-4ccb-9809-b317a9de5f9f",
                "name": "Tony Way"
            },
            {
                "id": "78d65b0c-51b0-4e03-8c28-fda307bb9c34",
                "name": "Carl Carter"
            },
            {
                "id": "c13e57a1-b771-4855-9359-b2b759bd2760",
                "name": "Jane Lamacraft"
            },
            {
                "id": "f80dcd60-9fcf-4550-922a-c05f21a8a309",
                "name": "Steven Burge"
            }
        ],
        "actors_names": [
            "Diane Abbott",
            "Peter Dickson",
            "Stephen Mulhern",
            "Tony Blackburn"
        ],
        "writers_names": [
            "Carl Carter",
            "James Harris",
            "Jane Lamacraft",
            "Marc Blakewill",
            "Martin Trenaman",
            "Matthew Leys",
            "Steven Burge",
            "Tony Cooke",
            "Tony Way"
        ],
        "directors_names": [
            "John F.D. Northover"
        ]
    },
    {
        "id": "5353633e-bd6d-4e6d-b284-918d66e5848f",
        "rating": 7.7,
        "title": "Smash Mouth: All Star",
        "description": "Music video for Smash Mouth's song, 'All Star'.",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            },
            {
                "id": "56b541ab-4d66-4021-8708-397762bff2d4",
                "name": "Music"
            },
            {
                "id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395",
                "name": "Short"
            }
        ],
        "directors": [
            {
                "id": "ad3c2885-69d4-4e88-8fd2-ded3c1dc971b",
                "name": "McG"
            }
        ],
        "actors": [
            {
                "id": "3a2575a6-4f08-41dc-add3-d38a17ee2b85",
                "name": "Greg Camp"
            },
            {
                "id": "af090823-64ae-4fcb-813c-5f7ffc4d8b15",
                "name": "Paul De Lisle"
            },
            {
                "id": "c21e8f21-c412-4a76-bcd2-b82f48c1e669",
                "name": "Dane Cook"
            },
            {
                "id": "c926c431-4931-4123-90ef-05f203784538",
                "name": "Hank Azaria"
            }
        ],
        "writers": [],
        "actors_names": [
            "Dane Cook",
            "Greg Camp",
            "Hank Azaria",
            "Paul De Lisle"
        ],
        "writers_names": [],
        "directors_names": [
            "McG"
        ]
    },
    {
        "id": "7b9ead63-df01-4a5d-b34e-2252173df08a",
        "rating": 7.4,
        "title": "AWA All-Star Wrestling",
        "description": "Syndicated series featuring wrestling matches as promoted by the American Wrestling Association (AWA).",
        "genres": [
            {
                "id": "2f89e116-4827-4ff4-853c-b6e058f71e31",
                "name": "Sport"
            },
            {
                "id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff",
                "name": "Action"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "70be91a0-6fbd-43e6-a08b-ebac9606d51f",
                "name": "Giant Baba"
            },
            {
                "id": "795d78e3-e0d2-4f74-a2e0-d7ab55195580",
                "name": "Ox Baker"
            },
            {
                "id": "87e85e9d-05fc-4312-9ff8-6dbf051be90b",
                "name": "Gene Okerlund"
            },
            {
                "id": "ea6ebdd0-cafc-4fa9-9d47-727e66aef3ec",
                "name": "Penny Banner"
            }
        ],
        "writers": [],
        "actors_names": [
            "Gene Okerlund",
            "Giant Baba",
            "Ox Baker",
            "Penny Banner"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "938eebcd-dc24-4026-beaf-c5d7fd3d958b",
        "rating": 4.7,
        "title": "All Star Mr & Mrs",
        "description": "",
        "genres": [
            {
                "id": "fb58fd7f-7afd-447f-b833-e51e45e2a778",
                "name": "Game-Show"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "5129890a-bbb6-4296-aa1f-e838a12b789c",
                "name": "Fern Britton"
            },
            {
                "id": "c115acef-d8bd-4cb9-9784-8fc2f6fc9571",
                "name": "Phillip Schofield"
            },
            {
                "id": "d0c33b8e-0a8a-45ae-9703-b32262eca1b0",
                "name": "Peter Dickson"
            }
        ],
        "writers": [],
        "actors_names": [
            "Fern Britton",
            "Peter Dickson",
            "Phillip Schofield"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "a9b57067-b910-47b8-bb83-3169429c84e1",
        "rating": 7.5,
        "title": "All Star Comedy Jam",
        "description": "The Original King of Comedy and Shaquille O'Neal presents this Stand-Up Special with some of the industry's most talented and sought after comedians.",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            },
            {
                "id": "6d141ad2-d407-4252-bda4-95590aaf062a",
                "name": "Documentary"
            }
        ],
        "directors": [
            {
                "id": "f09c267a-1a38-46c2-8b1a-35721b96ec34",
                "name": "Leslie Small"
            }
        ],
        "actors": [
            {
                "id": "22dbe9c3-cb14-4a1e-b6a9-47f9b76867c8",
                "name": "Tommy Davidson"
            },
            {
                "id": "272b3940-e37e-492a-9530-81848ed3a863",
                "name": "Cedric the Entertainer"
            },
            {
                "id": "474a88b6-110e-4a49-91b7-66839b9ebeaf",
                "name": "Kevin Hart"
            },
            {
                "id": "edc4f8f2-32a0-409d-9de2-4c34cbf1ae7d",
                "name": "DeRay Davis"
            }
        ],
        "writers": [],
        "actors_names": [
            "Cedric the Entertainer",
            "DeRay Davis",
            "Kevin Hart",
            "Tommy Davidson"
        ],
        "writers_names": [],
        "directors_names": [
            "Leslie Small"
        ]
    },
    {
        "id": "572814ae-165a-44a8-8420-db0ebf299ac2",
        "rating": 7.3,
        "title": "The All-Star Bond Rally",
        "description": "Inspirational documentary short film featuring Hollywood stars promoting the sales of War Bonds through songs and skits.",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            },
            {
                "id": "56b541ab-4d66-4021-8708-397762bff2d4",
                "name": "Music"
            },
            {
                "id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395",
                "name": "Short"
            }
        ],
        "directors": [
            {
                "id": "7e70921c-a4d5-409a-a571-b39bfeb658ee",
                "name": "Michael Audley"
            }
        ],
        "actors": [
            {
                "id": "41a4ae10-fe3e-4e06-ba60-ac70d26fb52f",
                "name": "Bob Hope"
            },
            {
                "id": "ab452435-59d2-43fc-a579-d3788317028a",
                "name": "Jeanne Crain"
            },
            {
                "id": "c475bfee-2b48-4183-853b-b4f1517d9fd9",
                "name": "Vivian Blaine"
            },
            {
                "id": "d05a86a4-b5b8-45ed-86ba-96eb6134b460",
                "name": "Bing Crosby"
            }
        ],
        "writers": [
            {
                "id": "80987b83-982b-48fe-9a36-87a5603b8abb",
                "name": "Don Quinn"
            }
        ],
        "actors_names": [
            "Bing Crosby",
            "Bob Hope",
            "Jeanne Crain",
            "Vivian Blaine"
        ],
        "writers_names": [
            "Don Quinn"
        ],
        "directors_names": [
            "Michael Audley"
        ]
    },
    {
        "id": "dd410e88-0c6a-4954-80ac-4c004bcba229",
        "rating": 5.2,
        "title": "All Star Family Fortunes",
        "description": "A celebrity version of Family Fortunes (1980).",
        "genres": [
            {
                "id": "fb58fd7f-7afd-447f-b833-e51e45e2a778",
                "name": "Game-Show"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "5b2b8d9d-ecf1-47f7-a3da-79355d2ff901",
                "name": "Vernon Kay"
            },
            {
                "id": "d0c33b8e-0a8a-45ae-9703-b32262eca1b0",
                "name": "Peter Dickson"
            },
            {
                "id": "d88abc26-e5bb-41a4-8761-6f8ada717440",
                "name": "Neil Hurst"
            }
        ],
        "writers": [],
        "actors_names": [
            "Neil Hurst",
            "Peter Dickson",
            "Vernon Kay"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "5f1a4219-b533-489f-8af2-0d2692504857",
        "rating": 7.2,
        "title": "An All-Star Toast to the Improv",
        "description": "To celebrate the \"birthday\" of the famous Improv comedy club, 6 famous comedians get up on stage and do their thing. However, to make things interesting, while each one does his particular routine, the other 5 comics sit at the back of the stage and heckle the performer. This video is especially notable for Martin Mull issuing a zinger at Robin Williams that shuts-up the otherwise motor-mouthed comic for at least 5 seconds.",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            }
        ],
        "directors": [
            {
                "id": "006d10a0-b0ba-4dac-bcf0-1111411c178b",
                "name": "Walter C. Miller"
            }
        ],
        "actors": [
            {
                "id": "45780fad-6861-457b-8617-80adf3c7b839",
                "name": "Richard Lewis"
            },
            {
                "id": "88ed8c24-fad6-4465-8304-2cc4927b55f9",
                "name": "Martin Mull"
            },
            {
                "id": "d85b6385-c814-44a2-92af-de93b936be80",
                "name": "Billy Crystal"
            },
            {
                "id": "e5b7d3e5-5c26-475b-803a-8575f724614e",
                "name": "Robert Klein"
            }
        ],
        "writers": [
            {
                "id": "7d47be2f-2e66-4c38-a9ef-e9d5bce360cc",
                "name": "Robin Williams"
            },
            {
                "id": "d85b6385-c814-44a2-92af-de93b936be80",
                "name": "Billy Crystal"
            },
            {
                "id": "e5b7d3e5-5c26-475b-803a-8575f724614e",
                "name": "Robert Klein"
            }
        ],
        "actors_names": [
            "Billy Crystal",
            "Martin Mull",
            "Richard Lewis",
            "Robert Klein"
        ],
        "writers_names": [
            "Billy Crystal",
            "Robert Klein",
            "Robin Williams"
        ],
        "directors_names": [
            "Walter C. Miller"
        ]
    },
    {
        "id": "5f51ddbc-4966-40a6-9030-262faa3b9b79",
        "rating": 7.4,
        "title": "Star Stories",
        "description": "Comedy Thats Shows Us How Some Of The Worlds Biggest Stars Came To Fame",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "81c353e7-a5d3-4e31-83e9-2cbe26c11808",
                "name": "Kevin Bishop"
            },
            {
                "id": "ccf47e38-eba1-41c1-961c-a96035a3165f",
                "name": "Harry Peacock"
            },
            {
                "id": "db40711a-d9d1-4071-91d4-d74af4cfbf81",
                "name": "Laura Patch"
            },
            {
                "id": "f111a93f-0a31-4b6f-bf3b-3a7177915bef",
                "name": "Tom Basden"
            }
        ],
        "writers": [],
        "actors_names": [
            "Harry Peacock",
            "Kevin Bishop",
            "Laura Patch",
            "Tom Basden"
        ],
        "writers_names": [],
        "directors_names": []
    },
    {
        "id": "f20e8a75-a7b0-4204-b3e6-edbc366e31d4",
        "rating": 7.5,
        "title": "Star na si Van Damme Stallone",
        "description": "The life story of a kid diagnosed with Down syndrome. He dreams of being an artista; his family has to make ends (and dreams) meet.",
        "genres": [
            {
                "id": "1cacff68-643e-4ddd-8f57-84b62538081a",
                "name": "Drama"
            }
        ],
        "directors": [
            {
                "id": "04439984-a8c5-4c53-ac74-1c39ac74b6e8",
                "name": "Randolph Longjas"
            }
        ],
        "actors": [
            {
                "id": "5b7206ed-9364-4b09-a4b8-430003a6fc02",
                "name": "Richard Joson"
            },
            {
                "id": "6c1dbabf-ce35-4471-b222-67e1ac052956",
                "name": "Acey Aguilar"
            },
            {
                "id": "8dc6c94a-18a6-4493-8856-b31dca7b4650",
                "name": "Candy Pangilinan"
            },
            {
                "id": "ba43c641-a595-461f-b7c9-866ab2d45cae",
                "name": "Sarah Pagcaliwagan"
            }
        ],
        "writers": [
            {
                "id": "017713b9-24cf-43a6-ab62-6b5e476499b8",
                "name": "Rod Marmol"
            },
            {
                "id": "524cbecd-d64f-4577-9736-5b5cb858767d",
                "name": "Alpha Habon"
            }
        ],
        "actors_names": [
            "Acey Aguilar",
            "Candy Pangilinan",
            "Richard Joson",
            "Sarah Pagcaliwagan"
        ],
        "writers_names": [
            "Alpha Habon",
            "Rod Marmol"
        ],
        "directors_names": [
            "Randolph Longjas"
        ]
    },
    {
        "id": "0ddc8a23-e625-4aa8-91f5-5aeb7ac82253",
        "rating": 8.5,
        "title": "Star Trek: The Next Generation: Interactive VCR Board Game - A Klingon Challenge",
        "description": "A Klingon named Kavok hijacks the USS Enterprise NCC-1701-D while it is docked for repairs at starbase 74. It is up to a repair crew to take the ship back before Kavok uses the ship to start a war between the United Federation of Planets and the Klingon Empire.",
        "genres": [
            {
                "id": "120a21cf-9097-479e-904a-13dd7198c1dd",
                "name": "Adventure"
            },
            {
                "id": "6c162475-c7ed-4461-9184-001ef3d9f26e",
                "name": "Sci-Fi"
            }
        ],
        "directors": [
            {
                "id": "cf54fca7-65f6-4b6a-a2b4-171ea2c6743e",
                "name": "Les Landau"
            }
        ],
        "actors": [
            {
                "id": "27b03478-fb81-4557-a306-bf27144122b5",
                "name": "Robert O'Reilly"
            },
            {
                "id": "5bddea2c-8609-499a-a444-77e0142743c0",
                "name": "Jonathan Frakes"
            }
        ],
        "writers": [],
        "actors_names": [
            "Jonathan Frakes",
            "Robert O'Reilly"
        ],
        "writers_names": [],
        "directors_names": [
            "Les Landau"
        ]
    },
    {
        "id": "a9ee0b3f-ec56-4107-9b6d-0458dfa3f415",
        "rating": 7,
        "title": "Star Trek: Short Treks",
        "description": "A series of stand-alone short films featuring characters and storylines from Star Trek: Discovery (2017).",
        "genres": [
            {
                "id": "120a21cf-9097-479e-904a-13dd7198c1dd",
                "name": "Adventure"
            },
            {
                "id": "1cacff68-643e-4ddd-8f57-84b62538081a",
                "name": "Drama"
            },
            {
                "id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff",
                "name": "Action"
            },
            {
                "id": "6c162475-c7ed-4461-9184-001ef3d9f26e",
                "name": "Sci-Fi"
            },
            {
                "id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395",
                "name": "Short"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "165f52f9-48bf-47b8-b14e-0b81079d1ba9",
                "name": "Ethan Peck"
            },
            {
                "id": "1d565221-1e6d-4bb1-b82a-b8d70d258c88",
                "name": "Rebecca Romijn"
            },
            {
                "id": "87a32a48-fdaa-4b6d-bd0d-ee4edfaec18d",
                "name": "Anson Mount"
            },
            {
                "id": "cd3765d7-a725-47a6-b602-02da78259f4b",
                "name": "Jenette Goldstein"
            }
        ],
        "writers": [
            {
                "id": "772faacb-5d57-4e72-b44f-01fde7f08c1a",
                "name": "Akiva Goldsman"
            },
            {
                "id": "82b7dffe-6254-4598-b6ef-5be747193946",
                "name": "Alex Kurtzman"
            },
            {
                "id": "8a9cb7b2-dd61-4f7f-94ec-61aac18ed5d9",
                "name": "Kirsten Beyer"
            },
            {
                "id": "b670fa3e-9f7b-4786-a00c-09d95f1e7b5c",
                "name": "Bryan Fuller"
            },
            {
                "id": "c5affe3b-e9f2-4fdb-a5ee-018dd751d3f4",
                "name": "Michael Chabon"
            }
        ],
        "actors_names": [
            "Anson Mount",
            "Ethan Peck",
            "Jenette Goldstein",
            "Rebecca Romijn"
        ],
        "writers_names": [
            "Akiva Goldsman",
            "Alex Kurtzman",
            "Bryan Fuller",
            "Kirsten Beyer",
            "Michael Chabon"
        ],
        "directors_names": []
    },
    {
        "id": "61dcf7a8-63b4-4cca-b6ea-e3f574acf93c",
        "rating": 5.4,
        "title": "Star Pink",
        "description": "In the year 2001 ½, the Pink Panther is a gas station attendant on a small planet. When a particularly dangerous-looking spaceship arrives, the panther panics and closes his station, which makes the green little pointy-nosed man flying the ship furious. The panther tries to elude the man and his search robot by all possible means, even evaporating himself in a molecular disassembler and reassembling himself in another. The man does the same, but the panther throws a flower into the reassembler, which turns the man into part flower.",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            },
            {
                "id": "6a0a479b-cfec-41ac-b520-41b2b007b611",
                "name": "Animation"
            },
            {
                "id": "a886d0ec-c3f3-4b16-b973-dedcf5bfa395",
                "name": "Short"
            }
        ],
        "directors": [
            {
                "id": "644e6c33-95fb-4c5c-bda3-5adf48128257",
                "name": "Arthur Davis"
            }
        ],
        "actors": [],
        "writers": [
            {
                "id": "0497b05c-40c3-4ad1-8fa0-e088b405bc59",
                "name": "John W. Dunn"
            }
        ],
        "actors_names": [],
        "writers_names": [
            "John W. Dunn"
        ],
        "directors_names": [
            "Arthur Davis"
        ]
    },
    {
        "id": "75475f58-c0ea-4d6d-9f78-bb44d971a21f",
        "rating": 6.5,
        "title": "Lego Star Wars: All-Stars",
        "description": "New faces team-up with iconic heroes Young Han Solo, Chewbacca, Young Lando Calrissian, BB-8, and General Leia for adventures that span all eras of the Star Wars universe.",
        "genres": [
            {
                "id": "120a21cf-9097-479e-904a-13dd7198c1dd",
                "name": "Adventure"
            },
            {
                "id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff",
                "name": "Action"
            },
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            },
            {
                "id": "6a0a479b-cfec-41ac-b520-41b2b007b611",
                "name": "Animation"
            },
            {
                "id": "6c162475-c7ed-4461-9184-001ef3d9f26e",
                "name": "Sci-Fi"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "05cece18-8d6b-4178-89e4-2af0e1afc902",
                "name": "Matthew Wood"
            },
            {
                "id": "3f6e8134-ce95-43bc-bfa9-dcf45cb89162",
                "name": "Montse Hernandez"
            },
            {
                "id": "e1e76fc6-c0c6-4f07-9ad5-55d07e925fe9",
                "name": "Dana Snyder"
            },
            {
                "id": "f1a17244-aa1d-4cec-b435-674c3ad4560b",
                "name": "John DiMaggio"
            }
        ],
        "writers": [
            {
                "id": "6abed654-6c30-4566-a811-6e10e2468496",
                "name": "Josh Rimes"
            },
            {
                "id": "6ba834a0-1039-4b5c-ab78-d5f1f18a4e7d",
                "name": "Carrie Beck"
            },
            {
                "id": "6e50ec85-bd49-45e6-9f2c-cd22a828c973",
                "name": "Bob Roth"
            },
            {
                "id": "76bf1d79-69da-48aa-8f02-05930d4449bf",
                "name": "Jason Cosler"
            },
            {
                "id": "79a4ab94-9062-4ac8-aa31-7236ba838ae9",
                "name": "Leland Chee"
            },
            {
                "id": "948d3351-ee5c-48c2-9553-3acd196e7e6b",
                "name": "Bill Motz"
            },
            {
                "id": "d1591574-8b7d-4436-b633-444e49926553",
                "name": "Keith Malone"
            },
            {
                "id": "e86eb86b-4115-4dbb-b499-3086e849f36b",
                "name": "Jake Blais"
            }
        ],
        "actors_names": [
            "Dana Snyder",
            "John DiMaggio",
            "Matthew Wood",
            "Montse Hernandez"
        ],
        "writers_names": [
            "Bill Motz",
            "Bob Roth",
            "Carrie Beck",
            "Jake Blais",
            "Jason Cosler",
            "Josh Rimes",
            "Keith Malone",
            "Leland Chee"
        ],
        "directors_names": []
    },
    {
        "id": "9f9a2a1f-1d6d-4cb4-b7c2-907dbeb88c03",
        "rating": 7.2,
        "title": "An All-Star Tribute to Johnny Cash",
        "description": "",
        "genres": [
            {
                "id": "56b541ab-4d66-4021-8708-397762bff2d4",
                "name": "Music"
            },
            {
                "id": "6d141ad2-d407-4252-bda4-95590aaf062a",
                "name": "Documentary"
            }
        ],
        "directors": [
            {
                "id": "f50ff2a0-2606-44d1-9817-634275a5cb11",
                "name": "Louis J. Horvitz"
            }
        ],
        "actors": [
            {
                "id": "0aafa35d-7d04-427c-a9e8-8eba4e0331e5",
                "name": "Kix Brooks"
            },
            {
                "id": "515c525e-f941-4b84-b97c-56bbc7b7084e",
                "name": "Bono"
            },
            {
                "id": "622703b7-f35a-427a-b67b-a5a99d551758",
                "name": "June Carter Cash"
            },
            {
                "id": "9ef9fd78-5715-4ca8-a182-2bb6e9abc9a2",
                "name": "Johnny Cash"
            }
        ],
        "writers": [
            {
                "id": "2d78e38c-b7f9-47a1-8ea1-21df0c3c11fb",
                "name": "Michael Rainin"
            },
            {
                "id": "d90676de-6443-48c7-b592-294d4c687e7b",
                "name": "Anthony DeCurtis"
            }
        ],
        "actors_names": [
            "Bono",
            "Johnny Cash",
            "June Carter Cash",
            "Kix Brooks"
        ],
        "writers_names": [
            "Anthony DeCurtis",
            "Michael Rainin"
        ],
        "directors_names": [
            "Louis J. Horvitz"
        ]
    },
    {
        "id": "e95044a7-1f66-4164-9650-3bf2132d7119",
        "rating": 5.8,
        "title": "The Young Comedians All-Star Reunion",
        "description": "Howie Mandel in Toronto, Steven Wright in Boston, Harry Anderson in Los Angeles, Richard Belzer in New York, and Robin Williams in San Fransisco (featured in the original \"Young Comedian\" TV specials) go back to where they started and showcase a new comedian.",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            }
        ],
        "directors": [
            {
                "id": "006d10a0-b0ba-4dac-bcf0-1111411c178b",
                "name": "Walter C. Miller"
            }
        ],
        "actors": [
            {
                "id": "07a54e6c-57ec-4f68-8561-be3abfe2b29a",
                "name": "Steven Wright"
            },
            {
                "id": "1071dc2b-0fd6-40be-9672-ef62297f2383",
                "name": "Howie Mandel"
            },
            {
                "id": "18b1fc7d-fc82-4a87-9c11-b90e3607cf6c",
                "name": "Howard Busgang"
            },
            {
                "id": "ba06c8bb-52c6-434b-b915-a1a673771a1f",
                "name": "Barry Crimmins"
            }
        ],
        "writers": [
            {
                "id": "42bc6979-f4c6-49dc-bdc2-ea6696bb6792",
                "name": "Rick Mitz"
            }
        ],
        "actors_names": [
            "Barry Crimmins",
            "Howard Busgang",
            "Howie Mandel",
            "Steven Wright"
        ],
        "writers_names": [
            "Rick Mitz"
        ],
        "directors_names": [
            "Walter C. Miller"
        ]
    },
    {
        "id": "ff750819-6004-426b-ae66-19a3ba15adcc",
        "rating": 6.8,
        "title": "General Electric's All-Star Anniversary",
        "description": "",
        "genres": [
            {
                "id": "6d141ad2-d407-4252-bda4-95590aaf062a",
                "name": "Documentary"
            }
        ],
        "directors": [],
        "actors": [
            {
                "id": "1b754e50-fc93-4f7e-b398-47edae55c3eb",
                "name": "Jon 'Bowzer' Bauman"
            },
            {
                "id": "e1ab5016-1539-47c9-9294-9ff1f96df44b",
                "name": "Albert Brooks"
            },
            {
                "id": "e22f0a9a-cd7c-4937-a44c-648b4a12f193",
                "name": "Lucille Ball"
            },
            {
                "id": "ec92a961-92d7-473a-a33f-cfee63946c5a",
                "name": "John Wayne"
            }
        ],
        "writers": [
            {
                "id": "28ae10bf-763b-48d5-9552-5c42e58cf19d",
                "name": "Bob Howard"
            },
            {
                "id": "c17de384-8c55-46d8-b993-ee24e239d28e",
                "name": "Paul Keyes"
            },
            {
                "id": "c4e774df-2333-45fa-b5b9-5da3ea1bffdf",
                "name": "Monty Aidem"
            },
            {
                "id": "e21d95af-81bc-45cd-8d74-d4275aa2da5c",
                "name": "Jeffrey Barron"
            }
        ],
        "actors_names": [
            "Albert Brooks",
            "John Wayne",
            "Jon 'Bowzer' Bauman",
            "Lucille Ball"
        ],
        "writers_names": [
            "Bob Howard",
            "Jeffrey Barron",
            "Monty Aidem",
            "Paul Keyes"
        ],
        "directors_names": []
    },
    {
        "id": "8167ee1a-61e2-4ec0-bb24-008822cde8cf",
        "rating": 5.4,
        "title": "All-Star Party for 'Dutch' Reagan",
        "description": "A televised event in honor of the 40th president, Ronald Reagan, the year he was sworn in for his second term of office.",
        "genres": [
            {
                "id": "5373d043-3f41-4ea8-9947-4b746c601bbd",
                "name": "Comedy"
            },
            {
                "id": "56b541ab-4d66-4021-8708-397762bff2d4",
                "name": "Music"
            }
        ],
        "directors": [
            {
                "id": "cc2b4b6e-c5b7-4b96-8a5b-25b05f682659",
                "name": "Dick McDonough"
            }
        ],
        "actors": [
            {
                "id": "55062f51-4656-4110-8dd2-7ebad228a787",
                "name": "Leon Ames"
            },
            {
                "id": "5aa92ef0-c076-4237-b1bc-1c1f981e36b3",
                "name": "June Allyson"
            },
            {
                "id": "6acb616f-fec4-4de8-937a-1377580e8b2f",
                "name": "Steve Allen"
            },
            {
                "id": "7ad0c1ab-9b5c-4e5f-8c3c-216ad32b5057",
                "name": "Edie Adams"
            }
        ],
        "writers": [
            {
                "id": "c17de384-8c55-46d8-b993-ee24e239d28e",
                "name": "Paul Keyes"
            }
        ],
        "actors_names": [
            "Edie Adams",
            "June Allyson",
            "Leon Ames",
            "Steve Allen"
        ],
        "writers_names": [
            "Paul Keyes"
        ],
        "directors_names": [
            "Dick McDonough"
        ]
    }
]
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
