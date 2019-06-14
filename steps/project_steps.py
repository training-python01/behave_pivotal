from behave import *
from compare import expect
from utils import project_util

@step("I expect the project Account should be the default one {account_name}")
def step_impl(context, account_name):
    current_account = project_util.get_account_by_name(context.client, account_name)
    expect(context.response.json()['account_id']).to_equal(current_account['id'])

