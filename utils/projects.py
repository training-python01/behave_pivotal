def delete_projects(context):
    project_list = context.request.execute_request('get', '/projects')
    if project_list.json():
        for project in project_list.json():
            end_point = '/projects/{}'.format(project['id'])
            context.request.execute_request('delete', end_point)
