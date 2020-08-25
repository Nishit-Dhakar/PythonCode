lst = [1,2,3,5,6,7,8,9,0]

#Function to count event and odd numbers

def counter(arg):
    even, odd =0,0
    for i in arg:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return even, odd

evennbrCtr, oddnbrCtr = counter(lst)
print("Even # count {} & Odd # count {}".format(evennbrCtr,oddnbrCtr))

