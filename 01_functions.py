def saudation ():
    print("Hello world!")

def sum(a, b):
    print("sum = " + str(a + b))

def sub(a, b):
    print("sub = " + str(a - b))

def mul(a, b):
    result = a * b
    return result


saudation()
sum(5, 1)
sub(10,5)

def calc(a, b, op='soma'):
    if op == 'soma':
        print(str(a + b))
    elif op == 'sub':
        print(str(a - b))

calc(1,2, 'sub')
calc(2, 3, 'soma')
calc(2, 10)

result = mul(1,10)
print(result)
    

