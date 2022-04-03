'''
Zadanie 1.1 Naprawa butów / dni tygodnia
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (numer
od 1 do 7). Ma też podać, ile dni będzie trwała naprawa. Program ma wypisać, w jaki dzień
tygodnia buty będą gotowe do odbioru. Postaraj się obsłużyć także sytuacje, że naprawa trwa
dłużej niż 7 dni.
W podstawowej wersji możesz wypisywać dzień odbioru też jako numer, ale docelowo zrób
wersję, w której program wypisuje dzień odbioru słownie.
'''


def end_day(start, count):
    if (start + count) % 7 > 0:
        return (start + count) % 7
    else:
        return 7


days_of_week = {
    1: 'poniedziałek',
    2: 'wtorek',
    3: 'środa',
    4: 'czwartek',
    5: 'piątek',
    6: 'sobota',
    7: 'niedziela',
}

print('NAPRAWA OBUWIA')
print('~~~~~~~~~~~~~~~\n')
start_day = 0
days_of_repair = 0

while start_day not in days_of_week.keys():
    try:
        start_day = int(input(f'dzień dostarczenia obuwia do naprawy {days_of_week} :'))
    except Exception:
        print('dopuszczalne wartości: 1, 2, 3, 4, 5, 6, 7')

while days_of_repair <= 0:
    try:
        days_of_repair = int(input(f'ilość dni naprawy: '))
        if days_of_repair <= 0:
            print('dopuszczalne tylko liczby większe od 0')
    except Exception:
        print('dopuszczalne tylko liczby całkowite, większe od 0')

print(
    f'\ndzień dostarczenia: {days_of_week[start_day]} \n     dzień odbioru: {days_of_week[end_day(start_day, days_of_repair)]}')
