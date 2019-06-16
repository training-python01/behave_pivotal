import json
import requests


class RequestManager:
    def __init__(self):
        config = json.loads(open('config.json').read())
        self.base_endpoint = config['baserUrl']
        self.headers = {
            'X-TrackerToken': config['tokenApi'],
            'Content-Type': 'application/json'
        }

    def execute_request(self, method, endpoint, data=None):
        api_url = "{}{}".format(self.base_endpoint, endpoint)
        if data:
            response = requests.request(method, api_url, headers=self.headers, data=json.dumps(data))
        else:
            response = requests.request(method, api_url, headers=self.headers)
        return response
