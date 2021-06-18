list = []
list.append(1)
list.append(2)
list.append(3)
for s in list:
    print(s)


#uc_2

dict = {}
for i in range(len(list)):
    dict[i] = list[i]

for key,values in dict.items():
    print(key,values)