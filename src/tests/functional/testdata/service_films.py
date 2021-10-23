EXPECTED_QUERY_TO_ES__QUERY_NO_ARGS = {"query": {"bool": {}}}

EXPECTED_QUERY_TO_ES__ONLY_QUERY = {
    "query": {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": "test",
                        "fields": ["title^3", "description"],
                        "fuzziness": "AUTO",
                    }
                }
            ]
        }
    }
}

EXPECTED_QUERY_TO_ES__ONLY_GENRE_ID = {
    "query": {
        "bool": {
            "must": [
                {
                    "nested": {
                        "path": "genres",
                        "query": {"bool": {"must": [{"match": {"genres.id": "test"}}]}},
                    }
                }
            ]
        }
    }
}

EXPECTED_QUERY_TO_ES__ONLY_PERSON_ID = {
    "query": {
        "bool": {
            "must": [
                {
                    "bool": {
                        "should": [
                            {
                                "nested": {
                                    "path": "directors",
                                    "query": {
                                        "bool": {
                                            "must": [
                                                {"match": {"directors.id": "test"}}
                                            ]
                                        }
                                    },
                                }
                            },
                            {
                                "nested": {
                                    "path": "actors",
                                    "query": {
                                        "bool": {
                                            "must": [{"match": {"actors.id": "test"}}]
                                        }
                                    },
                                }
                            },
                            {
                                "nested": {
                                    "path": "writers",
                                    "query": {
                                        "bool": {
                                            "must": [{"match": {"writers.id": "test"}}]
                                        }
                                    },
                                }
                            },
                        ]
                    }
                }
            ]
        }
    }
}

EXPECTED_QUERY_TO_ES__ONLY_SORT_ASC = {
    "query": {"bool": {}},
    "sort": {"rating": {"order": "asc"}},
}

EXPECTED_QUERY_TO_ES__ONLY_SORT_DESC = {
    "query": {"bool": {}},
    "sort": {"rating": {"order": "desc"}},
}

EXPECTED_QUERY_TO_ES__QUERY_AND_SORT_ASC = {
    "query": {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": "test",
                        "fields": ["title^3", "description"],
                        "fuzziness": "AUTO",
                    }
                }
            ]
        }
    },
    "sort": {"rating": {"order": "asc"}},
}

EXPECTED_QUERY_TO_ES__GENRE_ID_AND_SORT_ASC = {
    "query": {
        "bool": {
            "must": [
                {
                    "nested": {
                        "path": "genres",
                        "query": {"bool": {"must": [{"match": {"genres.id": "test"}}]}},
                    }
                }
            ]
        }
    },
    "sort": {"rating": {"order": "asc"}},
}

EXPECTED_QUERY_TO_ES__PERSON_ID_AND_SORT_ASC = {
    "query": {
        "bool": {
            "must": [
                {
                    "bool": {
                        "should": [
                            {
                                "nested": {
                                    "path": "directors",
                                    "query": {
                                        "bool": {
                                            "must": [
                                                {"match": {"directors.id": "test"}}
                                            ]
                                        }
                                    },
                                }
                            },
                            {
                                "nested": {
                                    "path": "actors",
                                    "query": {
                                        "bool": {
                                            "must": [{"match": {"actors.id": "test"}}]
                                        }
                                    },
                                }
                            },
                            {
                                "nested": {
                                    "path": "writers",
                                    "query": {
                                        "bool": {
                                            "must": [{"match": {"writers.id": "test"}}]
                                        }
                                    },
                                }
                            },
                        ]
                    }
                }
            ]
        }
    },
    "sort": {"rating": {"order": "asc"}},
}

EXPECTED_QUERY_TO_ES__QUERY_AND_PERSON_ID_AND_SORT_ASC = {
    "query": {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": "test",
                        "fields": ["title^3", "description"],
                        "fuzziness": "AUTO",
                    }
                },
                {
                    "bool": {
                        "should": [
                            {
                                "nested": {
                                    "path": "directors",
                                    "query": {
                                        "bool": {
                                            "must": [
                                                {"match": {"directors.id": "test"}}
                                            ]
                                        }
                                    },
                                }
                            },
                            {
                                "nested": {
                                    "path": "actors",
                                    "query": {
                                        "bool": {
                                            "must": [{"match": {"actors.id": "test"}}]
                                        }
                                    },
                                }
                            },
                            {
                                "nested": {
                                    "path": "writers",
                                    "query": {
                                        "bool": {
                                            "must": [{"match": {"writers.id": "test"}}]
                                        }
                                    },
                                }
                            },
                        ]
                    }
                },
            ]
        }
    },
    "sort": {"rating": {"order": "asc"}},
}

EXPECTED_QUERY_TO_ES__GENRE_ID_AND_PERSON_ID_AND_SORT_ASC = {
    "query": {
        "bool": {
            "must": [
                {
                    "nested": {
                        "path": "genres",
                        "query": {"bool": {"must": [{"match": {"genres.id": "test"}}]}},
                    }
                },
                {
                    "bool": {
                        "should": [
                            {
                                "nested": {
                                    "path": "directors",
                                    "query": {
                                        "bool": {
                                            "must": [
                                                {"match": {"directors.id": "test"}}
                                            ]
                                        }
                                    },
                                }
                            },
                            {
                                "nested": {
                                    "path": "actors",
                                    "query": {
                                        "bool": {
                                            "must": [{"match": {"actors.id": "test"}}]
                                        }
                                    },
                                }
                            },
                            {
                                "nested": {
                                    "path": "writers",
                                    "query": {
                                        "bool": {
                                            "must": [{"match": {"writers.id": "test"}}]
                                        }
                                    },
                                }
                            },
                        ]
                    }
                },
            ]
        }
    },
    "sort": {"rating": {"order": "asc"}},
}

EXPECTED_QUERY_TO_ES__QUERY_AND_GENRE_ID_AND_PERSON_ID_AND_SORT_ASC = {
    "query": {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": "test",
                        "fields": ["title^3", "description"],
                        "fuzziness": "AUTO",
                    }
                },
                {
                    "nested": {
                        "path": "genres",
                        "query": {"bool": {"must": [{"match": {"genres.id": "test"}}]}},
                    }
                },
                {
                    "bool": {
                        "should": [
                            {
                                "nested": {
                                    "path": "directors",
                                    "query": {
                                        "bool": {
                                            "must": [
                                                {"match": {"directors.id": "test"}}
                                            ]
                                        }
                                    },
                                }
                            },
                            {
                                "nested": {
                                    "path": "actors",
                                    "query": {
                                        "bool": {
                                            "must": [{"match": {"actors.id": "test"}}]
                                        }
                                    },
                                }
                            },
                            {
                                "nested": {
                                    "path": "writers",
                                    "query": {
                                        "bool": {
                                            "must": [{"match": {"writers.id": "test"}}]
                                        }
                                    },
                                }
                            },
                        ]
                    }
                },
            ]
        }
    },
    "sort": {"rating": {"order": "asc"}},
}
