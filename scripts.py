from datetime import datetime
from pandas import read_excel
from collections import defaultdict


def create_company_age_string(date):
    date_string = str(date)
    digits_1 = '1'
    digits_2 = '2', '3', '4'
    digits_3 = '0', '5', '6', '7', '8', '9'
    numbers = '11', '12', '13', '14'

    if len(date_string) > 1:
        if date_string[-1] == '1' and date_string[-2] != '1':
            year = 'год'
        elif date_string[-1] in digits_2 and date_string[-2] != '1':
            year = 'года'
        elif date_string[-1] in digits_3 or date_string[-2:] in numbers:
            year = 'лет'
    else:
        if date_string in digits_1:
            year = 'год'
        elif date_string in digits_2:
            year = 'года'
        elif date_string in digits_3:
            year = 'лет'

    return f'Уже {date} {year} с вами'


def get_company_age():
    foundation_year = 1920
    now = datetime.now().year
    company_age = now - foundation_year
    return company_age


def get_categories_with_wines(path_to_excel_file):

    excel_wines = read_excel(path_to_excel_file, keep_default_na=False, na_values=['nan', 'NA', 'N/A'])
    wines = excel_wines.to_dict(orient='records')
    wines_categories = defaultdict(list)
    for wine in wines:
        wines_categories[wine['Категория']].append(wine)

    return wines_categories

