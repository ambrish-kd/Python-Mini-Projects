import calendar

try:
    print("\nEnter a year between 1 to 9999")
    y = int(input())
    if 1>y or y>9999:
        print("\nChoose another year!!!\n")
    else:
        for i in range (12):
            print("\n" + calendar.month(y, i+1))
except:
    print("\nChoose a year in given range!\n")