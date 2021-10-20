print("40. Дана строка S и дано натуральное n. Удалить из строки S все группы длиной n подряд стоящих одинаковых символов.")

s: str = input("Введите строку: ")
n: int = int(input("Введите число n: "))

j = 0
new_s = ""
char = s[0]

for i in range(1, len(s)):
    if char != s[i]:
        char = s[i]
        new_s += s[i]

print(new_s)