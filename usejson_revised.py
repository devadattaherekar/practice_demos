import json


with open("testjson.json","r") as file:
    dict_data=json.load(file)
    print(type(dict_data))
    print(dict_data)
    print("First name is ",dict_data["myinfo"]["firstname"])
    print("Age is ",dict_data["myinfo"]["age"])
    print("Skills are ...")
    for each_skill in dict_data["myinfo"]['technologies']['skills']:
        print(each_skill)
    dict_data["myinfo"]["firstname"] = "Hrishikesh"
    dict_data["myinfo"]["lastname"] = "valzalwar"
    dict_data["myinfo"]["age"]=24
    dict_data["myinfo"]['technologies']['skills'][0] = "dockers"
    dict_data["myinfo"]['technologies']['skills'][1] = "aws"
    dict_data["myinfo"]['technologies']['skills'][2] = "kubernetes"
    del dict_data["myinfo"]["address"]
    print(dict_data)


with open("modified.json","w") as file:
    json.dump(dict_data,file,indent=4)
