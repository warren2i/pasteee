import requests
from os.path import exists


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
configparser()


def paste ( contents, name ):  ## make a new paste
    payload = {"description": name, "sections": [{"name": "Section1", "syntax": "autodetect", "contents": contents}]}
    headers = {'X-Auth-Token': apikey}
    post_response = requests.post(url = 'https://api.paste.ee/v1/pastes', json = payload, headers = headers)
    print(post_response.text)


# paste("this is the contents of the paste","pastename")

def showpastes ():  ## returns json data array of pastes linked to api key
    headers = {'X-Auth-Token': apikey}
    showpastes = requests.get(url = 'https://api.paste.ee/v1/pastes', headers = headers)
    print(showpastes.text)


# showpastes()

def getpaste ( id ):  ## returns data as json for paste
    headers = {'X-Auth-Token': apikey}
    url = 'https://api.paste.ee/v1/pastes/' + id
    getpaste = requests.get(url = url, headers = headers)
    print(getpaste.text)


getpaste('HxwAl')
