import json


with open("testjson.json","r") as file:
    str_data=file.read()
    dict_data=json.loads(str_data)
    print(type(dict_data))
    print(dict_data)
    print("First name is ",dict_data["myinfo"]["firstname"])
    print("Age is ",dict_data["myinfo"]["age"])
    print("Skills are ...")
    for each_skill in dict_data["myinfo"]['technologies']['skills']:
        print(each_skill)
    dict_data["myinfo"]["firstname"] = "shivani"
    dict_data["myinfo"]["lastname"] = "herekar"
    dict_data["myinfo"]["age"]=6
    dict_data["myinfo"]['technologies']['skills'][0] = "javascript"
    dict_data["myinfo"]['technologies']['skills'][1] = "css"
    dict_data["myinfo"]['technologies']['skills'][2] = "html"
    del dict_data["myinfo"]["address"]
    print(dict_data)


with open("modified1.json","w") as file:
    str_data=json.dumps(dict_data,indent=4)
    file.write(str_data)
