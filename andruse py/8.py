num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("more then zero")
else:
    print("less then zero")
    
year =num

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
