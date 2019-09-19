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


@step("I save the response as {key}")
def step_impl(context, key):
    if not hasattr(context, 'response_list'):
        context.response_list = {}
    context.response_list[key]= context.response.json()
