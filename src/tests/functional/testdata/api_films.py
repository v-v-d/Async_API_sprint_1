from pathlib import Path

import orjson

TEST_CONTAINER_SRC_DIR_PATH = Path("/code/tests/functional/testdata/elastic_src")

with open(TEST_CONTAINER_SRC_DIR_PATH / "films_list.json", encoding="utf-8") as file:
    LIST_FILMS_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "film_details.json", encoding="utf-8") as file:
    FILM_DETAILS_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "film_search_list.json", encoding="utf-8") as file:
    LIST_FILMS_SEARCH_ES_RESPONSE = orjson.loads(file.read())


with open(TEST_CONTAINER_SRC_DIR_PATH / "film_search_api_list.json", encoding="utf-8") as file:
    EXPECTED_LIST_SEARCH_FILMS_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "film_api_list.json", encoding="utf-8") as file:
    EXPECTED_LIST_FILMS_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "film_api_details.json", encoding="utf-8") as file:
    EXPECTED_FILM_DETAILS_RESPONSE = orjson.loads(file.read())
