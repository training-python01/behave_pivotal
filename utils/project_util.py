def get_account_by_name(client, account_name):
    accounts = client.execute_request('get', 'accounts').json()
    for account in accounts:
        if account_name == account['name']:
            return account
    raise AssertionError("Account was not found")
