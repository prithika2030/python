n,k = [int(x) for x in input().split()]
a = n*k
b = int(a**0.5)
if a == b*b : print('yes',end='')
else : print('no',end='')
