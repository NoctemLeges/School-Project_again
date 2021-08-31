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
ages=[]

for entry in db:
    ages.append(entry["age"])
ages.sort(reverse=True)
corrected_db=[]

for age in ages:
    for entry in db:
        if entry["age"]==age and entry not in corrected_db:
            corrected_db.append(entry)
print(corrected_db)



