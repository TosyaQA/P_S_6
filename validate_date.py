import argparse
from datetime import datetime

def validate(date = None):
    parser = argparse.ArgumentParser(description='Проверка даты')
    parser.add_argument('date', nargs='?', type=str, help='Дата для проверки в формате dd.mm.YYYY')


    testDate = date if date else parser.parse_args().date

    try:
        datetime.strptime(testDate, '%d.%m.%Y')
        print('Дата валидна')
    except ValueError as err:
        print('Дата невалидна')