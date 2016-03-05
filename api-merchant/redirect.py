#!/usr/local/bin/python
import requests
import json

f = open('.credentials', 'r')
auth = f.read().rstrip('\n').split(' ')
auth = (auth[0], auth[1])

session = requests.Session()

def add_redirect(origin, target, code):
    url = "http://api.cratejoy.com/v1/page_redirects/"
    response = requests.post(url, data=json.dumps({\
        'path': origin,\
        'target': target,\
        'enabled': True,\
        'code': code\
    }), auth=auth)
    print response.content

def disable_redirect(id):
    url = "http://api.cratejoy.com/v1/page_redirects/{}/".format(id)
    print url
    response = requests.put(url, data=json.dumps({\
        'enabled': False,\
    }), auth=auth)
    print response.content

def enable_redirect(id):
    url = "http://api.cratejoy.com/v1/page_redirects/{}/".format(id)
    print url
    response = requests.put(url, data=json.dumps({\
        'enabled': True,\
    }), auth=auth)
    print response.content

def show_redirects():
    url = "http://api.cratejoy.com/v1/page_redirects/"
    print url
    response = requests.get(url, auth=auth)
    print response.content
    
#add_redirect('/wrongplacetobe', '/placetobe', 302)
#show_redirects()
#disable_redirect(138398113)
#enable_redirect(138398113)
