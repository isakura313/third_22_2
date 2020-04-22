import random

amount_of_bullet = input(" сколько  патронов? ")
aob = int(amount_of_bullet)
baraban = [0, 0, 0, 0, 0, 0]

for i in range(aob):
    baraban[i] = 1

print("Посмотрите на барабан", baraban)

How_much = input("Сколько раз вы собираетесь нажать на курок? ")

hm = int(How_much)

for i in range(hm):
    # random.shuffle(baraban)
    dulo = random.choice(baraban)
    if dulo == 1:
        print("babah")
        exit()
        # exit используется для выхода тела скрипта
    else:
        print("щелк")
    print(dulo)

print("Посмотрите на барабан", baraban)