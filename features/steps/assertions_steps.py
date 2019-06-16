import json

from behave import then
from compare import expect
from utils import commons


@then("I expect status code {status_code}")
def step_impl(context, status_code):
    expect(str(context.response.status_code)).to_equal(status_code)


@then("I expect the response match with the schema {json_schema_name}")
def step_impl(context, json_schema_name):
    expect(commons.schema_validation(json_schema_name, context.response.json())).to_be(True)


@then("I expect the response match with the send data")
def step_impl(context):
    actual_result = context.response.json()
    expected_result = json.loads(context.text)
    for key in expected_result:
        expect(actual_result[key]).to_equal(expected_result[key])
