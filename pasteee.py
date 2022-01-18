from os.path import exists
from datetime import datetime

import requests

apikey = '<apikey>'


class StatusCheck:
    def __init__(self, status):
        self.status = status
        status = status.status_code
        if status == 200:
            statusflag = True
            statusmessage = 'success'
        if status == 201:
            statusflag = True
            statusmessage = 'Paste was a success'
        if status == 400:
            statusflag = False
            statusmessage = 'Bad Request – Your request sucks'
        if status == 401:
            statusflag = False
            statusmessage = 'Unauthorized – Your Application/User application key is wrong.'
        if status == 403:
            statusflag = False
            statusmessage = \
                'Forbidden – The application is a standard Application, and the resource requires a UserApplication.'
        if status == 404:
            statusflag = False
            statusmessage = 'Not Found – The specified resource could not be found.'
        if status == 405:
            statusflag = False
            statusmessage = 'Method Not Allowed – You tried to access an EndPoint with an invalid method.'
        if status == 406:
            statusflag = False
            statusmessage = 'Not Acceptable – You requested a format that isn’t json or xml.'
        if status == 429:
            statusflag = False
            statusmessage = 'Too Many Requests – You’re submitting pastes too fast, slow down and try again later.'
        if status == 500:
            statusflag = False
            statusmessage = 'Internal Server Error – Paste.ee had a problem with our server. Try again later.'
        if status == 503:
            statusflag = False
            statusmessage = \
                'Service Unavailable – Paste.ee is temporarially offline for maintanance. Please try again later.'
        self.statusflag = statusflag
        self.statusmessage = statusmessage


class EndPoint:
    pastes = 'https://api.paste.ee/v1/pastes'
    file = 'https://api.paste.ee/v1/pastes/file'
    syntaxes = 'https://api.paste.ee/v1/syntaxes/'
    users = 'https://api.paste.ee/v1/users/info'
    userauth = 'https://paste.ee/account/api/authorize/'
    viewpaste = 'https://paste.ee/p/'
    rawpaste = 'https://paste.ee/r/'
    pass


class GetPaste(object):
    def __init__(self, _id):
        self._id = _id
        headers = {'X-Auth-Token': apikey}
        url = 'https://api.paste.ee/v1/pastes/' + _id
        self.get = requests.get(url = url, headers = headers)
        self.status = StatusCheck(self.get).statusflag
        if self.status is True:
            self.encrypted = self.get.json()['paste']['encrypted']
            self.views = self.get.json()['paste']['views']
            self.expires_at = self.get.json()['paste']['expires_at']
            self.name = self.get.json()['paste']['description']
            self.data = self.get.json()['paste']
            self.created_at = self.get.json()['paste']['created_at']
            self.content = self.get.json()['paste']['sections'][0]['contents']
            self.syntax = self.get.json()['paste']['sections'][0]['syntax']
            self.size = self.get.json()['paste']['sections'][0]['size']
        else:
            self.encrypted = None
            self.views = None
            self.expires_at = None
            self.name = None
            self.data = None
            self.created_at = None
            self.content = None
            self.syntax = None
            self.size = None


class ShowAllPastes:
    def __init__(self):
        _id = []
        headers = {'X-Auth-Token': apikey}
        url = 'https://api.paste.ee/v1/pastes/?perpage=5000'
        get = requests.get(url = url, headers = headers)
        self.data = get.json()['data']
        self.total = get.json()['total']


class Make:
    def __init__(self, name, contents, expiration):
        self.name = name
        self.content = contents
        self.syntax = 'autodetect'
        self.expiration = expiration
        payload = {"description": name, "expiration": expiration,
                   "sections": [{"name": name, "syntax": self.syntax, "contents": contents}]}
        headers = {'X-Auth-Token': apikey, 'Content-Type': 'application/json'}
        post_response = requests.post(url = EndPoint.pastes, json = payload, headers = headers)
        status = StatusCheck(post_response).statusflag
        if status is True:
            paste_id = post_response.json()['id']
        else:
            paste_id = None
            pass
        self.status = status
        self.paste_id = paste_id
        self.expiration_time = datetime.fromtimestamp(expiration + datetime.now().timestamp())


class Users:
    def __init__(self):
        headers = {'X-Auth-Token': apikey}
        post_response = requests.get(url = EndPoint.users, headers = headers)
        status = StatusCheck(post_response).statusflag
        data = (post_response.json())
        self.status = status
        self.data = data


class Getsyntax:  # looks like the paste.ee doesnt support this documented function right now...
    def __init__(self, _id):
        headers = {'X-Auth-Token': apikey}
        post_response = requests.get(url = EndPoint.syntaxes + _id, headers = headers)
        status = StatusCheck(post_response).statusflag
        data = (post_response.json())
        self.status = status
        self.data = data


class File(object):
    def __init__(self, name, filename):
        if exists(filename) is True:
            f = open(filename, "r")
        else:
            self.status = None
            self.pasteid = None
        contents = f.read()
        payload = {"description": name, "sections": [{"name": name, "syntax": "autodetect", "contents": contents}]}
        headers = {'X-Auth-Token': apikey}
        post_response = requests.post(url = EndPoint.pastes, json = payload, headers = headers)
        status = StatusCheck(post_response).statusflag
        if status is True:
            pasteid = post_response.json()['id']
        else:
            pasteid = None
            pass
        self.status = status
        self.pasteid = pasteid
        self.name = name
        self.filename = filename


class Deletepaste(object):
    def __init__(self, _id):
        headers = {'X-Auth-Token': apikey}
        url = 'https://api.paste.ee/v1/pastes/' + _id
        delete = requests.delete(url = url, headers = headers)
        status = StatusCheck(delete).statusflag
        if status is True:
            data = delete.json()
        else:
            data = None
            pass
        self.status = status
        self.data = data
        self._id = _id


class Deleteallpastes:
    def __init__(self):
        getall = ShowAllPastes().data
        for x, val in (enumerate(getall)):
            _id = (getall[x]['id'])
            Deletepaste(_id)

# deleteallpastes()
