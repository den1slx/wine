from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from pandas import read_excel
from collections import defaultdict


def date_check(date):
    date = str(date)
    check_1 = '1'
    check_2 = '2', '3', '4'
    check_3 = '0', '5', '6', '7', '8', '9'
    check_4 = '11', '12', '13', '14'
    year = 'непредвиденная ошибка'

    if len(date) > 1:
        if date[-1] == '1' and date[-2] != '1':
            year = 'год'
        elif date[-1] in check_2 and date[-2] != '1':
            year = 'года'
        elif date[-1] in check_3 or date[-2:] in check_4:
            year = 'лет'
    else:
        if date in check_1:
            year = 'год'
        elif date in check_2:
            year = 'года'
        elif date in check_3:
            year = 'лет'

    return f'Уже {date} {year} с вами'


def get_unique_values(list_):
    sorted_list = []
    for i in list_:
        if i not in sorted_list:
            sorted_list.append(i)
    return sorted_list


def get_company_age():
    year_of_foundation = datetime(year=1920, month=1, day=1)
    now = datetime.now()
    year_total_seconds = 365 * 24 * 60 * 60
    delta = (now - year_of_foundation).total_seconds()
    company_age = int(delta // year_total_seconds)
    return company_age


def serialize_wines(path_to_excel_file):
    excel_wines = read_excel(path_to_excel_file, keep_default_na=False, na_values=['nan', 'NA', 'N/A'])
    dictionary_wines = defaultdict(str)
    dictionary_wines.update(excel_wines.to_dict())
    category, title, sort, price, image = excel_wines.columns.to_list()
    column_range = len(excel_wines[title])
    categories = (get_unique_values(excel_wines[category].to_list()))
    wines_categories = defaultdict(list)  # ??
    wines = []

    for i in range(column_range):
        wine = {
            'category': dictionary_wines[category][i],
            'title': dictionary_wines[title][i],
            'sort': dictionary_wines[sort][i],
            'price': dictionary_wines[price][i],
            'image': f"images/{dictionary_wines[image][i]}",
        }
        wines.append(wine)

    for category in categories:
        wines_categories.update({category: [wine for wine in wines if wine['category'] == category]})

    return wines_categories


title = date_check(get_company_age())
categories_wine = serialize_wines('wine2.xlsx')


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    company_age=title,
    categories_wine=categories_wine,
)

with open('index.html', 'w', encoding="utf8") as file:  # save to index.html filled pattern
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
