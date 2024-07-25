names = ["AlAmin", "Rashed", "Rahat", "Rakib", "Shamim", "Kafi"]

list = []
search = input("Type your alphabet ")
for name in names:
    if name.startswith(search):
        list.append(name)
if list:
    for name in list:
        print(name)
else:
    print("No data available")