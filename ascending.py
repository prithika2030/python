list=[]
a=int(input("how many element are enter:"))
for i in range(1,a+1):
    b=int(input("Please enter the number:"))
    list.append(b)
print(list)
for i in range(a):
    for j in range(i+1,a):
        if(list[i] > list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list)
