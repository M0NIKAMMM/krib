money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0

while True:
    difficite = spend - salary
    if money_capital < difficite:
        break

    spend *= (1 + increase)
    money_capital -= difficite
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
