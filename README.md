# Pasteee

````

██████╗  █████╗ ███████╗████████╗███████╗███████╗    
██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝    
██████╔╝███████║███████╗   ██║   █████╗  █████╗      
██╔═══╝ ██╔══██║╚════██║   ██║   ██╔══╝  ██╔══╝      
██║     ██║  ██║███████║   ██║   ███████╗███████╗    
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚══════╝    
                                                     

````
### Pastee a python libary to interface existing scripts with Paste.ee (Paste.ee is a FREE Pastebin with SSL, IPv6)
****
## Usage

### Import pasteee

#### Define api key 

`pasteee.apikey = '<apikey>'`

#### Get a single paste object

`paste1 = pasteee.GetPaste(<id>)`

`paste1.name` returns name

`paste1.created_at` returns created_at

`paste1.content` returns contents of the paste

`paste1.status` returns bool value of the request

`paste1.size` returns size of contents in bytes

`paste1.data` returns json data array of paste

##### Make a paste

`newpaste=pasteee.make(<name>, <contents>)` returns bool value of paste status & paste ID

##### Paste a file

`file = pasteee.file(<name>,<filename>)` returns bool value of paste status & paste ID

##### Delete a paste

`deletepaste(<id>)` returns bool value of the request 

#### Delete all pastes

`deleteallpastes()` doesn't return any data

#### Show all pastes

`showall = showallpastes()` returns all pasts as json object

`print(showall.data)`

enumerate example
```
getall = showallpastes()

for x in enumerate(getall['data']):
    print(x)
```

#### Get paste syntax

`getsyntax(<id>)` looks like the paste.ee doesnt support this documented function right now

#### Users

`pasteee.users()`This endpoint will return information about the current api key.