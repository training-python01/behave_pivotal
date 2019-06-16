import json

from behave import step
from utils import commons


@step(u'I send a {method} request to {end_point}')
def step_impl(context, method, end_point):
    url = commons.map_endpoint(context, end_point)
    if context.text:
        data = json.loads(context.text)
        context.response = context.request.execute_request(method, url, data=data)
    else:
        context.response = context.request.execute_request(method, url)


@step("I save the response ID as {value}")
def step_impl(context, value):
    exec(f"context.{value} = context.response.json()['id']")
