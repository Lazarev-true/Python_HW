START = 2
END = 11

for i in range(START, END):
    for j in range(START, END // 2 + 1):
        print(f'{j:>2} x {i:>2} = {j * i:>2}', end='    ')
    print('')
print('')

for i in range(START, END):
    for j in range(END // 2 + 1, END - 1):
        print(f'{j:>2} x {i:>2} = {j * i:>2}', end='    ')
    print('')
