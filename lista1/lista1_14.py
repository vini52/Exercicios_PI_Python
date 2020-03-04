n = input()
c = input()
if c == "TROCA":
    i = int(input())
    d = input()
    m = n.replace(n[len(n)-i],d)
    print(m)
elif c == "APAGA":
    i = int(input())
    if i <= len(n):
        m = n.replace(n[len(n)-i],'')
        print(m)
    else:
        print(n)
elif c == "INSERE":
    i = int(input())
    d = input()
    if i <= len(n):
        x = n
        m = list(x)
        m.insert(len(x)-i+1, d)
        print(''.join(map(str, m)))
    else:
        x = n
        m = list(x)
        while len(n) < i-1:
            m.insert(0, '0')
            i -= 1
        m.insert(0, d)
        print(''.join(map(str, m)))