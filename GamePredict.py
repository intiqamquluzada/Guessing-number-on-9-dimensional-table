import random

my_list = []

for i in range(9):
    my_list.append(random.randint(1, 10))

print("""X X X
X X X
X X X""")
new_list = []
for item in range(9):
    new_list.append('x')
wrong_attempts = 0
i = 0
while i < 5:
    location = int(input('\nEnter the index of element: '))
    number = int(input('Enter the number: '))
    if number == my_list[location - 1]:
        new_list[location - 1] = number
        for a in range(len(new_list)):
            print(new_list[a], end=' ')
            if a == 2 or a == 5:
                print()
        if new_list.count('x') == 4:
            print('\nYou won')
            break
    else:
        for a in range(len(new_list)):
            print(new_list[a], end=' ')
            if a == 2 or a == 5:
                print()
        if wrong_attempts == 2:
            print('\nYou lost')
            break
        wrong_attempts += 1
    i += 1
    print(f'\nCount of attempts: {i}\nRemaining attempts: {5-i}')
