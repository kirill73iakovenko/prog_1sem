l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
def Unique_elem(s):
    res = []
    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                continue
            elif s[i] == s[j]:
                break
        else:
            res.append(s[i])
    return set(res)
res1 = Unique_elem(l1) | Unique_elem(l2)
res2 = Unique_elem(l1 + l2)
res3 = set(l1) & set(l2)
print(res1)
print(res2)
print(res3)

