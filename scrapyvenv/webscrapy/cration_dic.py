import json
import os
import numpy as np 
import os


# this file transforms the json format of the medicines scrapped by the spider medic.py into :
# - a sorted numpy array of medecines
# - creates the dict

medicaments = np.array([])
def creat_dict():
    global medicaments
    #with makes sure the file gets closed properly without you worrying about it.
    try:
        with open("medic.json",'r') as f :
            data = json.load(f)
    except:
        print("File medic.json is empty try scrapping first (json file includes all the drugs)")
    else:
        with open("subst.dic",'w',encoding="utf-16 le") as o:
            for i in data:
                for y in i["medicament"]:
                    medicaments = np.append(medicaments,y)          
        medicaments = np.sort(medicaments)
        with open("subst.dic",'w',encoding="utf-16 le") as o:
            for i in medicaments:
                    o.write(i+",.N+subst\n")
        print("Dictionnaire subst.dic cree")
    return medicaments
    





               
