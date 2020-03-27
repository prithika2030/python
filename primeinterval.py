start =int(input("Enter the start number:"))
end = int(input("Enter the end number:"))
for val in range(start, end + 1):
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            print(val,"It is a prime number")
