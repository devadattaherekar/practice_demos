import xmltodict


with open("testxml.xml","r") as file:
    str_data=file.read()
    dict_data=xmltodict.parse(str_data)
    print(dict_data)
    dict_data['root']["myinfo"]["firstname"] = "Hrishikesh"
    dict_data['root']["myinfo"]["lastname"] = "valzalwar"
    dict_data['root']["myinfo"]["age"]=24
    dict_data['root']["myinfo"]['technologies']['skills'][0] = "dockers"
    dict_data['root']["myinfo"]['technologies']['skills'][1] = "aws"
    dict_data['root']["myinfo"]['technologies']['skills'][2] = "kubernetes"


with open("modifiedxml.xml","w") as file:
    str_data=xmltodict.unparse(dict_data,pretty=True)
    file.write(str_data)