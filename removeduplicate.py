arr=[1,1,1,2,3,4]
for i in range(0,len(arr)):
   for j in range(i+1,len(arr)):
   if(arr[i]==arr[j]):
      arr.remove(arr[i])
      print(arr)
   else:
      print("There is no duplicate value")
