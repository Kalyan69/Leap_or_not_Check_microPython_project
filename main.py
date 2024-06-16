def isLeapYear(year):
    if(year % 100 !=0 and year % 4 == 0):
        return True
    else:
        return False 

### User validation Loop
 
while True:
    try:
        CurrentYear = int(input("Please entera a year: 🎀 "))
        if(isLeapYear(CurrentYear)):
            print(CurrentYear, " is a valid leapYear ❤")   
        else:
            print(CurrentYear, " is  not  a valid leap year 🚨")     
    except:
        print("Pease Try aganin.")


