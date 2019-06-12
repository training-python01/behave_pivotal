from utils.api_client import APIRequest


def before_all(context):
    context.client = APIRequest('1a77ed61bf49f50a95282757b849b099', 'https://www.pivotaltracker.com/services/v5/')

def before_scenario(context, scenario):
    project_list = context.client.execute_request('get', 'projects')
    if project_list.json():
        for project in project_list.json():
            end_point = 'projects/{}'.format(project['id'])
            context.client.execute_request('delete', end_point)
