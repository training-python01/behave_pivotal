import json

from behave import step, then, when
from compare import expect

from utils import common_utils


@step(u'I make a {method} request to {end_point}')
def step_impl(context, method, end_point):
    url = common_utils.map_endpoint(context, end_point)
    if context.text:
        data = json.loads(context.text)
        context.response = context.client.execute_request(method, url, data=data)
    else:
        context.response = context.client.execute_request(method, url)


@then("I expect status code {status_code}")
def step_impl(context, status_code):
    expect(str(context.response.status_code)).to_equal(status_code)


@when("I save the response ID as {project_id}")
def step_impl(context, project_id):
    exec(f"context.{project_id} = context.response.json()['id']")


@step("I expect the response match with the schema {json_schema_name}")
def step_impl(context, json_schema_name):
    expect(common_utils.schema_validation(json_schema_name,context.response.json())).to_be(True)


@step("I expect the response match with the send data")
def step_impl(context):
    actual_result = context.response.json()
    expected_result = json.loads(context.text)
    for key in expected_result:
        expect(actual_result[key]).to_equal(expected_result[key])
