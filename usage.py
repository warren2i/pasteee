import pasteee

pasteee.apikey = '****'

#paste1 = pasteee.make('test import','paste') ##makes a new paste
#print(paste1)
print('----------------------')
print('GetPaste Test-*-')
paste1 = pasteee.GetPaste('RWDlj')
print(('Name:-           ')+(paste1.name)) ##retrive data array
print(('Created at:-     ')+(paste1.created_at)) ##retrive data array
print(('Contents:-       ')+(paste1.content)) ##retrive pastecontent
print(('Status Bool:-    ')+str(paste1.status)) ##retrive pastecontent
print(('Size:-           ')+str(paste1.size))
print(('Data:-           ')+str(paste1.data))
print('----------------------')
print('showallpastes test')
pasteee.showallpastes()
print(pasteee.showallpastes())
print('----------------------')
#file = pasteee.file('name','text.txt') ## paste the contents of a file
#print(file) ## return state of post, and returns paste ID
#d1 = pasteee.deletepaste('irM2')
#print(d1)
print('----------------------')