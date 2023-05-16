from datetime import datetime

import environs
from pandas import read_excel
from collections import defaultdict
from environs import Env
from pprint import pprint
import argparse


def get_company_with_us(date):
    date_string = str(date)
    checklist_1 = '1'
    checklist_2 = '2', '3', '4'
    checklist_3 = '0', '5', '6', '7', '8', '9'
    checklist_4 = '11', '12', '13', '14'
    # How better named checklist ?

    if len(date_string) > 1:
        if date_string[-1] == '1' and date_string[-2] != '1':
            year = 'год'
        elif date_string[-1] in checklist_2 and date_string[-2] != '1':
            year = 'года'
        elif date_string[-1] in checklist_3 or date_string[-2:] in checklist_4:
            year = 'лет'
    else:
        if date_string in checklist_1:
            year = 'год'
        elif date_string in checklist_2:
            year = 'года'
        elif date_string in checklist_3:
            year = 'лет'

    return f'Уже {date} {year} с вами'


def get_unique_values(list_):
    sorted_list = []
    for i in list_:
        if i not in sorted_list:
            sorted_list.append(i)
    return sorted_list


def get_company_age():
    year_of_foundation = datetime(year=1920, month=1, day=1).year
    now = datetime.now().year
    delta = (now - year_of_foundation)
    return delta


def get_categories_with_wines(path_to_excel_file, sort_by_key=0):

    excel_wines = read_excel(path_to_excel_file, keep_default_na=False, na_values=['nan', 'NA', 'N/A'])
    dictionary_wines = excel_wines.to_dict()

    keys = list(dictionary_wines.keys())
    column_range = len(dictionary_wines[keys[0]])
    categories = (get_unique_values(excel_wines[keys[sort_by_key]].to_list()))
    wines_categories = defaultdict(list)
    wines = [({key: dictionary_wines[key][i] for key in keys}) for i in range(column_range)]

    for category in categories:
        wines_categories.update({category: [wine for wine in wines if wine[keys[sort_by_key]] == category]})
    return wines_categories


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', help='path to images', default='example.xlsx')
    return parser


def main():
    env = Env()
    company_age = get_company_with_us(get_company_age())
    try:
        path = env('PATH_TO_IMAGES')
    except environs.EnvError:
        path = None
    if path:
        categories_wine = get_categories_with_wines(path)
    else:
        parser = create_parser()
        args = parser.parse_args()
        path = args.path
        categories_wine = get_categories_with_wines(path)

    print(company_age)
    pprint(categories_wine, sort_dicts=False)


if __name__ == '__main__':
    main()
