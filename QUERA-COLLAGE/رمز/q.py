k = int(input())
reshte = input()


def password(s: str, l: str):
    mid = len(l) // 2
    for i in l:
        if i == s:
            if l.index(i) == mid:
                return mid
            if l.index(i) < mid:
                return l.index(i)
            else:
                return len(l) - l.index(i)


javab = 0
for i in range(k):
    n = input()
    javab += password(reshte[i], n)
print(javab)
