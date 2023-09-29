import re#вызываем библиотеку для поиска чиселка
def poisk_chisel_in_string(text):#создаём функцию
    num=re.findall('\d', text)#ищем все числа в строке, используя библиотеку
    return num#возвращаемся к началу
text=input('Введите текст')#вводим предложение
num=poisk_chisel_in_string(text)#вызываем функцию
for num in num:
    print(num)#выводим числа, содержащиеся в тексте