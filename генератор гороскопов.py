import random

zodiakList = ['овен', 'телец', 'близнецы', 'рак', 'лев', 'дева','весы', 'скорпион', 'стрелец', 'козерог', 'водолей', 'рыбы']
timelist = ['Сегодня', 'Завтра', 'Очень скоро', 'В ближайщем будущем']
eventList = ['Вы встретите', 'с вами случится', 'вы найдете', 'вы потеряете']
objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз", 'большие беды']

while True:
    zodiak = input('Введите свой знак зодиака: ')
    if zodiak.lower() in list(zodiakList):
        time = timelist[random.randint(0, len(timelist)-1)]
        event = eventList[random.randint(0, len(eventList)-1)]
        object = objectList[random.randint(0, len(objectList)-1)]
        print(time + ' ' + event + ' ' + object)
        next = input('Желаете ли вы еще раз попробовать?')
        if next.lower() != 'да' or next.lower() != 'yes':
            break
    else:
        print('Введите верный знак зодиака')
        continue

print("Приходите ещё за новыми предсказаниями!")