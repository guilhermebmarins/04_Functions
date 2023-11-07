def saudation ():
    print("Hello world!")

def sum(a, b):
    print("sum = " + str(a + b))

def sub(a, b):
    print("sub = " + str(a - b))

def mul(a, b):
    result = a * b
    return result

def sqrt (a):
    a = a ** 2
    print("variable inside the function before the call: " + str(a))
    return a

def create_person(name, course):
    person = {'name' : name, 'course' : course}
    return person

def show_users(names):
    for name in names:
        print(name)

def change_notes(notes):
    for i in range(0, len(notes)):
        notes[i] += 10
    return(notes)

def print_notes(name, *notes):
    print("Student: " + name)
    for note in notes:
        print(note)

def calc_notes(*notes):
    sum = 0
    for note in notes:
        sum += note

    avg = sum / len(notes)

    return sum,avg