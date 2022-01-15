import requests
from os.path import exists
import json
import time

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

firstlaunch, apikey = configparser()

def statuscheck(status):
    status = status.status_code
    if status == 200:
        statusflag = True
        statusmessage =  'success'
    if status == 201:
        statusflag = True
        statusmessage = 'Paste was a success'
    if status == 400:
        statusflag = False
        statusmessage =  'Bad Request – Your request sucks'
    if status == 401:
        statusflag = False
        statusmessage =  'Unauthorized – Your Application/User application key is wrong.'
    if status == 403:
        statusflag = False
        statusmessage =  'Forbidden – The application is a standard Application, and the resource requires a UserApplication.'
    if status == 404:
        statusflag = False
        statusmessage =  'Not Found – The specified resource could not be found.'
    if status == 405:
        statusflag = False
        statusmessage =  'Method Not Allowed – You tried to access an endpoint with an invalid method.'
    if status == 406:
        statusflag = False
        statusmessage =  'Not Acceptable – You requested a format that isn’t json or xml.'
    if status == 429:
        statusflag = False
        statusmessage =  'Too Many Requests – You’re submitting pastes too fast, slow down and try again later.'
    if status == 500:
        statusflag = False
        statusmessage =  'Internal Server Error – Paste.ee had a problem with our server. Try again later.'
    if status == 503:
        statusflag = False
        statusmessage =  'Service Unavailable – Paste.ee is temporarially offline for maintanance. Please try again later.'
    print('Request status = '+statusmessage)
    return statusflag, statusmessage



def paste ( contents, name ):  ## make a new paste
    payload = {"description": name, "sections": [{"name": "Section1", "syntax": "autodetect", "contents": contents}]}
    headers = {'X-Auth-Token': apikey}
    post_response = requests.post(url = 'https://api.paste.ee/v1/pastes', json = payload, headers = headers)
    print(statuscheck(post_response)) ## returns the status of the request
    if statuscheck(post_response)[0] is True:
        print(post_response.text)
        time.sleep(0.5)
    else:
        print('slowing down, we hit a wall')
        time.sleep(5)
#for x in range(30):
paste('name','contents')
#paste('nik','hdhfhfhf')


def showpastes ():  ## returns json data array of pastes linked to api key
    headers = {'X-Auth-Token': apikey}
    showpastes = requests.get(url = 'https://api.paste.ee/v1/pastes/', headers = headers)
    print(showpastes.json())
    print(showpastes.json())
    for x in enumerate(showpastes.json()['data']):
        pass
        #print(x)
    return showpastes.json()


showpastes()

def getpaste ( id ):  ## returns data as json for paste
    headers = {'X-Auth-Token': apikey}
    url = 'https://api.paste.ee/v1/pastes/' + id
    getpaste = requests.get(url = url, headers = headers)
    if statuscheck(getpaste)[0] is True:
        print(getpaste.json())
    else: pass
#getpaste('LzEcl')

def deletepaste( id ):
    headers = {'X-Auth-Token': apikey}
    url = 'https://api.paste.ee/v1/pastes/' + id
    deletepaste = requests.delete(url = url, headers = headers)
    print(deletepaste.json())

#deletepaste('TGPAw')

def deleteallpastes():
    temparr=showpastes()['data']
    for x in enumerate(temparr): ## calls showpastes function, enumeate list, extract id and pass to delete paste function
        id=(x[1]['id'])
        deletepaste(id)
        pass

#deleteallpastes()




