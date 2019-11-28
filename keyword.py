def person(name,age):
    print(name)
    print(age)
person(age=20,name="preethika")

def sum(a,*b):
    print(a),print(b)       
sum(5,6,7,8,910)

def person(name,**data):      
  print(name)
  print(data)
person("prithika",age=20,city="harur",mobile=251063)


