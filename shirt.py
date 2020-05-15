def type_shirt(types):
   if(types=="cotton"):
      print("Your type is available")
   elif(types=="synthetic"):
      print("Your type is available")
   else:
      print("Sorry,your type is currently not available")
types=input("Enter the shirt type:")
type_shirt(types)
def model():
   if(models=="formal"):
      print("Your model is available")
   elif(models=="informal"):
      print("Your model is availble")
   else:
      print("Your model is currently not available")
models=input("Enter the shirt model:")
model()
def size_range(size):
   if(size>=40 and size<=50):
      print("Yes your shirt size is available")
   elif(size>=50 and size<=60):
      print("Your shirt size is available")
   elif(size>=60 and size<=70):
      print("Your shirt size is available")
   elif(size>=70 and size<=80):
      print("Your shirt size is available")
   elif(size>=80 and size<=90 ):
      print("Your shirt size is available")
   elif(size>=90 and size<=100):
      print("Your shirt size is available")
   else:
      print("Your shirt size is not available")
size=int(input("Enter the size:"))
size_range(size)
def colour():
   if(colours=="pink"):
      print("Yes,your colour is available")
   elif(colours=="red"):
      print("Yes,your colour is available")
   else:
      print("Your colour is not available")
colours=input("Enter your favourite colour:")
colour()
def hand():
   if(hands=="full"):
      print("Full hands is available")
   elif(hands=="Half"):
      print("Half hands is available")
   else:
      print("Sorry,currently not available that hands shirt")
hands=input("Enter the hands type:")
hand()
def design_model():
   if(design=="box"):
      print("your design model is available")
   elif(design=="plain"):
      print("your design model is available")
   elif(design=="Line"):
      print("Your design model is available")
   else:
      print("Sorry,currently not available for that design")
design=input("Enter the shirt design:")
design_model()
