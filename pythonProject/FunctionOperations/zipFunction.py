lst1 = ["Nishit", "Aryaa", "Roopam","Nishit"]
lst2 = [1,2,3,1]

lst3 = list(zip(lst1,lst2))
print(lst3)

set1 = set(zip(lst1,lst2))
print(set1)

dict1 = dict(zip(lst1,lst2))
print(dict1)

zipp = zip(lst1,lst2)
for (a,b) in zipp:
    print(a,b)