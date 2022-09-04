from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays
setlocale(LC_ALL, 'pt_BR.utf-8')

data1 = datetime(2022, 6, 2, 14, 47, 10)
print(data1.strftime('%d/%m/%Y %H:%M:%S'))

data2 = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(data2.timestamp())

data3 = datetime.fromtimestamp(1555729200.0)
print(data3)

data4 = datetime.strptime('21/04/2019 20:00:00', '%d/%m/%Y %H:%M:%S')
data4 = data4 + timedelta(seconds=59*60)
print(data4.strftime('%d/%m/%Y %H:%M:%S'))

data5 = datetime.strptime('02/06/2022 15:09:10', '%d/%m/%Y %H:%M:%S')
data6 = datetime.strptime('09/06/2022 00:09:10', '%d/%m/%Y %H:%M:%S')
dif = data6 - data5
print(dif.days)
print(data5.time())


data7 = datetime.now()
formatacao1 = data7.strftime('%A, %d de %B de %Y')
formatacao2 = data7.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)

mes_atual = int(data7.strftime('%m'))
print(mdays)
print(mes_atual, mdays[mes_atual])