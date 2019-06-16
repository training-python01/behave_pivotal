from behave import step
from compare import expect


@step("I expect the project Account should be the default one {account_name}")
def step_impl(context, account_name):
    accounts = context.request.execute_request('get', '/accounts').json()
    current_account = ''
    for account in accounts:
        if account_name == account['name']:
            current_account = account
            break
    expect(context.response.json()['account_id']).to_equal(current_account['id'])

