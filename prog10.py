file = open("patient.csv","r")
db = []
entries = file.readlines()
file.close()
for entry in entries:
    dt={}
    l = entry.split(",")
    dt["id"]=l[0]
    dt["name"]=l[1]
    dt["age"]=l[2]
    dt["city"]=l[3]
    db.append(dt)
print("The cities are:")
for entry in db:
    if entry["name"][0] =='O' or entry["name"][-1] == 'r' or int(entry["age"])>70:
        print(entry["city"])

