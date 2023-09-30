''''n=int(input())
if n>=18:
    print("elgible to vote")
else:
    print("not")'''

Book_return_days= int(input())
if Book_return_days == 0:
    print("NIL Fine")
elif Book_return_days >=5 and Book_return_days >=10:
    print("Fine", Book_return_days*5)


M1=int(input(""))

M2=int(input(""))

M3=int(input(""))

Total = M1+M2+M3
Average= Total/3

if Total>=35:
    print("passed")
else:
    print("Fail")
