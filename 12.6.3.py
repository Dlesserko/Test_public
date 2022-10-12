money = int(input('Введите сумму вклада '))

TKB = int(money * 5.6 / 100)
SKB = int(money * 5.9 / 100)
VTB = int(money * 4.28 / 100)
SBER = int(money * 4.0 / 100)
print ('Депозит ТКБ =',TKB, '\nДепозит СКБ =', SKB, '\nДепозит ВТБ =', VTB, '\nДепозит СБЕР =', SBER)

deposit = [TKB, SKB, VTB, SBER]
deposit_max = max(deposit)

print ('Самый лучший вариант для депозита', deposit_max)

# Это уже я допилил чтобы красота была
deposit_bank = {'ТКБ' : TKB, 'СКБ' : SKB, 'ВТБ' : VTB, 'СБЕР' : SBER}

max_value = max(deposit_bank.values())
max_value_key = max(deposit_bank, key=deposit_bank.get)

print ('Самый лучший банк по вкладу', max_value_key, '=', max_value, 'годовых')