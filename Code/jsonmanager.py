import json

# dont touch it works

def WriteJSON(newpassword):
    File = open('savedpasswords.json','r+')
    FileData = json.load(File)
    FileData['passwords'].append(newpassword)
    File.seek(0)
    json.dump(FileData, File, indent = 6)

def ClearJSON():
  File = open('savedpasswords.json', 'r+')
  File.truncate(0)

def DeleteJSON(deletepassword):
    File = open('savedpasswords.json','r+')
    FileData = json.load(File)
    
    passwordslist = FileData['passwords']

    for dictionary in passwordslist:
      if dictionary['Name'] == deletepassword:
        FileData['passwords'].remove(dictionary)
        
    ClearJSON()
    File.seek(0)
    
    json.dump(FileData, File, indent = 6)
    

# object example
# object = {'Name': 'Test', 'Content': 'pE36DAq!7P52Ddw5'}
