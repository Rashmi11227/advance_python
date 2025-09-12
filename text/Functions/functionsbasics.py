""" # print statement
print("welcome to the class")
for i in range(1,10):
     print(f"Rashmi {i}") """

def add_num(x:int,y:int):
    """
    take two numbers as input
    return addition of two numbers
    """
    z=x+y
    return z
add=add_num(12,23)
print(f"output of addition is {add}")

def simple_interest(p,n,r):
    """
    take principal amount,rate of interest,and number of years as input
    calculate simple interest for above provided input
    """
    if isinstance(p,int|float) and isinstance(n,int|float) and isinstance(r,int|float):
            si=(p*n*r)/100
            return si
    else:
         print("please provide correct inputs")



sim_int=simple_interest(100000,12,7)
print(sim_int)
sim_int1=simple_interest("rashmi",12,6)
print(sim_int1)