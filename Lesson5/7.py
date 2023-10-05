import string
with open('LICENSE_PYTHON.txt') as file:
    text = file.read().replace('\n', ' ')

Words = dict()
text_s = list(text.split())
text_n = []
for i in range(len(text_s)):
    if text_s[i] in string.punctuation:
        continue
    else:
        text_n.append(text_s[i].lower())

for i in range(len(text_n)):
    if text_n[i] in Words:
        continue
    else:
        Words[text_n[i]] = text_n.count(text_n[i])
Words_sort = list(Words.items())

for i in range(len(Words_sort)-1):
    for j in range(i + 1, len(Words_sort)):
        if Words_sort[i][1] < Words_sort[j][1]:
            Words_sort[i], Words_sort[j] = Words_sort[j], Words_sort[i]
res = ''
for i in range(10):
    res += Words_sort[i][0] + ' ' + str(Words_sort[i][1]) + '\n'
print(res)




