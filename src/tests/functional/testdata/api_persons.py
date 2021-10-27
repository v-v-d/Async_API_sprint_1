from pathlib import Path

import orjson

TEST_CONTAINER_SRC_DIR_PATH = Path("/code/tests/functional/testdata/")

with open(TEST_CONTAINER_SRC_DIR_PATH / "person_details.json", encoding="utf-8") as file:
    PERSON_DETAILS_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "person_list.json", encoding="utf-8") as file:
    PERSON_LIST_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "person_film_list.json", encoding="utf-8") as file:
    PERSON_FILM_LIST_ES_RESPONSE = orjson.loads(file.read())

EXPECTED_PERSON_FILM_LIST_RESPONSE = [
    {
        "id": "57beb3fd-b1c9-4f8a-9c06-2da13f95251c",
        "rating": 6.9,
        "title": "Solo: A Star Wars Story",
        "description": "During an adventure into the criminal underworld, Han Solo meets his future co-pilot Chewbacca and encounters Lando Calrissian years before joining the Rebellion.",
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
                "id": "6c162475-c7ed-4461-9184-001ef3d9f26e",
                "name": "Sci-Fi"
            }
        ],
        "directors": [
            {
                "id": "33eb3b88-69f2-4f38-a26d-ff32f1feb1a1",
                "name": "Ron Howard"
            }
        ],
        "actors": [
            {
                "id": "01377f6d-9767-48ce-9e37-3c81f8a3c739",
                "name": "Woody Harrelson"
            },
            {
                "id": "7a852205-2bf6-4b75-b3b2-8a46ed6e91ef",
                "name": "Emilia Clarke"
            },
            {
                "id": "c69da9bd-eb87-4a06-be70-95d4ee2da1cc",
                "name": "Joonas Suotamo"
            },
            {
                "id": "ce06e6d7-600b-4829-badf-5d02c61f1a92",
                "name": "Alden Ehrenreich"
            }
        ],
        "writers": [
            {
                "id": "3217bc91-bcfc-44eb-a609-82d228115c50",
                "name": "Lawrence Kasdan"
            },
            {
                "id": "a2c091a2-281e-4732-9357-79b213d8d92f",
                "name": "Jonathan Kasdan"
            },
            {
                "id": "a5a8f573-3cee-4ccc-8a2b-91cb9f55250a",
                "name": "George Lucas"
            }
        ],
        "actors_names": [
            "Alden Ehrenreich",
            "Emilia Clarke",
            "Joonas Suotamo",
            "Woody Harrelson"
        ],
        "writers_names": [
            "George Lucas",
            "Jonathan Kasdan",
            "Lawrence Kasdan"
        ],
        "directors_names": [
            "Ron Howard"
        ]
    }
]

