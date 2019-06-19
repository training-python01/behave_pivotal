import json
import os
import re

from jsonschema import validate
from jsonschema import ValidationError


def map_endpoint(context, end_point):
    split_endpoint = end_point.split("/")
    build_endpoint = []
    for url in split_endpoint:
        if re.match(r'^\{[a-zA-Z]+[.][a-zA-Z_]+\}$', url):
            s = url.replace("{", '').replace("}", '')
            id = eval(s)
            build_endpoint.append(str(id))
            continue
        build_endpoint.append(url)
    return '/'.join(build_endpoint)


def schema_validation(json_schema_name, instance):
    schema = load_schema(json_schema_name)
    try:
        validate(instance=instance, schema=schema)
        return True
    except ValidationError as error:
        print("Schema Validation Failed: {}".format, error.message)
        raise


def load_schema(json_schema_name):
    current_path = os.getcwd()
    path = "{}/schemas/{}".format(current_path, json_schema_name)
    with open(path) as json_schema:
        schema = json.load(json_schema)
    return schema
