# 55. Напечатать строки следующего вида
#          abc ........ xyz
#          bc ......... yza
#          c  ......... zab
#           ................             Всего 26 строк
#          yzab ......... x
#          zab ......... xy
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
step = 0
old_value = 0
print(abc)
while step < 25:
    for i in range(0, len(abc) - 1):
        old_value = abc[i + 1]
        abc[i + 1] = abc[i]
        abc[i] = old_value
    print(abc)
    step += 1
