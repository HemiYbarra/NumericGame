x = 50
cnt = 0

while True:
    user_number = int(input('Я загадал число от 1 до 100, угайдай его'))
    cnt += 1
    if user_number == x:
        print(f'Ты угадал число за {cnt} попыток')
        print('Спасибо за игру!')
        break
    elif user_number > x:
        print('Наше число меньше того, которое ты ввел')
    else:
        print('Наше число больше того, которое ты ввел')