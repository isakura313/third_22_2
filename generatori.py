# li = []
#
# for i in range(15):
#     li.append(i)
# неудобный и большой вариант
# print(li)

numbers = list(range(1, 14))
# зато теперь умещается в одну строку
print(numbers)

cube = [value**3 for value in range(1, 11)]
print(cube)

square = [num ** 2 for num in range(10, 100, 5)]
print(square)


cars = ['volvo', 'citroen', 'suzuki', 'bmw', 'jigul']
new_cars = cars[:] # полное дублирование
# new_cars = cars передача по ссылке

new_cars.append("oka")
del cars[0]
print(cars)
print(new_cars)

