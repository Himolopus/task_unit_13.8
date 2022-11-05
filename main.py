tickets_count = int(input('Сколько билетов желаете приобрести?\n-> '))
tickets_values = []    # Создаем вспомогательный список в который будут записываться цены заказываемых билетов
for i in range(tickets_count):    # Это цикл для формирования вспомогательного списка
    age = int(input(f'Сколько лет {i + 1}-му посетителю?\n-> '))
    if age < 18:    # Для оптимизации принято решение не дополнять список нулями (для решаемой задачи нам это не нужно)
        continue
    value = 1390 if age >= 25 else 990
    tickets_values.append(value)
price = sum(tickets_values) if tickets_count <= 3 else int(sum(tickets_values) - (sum(tickets_values) * 10 / 100))
print(f'Сумма к оплате: {price} руб')
