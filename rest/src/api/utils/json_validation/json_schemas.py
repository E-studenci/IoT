
ADD_USER_SCHEMA = {
    "type" : "object",
    "properties" : {
        "surname": {"type" : "string"},
        "name": {"type" : "string"},
        "email": {"type" : "string"},
        "card": {"type" : "string"}, 
    },
    "required": ["surname", "name", "email", "card"]
}


EDIT_USER_SCHEMA = {
    "type" : "object",
    "properties" : {
        "surname": {"type" : "string"},
        "name": {"type" : "string"},
        "email": {"type" : "string"},
        "status": {"enum" : ["ACTIVE", "DISABLED"]},
        "card": {"type" : "string"}, 
    }
}
