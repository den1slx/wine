from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
from pandas import read_excel


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


year_of_foundation = datetime(year=1920, month=1, day=1)
now = datetime.now()
year_total_seconds = 365*24*60*60
delta = (now - year_of_foundation).total_seconds()
company_age = int(delta // year_total_seconds)
title = date_check(company_age)

excel_wines = read_excel('wine.xlsx')
dictionary_wines = excel_wines.to_dict()
column_range = len(excel_wines['Название'])
wines = []

for i in range(column_range):
    wine = {
        'title': dictionary_wines['Название'][i],
        'sort': dictionary_wines['Сорт'][i],
        'price': dictionary_wines['Цена'][i],
        'image': f"images/{dictionary_wines['Картинка'][i]}",
    }
    wines.append(wine)

env = Environment(
    loader=FileSystemLoader('.'),  # where this html file
    autoescape=select_autoescape(['html', 'xml'])  # standard html settings
)

template = env.get_template('template.html')  # load pattern from template.html

rendered_page = template.render(  # add value for variables in template.html
    company_age=title,
    wines=wines,
)

with open('index.html', 'w', encoding="utf8") as file:  # save to index.html filled pattern
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
