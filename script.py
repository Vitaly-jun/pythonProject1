
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита:"))
deposit = (list(map(lambda num: money / 100 * num, per_cent.values())))
deposit = list(map(round, deposit))
print(deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))
