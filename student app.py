class student:
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print(self.name)
        print(self.reg)
        if(degree=="1"):
            print("B.E")
        elif(degree=="2"):
            print("B.TECH")
        elif(degree=="3"):
            print("MCA")
        elif(degree=="4"):
            print("M.E")
        else:
            print("B.Sc")
name=input("Enter the name:")
reg=input("Enter the regno:")
degree=input("Enter the choice:")
s=student(name,reg)
s.display()



