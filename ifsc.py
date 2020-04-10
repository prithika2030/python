num=input("Enter the ifsc code number:")
a=list(num)
b=" "
if(a[0]=="C" and a[1]=="N" and a[2]=="R" and a[3]=="B" and a[4]=="0" and a[5]=="0" and a[6]=="0" and a[7]=="4" and a[8]=="3"
 and a[9]=="6" and a[10]=="7"):
    for i in a:
        b+=str(i)
    print(b,"YOUR IFSC CODE IS VERIFIED SUCESSFULLY")
else:
    print("Please enter the correct IFSC code")
