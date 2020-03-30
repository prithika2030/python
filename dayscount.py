def days_in_month(month):
   if(month=='january'or month=='march' or month=='may' or month=='july'or month=='august' or month=='october' or month=='december'):
      print("This month having 31 days")
   elif(month=='april' or month=='june' or month=='september' or month=='november'):
      print("This month having 30 days")
   elif(month=='Febuary'):
      print("This month contain only 28 days")
   else:
      print("please enter the correct month")
month=input("Enter the month:")
days_in_month(month)
