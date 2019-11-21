a=int(input("Enter the rows:"))
for i in range(0,a):
  for j in range(1,i+1):
      print("*",end=" ")
  print()  
  
for i in range(a,0,-1):
  for j in range(i-1):
    print("*",end=" ")
  print() 
    
