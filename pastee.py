from os.path import exists

import requests

apikey = '****'

def configparser ():  ## checks if first launch, creates config file, asks for api key saves to file and in future loads from this
    file_exists = exists('config.cfg')
    if file_exists is False:  ## if config file doesnt exist create one.
        open('config.cfg', 'xt')
        print('Config file does not exist')
        print('creating config file')
        print('please enter paste.ee api key')
        f = open("config.cfg", "a")
        apikey = input()
        print(apikey)
        f.write('apikey:' + apikey)
        f.close()
        firstlaunch = True
    else:
        f = open("config.cfg", "r")
        apikey = f.read().strip('apikey:')
        # print(apikey)
        firstlaunch = False
    return firstlaunch, apikey

def statuscheck(status):
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
    print('Request status = ' + statusmessage)
    return statusflag, statusmessage


class EndPoint:
    pastes = 'https://api.paste.ee/v1/pastes'
    file = 'https://api.paste.ee/v1/pastes/file'
    syntaxes = 'https://api.paste.ee/v1/syntaxes/'
    users = 'https://api.paste.ee/v1/users/info'
    userauth = 'https://paste.ee/account/api/authorize/'
    pass


class GetPaste(object):
    def __init__(self, _id):
        self._id = _id
        headers = {'X-Auth-Token': apikey}
        url = 'https://api.paste.ee/v1/pastes/' + _id
        self.get = requests.get(url = url, headers = headers)
        self.status = statuscheck(self.get)[0]
        if self.status is True:
            self.name = self.get.json()['paste']['description']
            self.data = self.get.json()['paste']
            self.created_at = self.get.json()['paste']['created_at']
            self.content = self.get.json()['paste']['sections'][0]['contents']
            self.size = self.get.json()['paste']['sections'][0]['size']
        else:
            self.name = None
            self.data = None
            self.created_at = None
            self.content = None
            self.size = None


def showallpastes():
    headers = {'X-Auth-Token': apikey}
    url = 'https://api.paste.ee/v1/pastes/?perpage=5000'
    get = requests.get(url = url, headers = headers)
    for x in enumerate(get.json()['data']):
        print(x)
    return get.json()['data']


# showallpastes()

def make(name, contents):
    payload = {"description": name, "sections": [{"name": name, "syntax": "autodetect", "contents": contents}]}
    headers = {'X-Auth-Token': apikey, 'Content-Type': 'application/json'}
    post_response = requests.post(url = EndPoint.pastes, json = payload, headers = headers)
    status = statuscheck(post_response)[0]
    if status is True:
        pasteid = post_response.json()['id']
    else:
        pasteid = None
        pass
    return status, pasteid


# paste1 = make('paste','paste') #makes a new paste
# print(paste1) # returns status,pasteid


def users():
    headers = {'X-Auth-Token': apikey}
    post_response = requests.get(url = EndPoint.users, headers = headers)
    status = statuscheck(post_response)[0]
    data = (post_response.json())
    return status, data


# user = users() # This EndPoint will return information about the current api key.
# print(user) # returns status, data

def getsyntax(_id):  # looks like the paste.ee doesnt support this documented function right now...
    headers = {'X-Auth-Token': apikey}
    post_response = requests.get(url = EndPoint.syntaxes + _id, headers = headers)
    # print(EndPoint.syntaxes+_id)
    status = statuscheck(post_response)[0]
    data = (post_response.json())
    return status, data


# getsyntax('CRgNw')

def file(name, filename):
    if exists(filename) is True:
        f = open(filename, "r")
    else:
        print('file could not be found')
        return False, None
    contents = f.read()
    payload = {"description": name, "sections": [{"name": name, "syntax": "autodetect", "contents": contents}]}
    headers = {'X-Auth-Token': apikey}
    post_response = requests.post(url = EndPoint.pastes, json = payload, headers = headers)
    status = statuscheck(post_response)[0]
    if status is True:
        pasteid = post_response.json()['id']
    else:
        pasteid = None
        pass
    return status, pasteid


# file = file('name','fle.ps1')
# print(file)


def deletepaste(_id):
    headers = {'X-Auth-Token': apikey}
    url = 'https://api.paste.ee/v1/pastes/' + _id
    delete = requests.delete(url = url, headers = headers)
    status = statuscheck(deletepaste)[0]
    if status is True:
        data = delete.json()
    else:
        data = None
        pass
    return status, data


def deleteallpastes():
    pass
