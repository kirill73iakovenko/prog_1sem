n = int(input())
numbers=[]
for i in range(n-1):
    numbers.append(int(input()))
xor_numbers = numbers[0]
xor_all = 1
for i in range(2, n+1):
    xor_all = xor_all ^ i
for i in range(1,n-1):
    xor_numbers = xor_numbers ^ numbers[i]
rez = xor_numbers ^ xor_all
print(rez)
with open('rez', 'w') as fin:
    fin.write(f'{rez}\n')
