from pathlib import Path

import orjson

TEST_CONTAINER_SRC_DIR_PATH = Path("/code/tests/functional/testdata/elastic_src")

with open(TEST_CONTAINER_SRC_DIR_PATH / "genre_details.json", encoding="utf-8") as file:
    GENRE_DETAILS_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "genre_list.json", encoding="utf-8") as file:
    GENRE_LIST_ES_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "genre_api_list.json", encoding="utf-8") as file:
    EXPECTED_GENRE_LIST_RESPONSE = orjson.loads(file.read())

with open(TEST_CONTAINER_SRC_DIR_PATH / "genre_api_details.json", encoding="utf-8") as file:
    EXPECTED_GENRE_DETAILS_RESPONSE = orjson.loads(file.read())

