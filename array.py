import array as arr
a=arr.array('i',[1,2,3,4,5])
print(a)
print("first element:",a[0])
print("last element:",a[-1])
num=[1100,200,300,400,500]
b=arr.array('i',num)
print(num[1:2])
num[0]=2000000
print(num)
num[2:5]=arr.array('i',[1,2,3])
print(num)
num.append(4)
print(num)
num.extend([2,5,1,0,6,3])
print(num)
del num[2]
print(num)

