from pathlib import Path

import orjson

TEST_CONTAINER_SRC_DIR_PATH = Path("/code/tests/functional/testdata/elastic_src")

with open(TEST_CONTAINER_SRC_DIR_PATH / "person_details.json", encoding="utf-8") as file:
    PERSON_DETAILS_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "person_list.json", encoding="utf-8") as file:
    PERSON_LIST_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "person_film_list.json", encoding="utf-8") as file:
    PERSON_FILM_LIST_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "person_film_api_list.json", encoding="utf-8") as file:
    EXPECTED_PERSON_FILM_LIST_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "person_api_list.json", encoding="utf-8") as file:
    EXPECTED_PERSON_LIST_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "person_api_details.json", encoding="utf-8") as file:
    EXPECTED_PERSON_DETAILS_RESPONSE = orjson.loads(file.read())


