def sqrt(n):
    for i in range(1, n+1):
        if (n % i == 0) and (i * i == n):
            print("It is a perfect square number",a)
            break
    else:
      print("not a perfect")
a=int(input("Enter the number:"))
sqrt(a)
