import pasteee

pasteee.apikey = '<apikey>'

print('----------------------')
print('----------------------')
makepaste = pasteee.Make('name', 'contents', 86400)
print(makepaste.status) # prints bool value of status
print(makepaste.name) # prints paste name
print(makepaste.content) # prints paste content
print(makepaste.syntax) # prints paste syntax
print(makepaste.expiration) # prints paste expiration in datetime format
print(makepaste.paste_id) # prints pasteid
print(makepaste.expiration_time) # prints expiration_time in date time format
print('----------------------')

print('----------------------')
paste1 = pasteee.GetPaste('jLVES') # creates GetPaste object
print(('Name:-           ')+(paste1.name)) #prints paste name
print(('expires_at:-     ')+(paste1.expires_at)) #prints expires_at datetime
print(('syntax:-         ')+(paste1.syntax)) # prints paste syntax
print(('Created at:-     ')+(paste1.created_at)) #prints created at datetime
print(('Contents:-       ')+(paste1.content)) # prints pastecontent
print(('views:-          ')+str(paste1.views)) # prints number of paste views
print(('Status Bool:-    ')+str(paste1.status)) # prints bool status value
print(('encrypted:-      ')+str(paste1.encrypted)) # is data encrypted? bool
print(('Size:-           ')+str(paste1.size)) # prints size of data
print(('Data:-           ')+str(paste1.data)) # prints data
print('----------------------')

print('----------------------')
print('showallpastes test')
showall = pasteee.ShowAllPastes() # returns all pastes as json
print(showall.data) # print all pastes as json
print('----------------------')

print('----------------------')
user = pasteee.Users()
print(user.status) # prints bool value of status
print(user.data) # prints information about a pastes syntax.
print('----------------------')

print('----------------------')
file = pasteee.File('name','text.txt')
print(file.status) # prints bool value of file upload
print(file.pasteid) # prints paste id
print(file.name) # prints paste name
print(file.filename) # prints filename
print('----------------------')

print('----------------------')
delete = pasteee.Deletepaste('zb8ys')
print(delete.data) # prints data that was deleted
print(delete.status) # prints status of deletion
print(delete._id) # prints deleted paste id
print('----------------------')

print('----------------------')
pasteee.Deleteallpastes() # deletes all pastes
print('----------------------')