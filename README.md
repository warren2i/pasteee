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

`import pasteee`

#### Define api key 

`pasteee.apikey = '<apikey>'`

#### Get a single paste object

`paste1 = pasteee.GetPaste('<id>')`

`paste1.name` Returns paste name

`paste1.expires_at` Returns expires_at datetime

`paste1.syntax` prints Returns syntax

`paste1.created_at` Returns created at datetime 

`paste1.content` Returns paste content

`paste1.views` Returns number of paste views

`paste1.status` Returns bool status value

`paste1.encrypted` is data encrypted? bool

`paste1.size` Returns size of data

`paste1.data` Returns data


##### Make a paste

`makepaste = pasteee.Make('name', 'contents', 86400)` makepaste Make object

`makepaste.status` Returns bool value of status

`makepaste.name` Returns paste name

`makepaste.content` Returns paste content

`makepaste.syntax` Returns paste syntax

`makepaste.expiration` Returns paste expiration in datetime format

`makepaste.paste_id` Returns paste id

`makepaste.expiration_time` Returns expiration_time in date time format


##### Paste a file

`file = pasteee.File('name','text.txt')` Creates file object
`file.status` Returns bool value of file upload
`file.pasteid` Returns paste id
`file.name` Returns paste name
`file.filename` Returns filename

##### Delete a paste

`delete = pasteee.Deletepaste('<id>')` Creates delete object

`delete.data)` Returns data that was deleted

`delete.status)` Returns status of deletion

`delete._id)` Returns deleted paste id

#### Delete all pastes

`pasteee.Deleteallpastes()` # deletes all pastes

#### Show all pastes

`showall = pasteee.ShowAllPastes()` returns all pastes as json

`showall.data` Returns all pastes as json


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