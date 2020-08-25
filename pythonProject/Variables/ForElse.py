lst = [12,13,14,15,16,17,18,20]

for num in lst:
    if num % 10 == 0:
        print (num)
        break
else:
    print("not found")