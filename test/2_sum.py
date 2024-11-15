a=int(input("enter the first value:"))
b=int(input("enter the second value:"))

def sum_2(a,b):



    sum=a+b

    if sum in range(15, 20):
      return 20
    else:
     return sum


print(sum_2(a,b))


