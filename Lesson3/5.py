numbers = list(map(int, input().split()))
numbers.insert(0, numbers[len(numbers) - 1] )
numbers.pop(len(numbers)-1)
rez = ''
for num in numbers:
    rez += str(num) + ' '
print(rez)
with open('rez4','w') as fin:
    fin.write(f'{rez}\n')
