#Дратути)

money = int(input('Введите сумму вклада '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB = int(money * per_cent.get('ТКБ') / 100)
SKB = int(money * per_cent.get('СКБ') / 100)
VTB = int(money * per_cent.get('ВТБ') / 100)
SBER = int(money * per_cent.get('СБЕР') / 100)
print ('Депозит ТКБ =',TKB, '\nДепозит СКБ =', SKB, '\nДепозит ВТБ =', VTB, '\nДепозит СБЕР =', SBER)

deposit = [TKB, SKB, VTB, SBER]
deposit_max = max(deposit)

print ('Самый лучший вариант для депозита', deposit_max)

# Это уже я допилил чтобы красота была
deposit_bank = {'ТКБ' : TKB, 'СКБ' : SKB, 'ВТБ' : VTB, 'СБЕР' : SBER}

max_value = max(deposit_bank.values())
max_value_key = max(deposit_bank, key=deposit_bank.get)

print ('Самый лучший банк по вкладу', max_value_key, '=', max_value, 'годовых')