def create_person(name, course):
    person = {'name' : name, 'course' : course}
    return person

person = create_person('Gui', 'Programming')
print(person)

def show_users(names):
    for name in names:
        print(name)

names = ['Eddie', 'Lea', 'Phil']
show_users(names)

def change_notes(notes):
    for i in range(0, len(notes)):
        notes[i] += 10
    return(notes)

notes1 = [6, 6 , 5]
print(notes1)
new_notes1 = change_notes(notes1)
print(notes1)
print(new_notes1)

notes2 = [5, 5, 6, 7, 2]
new_notes2 = change_notes(notes2[:])
print(notes2)
print(new_notes2)

