import jsonschema


def validate_json(schema, json_data):
    if json_data is None:
        return False, "Provide json data."
    try:
        jsonschema.validate(instance=json_data, schema=schema)
    except jsonschema.ValidationError as err:
        return False, err.message
    return True, None
