bin=[2,7,9,11,20,25,27,50,51,60]
first=0
last=len(bin)-1
mid=first+last//2
print(bin[mid])
ele=int(input("Enter the search element:"))
if(bin[mid]<ele):
    low=mid+1
    print(bin[low],"Your searching element is here")
elif(bin[mid]>ele):
    high=mid-1
    print(bin[high],"your searching element is here")
elif(bin[mid]==ele):
    print(bin[mid])
else:
    print("Here not having your searching element")
