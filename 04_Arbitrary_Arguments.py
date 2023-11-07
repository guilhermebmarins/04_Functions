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

print_notes('Gui', 8)
print_notes('Alice', 5, 6 ,8)

sum, avg = calc_notes(5, 5, 8, 4)
print('Sum = ' + str(sum))
print('Avg = ' + str(avg))
