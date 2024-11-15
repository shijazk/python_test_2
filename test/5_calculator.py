
a=int(input("enter the value:"))

def multi_table(a, i=1):
    if (i == 11):
        return
    print(a, "*", i, "=", a * i)
    i += 1
    multi_table(a, i)




multi_table(a)