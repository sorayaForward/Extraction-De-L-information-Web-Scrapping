import json
# links of medicaments from a to z in json format transformed to array of links to be used by the spider medic


def links():
    Links = []
    try:
        with open("vidal.json",'r') as f:
            data = json.loads(f.read())
    except:
        print("File vidal.json is empty try scrapping first (json file includes all the links)")
    else :
            for i in data:
                Links.append(i["title"])
            print(Links)
    finally:
        print("inside links.py")
    return Links

