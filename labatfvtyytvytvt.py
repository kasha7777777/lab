a = int(input("Введите кол-во слов: "))
result = ""

for i in range(a):
    word = input("Напишите слово: ")
    result += word + " "

print("Результат:", result)