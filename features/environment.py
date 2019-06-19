from utils.projects import delete_projects
from utils.request_manager import RequestManager


def before_all(context):
    context.request = RequestManager()


def before_tag(context, tag):
    if tag == 'deleteProject':
        delete_projects(context)
