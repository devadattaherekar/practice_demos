import yaml

with open("testyaml.yml","r") as file:
    str_data=file.read()
    dict_data=yaml.load(str_data,Loader=yaml.FullLoader)
    print(dict_data)
    dict_data["myinfo"]["firstname"] = "Hrishikesh"
    dict_data["myinfo"]["lastname"] = "valzalwar"
    dict_data["myinfo"]["age"]=24
    dict_data["myinfo"]['technologies']['skills'][0] = "dockers"
    dict_data["myinfo"]['technologies']['skills'][1] = "aws"
    dict_data["myinfo"]['technologies']['skills'][2] = "kubernetes"


with open("modifiedyaml.yml","w") as file:
    str_data=yaml.dump(dict_data)
    file.write(str_data)