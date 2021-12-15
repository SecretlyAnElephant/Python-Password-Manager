import json

def write_json(newname, newpassword):
    file = open('passwords.json','r+')
    file_data = json.load(file)
    dictionary = {'Name': newname, 'Content': newpassword}
    file_data["Passwords"].append(dictionary)
    file.seek(0)
    json.dump(file_data, file, indent = 6)

def clear_json():
  file = open('passwords.json', 'r+')
  file.truncate(0)

def delete_json(deletepassword):
    file = open('passwords.json','r+')
    file_data = json.load(file)
    
    passwordslist = file_data["Passwords"]

    for dictionary in passwordslist:
      if dictionary["Name"] == deletepassword:
        
        file_data["Passwords"].remove(dictionary)
        
    clear_json()
    file.seek(0)
    
    json.dump(file_data, file, indent = 6)

def savePassword(name, password):
    if name == '':
        return 'error: set password name'
    else:
        write_json(name, password)
        return 'success'
