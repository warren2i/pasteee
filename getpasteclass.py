import json
import requests

class JSONObject:
  def __init__( self, dict ):
      vars(self).update( dict )

def getpaste ( id ):  ## returns data as json for paste
    headers = {'X-Auth-Token': 'u38yy4u89g7itIed4WWcKOxCPQxqB15PCPwdZ3fqT'}
    url = 'https://api.paste.ee/v1/pastes/' + id
    getpaste = requests.get(url = url, headers = headers)
    data = getpaste.text
    paste = json.loads(data, object_hook = JSONObject)
    return paste.paste ## returns values inside of paste json object

class Getpaste:
  def __init__(self, id):
    self.id = id
    paste = getpaste(id)
    self.encrypted = (paste.encrypted)
    self.description = (paste.description)
    self.views = (paste.views)
    self.created_at = (paste.created_at)
    self.expires_at = (paste.expires_at)
    self.syntax = (paste.sections[0].syntax)
    self.name = (paste.sections[0].name)
    self.contents = (paste.sections[0].contents)
    self.size = (paste.sections[0].size)

p1 = Getpaste('pbxpH')
print(p1.id)
print(p1.encrypted)
print(p1.description)
print(p1.views)
print(p1.created_at)
print(p1.expires_at)
print(p1.syntax)
print(p1.name)
print(p1.contents)
print(p1.size)

p2 = Getpaste('T4kyD')
print(p2.id)
print(p2.encrypted)
print(p2.description)
print(p2.views)
print(p2.created_at)
print(p2.expires_at)
print(p2.syntax)
print(p2.name)
print(p2.contents)
print(p2.size)

