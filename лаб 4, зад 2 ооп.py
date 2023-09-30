import random#добавляем рандом

a=tuple(random.randint(0,5) for i in range(10))#генерируем кортеж a
b=tuple(random.randint(-5,1) for i in range(10))#и кортеж b
c=a+b#образуем 3 картеж
kolvo_nuleu=c.count(0)#кол-во нулей
print('Третий кортеж:', c, 'Количество нулей в третьем кортеже:', kolvo_nuleu)#вывод кортежа и кол-ва нулей
