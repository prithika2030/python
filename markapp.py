class mark:
   def __init__(self,m1,m2,m3,m4,m5):
       self.m1=m1
       self.m2=m2
       self.m3=m3
       self.m4=m4
       self.m5=m5
   def display(self):
      print(self.m1)
      print(self.m2)
      print(self.m3)
      print(self.m4)
      print(self.m5)
      avg=(self.m1+self.m2+self.m3+self.m4+self.m5)/5
      print(avg)
      if(avg>=90):
          print("Grade:O")
          print("Destination")
      elif(avg>=80 and avg<90):
          print("Grade:A")
          print("First class")
      elif(avg>=70 and avg<80):
          print("Grade:A+")
          print("Second class")
      elif(avg>=60 and avg<70):
          print("Grade:B")
          print("Third class")
      else:
          print("Grade:C")
m1=int(input("Enter the mark1:"))
m2=int(input("Enter the mark2:"))
m3=int(input("Enter the mark3:"))
m4=int(input("Enter the mark4:"))
m5=int(input("Enter the mark5:"))
m=mark(m1,m2,m3,m4,m5)
m.display()
