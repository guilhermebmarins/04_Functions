def sqrt (a):
    a = a ** 2
    print("variable inside the function before the call: " + str(a))
    return a

a = 2
print("variable outside the function before the call: " + str(a))
result = sqrt(a)
print("variable outside the function after the call: " + str(a))
print(result)