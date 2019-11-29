n = int(input())
sum = 0
while n:
  d=n%10
  n//=10
  sum+=d*d
print(sum,end='')
