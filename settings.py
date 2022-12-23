import os

MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = 27017

MONGO_DBNAME = "government"

RESOURCE_METHODS = ["GET", "POST", "DELETE"]
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]


schema = {
    "verb": {
        "type": "string"
    },
    "preposition": {
        "type": "string"
    },
    "features": {
        "type": "list"
    }
}

genre_all = {
    "item_title": "verb_government",

    "cache_control": "max-age=10,must-revalidate",
    "cache_expires": 10,

    "resource_methods": ["GET", "POST"],
    "schema": schema
}

DOMAIN = {
    "genre_all": genre_all,
}