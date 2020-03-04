num = input()
if len(num) != 4:
    print("Número digitado não suportado!")
else:
    res = []
    for i in num:
        if i == "0" or i == "1" or i == "2" or  i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8":
            a = int(i)
            a += 1
            res.append(a)
        else:
            a = 0
            res.append(a)
        print(res)
    print(''.join(map(str, res)))