EXPECTED_PERSON_DETAILS_RESPONSE = {
    "id": "a5a8f573-3cee-4ccc-8a2b-91cb9f55250a",
    "full_name": "George Lucas",
    "roles": [
        "actor",
        "director",
        "writer"
    ],
    "film_ids": [
        "025c58cd-1b7e-43be-9ffb-8571a613579b",
        "0312ed51-8833-413f-bff5-0e139c11264a",
        "0659e0e6-504e-4482-8aa9-f7530f36cae2",
        "07f8bdbe-5246-4dfc-8d38-85043aeb307b",
        "118fd71b-93cd-4de5-95a4-e1485edad30e",
        "12a8279d-d851-4eb9-9d64-d690455277cc",
        "134989c3-3b20-4ae7-8092-3e8ad2333d59",
        "19babc93-62f5-481a-b6fe-9ebfef689cbc",
        "3a28f10a-433e-431c-8e7b-cc3f90af5a41",
        "3b1d0e70-42e5-4c9b-98cf-2681c420a99b",
        "3b914679-1f5e-4cbd-8044-d13d35d5236c",
        "3ba6c11a-0db6-4144-bc9d-c7e04b817dd2",
        "3cb639db-cd8a-48b0-90e3-9def109a4492",
        "3d825f60-9fff-4dfe-b294-1a45fa1e115d",
        "46f15353-2add-415d-9782-fa9c5b8083d5",
        "48495445-f04d-4d4c-9249-1faa28fc64eb",
        "4f53452f-a402-4a76-89fd-f034eeb8d657",
        "516f91da-bd70-4351-ba6d-25e16b7713b7",
        "57beb3fd-b1c9-4f8a-9c06-2da13f95251c",
        "5c612da0-9c15-48db-b46e-e6c82b071a9b",
        "5d62b55c-1ed5-4563-ae80-10c4baa21a36",
        "6313d0f5-e6a6-4071-a0c2-3d737fd1d56d",
        "64aa7000-698f-4332-b52f-9469e4d44ee1",
        "6cb927b3-4760-46c8-9002-ff4a47d57a4a",
        "73ecd1e6-6326-405a-b51b-69008f383b72",
        "75609cee-bc87-493d-8c1f-32c7e8ccc368",
        "88faa02d-f26f-40a1-9cc6-8045ed08d51e",
        "92dcddff-a70e-497c-92dc-0da12d1d528a",
        "943946ed-4a2b-4c71-8e0b-a58a11bd1323",
        "983e0b41-dd17-4fd6-b4e7-771f975fdc19",
        "991d143e-1342-4f7c-abf0-a9ede3abba20",
        "a8f6bd5b-036a-4d79-b952-3c7b5aa3ea83",
        "b503ced6-fff1-493a-ad41-73449b55ffee",
        "c35dc09c-8ace-46be-8941-7e50b768ec33",
        "c4c5e3de-c0c9-4091-b242-ceb331004dfd",
        "c8f57f93-b02a-40d4-ba55-9600cceddd7e",
        "cd19b384-babd-4b0c-ba0a-5c272bcf0238",
        "cddf9b8f-27f9-4fe9-97cb-9e27d4fe3394",
        "d6a7409f-87cd-49d7-8803-951a7352c2ce",
        "daae47e4-cbd0-4ffd-a150-55201b357d5b",
        "dc2dbf5d-de5d-4153-a049-51ba44f15e04",
        "dcab54f1-6958-4699-b3f5-2fb92c185b33",
        "e5a21648-59b1-4672-ac3b-867bcd64b6ea",
        "e99620fb-11bb-481b-8702-a14efa6bb0ef",
        "f241a62c-2157-432a-bbeb-9c579c8bc18b",
        "f553752e-71c7-4ea0-b780-41408516d0f4"
    ]
}

