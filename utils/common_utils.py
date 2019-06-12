import re


def map_endpoint(context, end_point):
    split_endpoint = end_point.split("/")
    build_enpoint =[]
    for url in split_endpoint:
        if re.match(r'^\{[a-zA-Z]+[.][a-zA-Z_]+\}$', url):
            s= url.replace("{",'').replace("}",'')
            id=eval(s)
            build_enpoint.append(str(id))
            continue
        build_enpoint.append(url)
    return '/'.join(build_enpoint)