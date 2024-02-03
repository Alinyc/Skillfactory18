ticket = int(input("Введите, пожалуйста, количество приобретаемых билетов: "))

if ticket <= 0:
    print("Недопустимое количество билетов. Обновите страницу и введите количество приобретаемых билетов заново")
else:
    count = 1
    price = 0
    for count in range(ticket):
        participant_age = int(input(f"Введите, пожалуйста, возраст посетителя № {count+1}: "))

        if participant_age <= 0:
            print("Недопустимый возраст. Обновите страницу и введите возраст посетителя заново")
        elif participant_age < 18:
            price = 0
        elif 18 <= participant_age <= 25:
            price += 990
        else:
            participant_age >= 26
            price += 1390
    count += 1

    if count > 3:
        price = price*90/100

    print(f"Сумма к оплате за {count} билет(-а/-ов) = {price} руб.")