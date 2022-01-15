import json
import jsonschema


def validate_json(schema, json_data): ## TODO
    if json_data is None:
        return False, "gimme json"
    # try:
    #     jsonschema.validate(instance=json_data, schema=schema)
    # except jsonschema.exceptions.ValidationError as err:
    #     return False, err.message
    return True, None
