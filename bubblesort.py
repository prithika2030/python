list=[2,4,3,6,5]
n=len(list)
for i in range(n):
  for j in range(0,n-1):
    if(list[j]>list[j+1]):
      list[j],list[j+1]=list[j+1],list[j]
print(list)  
