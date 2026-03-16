print("from start=0")
names=['thrishala','bhavani','keerthy']
for indx,name in enumerate(names,start=0):
    print(f"{indx} . {name}")

print(" from start=1")

for indx,name in enumerate(names,start=1):
    print(f"{indx} . {name}")

#default start=0
string="python"
for ind,ch in enumerate(string):
    print(f"{ind} . {ch}")

#list of enumeratenames=['thrishala','bhavani','keerthy']
names=['thrishala','bhavani','keerthy']
new_names=list(enumerate(names))
print(new_names)

#directly print without using variable
print(list(enumerate((10, 20, 30))))