EXPECTED_PERSON_LIST_RESPONSE = [
    {
        "id": "2f2446f6-fb6b-49ae-b273-14bbfe430e2b",
        "full_name": "Linda Park",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "94ca979d-8a5f-433d-93f1-076fdb838eed"
        ]
    },
    {
        "id": "e85f5b12-d028-4a9d-b268-5e3f93f3da88",
        "full_name": "Linda Newton",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "71948ef1-0cb2-4ce5-ad20-7c10764b0e42"
        ]
    },
    {
        "id": "35b8a8b3-c256-4bf3-801f-5dc699d14136",
        "full_name": "Linda Ellerbee",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "19babc93-62f5-481a-b6fe-9ebfef689cbc"
        ]
    },
    {
        "id": "727a5038-e163-4044-925e-5da41dcc3772",
        "full_name": "Linda Darnell",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "4e5184c8-54eb-4f09-be83-4f95affe42a8"
        ]
    },
    {
        "id": "7df60217-ff9a-4276-a17d-864944c4108f",
        "full_name": "Linda Ware",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "163fa9c6-7604-4b2f-8190-0da8b8a4ba6f"
        ]
    },
    {
        "id": "c31e4bec-9f94-468c-8991-1a6902a69576",
        "full_name": "Linda Schuyler",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "181c2b64-4b8e-45b0-8b2e-ea71a2b34285"
        ]
    },
    {
        "id": "cf2f60fe-be62-4672-90da-9bda91fc6622",
        "full_name": "Linda Gray",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "38f21901-7dcb-467f-b512-550955c072d2"
        ]
    },
    {
        "id": "dfefebfe-0bc2-4088-9913-e86f1db52895",
        "full_name": "Linda Blair",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "81fb9b97-8250-4c6c-9358-3ada29c0f795"
        ]
    },
    {
        "id": "62bceb24-965c-4c9b-9d9f-fe76f0973f51",
        "full_name": "Väinö Linna",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "201c0ec8-2add-4d55-90e9-6596afd6dfe9",
            "29106b0c-4374-443d-bce7-700b4121d144",
            "3c061ba9-49d2-4603-9ab8-d26954e29ef5"
        ]
    },
    {
        "id": "c7108665-b19d-4099-9d84-0b095023217e",
        "full_name": "Christopher Parks",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "198c9111-fdce-470d-8369-d8a29a85b254"
        ]
    },
    {
        "id": "c223f04b-e854-4829-860c-75c9e3779843",
        "full_name": "Lina Wertmüller",
        "roles": [
            "director",
            "writer"
        ],
        "film_ids": [
            "78c73283-cd39-48d8-aa59-9f573f740030"
        ]
    },
    {
        "id": "3d4286b8-1389-46f6-bf35-b8c65cd76568",
        "full_name": "Hae-Jin Park",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "5a5603b2-afb5-42f5-8235-bb75b2cd9edd"
        ]
    },
    {
        "id": "27ccee39-7c1a-48f1-9ad7-38529a509193",
        "full_name": "Jin-hee Park",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "e6744751-e419-4ad2-8acc-ea92db2a3fe3"
        ]
    },
    {
        "id": "a90d678c-72f2-4e19-b921-f7a44783c70d",
        "full_name": "Joong-Hoon Park",
        "roles": [
            "actor",
            "director",
            "writer"
        ],
        "film_ids": [
            "0657217e-9efa-48fe-be08-6ca29bcaf042",
            "8e57a1c4-e952-4c07-a5cf-40c61dac36fa"
        ]
    },
    {
        "id": "8e159d94-1b75-4d61-a774-f6ba5e734706",
        "full_name": "Paris Childers",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "f393a3a6-3242-4cc5-936f-e0539247c050"
        ]
    },
    {
        "id": "9a5d1eab-73ce-401b-a2da-f4cecdaa1288",
        "full_name": "Mark Hudson",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "2f0b8fa3-8930-4046-bdcf-2f257899a2b9"
        ]
    },
    {
        "id": "9aea30ef-00f0-40e8-aeca-4edbdb57bd8c",
        "full_name": "Mark Cartwright",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "8fc11ab2-44cb-48fe-989c-487f72103002"
        ]
    },
    {
        "id": "a1e38083-d780-464b-8631-cbf5053f7a90",
        "full_name": "Mark Klastorin",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "7dc44185-c268-476d-8b0e-488a091c1d4b"
        ]
    },
    {
        "id": "b61aaadc-28d5-413b-8203-9d1f4a14b307",
        "full_name": "Justin Mark",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "c06dd0f4-d75d-4952-a81c-36837a30351b"
        ]
    },
    {
        "id": "be814de6-7f17-4b7c-8130-a23977e335cd",
        "full_name": "Mark Critch",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "a99d6476-4b05-467d-a612-b7ebbec900dc"
        ]
    },
    {
        "id": "bed94cc7-6d2c-429a-a88b-5d0e36d55530",
        "full_name": "Mark Berman",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "07b2a2bb-81b8-418e-89ad-b4fb359c6d9a"
        ]
    },
    {
        "id": "bc3f8586-6ccf-4878-8ce2-9a3b6107652e",
        "full_name": "Mark Lund",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "11a73cea-3122-427a-bad9-81d8a19a2a9b"
        ]
    },
    {
        "id": "a7e5e6f2-a729-4fcf-9d54-88d38235246d",
        "full_name": "Mark Seidenberg",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "c1030990-2ae6-4056-8c63-a7e627ae6483"
        ]
    },
    {
        "id": "b5fa51d6-4753-4b64-819c-2de16af5c057",
        "full_name": "Mark Rosenthal",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "511b8ae8-f59d-450e-b9a2-22aabba2693b"
        ]
    },
    {
        "id": "3513bd79-7425-49eb-97cf-7aa03474eb59",
        "full_name": "Mark Kovalyov",
        "roles": [
            "director",
            "writer"
        ],
        "film_ids": [
            "0b227836-c56b-4c9e-b9d9-28be310e6182"
        ]
    },
    {
        "id": "4df78934-ac20-431d-8d45-6cebff0c9c6a",
        "full_name": "Mark Aguirre",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "e49c02da-e7ee-4da7-bae4-538a5dc7c0f2"
        ]
    },
    {
        "id": "58006678-1c01-4278-afef-95fde3803122",
        "full_name": "Mark Heller",
        "roles": [
            "director"
        ],
        "film_ids": [
            "19c21be1-3c42-448d-a088-cd5d61e26710"
        ]
    },
    {
        "id": "617831f8-be04-4f48-b95b-5f3902e53b23",
        "full_name": "Mark Whittlesey",
        "roles": [
            "director"
        ],
        "film_ids": [
            "19867a14-5e9e-481c-ab25-10f386a6faef"
        ]
    },
    {
        "id": "6885d8cd-88b4-415a-8cc0-fd611b14f7ab",
        "full_name": "Mark Redfield",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "28bae088-edbd-4a74-a887-4f5111ff2e37"
        ]
    },
    {
        "id": "03f35442-52f4-4338-84c9-2ff1c1675441",
        "full_name": "Ned Sparks",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "163fa9c6-7604-4b2f-8190-0da8b8a4ba6f"
        ]
    },
    {
        "id": "0d056b87-27a9-40a8-8b5c-888f797c4e00",
        "full_name": "Mark Williams",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "a2002931-73bc-4331-8381-c62af1ac2c46"
        ]
    },
    {
        "id": "2011cd38-8173-4958-8cf5-ea2628199d08",
        "full_name": "Mark Lenard",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "4090e081-2cad-4016-a8a9-cb15f38db64c"
        ]
    },
    {
        "id": "26e83050-29ef-4163-a99d-b546cac208f8",
        "full_name": "Mark Hamill",
        "roles": [
            "actor",
            "director"
        ],
        "film_ids": [
            "025c58cd-1b7e-43be-9ffb-8571a613579b",
            "0312ed51-8833-413f-bff5-0e139c11264a",
            "12a8279d-d851-4eb9-9d64-d690455277cc",
            "134989c3-3b20-4ae7-8092-3e8ad2333d59",
            "3a28f10a-433e-431c-8e7b-cc3f90af5a41",
            "3b1d0e70-42e5-4c9b-98cf-2681c420a99b",
            "3d825f60-9fff-4dfe-b294-1a45fa1e115d",
            "46f15353-2add-415d-9782-fa9c5b8083d5",
            "943946ed-4a2b-4c71-8e0b-a58a11bd1323",
            "b6b8a3b7-1c12-45a8-9da7-4b20db8867df",
            "c7bd11a4-30bf-4077-a618-97c3e5525427",
            "cddf9b8f-27f9-4fe9-97cb-9e27d4fe3394",
            "d4b010a5-2648-4850-b15d-307658020923",
            "dbb9b244-483b-4592-9194-4938338419bc"
        ]
    },
    {
        "id": "25423597-4cb0-4e9f-a9aa-86b1fd3aadee",
        "full_name": "Mark Wahlberg",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "496f504e-20fa-4dfd-b4cb-c7c4ef636e07"
        ]
    },
    {
        "id": "44e547b0-6664-4b6b-8f51-f8d994edea77",
        "full_name": "Mark Meer",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "5f600319-10de-49aa-b56f-710edec3ac73"
        ]
    },
    {
        "id": "466c8350-fda7-44b4-a08f-afceaa16bc31",
        "full_name": "Mark Griffiths",
        "roles": [
            "director"
        ],
        "film_ids": [
            "f60241d5-119d-42f8-850a-ea56e8a15cf1"
        ]
    },
    {
        "id": "4f9d60e0-f06c-470a-afc7-edb2daa30a09",
        "full_name": "Mark Calaway",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "27b726f2-40e9-4d81-b608-57f7c41bfe54"
        ]
    },
    {
        "id": "65e38201-f416-4176-b24e-ed0c89e1f2b5",
        "full_name": "Mark A. Altman",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "2b16f7be-b5b7-4851-9952-2ec310446690",
            "499987ef-5dde-481d-bd95-30ef26937894",
            "86607a8f-bc90-47fa-8261-15647186cbf5"
        ]
    },
    {
        "id": "3b999a71-ccb7-4d0e-83e1-e44d97d51e3a",
        "full_name": "Mark Chappell",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "338b80b5-d21a-4bbe-a465-13fae98f2d35"
        ]
    },
    {
        "id": "52826334-d36a-419a-87ca-f76123e31015",
        "full_name": "Mark Litton",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "c20c249f-91ac-4c6a-9afe-f1c85aa9b277"
        ]
    },
    {
        "id": "be2f35d9-811d-4db5-bed9-2ea714d3b74c",
        "full_name": "Mark Bessenger",
        "roles": [
            "actor"
        ],
        "film_ids": [
            "b8bb8ea6-93c8-4c80-9897-1f9b00b1265b"
        ]
    },
    {
        "id": "c576f59c-df96-4f8f-901b-44de16ffac6b",
        "full_name": "Mark McCorkle",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "0236282f-8ea5-418e-ab9b-13662a4688a9"
        ]
    },
    {
        "id": "c30b0678-3676-4a03-aaf5-a7ccdecb6ceb",
        "full_name": "Mark Evanier",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "f3731b08-80b1-4687-aa31-62c483eb24ef"
        ]
    },
    {
        "id": "e53df6eb-365d-4b20-933e-d10979c0fe4f",
        "full_name": "Hark Tsui",
        "roles": [
            "director",
            "writer"
        ],
        "film_ids": [
            "9b21babd-5eb7-432b-8d2b-d28980b740f1"
        ]
    },
    {
        "id": "d9f85a6d-1b1d-441a-80ce-5e8bcb4f27aa",
        "full_name": "Havana Marking",
        "roles": [
            "director"
        ],
        "film_ids": [
            "08c9c955-d91f-47aa-a34c-30982e8fdd9d"
        ]
    },
    {
        "id": "dcbd9b06-820c-4645-ada9-889f251ae831",
        "full_name": "Mark Hanna",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "63518f42-52c7-494e-a48f-4ac8090aeed7"
        ]
    },
    {
        "id": "ee51d023-30a8-4231-ab0d-30c1429a65ed",
        "full_name": "Mark O'Green",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "19867a14-5e9e-481c-ab25-10f386a6faef"
        ]
    },
    {
        "id": "f08dcf94-92f4-456b-80ea-02165990a4de",
        "full_name": "Mark Mendola",
        "roles": [
            "writer"
        ],
        "film_ids": [
            "6c6cb534-5013-4b5f-929e-cdc5436c38aa"
        ]
    },
    {
        "id": "97537947-aa79-4e3b-8aa8-891fa1ed302a",
        "full_name": "Jerry Paris",
        "roles": [
            "director"
        ],
        "film_ids": [
            "f73b492e-751e-446a-8c95-c291545033d8"
        ]
    },
    {
        "id": "721c5495-6a93-4b88-bd91-6ef9c434f9fc",
        "full_name": "Mark Alex Vogt",
        "roles": [
            "director"
        ],
        "film_ids": [
            "e891bebc-786c-4fe8-948e-c6d4007146f9"
        ]
    }
]
