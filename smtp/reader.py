import json, os

f = open(os.path.join(os.path.dirname(__file__), 'content.json'))
json_file = json.load(f)
f.close()

def get_header():
    return json_file['header']

def get_body():
    return json_file['body']

def get_dir():
    return json_file['dir']

def get_cred(path):
    f = open(os.path.join(os.path.dirname(__file__), path))
    json_file = json.load(f)
    f.close()
    return json_file
